s="%41%53%43%49%49%2D%43%68%61%72%74"

sol=""
for i in range(1,len(s),3):
	sol += chr(int(s[i:i+2],16))
print(sol)

