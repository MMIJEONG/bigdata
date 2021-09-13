import pandas as pd
import folium
import webbrowser
import pymongo,json

state_geo = ''

ip = ''
port =

# Connect MongoDB
connection = pymongo.MongoClient(ip, port)

# Connect MongoDB Database
database = connection.get_database('bigdata')

# Connect MongoDB Database Collection
collection = database.get_collection('disabled_kind')
result1 = collection.aggregate([{'$group':{'_id':"null",'total_people_num':{'$sum':'$등록장애인수'}}}])
for i in result1:
 print(int(i['total_people_num']))

results = collection.aggregate(([{'$group':{'_id':"$통계시도명",'people_num':{'$sum':'$등록장애인수'}}}]))

si = {
 '강원도':'42',
 '경기도':'41',
 '경상남도':'48',
 '경상북도':'47',
 '광주광역시':'29',
 '대구광역시':'27',
 '대전광역시':'30',
 '부산광역시': '26',
 '서울특별시': '11',
 '세종특별자치시': '36',
 '울산광역시':'31',
 '인천광역시':'28',
 '전라남도':'46',
 '전라북도':'45',
 '제주특별자치도':'50',
 '충청남도':'44',
 '충청북도':'43'
}
data = []
for result in results:
    data.append({'id':si[result['_id']],'people_num':result['people_num']})

state_data = pd.DataFrame(data)
state_data['id'] = state_data['id'].astype(str)


with open(state_geo, 'r', encoding='euc-kr') as f:
    map_data = json.load(f)


for i in range(len(state_data)):
 for j in range(len(map_data['features'])):
  id = state_data.loc[i]['id']
  properties = map_data['features'][j]['properties']
  CTPRVN_CD = properties['CTPRVN_CD']

  if str(id) == str(CTPRVN_CD):
   people_num = state_data.loc[i]['people_num']
   properties['tooltip'] = properties['CTP_KOR_NM'] + ' : ' + format(int(people_num),',') + '명'
   map_data['features'][j]['properties'] = properties
m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)


choropleth = folium.Choropleth(
 geo_data=map_data,
 name='choropleth',
 data=state_data,
 columns=['id', 'people_num'],
 key_on='feature.properties.CTPRVN_CD',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='장애인 수 (명)'
).add_to(m)


choropleth.geojson.add_child(
 folium.features.GeoJsonTooltip(['tooltip'], labels=False)
)

m.save('folium_kr.html')
webbrowser.open_new("folium_kr.html")
