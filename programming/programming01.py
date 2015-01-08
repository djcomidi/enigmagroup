#!/usr/bin/env python

import urllib
import urllib2
import re
from eg_utils import get_login_cookie, get_external_ip

URL="http://www.enigmagroup.org/missions/programming/1/"
values={'ip':get_external_ip(),'username':'djcomidi'}
data=urllib.urlencode(values)
opener = urllib2.build_opener()
ck = get_login_cookie()
opener.addheaders.append(('Cookie', 'mission=yes; '+ck[1]))
f = opener.open(URL,data)
data = f.read()
lines = data.split('\n')
print lines[15]
