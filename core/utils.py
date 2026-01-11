import plotly.graph_objs as go
from plotly.offline import plot


def build_risk_graph(recommendations):
    dates = [r.run_plan.planned_start for r in recommendations]
    risks = [r.risk_score for r in recommendations]

    if not dates:
        return "<p style='opacity:0.6'>Нет данных для отображения графика</p>"

    fig = go.Figure(
        data=[
            go.Scatter(
                x=dates,
                y=risks,
                mode="lines+markers",
                line=dict(width=3),
                marker=dict(size=8),
            )
        ]
    )

    fig.update_layout(
        title="График уровня риска",
        xaxis_title="Дата",
        yaxis_title="Риск",
        yaxis=dict(range=[0, 100]),
        template="plotly_white",
        height=400,
    )

    return plot(fig, output_type="div", include_plotlyjs=True)
