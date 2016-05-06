#Austin Ingraham
#simple Python syntax practice

import sys

def main():
	print("Hello world!")
	helloTest()
	print("Printing on same line works...", end=" ")
	print("Like this!")
	if len(sys.argv) > 1:
		print("Number of arguments:", len(sys.argv))
		print("Hello, {}!".format(sys.argv[1]))
	

def helloTest(): 
	print("Hello Function.\nThis is a test.")	

	

main()