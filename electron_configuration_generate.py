
elem = input(“What is the atomic number?“)
elem = int(elem)
electronconfig = “”
orbital = [“1s”, “2s,” “2p”, “3s”, “3p”, “4s”, “3d”, “4p”, “5s”, “4d”, “5p”, “6s”, “4f”, “5d”, “6p”, “7s”, “5f”, “6d”, “7p”]

# break down the electrons into valence shells s, p, d, and f
def valence (v):
	global valence
	if v[1] == “s”
		valence = 2
	else
		if v[1] == “p”
		valence = 6 
	else
		if v[1] == “d”
		valence = 10 
	else
		if v[1] == “f”
		valence = 14

for x in range(len(orbital)):
	valence(orbital[x])
	if elem == 0:
		break
	else 
		if elem >= valence:
		electronconfig = electronconfig+prefix[x]+str(electronconfig)+”” 
		elem = elem - valence
	else 
		if elem < valence:
		electronconfig = electronconfig+prefix[x]+str(elem)
		break
	print(elem)
print(electronconfig)
