from datetime import datetime
import time

# In this solution I assumed that I have a req_log table in DB which is saving time,ip,cookie,username of each requests.
# I'll provide the test data as req_log.csv.

#

fmt = '%Y-%m-%d %H:%M:%S'
now = datetime.now()
current_time = now.strftime('%Y-%m-%d %H:%M:%S')

def ip_rule(ip):
	last_time = 'select max(date) from req_log where ip=\'ip\' and user=username'
	max_limit_1 = current_time - 60 # I'm using max_limit variable to calculate the timestamp till when I have to look for requests in DB.
	max_limit_2 = current_time - 3600
	#calculate total no. of req by client_ip for last 60s
	count_1 = 'select COUNT(*) from req_log where ip=\'ip\' and time > max_limit_1' #0
	#calculate total no. of req by client_ip for last 3600s
	count_2 = 'select COUNT(*) from req_log where ip=\'ip\' and time > max_limit_2' #3

	time_diff = current_time - last_time #to calculate the diff between current req time and last req time in DB

	if time_diff < 60 and count_1 < 5: 
		return true
	elif time_diff < 3600 and count_2 < 12: 
		return true
	else:
		return false

def cookie_rule(cookie):
	last_time = 'select time from req_log where cookie=\'cookie\''
	max_limit = current_time - 10 
	count = 'select COUNT(*) from req_log where cookie=\'cookie\' and time > max_limit' # DB query to get total no. of rows that have time stamp greater than max_limit

	if time_diff < 10 and count < 2:
		return true
	else:
		return false


def user_rule(user):
	last_time = 'select time from req_log where user=\'username\''
	max_limit = current_time - 3600
	count = 'select COUNT(*) from req_log where user=\'username\' and time > max_limit'

	if time_diff < 3600 and count < 10:
		return true
	else:
		return false


def loginRateLimiter(client_ip, username, cookie_id = None):
	if ip_rule(client_ip) and cookie_rule(cookie_id) and user_rule(username):
		return true

	return false



