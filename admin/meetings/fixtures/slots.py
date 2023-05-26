from datetime import datetime, date, time

from counseling.models import Supervisor
from ..models import Slot


def add_slots(month: int, start_hour: int | None = 8, end_hour: int | None = 20, year: int = datetime.now().year):
    supervisors: list[Supervisor] = Supervisor.objects.all()
    for supervisor in supervisors:
        for day in range(1, 32):
            for hour in range(start_hour, end_hour):
                try:
                    slot: Slot = Slot.objects.update_or_create(
                        slot_date=date(year, month, day), slot_time=time(hour, 0), supervisor=supervisor
                    )
                    print(f"{slot} {year, month, day} создан")
                except ValueError:
                    continue
