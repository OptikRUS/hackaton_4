import openpyxl

from ..models import Supervisor, Supervision


def fill_supervisor_and_supervision() -> None:
    workbook = openpyxl.load_workbook('counseling/fixtures/files/kno_and_views.xlsx')
    supervisors = workbook['Перечень КНО г. Москвы']
    for row in supervisors.iter_rows(values_only=True):
        if type(row[0]) is int:
            supervisor_id: int = row[0]
            supervisor_name: str = row[1]
            supervision_name: str = row[2]
            supervisor: Supervisor = Supervisor.objects.update_or_create(id=supervisor_id, name=supervisor_name)
            Supervision.objects.update_or_create(
                name=supervision_name, supervisor=supervisor[0]
            )
        elif row[0] is None:
            supervision_name: str = row[2]
            Supervision.objects.update_or_create(
                name=supervision_name, supervisor=supervisor[0]
            )
