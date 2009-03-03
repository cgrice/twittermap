import urllib
import xml.dom.minidom


def geocode(address):
 # This function queries the Google Maps API geocoder with an
 # address. It gets back a csv file, which it then parses and
 # returns a string with the longitude and latitude of the address.

 # This isn't an actual maps key, you'll have to get one yourself.
 # Sign up for one here: http://code.google.com/apis/maps/signup.html
  mapsKey = 'ABQIAAAA1ORRj3__FZTZRsbd3hP75BRkCAOFX5CqsZdaq_QLTGpUBuP5GBRmKK_3LQ8kEsmVZ_2kDcYwLJmquQ'
  mapsUrl = 'http://maps.google.com/maps/geo?q='
     
 # This joins the parts of the URL together into one string.
  try:
      url = ''.join([mapsUrl,urllib.quote(address),'&output=csv&key=',mapsKey])
      coordinates = urllib.urlopen(url).read().split(',')
      coorText = '%s,%s' % (coordinates[3],coordinates[2])
      return coorText
  except:
      return ""
    
 # This retrieves the URL from Google, parses out the longitude and latitude,
 # and then returns them as a string.

def createKML(feed):
 # This function creates an XML document and adds the necessary
 # KML elements.

  kmlDoc = xml.dom.minidom.Document()
  
  kmlElement = kmlDoc.createElementNS('http://earth.google.com/kml/2.2','kml')

  kmlElement = kmlDoc.appendChild(kmlElement)

  documentElement = kmlDoc.createElement('Document')
  documentElement = kmlElement.appendChild(documentElement)

  for item in feed:
      placemarkElement = kmlDoc.createElement('Placemark')
      
      descriptionElement = kmlDoc.createElement('description')
      descriptionText = kmlDoc.createTextNode(item['status'])
      descriptionElement.appendChild(descriptionText)
      placemarkElement.appendChild(descriptionElement)
      pointElement = kmlDoc.createElement('Point')
      placemarkElement.appendChild(pointElement)
      coorElement = kmlDoc.createElement('coordinates')

      # This geocodes the address and adds it to a <Point> element.
      coorElement.appendChild(kmlDoc.createTextNode(item['coords']))
      pointElement.appendChild(coorElement)

      documentElement.appendChild(placemarkElement)

  return kmlDoc.toprettyxml(' ')
