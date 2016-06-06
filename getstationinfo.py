from tinydb import TinyDB, Query
from config import SL_HPL2_KEY
import json
import httplib2
http = httplib2.Http()
db = TinyDB('db.json')
sitestable = db.table('sites')
sitestable.purge()
sitesarr = []
url = 'http://api.sl.se/api2/LineData.json?model=site&key=' + SL_HPL2_KEY
resp, content = http.request(url)
sites = json.loads(str(content, 'utf8'))
sites = sites['ResponseData']['Result']
for index, site in enumerate(sites):
	sitename = site['SiteName']
	siteobj = {'name': sitename, 'id': site['SiteId']} 
	sitesarr.append(siteobj)
	print(index, site)
sitestable.insert_multiple(sitesarr)
print ('finished OK!')
exit()