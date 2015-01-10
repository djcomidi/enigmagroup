#!/usr/bin/env python

import re
import urllib2
from eg_utils import get_login_cookie

COOKIE = get_login_cookie()
URL="http://www.enigmagroup.org/missions/dev/urandom/3/"

opener = urllib2.build_opener()
opener.addheaders.append( COOKIE )
data = opener.open(URL).read()
colors = re.findall('(?<=td bgcolor\=\").{6}', data)
KEY = re.search('(?<=KEY)[1-6]+', data)
keys = map( int, list(KEY.group()) )
sol = ""
for i in xrange(len(colors)):
	sol += colors[i][keys[i]-1]
print sol
