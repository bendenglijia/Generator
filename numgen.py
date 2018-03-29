from random import randint
from random import choice

def gen_num():
	i = []
	num = raw_input("How many phone number you want to gen? >")
	if num.isdigit() == True:
		#filename = 'example.txt'
		for a in range(int(num)):
			i.append(choice([647,416, 437, 519,226,548,613,343,705,249,807,905,289,365]))
			for b in range(7):
				i.append(randint(0,9))
			#with open(filename, 'a') as f:
				#f.write( "(%d) - %d%d%d - %d%d%d%d \n" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
			print "(%d) - %d%d%d - %d%d%d%d" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
			i = []
	else:
		print "ValueError: Please type digit!!"
