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
from core.networking import ishttpwildcard
#ReadingSubdomains
domains_all=readfile('../target-data/no_wild_cards_2.txt')


#Reading Variables / Count Variables
redirect_count=0
leaked_count=0
subdomain_patterns=readfile('../payloads/subjack.txt')

cli=['open_redirect','subjack','leaked_files','login_finder','test']



##Imput Validation
if len(sys.argv)<2:
	print('Expected Arguments: ',cli)
	exit()

if sys.argv[1] not in cli:
	print('Expected Arguments: ',cli)
	exit()

choice=sys.argv[1]


## Scanners 



def leaked_files(url):
	domain=getdomain(url)
	print('[~] Scanning '+domain)
	blacklist_domains=[]
	if domain in blacklist_domains:
		return None
	name=inspect.stack()[0][3]
	log_file='../output/'+name+'/logs/'+name+'.log'
	output_file='../output/'+name+'/output/'+name+'.txt'
	global leaked_count
	leaked_count+=1
	if(leaked_count%10000==0):
		sendtoslack("[~] Status (leaked_files) :\nTotal Domains:"+str(len(domains_all))+"\n"+"Domains Scanned: "+str(leaked_count))
	writetofile(log_file,getdomain(url))	
	if ishttpwildcard(domain)==True:
		blacklist_domains.append(domain)
	try:
		res=requests.get(url,timeout=2,allow_redirects = False)
	except Exception as e:
		pass
	else:
		print(res.url,':',res.status_code)
		if res.status_code==200:
			appendtofile(output_file,res.url)
			sendtoslack("[~] Leaked Files "+res.url)



## ========================= Open Redirect ===================================================


def open_redirect(url):
	print('[~] Scanning '+getdomain(url))
	name=inspect.stack()[0][3]
	log_file='../output/'+name+'/logs/'+name+'.log'
	output_file='../output/'+name+'/output/'+name+'.txt'
	global redirect_count
	redirect_count+=1
	if(redirect_count%10000==0):
		sendtoslack("[~] Open_redirect (leaked_files) :\nTotal Domains:"+str(len(domains_all))+"\n"+"Domains Scanned: "+str(leaked_count))
	writetofile(log_file,getdomain(url))	
	try:
		res=requests.get(url,timeout=2)
	except Exception as e:
		pass
	else:
		print(res.url,' : ',res.status_code)
	for a in res.history:
		if a.status_code==302 and 'example' in a.headers['location']:
			writetofile(output_file,res.url)
			sendtoslack("[~] Open Redirect "+a.url)






##======================Subdomain takeover==================================================

def subjack(subdomain):
	print("[~] Scanning "+subdomain)
	writetofile('../output/subjack/logs/subjack.log',subdomain)
	new_subdomain_http=addprotocol(subdomain, 'http')
	new_subdomain_https=addprotocol(subdomain, 'https')

	try:
		res1=requests.get(new_subdomain_https,timeout=3)
	except Exception as e:
		print('[~] Request Error https')
	else:

		for pattern in subdomain_patterns:
			if pattern in res1.text:
				msg='[~] Possible Subdomain Takeover: '+res1.url+'\n'
				print(msg)
				sendtoslack(msg)
				appendtofile('../output/subjack/output/subjack.txt',res2.url)
		try:
			for a in res1.history:
				if 'statuspage.io' in a.headers['location']:
					msg='[~] Redirect Possible Subdomain Takeover: '+res1.url+'\n'
					print(msg)
					sendtoslack(msg)
					appendtofile('../output/subjack/output/subjack.txt',res1.url)
		except:
			pass

	try:
		res2=requests.get(new_subdomain_http,timeout=3)
	except Exception as e:
		print('[~] Request Error http')
	else:
		for pattern in subdomain_patterns:
			if pattern in res2.text:
				msg='[~] Possible Subdomain Takeover: '+res2.url
				print(msg)
				sendtoslack(msg)
				appendtofile('../output/subjack/output/subjack.txt',res2.url)
		try:
			for a in res2.history:
				if 'statuspage.io' in a.headers['location']:
					msg='[~http] Redirect Possible Subdomain Takeover: '+res2.url+'\n'
					print(msg)
					sendtoslack(msg)
					appendtofile('../output/subjack/output/subjack.txt',res2.url)
		except:
			pass



