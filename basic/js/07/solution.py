s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
s = s[::-1]
sol = []
sol.append(s[42])
sol.append(s[11])
sol.append(s[17])
sol.append(s[12])
sol.append(s[7])
sol.append(s[43])
sol.append(s[6])
result = "_".join(sol)
print(result)
