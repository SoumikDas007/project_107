import pandas as pd 
import plotly.graph_objects as px
import csv

df = pd.read_csv("data.csv")
student = df.loc[df["student_id"]=="TRL_xsl"]

print(student.groupby("level")["attempt"].mean())

graph = px.Figure(px.Bar(
            x = student.groupby("level")["attempt"].mean(), y = ["Level 1","Level 2", "Level 3", "Level 4"],orientation= "h"))

graph.show()