import tkinter
import encryption_decryption

def result():
    name=str(filename.get())
    length=int(keylength.get())
    key=str(keyfile.get())
    encryption_decryption.aesccm_mode_encryption(length,name,key)


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

button=tkinter.Button(root,text="Encrypt",command=result,bg="grey",fg="black")
button.place(x=200,y=80)

root.mainloop()
