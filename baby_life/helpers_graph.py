import plotly.graph_objects as go
import plotly
from .helpers_data import form_context_for_eat, form_sleep


def form_graph_eat():
    """Возвращает график с едой."""

    fig_eat = go.Figure(
        data=[go.Bar(x=form_context_for_eat()['x'], y=form_context_for_eat()['y'])],
        layout_title_text="График употребления пищи"
    )
    graph_div_eat = plotly.offline.plot(fig_eat, auto_open=False, output_type="div")

    return graph_div_eat


def form_graph_sleep_hours():
    """Сколько часов спит."""

    data_sleep = form_sleep(
        start_hour=6,
        start_minute=0,
        end_hour=20,
        end_minute=0
    )

    fig_sleep = go.Figure(
        data=[go.Bar(
            x=data_sleep['x'],
            y=data_sleep['y']
        )],
        layout_title_text="Количество сна в световой день (с 6:00-20:00)"
    )
    graph_div_sleep = plotly.offline.plot(fig_sleep, auto_open=False, output_type="div")

    return graph_div_sleep


def form_graph_not_sleep_hours():
    """Сколько часов не спит."""

    data_sleep = form_sleep(
        start_hour=0,
        start_minute=0,
        end_hour=23,
        end_minute=59
    )

    fig_not_sleep = go.Figure(
        data=[go.Bar(x=data_sleep['x'], y=data_sleep['y'])],
        layout_title_text="Количество сна за сутки"
    )
    graph_div_not_sleep = plotly.offline.plot(fig_not_sleep, auto_open=False, output_type="div")

    return graph_div_not_sleep
