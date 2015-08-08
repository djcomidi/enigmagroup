import sys

ABC = "abcdefghijklmnopqrstuvwxyz"
TARGET = 248410397744610

def find_passwords(t=TARGET,passw=""):
	if t < 27:
		passw = ABC[t-1] + passw
		print(passw)
		return
	r = t % 17
	find_passwords( (t-r)//17, ABC[r-1]+passw )
	r += 17
	if r <= 26:
		find_passwords( (t-r)//17, ABC[r-1]+passw )

find_passwords()
