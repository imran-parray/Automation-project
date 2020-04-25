import time
from core.subdomains import subdomainsall,addprotocol
from core.multi_requests import multiget,multipost
from core.networking import isalive
from core.files import readfile
from core.output import sendtoslack,writetofile
from core.networking import iswildcard

count=0
subdomains=subdomainsall('../target-data/no_wild_cards.txt')
print(subdomains)
payload=readfile('../payloads/open_redirect.txt')
for subdomain in subdomains:
	count+=1
	if(count%1000==0):
		sendtoslack("[~] Status (open_redirect) :\nTotal Domains:"+str(len(subdomains))+"\n"+"Domains Scanned: "+str(count))
	if isalive(subdomain):
		writetofile('open_redirect.logs',subdomain)
		new_subdomain=addprotocol(subdomain, 'https')
		ress=multiget(new_subdomain, payload)
		for res in ress:
			try:
				for a in res['response'].history:
					if a.status_code==302 and 'example' in a.headers['location']:
						vul_url=str(new_subdomain+res['word'])
						msg='[~] Open Redirect: '+vul_url
						sendtoslack(msg)

			except:
				pass

	else:
		print('Skipping Wildcard',subdomain)

