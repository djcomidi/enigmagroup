#!/usr/bin/env python

import urllib
import urllib2
import re
from eg_utils import get_login_cookie

URL="http://www.enigmagroup.org/missions/programming/2/"

opener = urllib2.build_opener()
opener.addheaders.append( get_login_cookie() )
data = opener.open(URL).read()
random_number = int(re.search( "random number (\d*) by", data ).group(1))
e_number = re.search( "E\[number\]\" value=\"(\d*)\"", data ).group(1)
e_time = re.search( "E\[time\]\" value=\"(\d*)\"", data ).group(1)
hash = re.search( "hash\" value=\"(.*)\"", data ).group(1)

print random_number, e_number, e_time, hash

values = { 'answer': str( 4 * random_number),
           'E[number]': e_number,
           'E[time]': e_time,
           'hash': hash,
           'submit': 'Submit Answer' }
data = urllib.urlencode(values)
lines = opener.open(URL,data).read().split('\n')
for line in lines:
	if 'ission' in line:
		print line
