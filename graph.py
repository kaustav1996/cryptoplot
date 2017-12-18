import plotly as py
import plotly.graph_objs as go
import csv
import time
import datetime
import urllib
import update_csv
import os, fnmatch
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
def update():
    update_csv.update1()
    with open('time.txt','wb') as time_file:
        time_file.write(current_date)
    time.sleep(10)
now = datetime.datetime.now()
current_date=str(now.year)+"-"+str(now.month)+"-"+str(now.day)
with open('time.txt') as time_file:
	if(str(time_file.readline())!=current_date):
		update()
btcprice=list()
ethprice=list()
bchprice=list()
xrpprice=list()
ltcprice=list()
day=list()
x="C:/data/"
import os

os.chdir(x)
with open('btc-eur-max.csv') as csvin:
	readfile=csv.reader(csvin, delimiter=",")
	for row in readfile:
		btcprice.append(row[1])
		day.append(row[0])
btcprice=btcprice[::-1]
btcprice=btcprice[0:30]
btcprice=btcprice[::-1]
with open('eth-eur-max.csv') as csvin:
	readfile=csv.reader(csvin, delimiter=",")
	for row in readfile:
		ethprice.append(row[1])
ethprice=ethprice[::-1]
ethprice=ethprice[0:30]
ethprice=ethprice[::-1]
with open("bch-eur-max.csv") as csvin:
	readfile=csv.reader(csvin, delimiter=",")
	for row in readfile:
		bchprice.append(row[1])
bchprice=bchprice[::-1]
bchprice=bchprice[0:30]
bchprice=bchprice[::-1]
with open("dash-eur-max.csv") as csvin:
	readfile=csv.reader(csvin, delimiter=",")
	for row in readfile:
		xrpprice.append(row[1])
xrpprice=xrpprice[::-1]
xrpprice=xrpprice[0:30]
xrpprice=xrpprice[::-1]
with open('ltc-eur-max.csv') as csvin:
	readfile=csv.reader(csvin, delimiter=",")
	for row in readfile:
		ltcprice.append(row[1])
ltcprice=ltcprice[::-1]
ltcprice=ltcprice[0:30]
ltcprice=ltcprice[::-1]
day=day[::-1]
day=day[0:30]
day=day[::-1]
trace0 = go.Scatter(
    x = day,
    y = btcprice,
    name = 'Bitcoin',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
trace1 = go.Scatter(
    x = day,
    y = ethprice,
    name = 'Ethereum',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)
trace2 = go.Scatter(
    x = day,
    y = bchprice,
    name = 'Bitcoin Cash',
    line = dict(
        color = ('rgb(100, 50, 24)'),
        width = 4)
)

trace3 = go.Scatter(
    x = day,
    y = xrpprice,
    name = 'Dash',
    line = dict(
        color = ('rgb(22, 200, 20)'),
        width = 4)
)

trace4 = go.Scatter(
    x = day,
    y = ltcprice,
    name = 'Litecoin',
    line = dict(
        color = ('rgb(205, 125, 204)'),
        width = 4)
)
data = [trace0 , trace1 , trace2 , trace3 , trace4]
layout = dict(title = 'Crypto-currency price compare (last 30 days)',
              xaxis = dict(title = 'Day'),
              yaxis = dict(title = 'Price ( pound )'),
              )

fig = dict(data=data, layout=layout)
py.offline.plot(fig, filename='styled-line')
