#This is the main function app
while True:
	print "----------------------------------------------"
	print "Welcome to the generation tool"
	print "----------------------------------------------"

	print "Please select your function:"
	print "1. Postal code gen"
	print "2. Phone number gen"
	print "3. lotto number gen"
	print "Exit press 0"

	promt = raw_input("> ")
	
	if promt == "1":
		while True:
			import genpost
			genpost.post_gen()
			promt = raw_input("Want to continue? >")
			if promt == "no" or promt == "0":
				break
			else:
				continue
	elif promt == "2":
		while True:
			import  numgen 
			numgen.gen_num()
			promt = raw_input("Want to continue? >")
			if promt == "no" or promt == "0":
				break
			else:
				continue
	elif promt == "3":
		while True:
			import  lottogen  
			lottogen.lotto_gen.gen_lotto()
			promt = raw_input("Want to continue? >")
			if promt == "no" or promt == "0":
				break
			else:
				continue
	elif promt == "0":
		print "Good try, but no this code, try another!"
		continue
	elif promt == "exit" or promt == "no" or promt == "000":
		print "There you go, BINGO!!!"
		break
	else:
		print "Wrong code, Please type again!!"
		raw_input()
		continue
	
	
	