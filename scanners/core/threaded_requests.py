import requests
import json
import time
import csv
import threading
from operator import attrgetter

### ################################## Temp Code ########################################

# for i in range(10):
# 	words.append(str(i))

#########################################################################################


allowed_method=['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']




#GET
get_final_data=[]
def multiget(get_final_data,url,temp_list,*res_property):
	multiget.counter=+1
	res_data={}
	if len(temp_list)>0:
		for word in temp_list:
			temp_list.remove(word)
			new_url=url+'/'+word
			try:
				res=requests.get(new_url,timeout=10)
			except Exception as e:
				print(e)
			else:
				for _ in range(len(res_property)):
					for prop in res_property:
						res_data[str(prop)]=(attrgetter(str(prop))(res))
					#print(data)
				get_final_data.append(res_data)

multiget.counter=0

def threadedget(url,wlist,no_of_threads,*res_property):
	temp_list=wlist
	threads=[]
	for _ in range(no_of_threads):
		t=threading.Thread(target=multiget,args=[get_final_data,url,temp_list,*res_property])
		time.sleep(0.000000001)
		t.start()
		threads.append(t)
	for th in threads:
		th.join()
	return get_final_data









#POST
post_final_data=[]

def multipost(post_final_data,url,temp_list,params):
	data=params['data']
	res_data={}
	if len(temp_list)>0:
		print(threading.currentThread().getName(),temp_list)
		for word in temp_list:
			temp_list.remove(word)
			new_url=url+'/'+word
			try:
				res=requests.post(new_url,timeout=4,data=data)
			except Exception as e:
				pass
			else:
				for _ in range(len(params['res_properties'])):
					for prop in params['res_properties']:
						res_data[str(prop)]=(attrgetter(prop)(res))
				post_final_data.append(res_data)

def threadedpost(url,wlist,no_of_threads,**params):
	temp_list=wlist
	threads=[]
	for _ in range(no_of_threads):
		t=threading.Thread(target=multipost,args=[post_final_data,url,temp_list,params])
		time.sleep(0.000000001)
		t.start()
		threads.append(t)
	for th in threads:
		th.join()
	return post_final_data







#PATCH
patch_final_data=[]

def multipatch(patch_final_data,url,temp_list,params):
	data=params['data']
	res_data={}
	if len(temp_list)>0:
		print(threading.currentThread().getName(),temp_list)
		for word in temp_list:
			temp_list.remove(word)
			new_url=url+'/'+word
			try:
				res=requests.patch(new_url,timeout=4,data=data)
			except Exception as e:
				pass
			else:
				for _ in range(len(params['res_properties'])):
					for prop in params['res_properties']:
						res_data[str(prop)]=(attrgetter(prop)(res))
				patch_final_data.append(res_data)

def threadedpatch(url,wlist,no_of_threads,**params):
	temp_list=wlist
	threads=[]
	for _ in range(no_of_threads):
		t=threading.Thread(target=multipatch,args=[patch_final_data,url,temp_list,params])
		time.sleep(0.000000001)
		t.start()
		threads.append(t)
	for th in threads:
		th.join()
	return patch_final_data


#delete
delete_final_data=[]

def multidelete(delete_final_data,url,temp_list,params):
	data=params['data']
	res_data={}
	if len(temp_list)>0:
		print(threading.currentThread().getName(),temp_list)
		for word in temp_list:
			temp_list.remove(word)
			new_url=url+'/'+word
			try:
				res=requests.delete(new_url,timeout=4,data=data)
			except Exception as e:
				pass
			else:
				for _ in range(len(params['res_properties'])):
					for prop in params['res_properties']:
						res_data[str(prop)]=(attrgetter(prop)(res))
				delete_final_data.append(res_data)

def threadeddelete(url,wlist,no_of_threads,**params):
	temp_list=wlist
	threads=[]
	for _ in range(no_of_threads):
		t=threading.Thread(target=multidelete,args=[delete_final_data,url,temp_list,params])
		time.sleep(0.000000001)
		t.start()
		threads.append(t)
	for th in threads:
		th.join()
	return delete_final_data



#PUT
put_final_data=[]

def multiput(put_final_data,url,temp_list,params):
	data=params['data']
	res_data={}
	if len(temp_list)>0:
		print(threading.currentThread().getName(),temp_list)
		for word in temp_list:
			temp_list.remove(word)
			new_url=url+'/'+word
			try:
				res=requests.put(new_url,timeout=4,data=data)
			except Exception as e:
				pass
			else:
				for _ in range(len(params['res_properties'])):
					for prop in params['res_properties']:
						res_data[str(prop)]=(attrgetter(prop)(res))
				put_final_data.append(res_data)

def threadedput(url,wlist,no_of_threads,**params):
	temp_list=wlist
	threads=[]
	for _ in range(no_of_threads):
		t=threading.Thread(target=multiput,args=[put_final_data,url,temp_list,params])
		time.sleep(0.000000001)
		t.start()
		threads.append(t)
	for th in threads:
		th.join()
	return put_final_data
