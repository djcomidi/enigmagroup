from PIL import Image
from io import BytesIO
from urllib import request

BASE_URL = "http://www.enigmagroup.org/missions/dev/urandom/1/"
NOTE_PNG = "note.png"
NOTE_URL = BASE_URL + NOTE_PNG

imgAbytes = BytesIO(request.urlopen(NOTE_URL).read())
imgA = Image.open(imgAbytes)
data = list(imgA.getdata())
newdata = []
for d in data:
    if d == (21, 21, 22, 255):
        newdata.append((255, 255, 255))
    else:
        newdata.append((0, 0, 0))
imgB = Image.new("RGB", imgA.size)
imgB.putdata(newdata)
imgB.save('note.png')
print("Enhanced picture saved as note.png")
print("Download " + BASE_URL + "<secret_file>")
print("Execute it (with wine it gave me some errors)")
print("(it seems to check whether it is in c:\\windows\\system32\\)")
print("It produces 2 new files, one containing the password")
