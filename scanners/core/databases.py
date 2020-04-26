import time
import json


def get_collection(subdomain):
	coll=subdomain.split('.')[-2:]
	collection=coll[0]+'.'+coll[1]
	return collection


def database_pattern(target,scan_type,data):
	j_data=json.dumps(data)
	ts=time.time()
	data='''


{
	"target":"'''+target+'''",
	"data":{
		"'''+str(ts).split('.')[0]+'''":{
			"type":"'''+scan_type+'''",
			"data":{
				"Found":'''+str(j_data)+'''
			}
		}
	}
}



	'''
	return json.loads(data)
