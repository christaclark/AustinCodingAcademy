CONCEPTUAL

1. List all three possible scenarios in which this is false: "It's cold and wet outside"
	# It's not cold, is wet (only one variable is true)
	# It's cold, but is not wet (only one variable is true)
	# It's hot and dry (neither variable is true)

"Boolean true & false is important to understand." 

2. If the expression not True evaluates to False, and the expression not False evaluates to True, 
	# What is the value of not not True? TRUE
	# What is the value of not not False? FALSE
	
	
3. Provide three real world scenarios where a while loop would be appropriate: 
	DEFINITION: A while-loop will keep executing the code block under it as long as a 
	boolean expression is True.  What they do is simply do a test like an if-statement, 
	but instead of running the code block once, they jump back to the "top" where the 
	while is, and repeat. It runs until the expression is False. 
	
		# If you don't have a tidy data structure to iterate through, or you don't have a 
		  generator function that drives your processing, you must use while.
		# While is useful in scenarios where the break condition doesn't logically depend 
		  on any kind of sequence. For example, consider unpredictable interactions: 
		  while user_is_sleeping(): wait()
		# You'd use a while loop to handle an iterable would be if you needed to access 
		  the iterator directly for some reason, e.g. you needed to skip over items in the 
		  list under some circumstances."
		
		
4. Explain the difference between the following values: 10 "10"
	# Python will read 10 as an integer and “10” as a string 


5. Explain the difference between the following values: 10 10.0
	# There’s no difference in Python. Decimals are included or not depending on the 
	  context the number is being written.


6. You’re attempting to store the value 2147483649. What’s a type of number you encounter 
in everyday life that would best be represented by a string instead of an integer? Would 
you ever perform arithmetic with this type of number? 
	# This type of number is typically used for IDs such as phone numbers; social security


7. Explain in your own words what returning a value from a function does. Provide an 
example of when you would want a function to return a value, and provide an example of 
when a return value is not necessary.
	# Returning a value from a function: If the function doesn’t return a value, it will 
	  just delete. Every time a function is called and runs, it will disappear all with 
	  all the information it put out until you save it (return the values). 
	# If you define a varibale inside of a funcion, it doesn't impact the outside world
	# If you want a function to impact your code outsdie of a local program 
	
	  
	  


	  
	  
	  

PROGRAMS

Skills & Understanding: 
"Functions" Are a re-usable subscript within your script 
			You can give it inputs (parameters, arugments)
			You can receive an output (return value) 
Example: 
def sum3(x,y,z)
	return x+y+z			
# x,y,z are all variables of the function the input

1. Write a program that prompts the user for their first name, last name, age, & gender. 
  - Print a welcome message which includes their provided information. 
  - Additionally, calculate and print how many years apart you and the user are in age. 
  - You may assume the age provided by the user is a valid integer.

name = raw_input("Enter your name here: ")
age = raw_input("Enter your age here: ")

print 'Hello,' , name 
print 'My name is Christa.'
print  "You're only" , age(x) "?"  

def age(x, y):
    if x >= y:
        result = x - y
    else:
        result = y - x
    return result 
  
  


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


