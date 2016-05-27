from app import app
import json
from tinydb import TinyDB, Query
import flask
import httplib2
from flask import render_template, flash, redirect, request, session
from .forms import SearchStationForm
from config import WTF_CSRF_ENABLED, SECRET_KEY, SL_HPL2_KEY, SL_R3_KEY

db = TinyDB('db.json')

http = httplib2.Http()

@app.route('/station/get', methods=['GET', 'POST'])
def getStation():
	Sites = Query()
	sitestable = db.table('sites')
	if not sitestable:
		initSL()
	searchstationform = SearchStationForm()
	resultsarr = []
	if searchstationform.validate_on_submit():
		searchquery = searchstationform.data['searchstation']
		results = sitestable.search(Sites.name.matches(searchquery))
		for result in results:
			if result not in resultsarr:
				resultsarr.append(result)
	else:
		results = False
	return render_template('getstation.html', searchstationform=searchstationform, results=resultsarr)

@app.route('/station/get/<stationid>', methods=['GET', 'POST'])
def getStationID(stationid):
	if 'hidenav' in request.args:
		hidenav = True
	else:
		hidenav = False 
	Site = Query()
	sitestable = db.table('sites')
	if not sitestable:
		initSL()
	station = sitestable.search(Site.id == stationid)[0]
	url = 'http://api.sl.se/api2/realtimedepartures.json?timewindow=20&siteid=' + stationid + '&key=' + SL_R3_KEY
	resp, content = http.request(url, headers={'Cache-Control': 'no-cache'})
	sites = json.loads(str(content, 'utf8'))
	sites = sites['ResponseData']
	return render_template('getstationid.html', json=sites, station=station, hidenav=hidenav)

@app.route('/')
def index():
	sitestable = db.table('sites')
	if not sitestable:
		initSL()
	return redirect(flask.url_for('getStation'))


def initSL():
	sitestable = db.table('sites')
	sitestable.purge()
	url = 'http://api.sl.se/api2/LineData.json?model=site&key=' + SL_HPL2_KEY
	resp, content = http.request(url)
	sites = json.loads(str(content, 'utf8'))
	sites = sites['ResponseData']['Result']
	for index, site in enumerate(sites):
		sitename = site['SiteName']
		siteobj = {'name': sitename, 'id': site['SiteId']} 
		sitestable.insert(siteobj)
		print(index, site)
	return None