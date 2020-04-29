These Changes are from linux system


### Simple Requests 

| Name  | Description  | parameters|  Example  |
|---|---|---|---|
| simpleget()     | Send an get request to an url     |  simpleget(string)  |simpleget(url)  |
| simplepost()    | Sends an post request to an url   |   simplepost('url',*list_of_tuples) |simplepost('url',('name','imran'),('class',10))  |
| simplepatch()   | Sends an patch request to an url  |   simplepost('url',*list_of_tuples)     |simplepatch('url',('name','imran'),('class',10))  |
| simpledelete()  | Sends an delete request to an url |    simplepost('url',*list_of_tuples)    |simpledelete('url',('name','imran'),('class',10)) |
| simpleput()     | Sends an put request to an url    |    simplepost('url',*list_of_tuples)    |simpleput('url',('name','imran'),('class',10)) |
|   |   |   |



## Multi requests 
| Name  | Description  |  parameters  | Output |Example  |
|---|---|---|---|---|
| multiget()  | Use to send a list of get requests to a single url  | multiget(string,list)  |  \<list of Response Objects\>  |    multiget('http://localhost:8000/get',words)  |
| multipost() | Use to send a list of POST requests to a single url   |multipost(string,list,dict)   | \<list of Response Objects\>  | multipost(url,list,data={"name":"value"}  |
| multiput()  | Use to send a list of PUT requests to a single url   |multiput(string,list,dict)   | \<list of Response Objects\>  |  multipost(url,list,data={"name":"value"}  |
| multidelete() | Use to send a list of DELETE requests to a single url   | multidelete(string,list,dict)  | \<list of Response Objects\> |   multipost(url,list,data={"name":"value"}  |
| multipatch()  | Use to send a list of PATCH requests to a single url   |multipatch(string,list,dict)   | \<list of Response Objects\>  | multipost(url,list,data={"name":"value"}  |



## Threaded Requests

| Name  | Description  |  parameters  | Output |Example  |
|---|---|---|---|---|
|  threadedget()  [threaded]| Use to send a list of GET requests to a single url using threads  | threadedget(string,list,int,\*res_property)  |\<List of dicts with response properties\>   |threadedget('http://localhost:8000',words,2,'url','status_code')   |
|  threadedpost()  [threaded]| Use to send a list of POST requests to a single url using threads  | threadedget(string,list,int,\*res_property)  |\<List of dicts with response properties\>   |threadedpost('http://localhost:8000',words,10,data={"name":"imran"},res_properties=('status_code','url'))   |
|  threadedpatch()  [threaded]| Use to send a list of PATCH requests to a single url using threads  | threadedget(string,list,int,\*res_property)  |\<List of dicts with response properties\>   |threadedpatch('http://localhost:8000',words,10,data={"name":"imran"},res_properties=('status_code','url'))   |
|  threadedput()  [threaded]| Use to send a list of PUT requests to a single url using threads  | threadedget(string,list,int,\*res_property)  |\<List of dicts with response properties\>   |threadedput('http://localhost:8000',words,10,data={"name":"imran"},res_properties=('status_code','url')) |
|  threadeddelete()  [threaded]| Use to send a list of DELETE requests to a single url using threads  | threadedget(string,list,int,\*res_property)  |\<List of dicts with response properties\>   |threadeddelete('http://localhost:8000',words,10,data={"name":"imran"},res_properties=('status_code','url'))|


## Networking

| Name  | Description  |  Parameters   | output | Example  | 
|---|---|---|---|---|
| isalive()  | Checks if the host is alive  | isalive(string)  | True\|False  | isalive('google.com')  |
| getips()  | Checks if host is live then grabs the ip or list of its ip's  | getips(string)  | True\|false  | isalive('google.com')|
| dnsresolver  |  Get any DNS records of an host | dnsresolver(string,string)  | <dnsResolver.Object>  |dnsresolver('google.com','AAAA')|
| iswildcard()  | checks if domain supports wildcard DNS  | iswildcard(string)  |  True\|False  |  iswildcard('google.com')  |
|  getlivelist() [Threaded]| Filters the list of hosts for live hosts  |getlivelist(string,int)   | <list> of live domains   |  getlivelist(domains[],no_of_threads)  |
|   |   |   |   |    |



## Wayback

| Name  | Description  |  Parameters   | output | Example  | 
|---|---|---|---|---|
| wayback()  | Retrieves the list of URL from wayback  | wayback(string,boolean)  | \<list of urls>  |wayback(url,True) |
| waybackwordlist()  | Retrives the list of URL and creates an Wordlist out of them  | wayback(string,boolean)  | \<list of words>  |  waybackwordlist(url,False) |
| waybackparamurls()  | Retrives the list of URL with parameters and creates a list of them  | wayback(string,boolean)  | \<list of words>  |  waybackwordlist(url,False) |
| waybackpattern()  | Retrives the list of URL and extracts all the url match the patterns out of them | wayback(string,boolean,string)  | \<list of words>  |  waybackwordlist(url,False,'login') |
|   |   |   |   |    |


## Files
| Name  | Description  |  Parameters   | output | Example  | 
|---|---|---|---|---|
| readfile() | Reads an File   | readfile(string)    | \<list of lines>   | readfile('filename.txt')   |
| readmultifile()  |  Reads an list of Files  | readfile(string,string,string)   | \<list of lines>    |readfile('filename.txt','file2.txt','file3.txt)    |
| readjson() | Reads an Json File   | readfile(string)    | \<json Python Object>  | readjson('filename.txt')   |
| removedupes()  |  Removes dupes from a list  |  removedupes(list)  | \<list>   | removedupes(list_name)   |




## Files
| Name  | Description  |  Parameters   | output | Example  | 
|---|---|---|---|---|
| subdomainsall()  | Returns subdomains of all domains in file  | subdomainsall(string)  | <list of subdomains>  | subdomainsall('file.txt')  |
| subdomainsofdomain()  | Returns subdomains of specific domain  | subdomainsofdomain(string,string)  | <list of subdomains>  | subdomainsall('file.txt','topleveldomain.com')  |
| addprotocol()  | Addss protocol handler to an domain  | addprotocol(string,string)  | <string domain with protocol>  | addprotocol('domain','xyz.domain.com')  |
| removeprotocol()  | Removes protocol handler from an domain  | removeprotocol(string)  | <string domain without protocol>  | removeprotocol('domain','https://xyz.domain.com')  |
| removeandappend()  | Removes old protocol handler and attached new one to the domain  | removeandappend(string,string)  | <string domain with new protocol handler>  |removeandappend('https://google.com','ftp')  |


## Template
| Name  | Description  |  Parameters   | output | Example  | 
|---|---|---|---|---|
|   |   |   |   |   |
|   |   |   |   |   |




```python
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

if len(sys.argv)-1 != 2:
    print("""
Usage: {} <port_number> <url>
    """.format(sys.argv[0]))
    sys.exit()

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', sys.argv[2])
       self.end_headers()

HTTPServer(("", int(sys.argv[1])), Redirect).serve_forever()
```
