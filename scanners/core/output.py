import json
import requests
import time

def sendtoslack(msg):
	t_data={}
	t_data['text']=msg
	data=json.dumps(t_data)
	res=requests.post("https://hooks.slack.com/services/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",data=data,headers={"content-type":"application/json"})
	print('Sending to Slack[ hackerXcreed ]')


def writetofile(file,msg):
	filename=file
	msg=str(msg)
	try:
		with open(filename,'a') as fh:
			fh.write(msg)
	except Exception as e:
		print(e)

	