import re


def subdomainsall(file):
	subdomains=[]
	with open(file,'r') as fh:
		for line in fh:
			subdomains.append(line.rstrip())
		return subdomains




def subdomainsofdomain(file,domain):
	subdomains=[]
	with open(file,'r') as fh:
		for line in fh:
			if domain in line:
				subdomains.append(line.rstrip())
		return subdomains

def addprotocol(domain,protocol):
	domain=str(protocol)+'://'+str(domain)
	return domain



def removeprotocol(domain):
	return re.sub(r'(^.*:|/)',"",domain)



def removeandappend(domain,newprotocol):
	old_domain=domain
	domain=re.sub(r'(^.*:|/)',"",old_domain)
	new_domain=str(newprotocol)+'://'+str(domain)
	return new_domain