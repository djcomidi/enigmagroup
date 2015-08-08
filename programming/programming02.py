from urllib import request, parse
import re
from eg_utils import get_login_cookie, get_external_ip

URL = "http://www.enigmagroup.org/missions/programming/2/"
values = {
    'ip': get_external_ip(),
    'username': 'djcomidi'
}
ck = get_login_cookie()
headers = {
    'Cookie': "mission=yes; " + ck[1]
}
data = parse.urlencode(values).encode()
req = request.Request(URL, data, headers)
data = request.urlopen(req).read().decode()
random_number = int(re.search("random number (\d*) by", data).group(1))
e_number = re.search("E\[number\]\" value=\"(\d*)\"", data).group(1)
e_time = re.search("E\[time\]\" value=\"(\d*)\"", data).group(1)
hash = re.search("hash\" value=\"(.*)\"", data).group(1)

# print(data)
print(random_number, e_number, e_time, hash)

values = {'answer': str(4 * random_number),
          'E[number]': e_number,
          'E[time]': e_time,
          'hash': hash,
          'submit': 'Submit Answer'}
data = parse.urlencode(values).encode()
req = request.Request(URL, data, headers)
lines = request.urlopen(req).read().decode().split('\n')
for line in lines:
    if 'ission' in line:
        print(line)
