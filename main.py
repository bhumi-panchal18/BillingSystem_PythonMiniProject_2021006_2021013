from tkinter import messagebox
from tkinter import *
import os

main1 = Tk()
main1.geometry("1366x768")
main1.title("Billing System")
main1.resizable(0, 0)
def Exit():
    display = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main1)
    if display == True:
        main1.destroy()
        
main1.protocol("WM_DELETE_WINDOW", Exit)

def emp():
    main1.withdraw()
    os.system("python employee.py")
    main1.deiconify()


def adm():
    main1.withdraw()
    os.system("python admin.py")
    main1.deiconify()

label1 = Label(main1)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/admin.png")
label1.configure(image=img)

button1 = Button(main1)
button1.place(relx=0.316, rely=0.446, width=200, height=200)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="./images/1.png")
button1.configure(image=img2)
button1.configure(command=emp)

button2 = Button(main1)
button2.place(relx=0.566, rely=0.448, width=200, height=200)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="./images/2.png")
button2.configure(image=img3)
button2.configure(command=adm)

main1.mainloop()
