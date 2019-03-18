from datetime import datetime
import time
import pymongo

import plotly 
plotly.tools.set_credentials_file(username='ID', api_key='API_KEY')

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from pandas import DataFrame as df

now = datetime.now()
conn = pymongo.MongoClient('MongoDBIP',27017)

db = conn.get_database('stream_db') #데이터베이스 선택
collection = db.get_collection('hyundai_stock') # 테이블 선택

df_realtime = df(columns=("시간","주가", "전체시간"))

documents = collection.find({"year":now.year,"month":now.month, "day":now.day})

for document in documents:
    df_realtime = df_realtime.append({'주가': document['가격'],
                                      '시간':  datetime.strptime(str(document['allTime']),'%Y%m%d%H%M%S'),
                                      '전체시간': str(document['hour']) +'시 '+ str(document['minute']) +'분 '+ str(document['second']) + '초'
                                     },
                                     ignore_index=True)

df_realtime = df_realtime.sort_values(["시간"], ascending=[False])
df_realtime = df_realtime.reset_index(drop=True)

print(df_realtime.head())
# # # 시계열 이미지

trace_high = go.Scatter(
    x=df_realtime['시간'],
    y=df_realtime['주가'],
    name = "주가",
    line = dict(color = '#17BECF'),
    opacity = 0.8)
data = [trace_high]

layout = dict(
    title='현대정보기술 주가변동 현황',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename = "현대정보기술 주가변동 현황")

