from gmpy import next_prime

N=25777
E=3
P=2
while N%P != 0:
	P = int(next_prime(P))
Q=N//P
PHI_N=(P-1)*(Q-1)
D=PHI_N//3
while (D*E)%PHI_N != 1:
	D += 1
print("E=%d N=%d P=%d Q=%d PHI_N=%d D=%d" % (E,N,P,Q,PHI_N,D))

encMsg="07484 14541 07484 14541 14541 14541 07484 14541 07484 07484 14541 07484 14541 14541 07484 14541 14541 07484 07484 14541 07484 07484 07484 14541 14541 07484 07484 07484 14541 14541 14541 14541 14541 14541 07484 14541 14541 07484 07484 14541 07484 07484 07484 14541 07484 07484 14541 14541 07484 14541 07484 07484 07484 14541 07484 07484 14541 14541 14541 14541 07484 14541 14541 07484 14541 14541 14541 07484 07484 07484 14541 07484 14541 07484 14541 14541 14541 07484 07484 07484"
stepA=list(map( int, encMsg.split() ))
print(stepA)
print("A->B Decrypt RSA message")
stepB=[]
for v in stepA:
	stepB.append( pow(v,D,N) )
print(stepB)
print("B->C Convert to characters")
stepC = ''.join( map( chr, stepB ) )
print(stepC)
print("C->D Split in half and xor")
stepD = ""
for i in range(40):
	if stepC[i] == stepC[i+40]: stepD += "0"
	else: stepD += "1"
print(stepD)
print("D->E Divide in groups of 8 and convert to characters")
stepE = ""
for i in range(0,len(stepD),8):
	stepE += chr(int(stepD[i:i+8],2))
print(stepE)
