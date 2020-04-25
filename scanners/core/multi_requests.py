import requests
import json
import csv
import threading
from operator import attrgetter

allowed_method=['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']


def counter(value,num):
	value=value+num
	print(value)

#GET


def multiget(url,wlist):
	dic_res={}
	timeout=0
	get_final_data=[]
	temp_list=wlist
	if len(temp_list)>0:
		for word in temp_list:
			dic_res={}
			new_url=url+'/'+word
			try:
				if timeout==2:
					print('Skipping',new_url)
					break
				res=requests.get(new_url,timeout=4)
				pass
				print('[!] Core: GET',res.url,res.status_code,res.is_redirect)
			except Exception as e:
				print(e)
				timeout=timeout+1
			else:
				dic_res['word']=word
				dic_res['response']=res
			get_final_data.append(dic_res)
		return get_final_data





def multipost(url,wlist,**params):
	dic_res={}
	data=params['data']
	timeout=0
	get_final_data=[]
	temp_list=wlist
	if len(temp_list)>0:
		for word in temp_list:
			dic_res={}
			new_url=url+'/'+word
			try:
				if timeout==2:
					print('Skipping',new_url)
					break
				res=requests.post(new_url,timeout=4,data=data)
				print('[!] Core: POST',res.url,res.status_code)
			except Exception as e:
				print(e)
				timeout=timeout+1
			else:
				dic_res['word']=word
				dic_res['response']=res
			get_final_data.append(dic_res)
		return get_final_data




def multipatch(url,wlist,**params):
	dic_res={}
	data=params['data']
	timeout=0
	get_final_data=[]
	temp_list=wlist
	if len(temp_list)>0:
		for word in temp_list:
			dic_res={}
			new_url=url+'/'+word
			try:
				if timeout==2:
					print('Skipping',new_url)
					break
				res=requests.patch(new_url,timeout=4,data=data)
				print('[!] Core: POST',res.url,res.status_code)
			except Exception as e:
				print(e)
				timeout=timeout+1
			else:
				dic_res['word']=word
				dic_res['response']=res
			get_final_data.append(dic_res)
		return get_final_data





def multiput(url,wlist,**params):
	dic_res={}
	data=params['data']
	timeout=0
	get_final_data=[]
	temp_list=wlist
	if len(temp_list)>0:
		for word in temp_list:
			dic_res={}
			new_url=url+'/'+word
			try:
				if timeout==2:
					print('Skipping',new_url)
					break
				res=requests.put(new_url,timeout=4,data=data)
				print('[!] Core: POST',res.url,res.status_code)
			except Exception as e:
				print(e)
				timeout=timeout+1
			else:
				dic_res['word']=word
				dic_res['response']=res
			get_final_data.append(dic_res)
		return get_final_data





def multidelete(url,wlist,**params):
	dic_res={}
	data=params['data']
	timeout=0
	get_final_data=[]
	temp_list=wlist
	if len(temp_list)>0:
		for word in temp_list:
			dic_res={}
			new_url=url+'/'+word
			try:
				if timeout==2:
					print('Skipping',new_url)
					break
				res=requests.delete(new_url,timeout=4,data=data)
				print('[!] Core: POST',res.url,res.status_code)
			except Exception as e:
				print(e)
				timeout=timeout+1
			else:
				dic_res['word']=word
				dic_res['response']=res
			get_final_data.append(dic_res)
		return get_final_data






