import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def draw_graph(puth="src/temp/graph.csv", max_xticks=15):
    if not os.path.exists(puth):
        return None

    df = pd.read_csv(puth, parse_dates=["date"], dayfirst=True)

    df = df[::-1]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df["date"], df["square"], marker='o')
    ax.set_title('Стоимость по датам')
    ax.set_xlabel('Дата')
    ax.set_ylabel('Площадь, кв. метров')
    ax.grid(True)

    ax.tick_params(axis='x', labelrotation=45)
    plt.subplots_adjust(bottom=0.2)

    xticks = np.linspace(0, len(df) - 1, max_xticks, dtype=int)
    ax.set_xticks(df.index[xticks])
    ax.set_xticklabels(df["date"].iloc[xticks])

    return fig
