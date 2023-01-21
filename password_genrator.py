# sobhan fbouna (sanati)
#2022/9/8
# class base 

import time 
import random
import string


class passwordgenerator(object):
	def PG1(self,q):
		print('this password only contain two type of letters (digits,symbol)')
		digits = '123456789'
		symbol = '!@#$%^&*_'
		to = digits + symbol 
		password = "".join(random.sample(to,q))
		print(password)
	def PG2(self,q):
		print('secound method :)')
		lower = string.ascii_lowercase
		upper = string.ascii_uppercase
		num = string.digits
		symbols = string.punctuation
		total = lower + upper + num + symbols
		passtemp = random.sample(total,q)
		passw="".join(passtemp)
		print(passw)
	def PG3(self,q):
		print('third method (last one ) the password is : ')
		chars = list(string.ascii_letters + string.digits + "!@#$%^&*()")
		random.shuffle(chars)
		password = []
		for i in range(q):
			password.append(random.choice(chars))
		random.shuffle(password)
		print("".join(password))




q = int(input('please enter the length of the password you want (3 to 16 ) :'))
mainclass = passwordgenerator()
mainclass.PG1(q)
time.sleep(1)
mainclass.PG2(q)
time.sleep(2)
mainclass.PG3(q)







