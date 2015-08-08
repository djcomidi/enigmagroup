from urllib import request, parse
import re
from eg_utils import get_login_cookie, get_external_ip

URL = "http://www.enigmagroup.org/missions/programming/1/"
values = {
    'ip': get_external_ip(),
    'username': 'djcomidi'
}
data = parse.urlencode(values).encode()
ck = get_login_cookie()
headers = { 'Cookie': "mission=yes; " + ck[1] }
req = request.Request(URL, data, headers)
with request.urlopen(req) as f:
    data = f.read().decode()
lines = data.split('\n')
print(lines[15])


