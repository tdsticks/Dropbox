# python dropbox api - save token file?
# Include the Dropbox SDK libraries
from dropbox import client, rest, session

# Get your app key and secret from the Dropbox developer website

APP_KEY = 'enter you app key'
APP_SECRET = 'enter your app secret'
ACCESS_TYPE = 'dropbox' # make sure this matches your api app type

#acces token file
try: 
	TOKENS = 'dropbox_token.txt'
	token_file = open(TOKENS)
	token_key,token_secret = token_file.read().split('|')
	token_file.close()
except:
	print "Error, no file found:", TOKENS

sess = session.DropboxSession(APP_KEY,APP_SECRET, ACCESS_TYPE )

request_token = sess.obtain_request_token()

# Make the user sign in and authorize this token
url = sess.build_authorize_url(request_token)
print "url:", url
print "Please authorize in the browser. After you're done, press enter."
raw_input()

# This will fail if the user didn't visit the above URL and hit 'Allow'
access_token = sess.obtain_access_token(request_token)
#save token file

token_file = open(TOKENS,'w')
token_file.write("%s|%s" % (access_token.key,access_token.secret) )
token_file.close()

client = client.DropboxClient(sess)

print "linked account:", client.account_info()

f = open('t.txt')
response = client.put_file(srv_path + '/uploaded_with_python.txt', f)
print "uploaded:", response

folder_metadata = client.metadata(srv_path + '/')
print "metadata:", folder_metadata

f, metadata = client.get_file_and_metadata(srv_path + '/uploaded_with_python',rev='362e2029684fe')
out = open(srv_path + '/uploaded_with_python.txt', 'w')
out.write(f)
print(metadata)

token_file = open(TOKENS,'w')
token_file.write("%s|%s" % (access_token.key,access_token.secret) )
token_file.close()
	
token_file = open(TOKENS)
token_key,token_secret = token_file.read().split('|')
token_file.close()

sess = session.DropboxSession(APP_KEY,APP_SECRET, ACCESS_TYPE )
print sess

sess.set_token(token_key,token_secret)
print sess

client = client.DropboxClient(sess)
print client