##=========================== Default Login ====================================================




blacklist_domains_login_finder=[]
def login_finder(url):
	global blacklist_domains_login_finder
	global leaked_count
	domain=getdomain(url)
	#print('[~] Scanning '+domain)
	blacklist_domains_login_finder=[]
	if domain in blacklist_domains_login_finder:
		print('[!] Blacklisted')
	name=inspect.stack()[0][3]
	log_file='../output/'+name+'/logs/'+name+'.log'
	output_file='../output/'+name+'/output/'+name+'.txt'
	
	leaked_count+=1
	if(leaked_count%10000==0):
		sendtoslack("[~] Status (login_finder) :\nTotal Domains:"+str(len(domains_all))+"\n"+"Domains Scanned: "+str(leaked_count))
	writetofile(log_file,getdomain(url))	
	if ishttpwildcard(domain)==True:
		blacklist_domains_login_finder.append(domain)
	try:
		res=requests.get(url,timeout=2,allow_redirects = False)
	except Exception as e:
		pass
	else:
		print(res.url,':',res.status_code)
	if res.status_code==200:
		if '<form' in res.text:
			appendtofile(output_file,res.url)
			sendtoslack("[~] Login Finder "+res.url)



##=========================== Wayback XSS  ====================================================


blacklist_domains_waybackxss=[]
def waybackxss(url):
	pattern='AB_X@Y'
	global blacklist_domains_waybackxss
	global leaked_count
	domain=getdomain(url)
	#print('[~] Scanning '+domain)
	blacklist_domains_waybackxss=[]
	if domain in blacklist_domains_waybackxss:
		print('[!] Blacklisted')
	name=inspect.stack()[0][3]
	log_file='../output/'+name+'/logs/'+name+'.log'
	output_file='../output/'+name+'/output/'+name+'.txt'
	
	leaked_count+=1
	if(leaked_count%10000==0):
		sendtoslack("[~] Status (login_finder) :\nTotal Domains:"+str(len(domains_all))+"\n"+"Domains Scanned: "+str(leaked_count))
	writetofile(log_file,getdomain(url))	
	if ishttpwildcard(domain)==True:
		blacklist_domains_waybackxss.append(domain)
	try:
		res=requests.get(url,timeout=2,allow_redirects = False)
	except Exception as e:
		pass
	else:
		print(res.url,':',res.status_code)
	if res.status_code==200:
		if pattern in res.text:
			appendtofile(output_file,res.url)
			sendtoslack("[~] Login Finder "+res.url)




##=========================== General Code ====================================================



#Writing time to output Output file

xtime=current_en_time()
if len(choice)>0:
	appendtofile('../output/'+choice+'/output/'+choice+'.txt', xtime)




# ##Starter

for domain in domains_all:


	if choice=='test':
		pass

	if choice=='leaked_files':
		urls=makeurls('https',domain,readfile('../payloads/leaked_files.txt'))
		with concurrent.futures.ThreadPoolExecutor() as executor:
			executor.map(leaked_files,urls)

	if choice=='open_redirect':
		urls=makeurls('http',domain,readfile('../payloads/open_redirect.txt'))
		urls2=makeurls('https',domain,fuzzableurls(waybackparamurls(domain,True),'http://www.example.com'))
		urls=urls+urls2
		with concurrent.futures.ThreadPoolExecutor() as executor:
			executor.map(open_redirect,urls)

	if choice=='subjack':
		with concurrent.futures.ThreadPoolExecutor() as executor:
			executor.map(subjack,domains_all)

	if choice=='login_finder':
		urls=makeurls('https',domain,readfile('../payloads/login_finder.txt'))
		with concurrent.futures.ThreadPoolExecutor() as executor:
			executor.map(login_finder,urls)

	
	if choice=='waybackxss':
		urls=makeurls('https',domain,fuzzableurls(waybackparamurls(domain,True),'AB_X@Y'))
		with concurrent.futures.ThreadPoolExecutor() as executor:
			executor.map(open_redirect,urls)











