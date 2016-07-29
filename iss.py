import requests
from datetime import datetime
import webbrowser

# get ISS position data
response = requests.get('http://api.open-notify.org/iss-now.json')
pos = response.json()

lat = pos['iss_position']['latitude']
lon = pos['iss_position']['longitude']
when = datetime.now()
google_url = "http://maps.google.com/maps/search/@%.5f,%.5f,5z" % (lat, lon)

print('ISS Location For for %s Lat: %.2f Long: %.2f' % (when.strftime("%d %b %Y %H:%M:%S"),lat,lon))
print("Location on Google Maps: ", google_url)
webbrowser.open(google_url)
