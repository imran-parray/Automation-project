from core.wayback import waybackparamurls
from core.files import removedupes
import re
import sys


def fuzzableurls(list_of_urls,payload=''):
	if payload=='':
		urls=list_of_urls
		regex2=r'=(.*)$'

		final=[]

		for line in urls:
			params=[]
			if '?' in line:
				params.append(line.split('?')[0])
				x=line.split('?')[1]
				z=x.split('&')
				for a in z:
					params.append(re.sub(regex2, '=FUZZ&', a))

			final.append('?'.join(params).replace('&?','&').rstrip('&'))

		finalx=removedupes(final)
		return finalx
	if payload!='':
		payloads=[]
		urls=list_of_urls
		regex2=r'=(.*)$'

		final=[]

		for line in urls:
			params=[]
			if '?' in line:
				params.append(line.split('?')[0])
				x=line.split('?')[1]
				z=x.split('&')
				for a in z:
					params.append(re.sub(regex2, '=FUZZ&', a))

			final.append('?'.join(params).replace('&?','&').rstrip('&'))

		finalx=removedupes(final)
		for line in finalx:
				pay='/'.join(''.join(line.split('.')[1:]).split('/')[1:])
				pay_new=pay.replace('FUZZ', payload)
				payloads.append(pay_new)
		return payloads

def fuzzableurlswithpayload(list_of_urls,payload):
	payloads=[]
	urls=list_of_urls
	regex2=r'=(.*)$'

	final=[]

	for line in urls:
		params=[]
		if '?' in line:
			params.append(line.split('?')[0])
			x=line.split('?')[1]
			z=x.split('&')
			for a in z:
				params.append(re.sub(regex2, '=FUZZ&', a))

		final.append('?'.join(params).replace('&?','&').rstrip('&'))

	finalx=removedupes(final)
	for line in finalx:
			pay='/'.join(''.join(line.split('.')[1:]).split('/')[1:])
			pay_new=pay.replace('FUZZ', 'xxxxxxxxxxxxx')
			payloads.append(pay_new)
			print(pay_new)