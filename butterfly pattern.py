length = int(input("Enter number of rows:"))
#upper selection
for i in range(length):
	for j in range(i):
		print("*",end=" ")

	for k in range(2*(length-i)):
		print(" ",end=" ")

	for l in range(i):
		print("*",end=" ")


	print() #for new line

# lower section
for i in range(length):
	for j in range((length-1)-i+1):
		print("*",end=" ")

	for k in range(2*i):
		print(" ",end=" ")

	for l in range((length-1)-i+1):
		print("*",end=" ")

	print() #for new line