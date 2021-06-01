import pandas as pd
import plotly.express as px

df=pd.read_csv("Project103/data.csv")
fig=px.scatter(df,x="date",y="cases",color="country",title="Number Of Covid-19 Cases")
fig.show()