2. Write a program that prompts the user for a number and determines if that number was an 
   integer or floating point. You may assume that the number provided by the user is 
   numeric (you don't need to account for random strings like 'Hello'), but you may only 
   use the functions float() and int() in your logic for determining if the value is an 
   integer or floating point.
   
   I would like the program to determine if the number entered is a whole number, not if 
   the number is an int or float. The distinction is that I want the program to determine, 
   for example, that 15 and 15.0 are whole numbers while 14.5 is not. 15.0 is a whole 
   number *and* a float, the two are not mutually exclusive. 

   Hint: Observe the following shell session

>>> float(2.5)
2.5
>>> int(2.5)
2
>>> 2.0 == 2
True

!! ANSWER !!

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


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


3. Your manager orders Austin's Pizza every Friday for you and your fellow coworkers. 
   You're getting tired of figuring out how many pizzas you need to buy, so you decide to 
   automate the process. You're also getting tired of Austin's Pizza and would prefer East 
   Side Pies, but complaining about free food doesn't set you up well for a promotion. 
   Create a program which lets the user input the number of people eating, the number of 
   slices each will eat, and the number of slices per box of pizza. The program should 
   print out the minimum number of pizza boxes necessary to feed the office based on the 
   values provided.


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


4. FizzBuzz is a classic technical interview problem. Complete the exercise below:
	- Write a program that prints the numbers from 1 to 100. But for multiples of three 
	print 'Fizz' instead of the number and for the multiples of five print 'Buzz' For 
	numbers which are multiples of both three and five print 'FizzBuzz'

if (theNumber is divisible by 3) and (theNumber is divisible by 5) then
	print "FizzBuzz"
	else if (theNumber is divisible by 3) then
	print "Fizz"
	else if (theNumber is divisible by 5) then
	print "Buzz"
	else /* theNumber is not divisible by 3 or 5 */
	print theNumber
	end if 
	
def fizzbuzz(n):
 
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)
 
 #xrange creates an iterable (interchangeable for a loop) list  
 #(1,21) tells Python to run a list 1 through 21
print "\n".join(fizzbuzz(n) for n in xrange(1, 21))
	
	
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


5. Fortune cookie ASCII frame

PART 1

- Create a program containing a function called print_ascii_frame that has an argument named message.

def print_ascii_frame(message):
    # ...
    # ...
    


#This function should create and print an ASCII art border around the message passed in. 
For example, the following function call print_ascii_frame('My name is Joe!')
#Would result in something resembling
#The function should be able to handle strings of arbitrary length.


|=====================|
|                     |
| ~ My name is Joe! ~ |
|                     |
|=====================|



#HINTS:

#You can use len() to get the number of characters in a string...
>>> len('hello')
5

#Observing that multiplying a string returns the string repeated that many times...
>>> "=" * 30
'=============================='


!! ANSWER !!


def fortune_cookie(name):
	print "|=====================\t|"
	print "|                     \t|"
	print "| ~ My name is %s! ~ |" % name
	print "|                     \t|"
	print "|=====================\t|"



myName = "Christa"

fortune_cookie(myName)





- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



#PART 2

#Now that you have your ascii frame function finished, it's time to frame a noteworthy 
#phrase. We're going to grab some fortune cookies phrases from the internet.

#The following function scrapes the website www.fortunecookiemessage.com to get a random 
#fortune (you do not have to understand how the function works yet):

def get_random_fortune():
    import urllib2
    fortune_url = 'http://www.fortunecookiemessage.com'
    resp = urllib2.urlopen(fortune_url)
    html = resp.read()

    start_flag = 'cookie-link">'
    fortune_start =  html.index(start_flag) + len(start_flag)
    fortune_end = html.index('<', fortune_start)
    fortune =  html[fortune_start:fortune_end]
    if not fortune or len(fortune) > 70:
        return get_random_fortune()
    else:
        return fortune
The function returns a string representing the retrieved fortune

>>> my_fortune = get_random_fortune()
>>> my_fortune
'In human endeavor, chance favors the prepared mind.'
Copy and paste the function to the top of your the file where your print_ascii_frame function is defined.

Combine your print_ascii_frame function and the get_random_fortune function to create a program that downloads a fortune from the internet and frames it with your fancy ASCII art border.

Below are a few sample runs of my version of the program, which I have saved in a file called fortune.py:

~$ python fortune.py
|============================|
|                            |
| ~ You love Chinese food. ~ |
|                            |
|============================|

~$ python fortune.py

|=========================================================================|
|                                                                         |
| ~ A short stranger will soon enter your life with blessings to share. ~ |
|                                                                         |
|=========================================================================|

~$ python fortune.py
|=========================================|
|                                         |
| ~ Great thoughts come from the heart. ~ |
|                                         |
|=========================================|