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
    {'$group':{'_id':"$관할지사",'total_money':{'$sum':'$기준금액(원)'}}}
])


branch_list=[]
money_list=[]


for i in result:
    branch_list.append(i['_id'])
    money_list.append(i['total_money'])

branch = branch_list
money = money_list
tran_money=[]
for i in money:
    tran_money.append(format(i,',')+'원')

trace1 = go.Bar(
    x = branch,
    y = money,
    name = '지원금액(원)',
    marker = dict(
        #color = 'rgb(49,130,189)',
        #color = 'rgb(204,204,204)',
        color = 'rgb(153,153,153)',
       opacity = 0.7
    ),
    text = tran_money,
    textposition = 'outside',
)


data = [trace1]
layout = go.Layout(barmode = 'group')

fig = go.Figure(data = data, layout = layout)
fig.update_layout(
    title={
        'text': "Budget used to support assistive engineering devices by region",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    plot_bgcolor='#FFFFFF'
)
fig.update_yaxes(visible=False)
fig.show()










