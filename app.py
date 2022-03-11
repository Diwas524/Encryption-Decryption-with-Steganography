from fileinput import filename
from flask import Flask, render_template, request
import os
app = Flask(__name__)
app.config["UPLOAD_PATH"]="static/"
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/decryption')
def decrypt():
    return render_template('dec.html')

@app.route("/dec",methods=["GET", "POST"])
def upload_dec():
    if request.method=="POST":
        #print('diw')
        file=request.files['file_name']
        import re
        ss = re.findall("<FileStorage: '(.+)' ", str(file))
        filename=(str(ss).replace("['", "")).replace("']", "")
        dk = int(request.form['dk'])
        hk = str(request.form['hk'])
    
    public = (dk,391)
    print(public)
    from encryptor import decrypt, generate_keypair, encrypt
    from steganography import steganography_decode, steganography_encode
    from base import call ,dec
    steganophaphy_decoded_msg = steganography_decode(filename)
    steganography_decoded_msg_list = list(steganophaphy_decoded_msg.split('-'))
    # print(steganography_decoded_msg_list)
    decrypted_msg = list(decrypt(public, steganography_decoded_msg_list))
    decrypted_msg_string = ''
    for letter in decrypted_msg:
        decrypted_msg_string += letter
    input_hash = hk
    # print(input_hash)
    # print(decrypted_msg[0:64])
    if input_hash == decrypted_msg_string[0:64]:
        b=decrypted_msg_string[64:]
        result = dec(b)
        return render_template("final.html",ext=result)

    else:
        return render_template("final.html",ext='FAILED !! Incorrect hash message')
    
    
   
    
@app.route("/shortenurl",methods=["GET", "POST"])
def upload_file():
    
    if request.method=="POST":
        print('diw')
        file=request.files['file_name']
        print(file)

        from random import randrange
        no=(randrange(100000))
        filename=str(no)+'.png'
        s=os.path.join(app.config["UPLOAD_PATH"],filename)
        file.save(s)
        dev = str(request.form['devanagari'])
        print(dev)
    from encryptor import decrypt, generate_keypair, encrypt
    from steganography import steganography_decode, steganography_encode
    import hashlib
    from base import call ,dec
    raw_message=call(dev)
    hash_of_message = hashlib.sha256(str(raw_message).encode('utf-8'))
    message = str(hash_of_message.hexdigest()) + raw_message
    if (len(message)==0):
        raise ValueError('Data is empty')
    public, private = generate_keypair(17,23)
    print(public)

    # provide the receiver the public key 
    print('Use this key to decode: ' + str(public[0]))
    print('hash of message: ' + hash_of_message.hexdigest())
    encrypted_msg = encrypt(private,message) 
    encrypted_message_string = ''
    for item in encrypted_msg:
        encrypted_message_string+=str(item)+'-'
    print('The encrypted message is : ' + encrypted_message_string)
    encrypted_message_string = encrypted_message_string 
    # now encrypting with steganography
    steganography_encode(encrypted_message_string,filename)
    bill=open('data.txt','a+')
    bill.write("\n"+str(public[0])+","+str(hash_of_message.hexdigest())+","+str(filename))
    bill.close()
    
    
    return render_template("shortenurl.html",hash=public[0],hash1=hash_of_message.hexdigest(), user_image = filename)
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

