import urllib.request
import json
from datetime import datetime
import webbrowser
 
def getiss():
    # call opennotify api
    response = urllib.request.urlopen('http://api.open-notify.org/iss-now.json')
    mydata = response.readall().decode('utf-8')
    return(mydata)
 
iss = getiss()
pos = json.loads(iss)

lat = pos['iss_position']['latitude']
lon = pos['iss_position']['longitude']
when = datetime.now()
google_url = "http://maps.google.com/maps/search/@%.5f,%.5f,5z" % (lat, lon)

print('ISS Location For for %s Lat: %.2f Long: %.2f' % (when.strftime("%d %b %Y %H:%M:%S"),lat,lon))
print("Location on Google Maps: ", google_url)
webbrowser.open(google_url)
