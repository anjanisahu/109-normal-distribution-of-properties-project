import pandas as pd
import csv
import plotly.express as px
import plotly.graph_objects as go
import random
import statistics
import plotly.figure_factory as ff
normalDistribution=[]
property=[]
for i in range(10,1000):
    goal1=random.randint(1,100)
    goal2=random.randint(1,100)
    property.append(goal1+goal2)
    normalDistribution.append(i)


# mean nikal rhe h
mean=sum(property)/len(property)
print("THIS IS MEAN :")
print(mean)

#now median
median=statistics.median(property)
print("THIS IS MEDIAN:")
print(median)

#now for mode
mode=statistics.mode(property)
print("THIS IS MODE:")
print(mode)

#standard deviation
standard_deviation=statistics.stdev(property)
print("THIS IS STANDARD DEVIATION :")
print(standard_deviation)

fig=ff.create_distplot([property],["result"],show_hist=False)
fig.show()


