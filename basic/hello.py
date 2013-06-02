import sys

def Cat(filename):
	#you should have to provide complete directory location with filename
	#else no file error appears
	f = open(filename,'rU')
	#for line in f:
	#	print line,
	text = f.read()
	print text,
	#lines = f.readlines()
	#print lines

	f.close()


def main():
	Cat(sys.argv[1])

if __name__ == '__main__':
	main()