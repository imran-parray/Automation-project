import time
import sys
from core.subdomains import subdomainsall,addprotocol
from core.multi_requests import multiget,multipost
from core.networking import isalive
from core.files import readfile
from core.output import sendtoslack,writetofile
from core.networking import iswildcard
from core.timendate import current_en_time
from core.wayback import waybackparamurls
from core.urls import fuzzableurls
import os

xtime=current_en_time()
log_file='../output/open_redirect/logs/open_redirect.log'
output_file='../output/cloudflair/output/cloudflair.txt'
writetofile(output_file, xtime)

subdomains=[]
payloads=[]
resume=''
try:
    domain_list=sys.argv[1]
    payload_list=sys.argv[2]
    resume=sys.argv[3]
except Exception as e:
	print('[~] Incomplete Parameters [Needed : 3] - [Passed '+str(len(sys.argv)-1)+']')
	print('Usage: pthon3 script.py domains.txt payloads.txt (resume|noresume)')
	exit()
subdomains=subdomainsall(domain_list)
payloads=readfile(payload_list)
if resume=='resume':
    resumed=readfile(log_file)[0]
    d_index=subdomains.index(resumed)
    del subdomains[0:d_index+1] 


#=================Start From here==============================#

