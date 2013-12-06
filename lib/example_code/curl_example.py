import urllib2

#manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
#manager.add_password(None, 'https://app.streamsend.com/emails', 'login', 'key')
#handler = urllib2.HTTPBasicAuthHandler(manager)

director = urllib2.OpenerDirector()
#director.add_handler(handler)

req = urllib2.Request('https://app.streamsend.com/emails', headers = {'Accept' : 'application/xml'})

result = director.open(req)
# result.read() will contain the data
# result.info() will contain the HTTP headers

print result.info()
print result.read()

# To get say the content-length header
#length = result.info()['Content-Length']



################################################



# This packages the request (it doesn't make it) 
request = urllib2.Request(url)
 
# Sends the request and catches the response
response = urllib2.urlopen(request)
 
# Extracts the response
html = response.read()
 
# Print it out
print html 