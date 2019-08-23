from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers.aead import AESCCM
import os
import shelve
import tkinter


def aesccm_mode_encryption(bitlength,filename,key):
    fd=open(filename,"r")
    data=fd.read()
    data=data.encode()
    fd.close()
    
    if not key:
        print("****Generating key with key length:"+str(bitlength))
        key=AESCCM.generate_key(bit_length=bitlength)
    else:
        fd=shelve.open(key)
        key=fd["key"]
    key1=AESCCM(key[0])
    nonce=os.urandom(12)

    print("***Encrypting your data***")
    ct=key1.encrypt(nonce,data,None)
    ls=[key,nonce]
    print("***Saving your data to file:"+filename+"_decrypted.db***")
    new_name=filename+"_decrypted"
    db=shelve.open(new_name)
    db["data"]=ct
    db.close()
    print("***saving you key and nonces to file:"+filename+"_keys.db")
    key_file=filename+"_keys"
    db=shelve.open(key_file)
    db["key"]=ls
    db.close()




def aesccm_mode_decryption(filename,key):
    fd=shelve.open(filename)
    fs=fd["data"]
    fd.close()
    print("***Reading your keys***")
    fd=shelve.open(key)
    ls=fd["key"]
    data=AESCCM(ls[0]).decrypt(ls[1],fs,None)
    new_file=filename + "_decrypted"
    fd=open(new_file,"w")
    fd.write(str(data))
    fd.close()

if __name__=="__main__":
    pass
