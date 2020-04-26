import time
from core.subdomains import subdomainsall,addprotocol
from core.multi_requests import multiget,multipost
from core.networking import isalive
from core.files import readfile
from core.output import sendtoslack,writetofile
from core.networking import iswildcard


count=0
subdomains=subdomainsall('../target-data/test1.txt')
payload=readfile('../payloads/leaked_files.txt')
for subdomain in subdomains:
	count+=1
	if(count%1000==0):
		sendtoslack("[~] Status (open_redirect) :\nTotal Domains:"+str(len(subdomains))+"\n"+"Domains Scanned: "+str(count))
	if isalive(subdomain):
		writetofile('../output/open_redirect/logs/open_redirect.log',subdomain)
		new_subdomain=addprotocol(subdomain, 'http')
		ress=multiget(new_subdomain, payload)
		for res in ress:
			try:
				for a in res['response'].history:
					datax={}
					if a.status_code==302 and 'example' in a.headers['location']:
						vul_url=str('\n'+new_subdomain+res['word']+'\n')
						msg='[~] Open Redirect: '+vul_url
						sendtoslack(msg)
						writetofile('../output/open_redirect/output/open_redirect.txt', vul_url)
			except:
				pass

	else:
		print('Skipping Wildcard',subdomain)

