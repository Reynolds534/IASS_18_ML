import os
path = str(os.path.dirname(os.path.abspath(__file__)))
path = path + "\errorlog.txt"

f = open(path, 'w')

print
try:
	import numpy as np
	message = "Numpy has been initiated successfully!\n"
	f.write(message)
	print message
except Exception(e):
	message = str(e)+"\n"
	f.write(message)
	print message
	
try:
	import scipy as sp
	message = "Scipy has been initiated successfully!\n"
	f.write(message)
	print message
except :
	message = "Scipy has failed to initiate.\n"
	f.write(message)
	print message

	
try:
	import sklearn
	message = "Scikit-learn has been initiated successfully!\n"
	f.write(message)
	print message
except:
	message = "Scikit-learn has failed to initiate.\n"
	f.write(message)
	print message

try:
	import MySQLdb
	message = "MySQL has been initiated successfully!\n"
	f.write(message)
	print message
except:
	message = "MySQL has failed to initiate.\n"
	f.write(message)
	print message

f.close()