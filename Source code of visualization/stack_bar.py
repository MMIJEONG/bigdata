import pymongo
import plotly.graph_objects as go

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
    {'$group':{'_id':"$장애유형",'count':{'$sum':1}}}
])

disabled_kind=[]
for i in result:
    disabled_kind.append(i['_id'])

result1 = collection.aggregate([
    {'$group':{'_id':"$품목",'count':{'$sum':1}}}
])

device_kind=[]
for i in result1:
    device_kind.append(i['_id'])
print(device_kind)#보조공학기기 유형

arr=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

k=0

for i in device_kind:
    for j in disabled_kind:
        result2 = list(collection.aggregate([
            {'$match': {'품목': i}},
            {'$match': {'장애유형': j}},
            {'$group': {'_id': 'null', 'count': {'$sum': 1}}}
        ]))
        if result2:
            for t in result2:
                arr[k].append(t['count'])
        else:
            w=0
            arr[k].append(w)
    k+=1

print(arr)



x=disabled_kind #장애유형

fig = go.Figure(go.Bar(x=x, y=arr[0], name=device_kind[0]))
fig.add_trace(go.Bar(x=x, y=arr[1], name=device_kind[1]))
fig.add_trace(go.Bar(x=x, y=arr[2], name=device_kind[2]))
fig.add_trace(go.Bar(x=x, y=arr[3], name=device_kind[3]))
fig.add_trace(go.Bar(x=x, y=arr[4], name=device_kind[4]))
fig.add_trace(go.Bar(x=x, y=arr[5], name=device_kind[5]))
fig.add_trace(go.Bar(x=x, y=arr[6], name=device_kind[6]))
fig.add_trace(go.Bar(x=x, y=arr[7], name=device_kind[7]))
fig.add_trace(go.Bar(x=x, y=arr[8], name=device_kind[8]))
fig.add_trace(go.Bar(x=x, y=arr[9], name=device_kind[9]))
fig.add_trace(go.Bar(x=x, y=arr[10], name=device_kind[10]))
fig.add_trace(go.Bar(x=x, y=arr[11], name=device_kind[11]))
fig.add_trace(go.Bar(x=x, y=arr[12], name=device_kind[12]))
fig.add_trace(go.Bar(x=x, y=arr[13], name=device_kind[13]))
fig.add_trace(go.Bar(x=x, y=arr[14], name=device_kind[14]))
fig.add_trace(go.Bar(x=x, y=arr[15], name=device_kind[15]))
fig.add_trace(go.Bar(x=x, y=arr[16], name=device_kind[16]))
fig.add_trace(go.Bar(x=x, y=arr[17], name=device_kind[17]))
fig.add_trace(go.Bar(x=x, y=arr[18], name=device_kind[18]))
fig.add_trace(go.Bar(x=x, y=arr[19], name=device_kind[19]))
fig.add_trace(go.Bar(x=x, y=arr[20], name=device_kind[20]))
fig.add_trace(go.Bar(x=x, y=arr[21], name=device_kind[21]))
fig.add_trace(go.Bar(x=x, y=arr[22], name=device_kind[22]))
fig.add_trace(go.Bar(x=x, y=arr[23], name=device_kind[23]))
fig.add_trace(go.Bar(x=x, y=arr[24], name=device_kind[24]))
fig.add_trace(go.Bar(x=x, y=arr[25], name=device_kind[25]))
fig.add_trace(go.Bar(x=x, y=arr[26], name=device_kind[26]))


fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'},
    title={
        'text': "Supported assistive engineering devices depending on the type of disability",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    })
fig.show()
