import Credentials
import cli_client


class RunDropbox():

	def __init__(self):
		#print "RunDropbox::__init__"

		self.C 					= Credentials.Credentials()
		#print self.C

		self.init_dropbox()

	def init_dropbox(self):
		print "RunDropbox::init_dropbox"

		APP_KEY				= self.C.KEY
		APP_SECRET 			= self.C.SECRET

		db_usr 				= self.C.usr
		db_pwd				= self.C.pwd

		self.d 				= cli_client

		if APP_KEY == '' or APP_SECRET == '':
			exit("You need to set your APP_KEY and APP_SECRET!")

		term 				= self.d.DropboxTerm(APP_KEY, APP_SECRET, db_usr, db_pwd)
		term.cmdloop()

		#term.login()


if __name__ == '__main__':

    RunDropbox()