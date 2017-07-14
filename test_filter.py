def filter_3_and_5(number):
	count3 = number / 3
	count5 = number / 5
	count15 = number / 15

	return number - count3 - count5 + 2*count15


print filter_3_and_5(15)