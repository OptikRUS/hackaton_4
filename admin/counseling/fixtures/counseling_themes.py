import openpyxl

from ..models import Topic, Supervision, Supervisor


def fill_counseling_themes() -> None:
    workbook = openpyxl.load_workbook('counseling/fixtures/files/kno_and_views.xlsx')
    counseling_themes = workbook['Темы консультирования']
    for row in counseling_themes.iter_rows(values_only=True):
        if row[0].isdigit():
            supervisor_name: str = row[1]
            supervision_name: str = row[2]
            topic_name: str = row[3]
            supervisor = Supervisor.objects.filter(name__icontains=supervisor_name).first()
            supervision = Supervision.objects.filter(name__icontains=supervision_name).first()
            if supervisor and supervision:
                Topic.objects.create(name=topic_name)
