from debug import *
from zoodb import *
import rpclib

def login(username, password):
	with rpclib.client_connect('/authsvc/sock') as rpcc:
		kwargs = {'username':username, 'password':password}
		return rpcc.call('login', **kwargs)

def register(username, password):
	with rpclib.client_connect('/authsvc/sock') as rpcc:
		kwargs = {'username':username, 'password':password}
		return rpcc.call('register', **kwargs)

def check_token(username, token):
	with rpclib.client_connect('/authsvc/sock') as rpcc:
		kwargs = {'username':username, 'token':token}
		return rpcc.call('check_token', **kwargs)