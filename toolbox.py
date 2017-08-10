

def time_diff(date1, date2):
    """
    Returns the number of seconds between two dates, in absolute terms.
    """
    diff = date2 - date1
    seconds = abs(diff.days*86400 + diff.seconds)
    return seconds




def str_to_datetime(date_str):
	"""
	Takes string representation of datetime and returns an actual datetime.
	Follows very specific format: 'YYYY-MM-DD HH:MM:SS'. Hour is 24h format.

	Expects datetime to be imported as "import datetime". 
	TO DO: exception handling for datetime not imported / imported in a different manner

	Inspiration and more solutions:
	https://stackoverflow.com/questions/466345/converting-string-into-datetime
	
	Very useful documentation about the time formatting:
	https://www.tutorialspoint.com/python/time_strptime.htm
	"""

	Try:
		return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
	Except exception as e:
		return e

