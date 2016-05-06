#Austin Ingraham
#simple Python syntax practice

import sys

def main():
	print("Hello world!")
	helloTest()
	print("Printing on same line works...", end=" ")
	print("like this!")
	if len(sys.argv) > 1:
		print("Number of arguments:", len(sys.argv))
		print("Hello, {}!".format(sys.argv[1]))
		
	alternateStringFormatting()

def helloTest(): 
	print("Hello Function.\nThis is a test.")	

def alternateStringFormatting():
	s = "repr\tfunction"
	print(s)
	print(repr(s))

main()