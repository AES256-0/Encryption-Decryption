import tkinter
import encryption_decryption

def result():
    fname=filename.get()
    keyf=key.get()
    alg=aes.get()
    if alg=="AESCCM":
        encryption_decryption.aesccm_mode_decryption(fname,keyf)
    elif(alg=="AESGCM"):
        encryption_decryption.aesgcm_mode_decryption(fname,keyf)
    else:
        print("Error")



root=tkinter.Tk()
root.geometry("450x200")
root.title("DECRYPTER")


label1=tkinter.Label(root,text="Filename:")
label1.place(x=0,y=0)

filename=tkinter.Entry(root,width=30)
filename.place(x=200,y=0)

label2=tkinter.Label(root,text="key:")
label2.place(x=0,y=20)

key=tkinter.Entry(root,width=30)
key.place(x=200,y=20)

label3=tkinter.Label(root,text="AESGCM OR AESCCM")
label3.place(x=0,y=40)

aes=tkinter.Entry(root,width=30)
aes.place(x=200,y=40)

button=tkinter.Button(root,text="Decrypt",command=result,bg="grey",fg="black")
button.place(x=200,y=80)

root.mainloop()
