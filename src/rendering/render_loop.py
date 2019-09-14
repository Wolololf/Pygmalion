import plotly.graph_objects as go
import numpy as np


def render():
    # Generate curve data
    t = np.linspace(-1, 1, 100)
    x = t + t ** 2
    y = t - t ** 2
    xm = np.min(x) - 1.5
    xM = np.max(x) + 1.5
    ym = np.min(y) - 1.5
    yM = np.max(y) + 1.5
    N = 50
    s = np.linspace(-1, 1, N)
    xx = s + s ** 2
    yy = s - s ** 2

    # Create figure
    fig_dict = {
        "data": [],
        "layout": {},
        "frames": []
    }

    # fill in most of layout
    fig_dict["layout"]["xaxis"] = dict(range=[xm, xM], autorange=False, zeroline=False, showticklabels=False,
                                       showgrid=False)
    fig_dict["layout"]["yaxis"] = dict(range=[ym, yM], autorange=False, zeroline=False, showticklabels=False,
                                       showgrid=False)
    fig_dict["layout"]["hovermode"] = "closest"
    fig_dict["layout"]["showlegend"] = False
    fig_dict["layout"]["sliders"] = {
        "args": [
            "transition", {
                "duration": 400,
                "easing": "cubic-in-out"
            }
        ],
        "initialValue": "0",
        "plotlycommand": "animate",
        "values": s,
        "visible": True
    }
    fig_dict["layout"]["updatemenus"] = [
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": False},
                                    "fromcurrent": True, "transition": {"duration": 300,
                                                                        "easing": "quadratic-in-out"}}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                      "mode": "immediate",
                                      "transition": {"duration": 0}}],
                    "label": "Pause",
                    "method": "animate"
                }
            ],
            "direction": "left",
            "pad": {"r": 10, "t": 87},
            "showactive": False,
            "type": "buttons",
            "x": 0.1,
            "xanchor": "right",
            "y": 0,
            "yanchor": "top"
        }
    ]

    sliders_dict = {
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 20},
            "prefix": "Step:",
            "visible": True,
            "xanchor": "right"
        },
        "transition": {"duration": 300, "easing": "cubic-in-out"},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": 0,
        "steps": []
    }

    fig_dict["data"] = [go.Scatter(x=x, y=y,
                                   mode="lines",
                                   line=dict(width=2, color="blue")),
                        go.Scatter(x=x, y=y,
                                   mode="lines",
                                   line=dict(width=2, color="blue"))]

    for k in range(N):
        frame = {"data": go.Scatter(
            x=[xx[k]],
            y=[yy[k]],
            mode="markers",
            marker=dict(color="red", size=10)), "name": str(k)}

        fig_dict["frames"].append(frame)
        slider_step = {"args": [
            [k],
            {"frame": {"duration": 300, "redraw": False},
             "mode": "immediate",
             "transition": {"duration": 0}}
        ],
            "label": k,
            "method": "animate"}
        sliders_dict["steps"].append(slider_step)

    fig_dict["layout"]["sliders"] = [sliders_dict]

    fig = go.Figure(fig_dict)
    fig.show()
