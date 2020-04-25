import time
from core.subdomains import subdomainsall,addprotocol
from core.multi_requests import multiget
from core.threaded_requests import threadedput

subdomains=subdomainsall('../target-data/subdomains.txt')

for subdomain in subdomains:
	domain=addprotocol(subdomain,'http')
	pathsx=['a','b','c','d']
	data=threadedput(domain,pathsx,10,res_properties=('url','status_code'),data={"name":"imran"})
print(data)


