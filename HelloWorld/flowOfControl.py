#Austin Ingraham
#Practice with loops, conditionals, other such flow-of-control syntax

import sys

def main():
	x = 5
	if(x < 6):
		#for loop
		string = "hello"
		for s in string:
			print(s)
		print()
		 
		#printing strings using index
		string = "world"
		for i in range(len(string)):
			print(string[i], end=" ")

			for n in range(i + 1, len(string)):
				print(string[n], end=" ")
			print()
	
		#numerically, what does range(len(string)) give?
		array = range(len(string))
		for i in array:
			print(i, end=" ")
		print()
		
		#while loops
		while(x <= 10):
			print(x, end=", ")
			x += 1
		print("\n")
		arrays()
		
	else:
		print(x, "is not less than six!")
	
def arrays():
	array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	for row in array:
		for col in row:
			print(col, end=" ")
		print()
	print()
	#need to figure out how to do this properly
	
main()