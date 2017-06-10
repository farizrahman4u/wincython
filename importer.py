# Wrap your Cython modules using this 
# to guarantee a successful import on
# windows systems.

import time

module = 'helloworld'

while True:
	try:
		exec('from ' + module + ' import *')
		break
	except:
		time.sleep(1)
