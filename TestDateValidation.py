import DateValidation
from datetime import date

myDate = date(2019, 12, 28)

try:
	if DateValidation.validateDate(myDate):
		print 'valid date'
except Exception as e:
	print str(e)