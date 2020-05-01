from core.urls import fuzzableurls,fuzzableurlswithpayload
from core.wayback import waybackparamurls

print(fuzzableurls(waybackparamurls('miraki.com',False),'endpoints'))