# from collections import OrderedDict
# def runLengthEncoding(input):

# 	dict=OrderedDict.fromkeys(input, 0)

# 	for ch in input:
# 		dict[ch] += 1

# 	output = ''
# 	for key,value in dict.items():
# 		output = output + key + str(value)
# 	return output

# # Driver function
# if __name__ == "__main__":
# 	input="wwwwaaadexxxxxx"
# 	print (runLengthEncoding(input))

def encode(message):
	encoded_message = ""
	i = 0

	while (i <= len(message)-1):
		count = 1
		ch = message[i]
		j = i
		while (j < len(message)-1):
			if (message[j] == message[j+1]):
				count = count+1
				j = j+1
			else:
				break
		encoded_message=encoded_message+str(count)+ch
		i = j+1
	return encoded_message
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)


