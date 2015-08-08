p1 = "bewareoftheenigmagroupunderground"
p2 = "betterofftohacktherealownersboxes"
p3 = "wassaidbyadudepseudodpsychomarine"

sol = ""
for i in range(len(p1)):
    if p1[i] == p3[i]:
        sol += p1[i]
    if p1[i] == p2[i]:
        sol += p1[i]
    if p2[i] == p3[i]:
        sol += p2[i]
print(sol)
