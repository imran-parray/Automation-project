import json
import yaml

def readfile(file):
	words=[]
	try:
		with open(file,'r') as fh:
			for line in fh:
				words.append(line.rstrip())
	except Exception as e:
		pass
	else:
		return words



def readyaml(file):
	with open(file) as f:
		dataMap = yaml.safe_load(f)
	return dataMap


def readmultifiles(*files):
	words=[]
	for file in files:
		try:
			with open(file,'r') as fh:
				for line in fh:
					words.append(line.rstrip())
		except Exception as e:
			pass
	else:
		return words





def readjson(file):
	words=''
	try:
		with open(file,'r') as fh:
			for line in fh:
				words=words+line
			json_data=json.loads(words)
	except Exception as e:
		pass
	else:
		return json_data

def removedupes(mylist):
	return list(dict.fromkeys(mylist))

