

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

	try:
		return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
	except Exception as e:
		return e



def sort_dict(d, sort_by=1, ascending=False):
    """
    Takes a dictionary and sorts it by key or value, ascending or descending. 
    Returns a list of (key, value) tuples.
    
    Requires operator module.
    
    Parameters:
    -----------
    d: dictionary to sort
    sort_by: 0 sort by key, 1 sort by value
    ascending: True for low to high, False for high to low.
    """
    
    # Lame check if operator was imported
    # read more here: 
    # https://stackoverflow.com/questions/30483246/how-to-check-if-a-python-module-has-been-imported
    
    try:
        operator
    except:
        print 'operator module required. Importing it now'
        import operator
    
    sorted_d = sorted(d.iteritems(), key=operator.itemgetter(sort_by))
    
    if ascending:
        return sorted_d
    
    else:
        return sorted_d[::-1]