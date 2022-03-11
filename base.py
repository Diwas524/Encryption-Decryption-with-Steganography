import base64
def call(mess):
    
    message_bytes = mess.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    #print(base64_message)
    return(base64_message)
def dec(a):    
    base64_bytes = a.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    mess = message_bytes.decode('ascii')
    return mess


