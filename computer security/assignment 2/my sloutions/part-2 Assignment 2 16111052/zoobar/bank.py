from zoodb import *
from debug import *

import time

def transfer(sender, recipient, zoobars):
    if zoobars < 0 :
        return ValueError()
    # if sender == recipient:
    #     raise AttributeError()


    bankdb = bank_setup()
    senderp = bankdb.query(Bank).get(sender)
    recipientp = bankdb.query(Bank).get(recipient)

    sender_balance = senderp.zoobars - zoobars
    recipient_balance = recipientp.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    senderp.zoobars = sender_balance
    recipientp.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    db = bank_setup()
    bk = db.query(Bank).get(username)
    return bk.zoobars

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))

def newuser(username):
     # Adding User Balance Details In Bank DB
    bankdb = bank_setup()
    bank = bankdb.query(Bank).get(username)
    if bank:
        return None
    newBank = Bank()
    newBank.username = username
    bankdb.add(newBank)
    bankdb.commit()