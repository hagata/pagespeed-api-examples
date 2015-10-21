import requests
from config import apikey

pagespeed = 'https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url='
options = '&strategy=mobile&key=' + apikey
testurl = 'http://hugeinc.com'

CHECK = pagespeed + testurl + options
print "Analyzing...", testurl

r = requests.get(CHECK).json()

print "\n\n Response:: \n"
print r

