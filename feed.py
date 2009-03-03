import urllib2, threading, time, googlegeo, codecs
from elementtree.ElementTree import parse

class Feed:

    def __init__(self):
        self.feed = []
        url = "http://twitter.com/statuses/public_timeline.xml"
        self.xml = parse(urllib2.urlopen(url))
        map(self._parseNode, self.xml.getiterator('status'))
        kml = googlegeo.createKML(self.feed)
        kmlFile = codecs.open('feed.xml', 'w', "utf-8")
        kmlFile.write(unicode(kml))  
        kmlFile.close()

    def _parseNode(self, node):
        user = node.find('user')
        status = {'uname': user.find('name').text ,
                  'loc': user.find('location').text,
                  'coords': googlegeo.geocode(unicode(user.find('location').text)),
                  'status': node.find('text').text 
                 }
        print status['uname'] + ' is at: ' + status['coords'] + ". They said: \n" + status['status']
        self.feed.append(status)


f = Feed()
