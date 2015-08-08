from PIL import Image

imgA = Image.open('note.png')
print(list(imgA.getcolors()))
data = list(imgA.getdata())
newdata = []
for d in data:
	if d == (21,21,22,255): newdata.append((255,255,255))
	else: newdata.append((0,0,0))
imgB = Image.new("RGB",imgA.size)
imgB.putdata(newdata)
imgB.save('noteB.png')

