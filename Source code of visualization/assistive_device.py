import pymongo
import plotly.graph_objs as go


ip = ''
port = 

# Connect MongoDB
connection = pymongo.MongoClient(ip, port)

# Connect MongoDB Database
database = connection.get_database('bigdata')


# Connect MongoDB Database Collection
collection = database.get_collection('assistive_device')


#aggregate Data
result = collection.aggregate([
    {'$group':{'_id':"$품목",'count':{'$sum':1}}}
])

kind_list=[]
count_list=[]

for i in result:
     kind_list.append(i['_id'])
     count_list.append(i['count'])


device=kind_list
percent=count_list


# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=device, values=percent, hole=.3)])
fig.update_layout(
title={
        'text': "Support status for assistive engineering devices",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
annotations=[dict(text='Device', x=0.50, y=0.5, font_size=20, showarrow=False)])

fig.show()
