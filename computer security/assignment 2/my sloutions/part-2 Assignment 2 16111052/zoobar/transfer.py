from flask import g, render_template, request

from login import requirelogin
from zoodb import *
from debug import *
import bank_client
import traceback

@catch_err
@requirelogin
def transfer():
    warning = None
    try:
        if 'recipient' in request.form:
            zoobars = eval(request.form['zoobars'])

            if g.user.person.username == request.form['recipient']:
                raise AttributeError()

            ret = bank_client.transfer(str(g.user.person.username), str(request.form['recipient']), zoobars)
            if ret == 0: 
                raise AttributeError()

            warning = "Sent %d zoobars" % zoobars
    except (KeyError, ValueError, AttributeError) as e:
        traceback.print_exc()
        warning = "Transfer to %s failed" % request.form['recipient']

    return render_template('transfer.html', warning=warning)
