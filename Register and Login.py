#Python Login Script

import time
print('Registration =>')
time.sleep(2)

#Regsiter Script
reg_nickname = input('Enter Your Nickname:')
reg_password = input('Enter Your Password:')
reg_passwd_again = input('Enter You Passowrd Again:')
reg_fn = input('First Name:')
reg_ln = input('Last Name:')
reg_age = input('Your Age:')
time.sleep(3)
print('Creating your Acoount...')
time.sleep(4)

if reg_nickname ==reg_nickname and reg_password ==reg_password and reg_fn ==reg_fn and reg_ln ==reg_ln and reg_age ==reg_age:
	print('Nickname:' , reg_nickname)
	print('Password:' , reg_password)
	print('Name:' , reg_fn , reg_ln)
	print('Age:' , reg_age)
	time.sleep(3)
	print('Login With Nickname:' , reg_nickname , 'Password:' , reg_password)
	
#Login Script
while True:
	log_nickname = input('Nickname:')
	log_password = input('Password:')
	
	if log_nickname ==reg_nickname and log_password ==reg_password:
		print('Succesfully Login')
		
	else:
		print('Try Again :(')
	