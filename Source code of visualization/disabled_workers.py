import pymongo
import plotly.graph_objs as go

ip = ''
port = 

# Connect MongoDB
connection = pymongo.MongoClient(ip, port)

# Connect MongoDB Database
database = connection.get_database('bigdata')

# Connect MongoDB Database Collection
collection = database.get_collection('workers')

result1 = collection.aggregate([
    {'$group':{'_id':"null",'total_count':{'$sum':1}}}
])
for i in result1:
    print(i['total_count'])

#aggregate Data
result = collection.aggregate([
    {'$group':{'_id':"$장애유형",'count':{'$sum':1}}}
])
kind_list=[]
count_list=[]

for i in result:
    kind_list.append(i['_id'])
    count_list.append(i['count'])


destinations = kind_list
percent = count_list
data = [go.Pie(
    labels = destinations,
    values = percent,
    pull = [0,0,0,0,0],
)]

fig = go.Figure(data=data)
fig.update_layout(
    title={
        'text': "Status of Disabled Worker(2020)",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    plot_bgcolor='#FFFFFF'
)
fig.show()
