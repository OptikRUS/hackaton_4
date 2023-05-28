import os
import re

import pandas as pd
from haystack.schema import Document
from haystack.nodes import PreProcessor
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import BM25Retriever
from haystack.nodes import FARMReader
from haystack import Pipeline

from config import base_dir


class BotAnswerService:
    def __init__(self, path):
        self.path: str = base_dir + path
        self.preprocessor = PreProcessor(
            clean_whitespace=True,
            clean_header_footer=True,
            clean_empty_lines=True,
            split_by="word",
            split_length=4000,
            split_overlap=20,
            split_respect_sentence_boundary=True,
            language='ru',
        )

    def init_document_store(self):
        preprocessed_docs = self.preprocess_docs()
        document_store = InMemoryDocumentStore(use_bm25=True)

        document_store.write_documents(preprocessed_docs)
        retriever = BM25Retriever(document_store=document_store)
        reader = FARMReader(model_name_or_path="xlm-roberta-base", use_gpu=False)
        querying_pipeline = Pipeline()

        querying_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
        querying_pipeline.add_node(component=reader, name="Reader", inputs=["Retriever"])

        return querying_pipeline

    def get_answer(self, query: str):
        querying_pipeline = self.init_document_store()
        prediction = querying_pipeline.run(
            query=query,
            params={
                "Retriever": {"top_k": 5},
                "Reader": {"top_k": 3}
            }
        )

        return prediction

    def split_for_docs(self, df, kno):
        texts = []
        split_req = re.split('\d', df.columns[4])

        req_text = {1: f"{split_req[0][:-1]}{split_req[1][:-2]}",
                    0: f"{split_req[0][:-1]}{split_req[2][:-1]}"}
        split_methods = re.split('\d+', df.columns[8])
        methods_text = {}

        for i in range(1, 9):
            methods_text[i] = f"{split_methods[0][:-1]} {split_methods[i]}"

        docs = ""
        responsibility = ""
        header = ""
        sub_header = ""
        id_doc = ""
        rec_type = ""
        npa = ""
        npa_period = ""
        meth_type = ""
        tail_msg = {}
        for idx, row in df.iterrows():
            if idx < df.shape[0] - 1:
                next_row = df.iloc[idx + 1]
            if pd.notnull(row[df.columns[2]]):
                header = f"{row[df.columns[2]]}"
            if (idx < df.shape[0] - 1) and pd.isna(next_row[df.columns[2]]) and pd.notnull([row[df.columns[2]]]):
                continue
            if pd.notnull(row[df.columns[3]]):
                sub_header = f"{row[df.columns[3]]}"
                id_doc = f"{row[df.columns[0]]}"
                tail_msg = {}
                for i in range(21, 27):
                    if pd.notnull(row[df.columns[i]]):
                        tail_msg[df.columns[i]] = f"{row[df.columns[i]]}"
            if pd.notnull(row[df.columns[4]]):
                rec_type = f"{req_text[int(row[df.columns[4]])]}"
            if pd.notnull(row[df.columns[8]]):
                meth_type = f"{methods_text[int(row[df.columns[8]])]}"
            if pd.notnull(row[df.columns[5]]):
                npa = f"{row[df.columns[5]]}"
            if pd.notnull(row[df.columns[6]]):
                if row[df.columns[6]]:
                    npa_period = f"действует с: {row[df.columns[6]]}"
            for i in range(9, 13):
                doc_rec = ""
                if pd.notnull(row[df.columns[i]]):
                    if [i] == 9:
                        doc_rec += f"документ: {row[df.columns[i]]} "
                    if [i] == 10:
                        doc_rec += f"выдающие органы: {row[df.columns[i]]} "
                    if [i] == 11:
                        doc_rec += f"кно может получить: {row[df.columns[i]]} "
                    if [i] == 11:
                        doc_rec += f"срок действия документов: {row[df.columns[i]]} "
                if doc_rec:
                    docs += doc_rec + ";\n"
            for i in range(13, 21):
                res_rec = ""
                if pd.notnull(row[df.columns[i]]):
                    if i == 13:
                        res_rec += f"ответсвенность: {row[df.columns[i]]} "
                    else:
                        res_rec += f" {row[df.columns[i]]} "
                    #     h = df.columns[i]
                if res_rec:
                    responsibility += f" {res_rec};"

            if ((idx < df.shape[0] - 1) and pd.notnull(next_row[df.columns[5]])) or (idx == df.shape[0] - 1):
                ### content для таблицы
                content = f"{header}\n{sub_header}\n{rec_type}\n{npa}\n{npa_period}\n{meth_type}\n{docs}\n{responsibility}".lower()

                tail_msg['КНО'] = kno
                d = Document(
                    content=content,
                    content_type='text',
                    id=f"{id_doc}",
                    meta=tail_msg,
                    score=None
                )

                ###Id документа для удаления из documentStore

                texts.append(d)
                docs = ""
                responsibility = ""
                tail_msg = {}
        return texts

    def preprocess_docs(self):
        docs = []

        def tail_preprocess_docs(p, kno_tail):
            nonlocal docs
            for filename in os.listdir(p):
                file = os.path.join(p, filename)
                if os.path.isdir(file):
                    tail_preprocess_docs(file, kno_tail)
                if os.path.isfile(file):
                    if os.path.splitext(file)[-1].lower() == ".xlsx":
                        xls_tail = pd.ExcelFile(file)
                        df_tail = xls_tail.parse(skiprows=1)
                        df_tail.rename(columns={df_tail.columns[0]: 'id', df_tail.columns[1]: '№'}, inplace=True)
                        split_docs = self.split_for_docs(df_tail, kno_tail)
                        docs += split_docs

        for fn in os.listdir(self.path):
            kno = fn
            f = os.path.join(self.path, fn)
            if os.path.isdir(f):
                tail_preprocess_docs(f, kno)
            if os.path.isfile(f):
                if os.path.splitext(f)[-1].lower() == ".xlsx":
                    xls = pd.ExcelFile(f)
                    df = xls.parse(skiprows=1)
                    df.rename(columns={df.columns[0]: 'id', df.columns[1]: '№'}, inplace=True)
                    docs += self.split_for_docs(df, kno)

        ds = self.preprocessor.process(docs)
        return ds
