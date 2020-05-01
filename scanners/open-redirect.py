import time
import sys
from core.subdomains import subdomainsall,addprotocol
from core.multi_requests import multiget,multipost
from core.networking import isalive
from core.files import readfile
from core.output import sendtoslack,writetofile
from core.networking import iswildcard
from core.timendate import current_en_time
from core.wayback import waybackparamurls
from core.urls import fuzzableurls

#Insert time
xtime=current_en_time()
writetofile('../output/open_redirect/output/open_redirect.txt', xtime)

redirect_url='http://www.example.com'
count=0
payloadsx=[]
subdomains=subdomainsall('../target-data/test.txt')
file_payload=readfile('../payloads/leaked_files.txt')
payload=[]
fuzzabl_urls=fuzzableurls(waybackparamurls('miraki.com', False),redirect_url)
for line in file_payload:
	payloads.append(line)
for line in fuzzabl_urls:
	payloadsx.append(line)

for line in payloadsx:
	xline=line.lstrip('/')
	payloads.append(line)
for subdomain in subdomains:
	count+=1
	if(count%1000==0):
		sendtoslack("[~] Status (open_redirect) :\nTotal Domains:"+str(len(subdomains))+"\n"+"Domains Scanned: "+str(count))
	if isalive(subdomain):
		writetofile('../output/open_redirect/logs/open_redirect.log',subdomain)
		new_subdomain=addprotocol(subdomain, 'http')
		ress=multiget(new_subdomain, payloads)
		for res in ress:
			try:
				for a in res['response'].history:
					datax={}
					if a.status_code==302 and 'example' in a.headers['location']:
						vul_url=str('\n'+new_subdomain+res['word'])
						msg='[~] Open Redirect: '+vul_url
						sendtoslack(msg)
						writetofile('../output/open_redirect/output/open_redirect.txt', vul_url)
			except:
				pass

	else:
		print('Skipping Wildcard',subdomain)

