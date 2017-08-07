from zoodb import *
from debug import *
import os
import hashlib
import random
import pbkdf2
import bank_client

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return cred.token

def login(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if not cred:
        return None
    if cred.password == pbkdf2.PBKDF2(password, cred.salt).hexread(64):
        return newtoken(db,cred)
    else:
        return None

def register(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred:
        return None
    # Adding User Credentials In Cred DB    
    newCred = Cred()
    newCred.username = username
    newCred.salt = os.urandom(8).encode('base_64')   
    newCred.password = pbkdf2.PBKDF2(password, newCred.salt).hexread(64)
    db.add(newCred)
    db.commit()
    # Adding User Details In Person DB
    db1 = person_setup()
    newPerson = Person()
    newPerson.username = username
    db1.add(newPerson)
    db1.commit()
    bank_client.newuser(username)
    return newtoken(db,newCred)

def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False

