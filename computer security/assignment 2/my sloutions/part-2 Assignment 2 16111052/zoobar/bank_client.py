from debug import *
from zoodb import *
import rpclib

def transfer(sender, recipient, zoobars):
	with rpclib.client_connect('/banksvc/sock') as rpcc:
		kwargs = {'sender':sender, 'recipient':recipient, 'zoobars':zoobars}
		return rpcc.call('transfer', **kwargs)

def balance(username):
	with rpclib.client_connect('/banksvc/sock') as rpcc:
		kwargs = {'username':username}
		return rpcc.call('balance', **kwargs)

def get_log(username):
	with rpclib.client_connect('/banksvc/sock') as rpcc:
		kwargs = {'username':username}
		return rpcc.call('get_log', **kwargs)

def newuser(username):
	with rpclib.client_connect('/banksvc/sock') as rpcc:
		kwargs = {'username':username}
		return rpcc.call('newuser', **kwargs)