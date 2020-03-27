from Tkinter import *
root2=Tk()
root2.geometry('900x400')
Label(root2,text="Project Title: PhoneBook", font="times 20 bold").grid(row=0,column=0)
Label(root2,text="Project of Python and Database", font="times 25 bold", fg="red").grid(row=1,column=1)
Label(root2,text="Developed By: Aryan Shukla", font="times 15 bold", fg="blue").grid(row=2,column=1)
Label(root2,text="---------------------------------------", font="times 15 bold", fg="red").grid(row=3,column=1)
Label(root2,text="make mouse movement over this screen to close", fg="blue").grid(row=4,column=1)
def motion(e=1):
    root2.destroy()
root2.bind("<Motion>",motion)
root2.mainloop()
