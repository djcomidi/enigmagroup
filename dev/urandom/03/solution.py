import re
from urllib import request
from eg_utils import get_login_cookie

COOKIE = get_login_cookie()
URL="http://www.enigmagroup.org/missions/dev/urandom/3/"

opener = request.build_opener()
opener.addheaders.append( COOKIE )
data = opener.open(URL).read()
colors = re.findall('(?<=td bgcolor\=\").{6}', data)
KEY = re.search('(?<=KEY)[1-6]+', data)
keys = list(map( int, list(KEY.group()) ))
sol = ""
for i in range(len(colors)):
	sol += colors[i][keys[i]-1]
print(sol)
