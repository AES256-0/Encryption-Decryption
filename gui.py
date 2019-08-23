import tkinter
import encryption_decryption

def result():
    name=str(filename.get())
    length=int(keylength.get())
    filekey=str(keyfile.get())
    encryption_decryption.aesccm_mode_encryption(length,name,filekey)

    



root=tkinter.Tk()
root.geometry("500x200")
root.title("Encryption tool")


label1=tkinter.Label(root,text="filename:")
label1.place(x=0,y=0)

filename=tkinter.Entry(root,width=30,textvariable=tkinter.StringVar())
filename.place(x=200,y=0)

label2=tkinter.Label(root,text="Keylength(128,192,256):")
label2.place(x=0,y=20)

keylength=tkinter.Entry(root,width=30)
keylength.place(x=200,y=20)

label3=tkinter.Label(root,text="keyfile:")
label3.place(x=0,y=40)

keyfile=tkinter.Entry(root,width=30)
keyfile.place(x=200,y=40)

button1=tkinter.Button(root,text="ENCRYPT",command=result)
button1.place(x=200,y=80)




root.mainloop()
