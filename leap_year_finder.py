# Tells user if a given year is a leap year.

year = raw_input("Year: ")
year = int(year) # Converts input from string to integer

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
	print "{0} is a leap year.".format(year)
else:
	print "{0} is not a leap year.".format(year)
	
