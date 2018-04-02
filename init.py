import sys

sys.path.insert(0, './lib')

import HelloWolrd
import Location


def run():
    menu()
    option = input('Choose your option: ')
    choose(option)
    return;

def choose(value):
    if value == 1:
        HelloWolrd.main()
    elif value == 2:
        Location.main()
    elif value == 3:
        print '3 - Not implemented'
    else:
        print 'Invalid option'
	return;

def menu():
    print '************************'
    print 'Your Options'
    print '************************'
    print '1 - Hello Wolrd'
    print '2 - Location'
    print '3 - Not implemented'
    print '************************'
    return;

run()
