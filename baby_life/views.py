from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
from .models import EatBaby
from .models import SleepBaby
from datetime import datetime
from .helpers_graph import form_graph_eat
from .helpers_graph import form_graph_not_sleep_hours
from .helpers_graph import form_graph_sleep_hours


def main_index(request):
    context = dict()

    graph_div_eat = form_graph_eat()
    graph_sleep = form_graph_sleep_hours()
    graph_not_sleep = form_graph_not_sleep_hours()

    return TemplateResponse(
        request,
        'main.html',
        context={
            'graph_div_eat': graph_div_eat,
            'graph_sleep': graph_sleep,
            'graph_not_sleep': graph_not_sleep,
        }
    )


@require_http_methods(['POST'])
def baby_eat(request):
    """"Срабатывает на нажатие если ребенок ест."""""
    eat_baby = EatBaby.objects.create(
            datetime_when_eat=datetime.now()
    )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@require_http_methods(['POST'])
def baby_sleep(request):
    """Срабатывает если ребенок заснул."""
    SleepBaby.objects.create(
        datetime_when_sleep=datetime.now()
    )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@require_http_methods(['POST'])
def baby_not_sleep(request):
    """Срабатывает если ребенок не спит."""
    SleepBaby.objects.create(
        datetime_when_not_sleep=datetime.now()
    )

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
