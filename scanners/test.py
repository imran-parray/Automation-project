import time
import sys
import concurrent.futures
import requests
import inspect
from core.files import readfile
from core.output import sendtoslack
from core.urls import makeurls,getdomain
from core.timendate import current_en_time
from core.output import writetofile,appendtofile
from core.urls import fuzzableurls
from core.wayback import waybackparamurls
from core.networking import isalive
from core.subdomains import addprotocol
from core.networking import ishttpwildcard,restojson
#ReadingSubdomains
domains_all=readfile('../target-data/test.txt')


#Reading Variables / Count Variables
redirect_count=0
leaked_count=0
subdomain_patterns=readfile('../payloads/subjack.txt')

choice=sys.argv[1]





##==========================================================================================

def crlf(url):
	print('[~] Scanning '+getdomain(url))
	name=inspect.stack()[0][3]
	log_file='../output/'+name+'/logs/'+name+'.log'
	output_file='../output/'+name+'/output/'+name+'.txt'
	global redirect_count
	redirect_count+=1
	if(redirect_count%10000==0):
		sendtoslack("[~] CRLF (leaked_files) :\nTotal Domains:"+str(len(domains_all))+"\n"+"Domains Scanned: "+str(leaked_count))
	writetofile(log_file,getdomain(url))	
	try:
		res=requests.get(url,timeout=2)
	except Exception as e:
		pass
	else:
		print(res.url,' : ',res.status_code)
	for a in res.headers:
		print(a)
		if 'Header-Test' in a:
			appendtofile(output_file,res.url+" : "+str(res.status_code)+" : "+str(len(res.text)))
			sendtoslack("[~] CRLF "+res.url)



##=========================== General Code ====================================================



#Writing time to output Output file

xtime=current_en_time()
if len(choice)>0:
	appendtofile('../output/'+choice+'/output/'+choice+'.txt', xtime)




# ##Starter

for domain in domains_all:


	if choice=='test':
		pass


	if choice=='crlf':
		urls=makeurls('http',domain,readfile('../payloads/crlf.txt'))
		with concurrent.futures.ThreadPoolExecutor() as executor:
			executor.map(crlf,urls)








