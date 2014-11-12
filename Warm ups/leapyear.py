def is_leap(year):
	if year % 4: 
		return true 
	else:
		if year % 100:
			return false
		if year % 100 and year % 400: 
			return true 


print is_leap(2014)	



