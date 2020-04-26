import requests
import json
import csv
import threading


### ################################## Temp Code ########################################

words=[]

for i in range(10000):
	words.append(str(i))


#########################################################################################




### Simple requests


def simpleget(url):
	try:
		res=requests.get(url,timeout=4)
	except Exception as e:
		print(e)
	else:
		return res




def simplepost(url,param):
	try:
		res=requests.post(url,params=param,timeout=4)
	except Exception as e:
		print(e)
	else:
		return res



def simpleput(url,*param):
	parameters=dict(param)
	try:
		res=requests.put(url,params=param,timeout=4)
	except Exception as e:
		print(e)
	else:
		return res



def simpledelete(url,*param):
	parameters=dict(param)
	try:
		res=requests.delete(url,params=param,timeout=4)
	except Exception as e:
		print(e)
	else:
		return res





def simplepatch(url,*param):
	parameters=dict(param)
	try:
		res=requests.patch(url,params=param,timeout=4)
	except Exception as e:
		print(e)
	else:
		return res


