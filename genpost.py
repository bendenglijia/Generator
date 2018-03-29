import random
import string

def post_gen():
	l = []
	n = []
	num = raw_input("How many postal code you want to gen?  > ")
	if num.isdigit() == True:
		for i in range(int(num)):
			for a in range(3):
				l.append(random.choice(string.ascii_uppercase))
			for b in range(3):
				n.append(random.randint(0,9))
			print "%s%r%s %r%s%r" % (l[0], n[0], l[1], n[1], l[2], n[2])
			l = []
			n = []
	else:
		print "ValueError: Please type digit!!"