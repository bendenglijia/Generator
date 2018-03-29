#Lotto Max
#randomly generate  7 numbers from 1 to 49

class MainBody(object):
	def gen_lotto(self):
		import random
		#filename = "lottogen.txt"
		bingo = 0
		total = 0
		count = {}
		num = raw_input("How many set of lotto number you want to gen? >")
		if num.isdigit() == True:
			for x in range(1,50): 
				count[x] = 0
			for c in range(int(num)): #How many times
				l  = []
				n = []
				for i in range(1,50):
					l.append(i)
				for k in range(7):	
					p = random.choice(l)
					n.append(p)
					l.remove(p)
					count[p] +=1 
				#with open (filename, 'a') as f:
					#f.write(str(n) + "\n")
				sort_n = sorted(n)
				for k in range(7):
					print sort_n[k], 
				print "\n"
			#	if 24 in n and 25 in n and 18 in n and 4 in n:
				#	print "Bingo Your are a Billninare now!"
				#	bingo += 1
			#	else:
				#	print "You are not! Work Hard!"
		else:
			print "Value Error: Please type digit!!" 
		promt = raw_input("Do you want to analyze your result? > ")
		if promt == "yes":
			analy.analysis(num, count)	

lotto_gen = MainBody()


class Analy(MainBody):
	def analysis(self, num, count):
		self.num = num
		self.count = count
		list = []
		list_min = []
		same = 0
		same_min = 0
		max = 0
		min = num*7
		for p in range(1,50):		
			print "%d:" % p, str(count[p])	
			if max < count[p]:
				max = count[p]
				number = p
			if min > count[p]:
				min = count[p]
				number_min = p
		for i in range(1,50):
			if max == count[i] and i != number:
				same += 1
				list.append(i)
			if min == count[i] and i != number_min:
				same_min += 1
				list_min.append(i)
		if same == 0:
			print "Max appear: %d:" % number, str(max)
		else:
			list.append(number)
			print "Max appear:", list, "of", str(max)
		if same_min == 0:	
			print "min appear: %d:" % number_min, str(min)
		else:
			list_min.append(number_min)
			print "min appear:", list_min, "of", str(min)

analy = Analy()
	

		#if bingo != 0:
		#	print "Amazing! %d" % bingo '''
	

	

	

	
	
