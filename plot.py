# import pandas as pd

# import plotly.express as px

# df = pd.read_csv("line_chart.csv")

# fig = px.line(df, x="Year", y="Per capita income", color="Country", title='Per Capita Income')

# fig.show()


import pandas as pd
import plotly.express as px

df = pd.read_csv("Line_chart.csv")

fig = px.line(df, x = "Year", y = "Per capita income", color = "Country",title="Per Capita Income")

fig.show()