values=[
'admin',
'admin',
'admin',
'admin',
'password',
'admin',
'user',
'userpass',
'userpasst'
]

params=['a','b','c']
dic={}
count=0
for i in range(len(values)):
	count+=1
	dic[params[i%len(params)]]=values[i]
	if len(dic)==len(params):
		print(dic)