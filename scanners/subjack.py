import time
from core.subdomains import subdomainsall,addprotocol
from core.simple_requests import simpleget
from core.networking import isalive
from core.files import readfile,findforme
from core.output import sendtoslack,writetofile
from core.networking import iswildcard



data=["<strong>Trying to access your account",
"Use a personal domain name",
 "The request could not be satisfied",
 "Sorry, We Couldn't Find That Page",
 "Fastly error: unknown domain",
 "The feed has not been found",
 "You can claim it now at",
 "Publishing platform",                        
 "<title>No such app</title>",                        
 "No settings were found for this company",
 "<title>No such app</title>",
 "is not a registered InCloud YouTrack.",
 "You've Discovered A Missing Link. Our Apologies!",
 "Sorry, couldn&rsquo;t find the status page",                        
 "NoSuchBucket",
 "Sorry, this shop is currently unavailable",
 "<title>Hosted Status Pages for Your Company</title>",
 "data-html-name=\"Header Logo Link\"",                        
 "<title>Oops - We didn't find your site.</title>",
 "class=\"MarketplaceHeader__tictailLogo\"",                        
 "Whatever you were looking for doesn't currently exist at this address",
 "The page you have requested does not exist",
 "This UserVoice subdomain is currently available!",
 "but is not configured for an account on our platform",
 "Looks like you've traveled too far into cyberspace.",
 "The specified bucket does not exist",
 "Bad Request: ERROR: The request could not be satisfied",
 "Please try again or try Desk.com free for",
 "We could not find what you're looking for",
 "No Site For Domain",
 "Project doesnt exist... yet!",
 "project not found",
 "Please renew your subscription",
 "Double check the URL or <a href=\"mailto:help@createsend.com",
 "There is no portal here",
 "You may have mistyped the address or the page may have moved",
 "Repository not found",
 "<title>404 &mdash; File not found</title>",
 "This page is reserved for artistic dogs",
 "<h1>The page you were looking for doesn",
 "<h1>https://www.wishpond.com/404?campaign=true",
 '<p class="bc-gallery-error-code">Error Code: 404</p>',
 "<h1>Oops! We couldn&#8217;t find that page.</h1>",
 "Unrecognized domain <strong>",
 "NoSuchKey",
 "The specified key does not exist",
 "<title>Help Center Closed | Zendesk</title>",
 "If this is your website and you've just created it, try refreshing in a minute", 
"The specified bucket does not exist",                                   
"Repository not found",                                                  
"Trying to access your account?",                                                          
"404 Not Found",                                                         
"The feed has not been found.",                                          
"404 Not Found",                                         
"The thing you were looking for is no longer here, or never was",        
"There isn't a Github Pages site here.",                                 
"We could not find what you're looking for.",                            
"No settings were found for this company:",                              
"Uh oh. That page doesn't exist.",                                         
"is not a registered InCloud YouTrack",                                  
"No Site For Domain",                                                 
"It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.",                                                 
"Tunnel *.ngrok.io not found", 
"404 error unknown site!",                                                 
"Project doesnt exist... yet!", 
"This job board website is either expired or its domain name is invalid.", 
"page not found",                                                 
"project not found",                                                     
"page not found",                                                 
"This UserVoice subdomain is currently available!",                      
"Do you want to register *.wordpress.com?",
"There isn't a GitHub Pages site here.",
"For root URLs (like http://example.com/) you must provide an index.html file",
"There's nothing here",
"No such app",
"There's nothing here.",
"Whatever you were looking for doesn't currently exist at this address",
"Only one step left!",
"You've Discovered A Missing Link. Our Apologies!",
"Building a brand of your own?",
"Trying to access your account?",
"404 Not Found",
"NoSuchBucket",
"The specified bucket does not exist",
"Domain is not configured",
"If you are an Acquia Cloud customer and expect to see your site at this address",
"Please check that this domain has been added to a service",
"Fastly error: unknown domain:",
"The gods are wise",
"This UserVoice subdomain is currently available!",
"The thing you were looking for is no longer here",
"pingdom",
"The feed has not been found",
"We could not find what you're looking for.",
"project not found",
"data-html-name",
"Oops - We didn't find your site.",
"Domain mapping upgrade for this domain not found",
"Do you want to register *.wordpress.com?",
"Repository not found",
"No settings were found for this company:",
"is not a registered InCloud YouTrack",
"404 Web Site not found",
"Project doesnt exist... yet!",
"No Site For Domain",
"Uh oh. That page doesn't exist.",
"It looks like you may have taken a wrong turn somewhere",
"404 error unknown site",
"page not found",
"page not found",
"404 Not Found",
"404 Blog is not found",
"Unrecognized domain",
"Please renew your subscription"]



count=0
subdomains=subdomainsall('../target-data/test1.txt')
for subdomain in subdomains:
	count+=1
	if(count%1000==0):
		sendtoslack("[~] Status (subdomain Takeover) :\nTotal Domains:"+str(len(subdomains))+"\n"+"Domains Scanned: "+str(count))
		writetofile('../output/subjack/logs/subjack.log',subdomain)
		new_subdomain_http=addprotocol(subdomain, 'http')
		new_subdomain_https=addprotocol(subdomain, 'http')
		res1=simpleget(new_subdomain_http)

		# try:
		# 	res1=simpleget(new_subdomain_http)
		# except Exception as e:
		# 	print(e)
		# else:
		# 	if findforme(res1.text, data)==True:
		# 		msg='[~] Possible Subdomain Takeover: '+res1.url
		# 		sendtoslack(msg)

		# try:
		# 	res2=simpleget(new_subdomain_https)
		# except Exception as e:
		# 	print(e)
		# else:
		# 	if findforme(res2.text, data)==True:
		# 		msg='[~] Possible Subdomain Takeover: '+res2.url
		# 		sendtoslack(msg)


