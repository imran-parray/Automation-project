import time
from core.subdomains import subdomainsall,addprotocol
from core.threaded_requests import threadedget
from core.networking import isalive
from core.files import readfile,removedupes
from core.output import sendtoslack,writetofile
from core.networking import iswildcard,ishttpwildcard
from core.timendate import current_en_time
#Insert time
xtime=current_en_time()
writetofile('../output/leaked_files/output/leaked_files.txt', xtime)

count=0
subdomains=subdomainsall('../target-data/test1.txt')
payload=readfile('../payloads/leaked_files.txt')
for subdomain in subdomains:
	count+=1
	if(count%500==0):
		sendtoslack("[~] Status (leaked_files) :\nTotal Domains:"+str(len(subdomains))+"\n"+"Domains Scanned: "+str(count))
	data=[]
	res=''
	new_subdomain=addprotocol(subdomain, 'http')
	print(new_subdomain)
	print(ishttpwildcard(new_subdomain))
	if ishttpwildcard(new_subdomain)==False:
		writetofile('../output/open_redirect/logs/leaked_files.log',subdomain)
		res=threadedget(new_subdomain,payload,10,'url','status_code')


	for response in res:
		if response['status_code']==200:
			data.append(response['url'])

	if len(data)>0:
		strx='\n[Module : Leaked_files]\n\n'
		data2=removedupes(data)
		for d in data2:
			strx=strx+d+'\n'
			writetofile('../output/leaked_files/output/leaked_files.txt', d+'\n')
		sendtoslack(strx)
		
