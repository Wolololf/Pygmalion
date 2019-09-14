import random
import numpy as np
import plotly.graph_objects as go
from chart_studio.grid_objs import Grid, Column


def render(width, height, steps):
    step_sequence = range(0, steps)

    grid, zmax = create_grid(width, height, steps)

    fig_dict = create_empty_fig_dict()

    setup_layout(fig_dict)
    setup_menu(fig_dict, step_sequence)

    fig_dict["data"] = go.Heatmap(
        x=grid.get_column('x').data,
        y=grid.get_column('y').data,
        z=grid.get_column('z1').data,
        zmin=0,
        zmax=zmax[0],
        zsmooth=False)

    fig_dict["frames"] = [dict(data=go.Heatmap(
        z=grid.get_column('z{}'.format(k + 1)).data,
        zmin=0,
        zmax=zmax[k],
        zsmooth=False),
        traces=[0],
        name=str(k))
        for k in step_sequence]

    fig_dict["layout"]["sliders"] = [create_sliders_dict(step_sequence)]

    fig = go.Figure(fig_dict)
    fig.show()


def create_empty_fig_dict():
    return {
        "data": [],
        "layout": {},
        "frames": []
    }


def setup_layout(fig_dict):
    fig_dict["layout"]["xaxis"] = dict(autorange=False, zeroline=False, showticklabels=False)
    fig_dict["layout"]["yaxis"] = dict(autorange=False, zeroline=False, showticklabels=False, scaleanchor="x", scaleratio=1)
    fig_dict["layout"]["hovermode"] = "closest"
    fig_dict["layout"]["showlegend"] = False


def setup_menu(fig_dict, step_sequence):
    fig_dict["layout"]["sliders"] = {
        "args": [
            "transition", {
                "duration": 400,
                "easing": "cubic-in-out"
            }
        ],
        "initialValue": "0",
        "plotlycommand": "animate",
        "values": step_sequence,
        "visible": True
    }

    fig_dict["layout"]["updatemenus"] = [
        {
            "buttons": [
                {
                    "args": [None, {"frame": {"duration": 500, "redraw": True},
                                    "fromcurrent": True, "transition": {"duration": 0,
                                                                        "easing": "quadratic-in-out"}}],
                    "label": "Play",
                    "method": "animate"
                },
                {
                    "args": [[None], {"frame": {"duration": 0, "redraw": True},
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


def create_grid(width, height, steps):
    zmax = []
    columns = [Column(np.linspace(0, width, width), 'x'), Column(np.linspace(0, height, height), 'y')]
    for k in range(steps):
        z = [[create_heatmap_entry() for x in range(0, width)] for y in range(0, height)]
        columns.append(Column(z, 'z{}'.format(k + 1)))
        zmax.append(np.max(z))
    return Grid(columns), zmax


def create_sliders_dict(step_sequence):
    return {
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
        "steps": [{"args": [
            [k],
            {"frame": {"duration": 300, "redraw": True},
             "mode": "immediate",
             "transition": {"duration": 0}}
        ],
            "label": k,
            "method": "animate"} for k in step_sequence]
    }


def create_heatmap_entry():
    return random.randint(0, 10)
