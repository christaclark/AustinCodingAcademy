#3.2
number = float(raw_input('Please enter a number: '))

#float or a decimal number: 2.3, 3.4, 24.4
# int or a whole number : 2, 3, 4, 6

#Casted will convert the number from Raw_input (such as 3.2) into an integer 
#then we will compare it to the original number
castedNumber = int(number) 

if number == castedNumber:
	print "Number is whole"
else:
	print "Number is not whole"

