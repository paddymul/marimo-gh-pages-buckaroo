import marimo

__generated_with = "0.11.22"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
async def _():
    import micropip
    await micropip.install("buckaroo")
    import pandas as pd
    import numpy as np
    from buckaroo import BuckarooInfiniteWidget
    return BuckarooInfiniteWidget, np, pd


@app.cell
def _(np, pd):
    ROWS2 = 340_000
    df1 = pd.DataFrame(
        {
            "int_col2": np.random.randint(1, 50, ROWS2),
            "float_col2": np.random.randint(1, 30, ROWS2) / 0.7,
            "str_col2": ["foobar"] * ROWS2,
        }
    )
    df2 = pd.DataFrame(
        {
            "88888": np.random.randint(1, 30, ROWS2) / 0.7,
            "float_col3332": np.random.randint(1, 30, ROWS2) / 0.7,
            "str_col2": ["df2"] * ROWS2,
        }
    )

    df3 = pd.DataFrame(
        {
            "constant": ["df2"] * ROWS2,
            "8asdfa": np.random.randint(1, 30, ROWS2) / 0.7,
            "3234": np.random.randint(1, 30, ROWS2) / 0.7,
            "str_col2": ["df3"] * ROWS2,
        }
    )
    return ROWS2, df1, df2, df3


@app.cell
def _(df1, df2, df3, mo):
    dfs = {"a":df1, "b":df2, "c":df3}
    dropdown_dict = mo.ui.dropdown(
        options=dfs,
        value="b",
        label="Choose the Dataset",
    )
    return dfs, dropdown_dict


@app.cell
def _(BuckarooInfiniteWidget, dropdown_dict, mo):
    mo.vstack(
        [
            dropdown_dict,
            #mo.ui.text(value=dropdown_dict.value),
            BuckarooInfiniteWidget(dropdown_dict.value)
        ]
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
