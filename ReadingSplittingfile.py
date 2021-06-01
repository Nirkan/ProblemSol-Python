

fp = open("sampletext.txt")
data = fp.read()

print(data)

lines = data.split("\n")

for line in lines:
	words = line.split(" ")
	for word in words:
		print(word)

fp.close()
