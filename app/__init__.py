from flask import Flask
import os
from config import basedir
import re
from datetime import datetime
from time import strftime

app = Flask(__name__)
app.config.from_object('config')

@app.template_filter()
def dateFormat(value):
	return value.strftime('%Y-%m-%d %H:%M')

@app.template_filter()
def sortDeparture(dt):
	nowlist = []
	minlist = []
	timelist = []
	for entry in dt:
		if entry['DisplayTime'] == 'Nu':
			nowlist.insert(0, entry)
		elif re.match(r'^[0-9]+ min$', entry['DisplayTime']):
			if len(minlist) == 0:
				minlist.append(entry)
			else:
				for index, item in enumerate(minlist):
					time1 = entry['DisplayTime'].split(' ')
					time2 = item['DisplayTime'].split(' ')
					if int(time1[0]) < int(time2[0]):
						minlist.insert(index, entry)
						break;
				if entry not in minlist:
					minlist.append(entry)
		elif re.match(r'^[0-2][0-9]:[0-5][0-9]$', entry['DisplayTime']):
			if len(timelist) == 0:
					timelist.append(entry)
			else:
				for index, item in enumerate(timelist):
					date1 = datetime.strptime(entry['DisplayTime'], '%H:%M')
					date2 = datetime.strptime(item['DisplayTime'], '%H:%M')
					if date1 < date2:
						timelist.insert(index, entry)
						break;
				if entry not in timelist:
					timelist.append(entry)
	return nowlist + minlist + timelist

app.jinja_env.filters['sortDeparture'] = sortDeparture
app.jinja_env.filters['dateFormat'] = dateFormat

from app import views