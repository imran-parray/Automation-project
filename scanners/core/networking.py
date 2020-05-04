import dns.resolver 
import threading
import time
import requests

def isalive(domain):
	myResolver = dns.resolver.Resolver() 
	try:
		myAnswers = myResolver.query(domain, "A") 
	except Exception as e:
		return False
	else:
		return True
			



def getips(domain):
	ips=[]
	myResolver = dns.resolver.Resolver() 
	try:
		myAnswers = myResolver.query(domain, "A") 
	except Exception as e:
		return False
	else:
		for rdata in myAnswers:
			ips.append(rdata.address)
	return ips	




def dnsresolver(domain,q_type):
	ips=[]
	myResolver = dns.resolver.Resolver() 
	try:
		myAnswers = myResolver.query(domain, q_type) 
	except Exception as e:
		return False
	else:
		return myAnswers


def iswildcard(domain):
	myResolver = dns.resolver.Resolver() 
	try:
		domain='someRandomString1121.'+str(domain)
		myAnswers = myResolver.query(domain, 'A') 
	except Exception as e:
		return False
	else:
		return True

def ishttpwildcard(domain):
	url1=domain+"/someRandomStringAdmin1121"
	url2=domain+"/SomeLoginRegister.php"
	url4=domain+"/.bashrc"
	url5=domain+"/.git"
	
	try:
		r1=requests.head(url1,timeout=3)
		r2=requests.head(url2,timeout=3)
		r4=requests.head(url4,timeout=3)
		r5=requests.head(url5,timeout=3)
	
	except:
		return True
	else:
		if r1.status_code and r2.status_code and r4.status_code and r5.status_code in [200,301,302]:
			print(r1.status_code,r2.status_code,r4.status_code,r5.status_code)
			return True

		else:
			print(r1.status_code,r2.status_code,r4.status_code,r5.status_code)
			return False




def restojson(domain):
	resobj={}
	url1=domain+"/.git/admin/login_Random_String"
	
	try:
		r1=requests.head(url1,timeout=3)
	
	except Exception as e:
		print(e)
		return True
	else:
		resobj['url']=r1.url
		resobj['status_code']=r1.status_code
		resobj['headers']=r1.headers
		return resobj





def check_url(url):
  url = urlparse(url)
  conn = httplib.HTTPConnection(url.netloc)   
  conn.request("HEAD", url.path)
  if conn.getresponse():
    return True
  else:
    return False


def xxyyzz(final_data,domains):
	new_domains=[]
	for domain in domains:
		myResolver = dns.resolver.Resolver() 
		try:
			domains.remove(domain)
			print(domain,'\n=============')
			print(domains)
			time.sleep(1)
			print('\n\n\n\n')
			myAnswers = myResolver.query(domain, "A") 
		except:
			pass
		else:
			final_data.append(domain)




def getlivelist_abc(final_data,domains):
	new_domains=[]
	while len(domains)!=0:
		domain=domains[0]
		myResolver = dns.resolver.Resolver() 
		try:
			domains.remove(domains[0])
			myAnswers = myResolver.query(domain, "A") 
		except:
			pass
		else:
			final_data.append(domain)

def getlivelist(domains,no_of_threads):
	temp_list=domains
	final_data=[]
	threads=[]
	for _ in range(no_of_threads):
		t=threading.Thread(target=getlivelist_abc,args=[final_data,domains])
		time.sleep(0.000000001)
		t.start()
		threads.append(t)
	for th in threads:
		th.join()
	return final_data



# def xxyyzzz(final_data,domain):
# 	myResolver = dns.resolver.Resolver() 
# 	try:
# 		print('checking -->',domain)
# 		myAnswers = myResolver.query(domain, "A") 
# 	except:
# 		pass
# 	else:
# 		final_data.append(domain)
# 	return final_data
