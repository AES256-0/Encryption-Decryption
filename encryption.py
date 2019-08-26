import tkinter
import encryption_decryption

def result():
    name=str(filename.get())
    length=int(keylength.get())
    key=str(keyfile.get())
    algo_name=gcm_ccm.get()
    if algo_name=="AESCCM":
        encryption_decryption.aesccm_mode_encryption(length,name,key)
    elif (algo_name=="AESGCM"):
        encryption_decryption.aesgcm_mode_encryption(length,name,key)
    else:
        print("Provide the correct algoriithm")



root=tkinter.Tk()
root.geometry("500x300")
root.title("ENCRYPTOR")

label1=tkinter.Label(root,text="filename:")
label1.place(x=0,y=0)

filename=tkinter.Entry(root,width=30)
filename.place(x=200,y=0)

label2=tkinter.Label(root,text="keylength:")
label2.place(x=0,y=20)

keylength=tkinter.Entry(root,width=30)
keylength.place(x=200,y=20)

label3=tkinter.Label(root,text="keyfile:")
label3.place(x=0,y=40)

keyfile=tkinter.Entry(root,width=30)
keyfile.place(x=200,y=40)

label4=tkinter.Label(root,text="AESGCM OR AESCCM:")
label4.place(x=0,y=60)

gcm_ccm=tkinter.Entry(root,width=30)
gcm_ccm.place(x=200,y=60)

button=tkinter.Button(root,text="Encrypt",command=result,bg="grey",fg="black")
button.place(x=200,y=100)

root.mainloop()
