from django.db.models import Q

from .models import EatBaby
from .models import SleepBaby
from datetime import datetime


def form_context_for_eat():
    """Формирование данных для графика, который дает информацию о пищи."""
    month = datetime.now().month

    eats_baby = EatBaby.objects.filter(
        datetime_when_eat__month=month
    )

    list_num_days = set([eat_baby.datetime_when_eat.day for eat_baby in eats_baby])
    count_eats = []

    for num_day in list_num_days:
        count_eat = eats_baby.filter(
            datetime_when_eat__day=num_day
        ).count()
        count_eats.append(count_eat)

    return {'x': list(list_num_days), 'y': count_eats}


def form_sleep(start_hour, start_minute, end_hour, end_minute):
    """Формирует информацию о сне."""
    month = datetime.now().month

    sleeps_baby = SleepBaby.objects.filter(
        datetime_when_sleep__month=month
    )

    list_num_days = set([sleep.datetime_when_sleep.day for sleep in sleeps_baby])
    count_hours = []

    start_datetime = datetime(
        year=datetime.now().year,
        month=month,
        day=datetime.now().day,
        hour=start_hour,
        minute=start_minute,
    )

    end_datetime = datetime(
        year=datetime.now().year,
        month=month,
        day=datetime.now().day,
        hour=end_hour,
        minute=end_minute,
    )

    for num_day in list_num_days:
        eats_sleep = SleepBaby.objects.filter(
            Q(datetime_when_sleep__range=(start_datetime, end_datetime)) |
            Q(datetime_when_sleep__day=num_day)
        )

        # алгоритм расчета количества сна
        # 1) вычитаем время когда не спит и спит
        # 2) аппендим часы когда все посчитали

        hours_sleep = 0

        for eat_sleep in eats_sleep:
            when_sleep_hours = eat_sleep.datetime_when_sleep.hour if eat_sleep.datetime_when_sleep.hour else 0
            not_sleep_hours = eat_sleep.datetime_when_not_sleep if eat_sleep.datetime_when_not_sleep else 0

            hours_sleep += abs(when_sleep_hours - not_sleep_hours)

        count_hours.append(hours_sleep)

    return {'x': list(list_num_days), 'y': count_hours}
