import random
password = [ '1','0','5','6', ]
name = [ 'user1','user2','user3','user4', ]
accesscode = input('...|')
if accesscode == random.choice(password) :
	print('hello, ',random.choice(name),'...')
	print('proccessing...')
