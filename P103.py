import pandas as pd

import plotly.express as px

df = pd.read_csv("Copy+of+data+-+data (1).csv")

fig = px.line(df, x="date", y="cases", color="country", title='Covid Data')

fig.show()
