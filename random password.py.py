import random
password = [ '1','0','5','6', ]
name = [ '1','1','1','1', ]
accesscode = input('...|')
if accesscode == random.choice(password) :
	print('hello, ',random.choice(name),'importing code')
	print('proccessing...')