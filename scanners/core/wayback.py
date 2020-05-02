import requests
from core.subdomains import removeprotocol
import re
from core.files import removedupes

def wayback(url,include_subdomains):
	url=removeprotocol(url)
	print(url)
	final_data=[]
	try:
		if include_subdomains==True:
			wayback_url='http://web.archive.org/cdx/search/cdx?url=*.'+url+'/*&output=texts&fl=original&collapse=urlkey'
		else:
			wayback_url='http://web.archive.org/cdx/search/cdx?url='+url+'/*&output=texts&fl=original&collapse=urlkey'
		res=requests.get(wayback_url,timeout=15)
	except Exception as e:
		print(e)
	else:
		data=res.text
		for line in data.splitlines():
			final_data.append(line)
	print(final_data)


def waybackwordlist(url,include_subdomains):
	blacklist=r'(.*\.svg|.*\.png|.*\.img|.*\.ttf|http:|:|.*\.eot|.*\woff|.*\.ico|.*\.css|bootstrap|wordpress|.*\.jpg|.*\.jpeg)'
	final_data=[]
	try:
		if include_subdomains==True:
			wayback_url='http://web.archive.org/cdx/search/cdx?url=*.'+url+'/*&output=texts&fl=original&collapse=urlkey'
		else:
			wayback_url='http://web.archive.org/cdx/search/cdx?url='+url+'/*&output=texts&fl=original&collapse=urlkey'
		res=requests.get(wayback_url,timeout=15)
	except Exception as e:
		print(e)
	else:
		data=res.text
		for line in data.splitlines():
			for word in line.split('/'):
				if not re.findall(blacklist, word):
					final_data.append(word)

	return(removedupes(final_data))


def waybackparams(url,include_subdomains):
	blacklist=r'(.*\.svg|.*\.png|.*\.img|.*\.ttf|http:|:|.*\.eot|.*\woff|.*\.ico|.*\.css|bootstrap|wordpress|.*\.jpg|.*\.jpeg)'
	final_data=[]
	try:
		if include_subdomains==True:
			wayback_url='http://web.archive.org/cdx/search/cdx?url=*.'+url+'/*&output=texts&fl=original&collapse=urlkey'
		else:
			wayback_url='http://web.archive.org/cdx/search/cdx?url='+url+'/*&output=texts&fl=original&collapse=urlkey'
		res=requests.get(wayback_url,timeout=15)
	except Exception as e:
		print(e)
	else:
		all_prms=[]
		final_params=[]
		data=res.text
		for line in data.splitlines():
			if '?' in line:
				all_prms.append(line.split('?')[1:][0].split('&'))

		for line in all_prms:
			for l in line:
				final_params.append(l.split('=')[0])

		unique_final=list(dict.fromkeys(final_params))

		return unique_final



def waybackparamurls(url,include_subdomains):
	blacklist=r'(.*\.svg|.*\.png|.*\.img|.*\.ttf|http:|:|.*\.eot|.*\woff|.*\.ico|.*\.css|bootstrap|wordpress|.*\.jpg|.*\.jpeg)'
	final_data=[]
	try:
		if include_subdomains==True:
			wayback_url='http://web.archive.org/cdx/search/cdx?url=*.'+url+'/*&output=texts&fl=original&collapse=urlkey'
		else:
			wayback_url='http://web.archive.org/cdx/search/cdx?url='+url+'/*&output=texts&fl=original&collapse=urlkey'
		res=requests.get(wayback_url,timeout=15)
	except Exception as e:
		print(e)
	else:
		data=res.text
		for line in data.splitlines():
			if '?' in line:
				final_data.append(line)
	return(final_data)	




def waybackpattern(url,include_subdomains,pattern):
	blacklist=r'(.*\.svg|.*\.png|.*\.img|.*\.ttf|http:|:|.*\.eot|.*\woff|.*\.ico|.*\.css|bootstrap|wordpress|.*\.jpg|.*\.jpeg)'
	final_data=[]
	try:
		if include_subdomains==True:
			wayback_url='http://web.archive.org/cdx/search/cdx?url=*.'+url+'/*&output=texts&fl=original&collapse=urlkey'
		else:
			wayback_url='http://web.archive.org/cdx/search/cdx?url='+url+'/*&output=texts&fl=original&collapse=urlkey'
		res=requests.get(wayback_url,timeout=15)
	except Exception as e:
		print(e)
	else:
		data=res.text
		for line in data.splitlines():
			if pattern in line:
				final_data.append(line)
	return(final_data)	




