"""
File: weather_master.py
Name:Bright Yeh
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


EXIT = -100


def main():
	"""
	Calculate and compare the input data
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data = int(input('Next temperature: (or ' + str(EXIT) + ' to quit)? '))
	n = 0
	cold_day = 0
	if data == EXIT:
		print('No temperature were entered.')
	else:
		maximum = data
		minimum = data
		amount = data
		if data < 16:
			cold_day += 1
		while True:
			data = int(input('Next temperature: (or ' + str(EXIT) + ' to quit)? '))
			n += 1
			# count days for average
			if data == EXIT:
				break
			amount += data
			# amount for average
			if data < 16:
				cold_day += 1
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
		average = amount / n
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold_day) + ' cold day(s) (under 16 degree)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
