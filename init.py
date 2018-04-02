import sys

sys.path.insert(0, './lib')

import HelloWolrd


def run():
	menu()
	option = input('Choose your option: ')
	choose(option)

def choose(value):
	if value == 1:
		HelloWolrd.main()
	elif value == 2:
	   print "2 - Not implemented"
	elif value == 3:
	   print "3 - Not implemented"
	else:
	   print "Invalid option"
	   run()


def menu():
	print("************************")
	print "Your Options"
	print("************************")
	print "1 - Hello Wolrd"
	print "2 - Not implemented"
	print "3 - Not implemented"
	print("************************")

run()
