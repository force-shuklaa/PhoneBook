import func
from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('phonebook-database')
cur=con.cursor()
cur.execute("create table if not exists record(contact_id integer primary key autoincrement, fname varchar2(20),mname varchar2(20),lname varchar2(20),company varchar(20),address varchar(20),city char(20),pin integer(6),website varchar2(20),dob date)")
cur.execute("create table if not exists phone(contact_id integer, contact_type text, phone_number text,foreign key(contact_id) references record(contact_id) on delete cascade)")
cur.execute("create table if not exists email(contact_id integer, email_type text, email_id text,foreign key(contact_id) references record(contact_id) on delete cascade)")
root = Tk()
root.geometry('550x700')
#page to save contact
def save():
    if v1.get()==1:
        phone_type='OFFICE'
    elif v1.get()==2:
        phone_type='HOME  '
    elif v1.get()==3:
        phone_type='OTHER '
    if v2.get()==1:
        email_type='OFFICE'
    elif v2.get()==2:
        email_type  ='PERSONAL'
    else :
        x=showerror('Error','Select Type')
        return
    cur.execute("insert into record(fname,mname,lname,company,address,city,pin, website, dob) values(?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get()))
    cur.execute("insert into phone values((select max(contact_id) from record),?,?)",(phone_type,e10.get()))
    cur.execute("insert into email values((select max(contact_id) from record),?,?)",(email_type,e11.get()))
    ##delete
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)
    showinfo("Saved!"," Entry Successful!")
    con.commit()

def close():
    x=askokcancel('Alert','Contact Unsaved')
    if x==True:
        root.destroy()
    
def search():
    def cursel(event1):
        a=lb.curselection()
        if(a==()):
            return 
        else:
            def delete_rec():
                cur.execute('delete from record where fname=? and mname=? and lname=?',k)
                showinfo("Delete","Record successfully deleted")
                root1.destroy()
                root2.destroy()
                con.commit()
            root2=Tk()
            root2.geometry('500x500')
            k=lb.get(a[0])
            cur.execute('select fname,mname,lname,company,address,city,pin,website,dob,contact_type,phone_number,email_type,email_id from record,phone,email where fname=? and mname=? and lname=?',k)
            m=cur.fetchall()
            m=m[0] 
            lo=Listbox(root2,height=15,width=50)
            lo.pack()
            lo.insert(0,"First Name: "+m[0])
            lo.insert(1,"Middle Name: "+m[1])
            lo.insert(2,"Last Name:"+m[2])
            lo.insert(3,"Company Name:"+m[3])
            lo.insert(4,"Address:"+m[4])
            lo.insert(5,"City:"+m[5])
            lo.insert(6,"Pin:"+str(m[6]))
            lo.insert(7,"Website:"+m[7])
            lo.insert(8,"DOB: "+m[8])
            lo.insert(9,"Contact Type:"+m[9])
            lo.insert(10,"Phone no.:"+str(m[10]))
            lo.insert(11,"Email Type:"+m[11])
            lo.insert(12,"Email id:"+m[12])
            Button(root2,text="Close",bg = 'Black',fg = 'White',font = '30',command=root2.destroy).pack()
            Button(root2,text="Delete",bg = 'Black',fg = 'White',font = '30',command=delete_rec).pack()
            
        
    def get_text(event):
        lb.delete(0, END)
        print m1.get()
        cur.execute('select fname,mname,lname from record where fname like "%'+m1.get()+'%" or mname like " %'+m1.get()+'%" or lname like " %'+m1.get()+'%" ')
        res=cur.fetchall()
        for item in range(len(res)):
            lb.insert(item,res[item])
            

    root1=Tk()
    root1.geometry('600x600')
    root1.bind('<Button-1>', cursel)
    Label(root1,text="Searching Phone Book",font="Arial 15",bg="light blue").pack()
    Label(root1,text="Enter Your Name").pack()
    m1=Entry(root1)
    m1.pack()
    m1.bind('<KeyRelease>',get_text)
    lb=Listbox(root1,height=30,width=80,fg="red",selectmode=SINGLE)
    lb.pack()
    Button(root1,text="Close",bg = 'Black',fg = 'White',font = '30',command=root1.destroy).pack()
    root1.mainloop()

def edit():
    def curse2(event2):
        a1=lb2.curselection()
        if(a1==()):
            return 
        else:
            def edit_rec():
                root7=Tk()
                root7.geometry('700x700')
                root4.destroy()
                ee1 = Entry(root7)
                ee1.insert(0,m11[0])
                ee1.grid(row=2,column=1)
                ee2 = Entry(root7)
                ee2.insert(0,m11[1])
                ee2.grid(row=3,column=1)
                ee3 = Entry(root7)
                ee3.insert(0,m11[2])
                ee3.grid(row=4,column=1)
                ee4 = Entry(root7)
                ee4.insert(0,m11[3])
                ee4.grid(row=5,column=1)
                ee5 = Entry(root7)
                ee5.insert(0,m11[4])
                ee5.grid(row=6,column=1)
                ee6 = Entry(root7)
                ee6.insert(0,m11[5])
                ee6.grid(row=7,column=1)
                ee7 = Entry(root7)
                ee7.insert(0,m11[6])
                ee7.grid(row=8,column=1)
                ee8 = Entry(root7)
                ee8.insert(0,m11[7])
                ee8.grid(row=9,column=1)
                ee9 = Entry(root7)
                ee9.insert(0,m11[8])
                ee9.grid(row=10,column=1)
                ee10 = Entry(root7)
                ee10.insert(0,m11[10])
                ee10.grid(row=12,column=1)
                ee11 = Entry(root7)
                ee11.insert(0,m11[12])
                ee11.grid(row=14,column=1)
                cur.execute("select contact_id from record where fname=? and mname=? and lname=?",k1)
                cci=cur.fetchall()
                cci=cci[0][0]
                def update():
                    cur.execute("UPDATE record SET fname=?,mname=?,lname=?,company=?,address=?,city=?,pin=?, website=?, dob=? WHERE contact_id =?",(ee1.get(),ee2.get(),ee3.get(),ee4.get(),ee5.get(),ee6.get(),ee7.get(),ee8.get(),ee9.get(),cci))
                    cur.execute("UPDATE phone SET phone_number=? where contact_id=?",(ee10.get(),cci))
                    cur.execute("UPDATE email SET email_id=? where contact_id=?",(ee11.get(),cci))
                    root7.destroy()
                    showinfo("Saved!"," Phonebook Updated!")
                    con.commit()
                        
                def close1():
                    root7.destroy()
                root3.destroy()
                Label(root7,text = 'Update Phonebook', font = 'Arial 20',fg = 'Blue').grid(row=0,column=1) 
                Label(root7,text = '----------------------------------------',font = 'Arial 20',fg = 'Blue').grid(row=1,column=1)
                Label(root7,text = 'First Name').grid(row=2,column=0)
                Label(root7,text = 'Middle Name').grid(row=3,column=0)
                Label(root7,text = 'Last Name').grid(row=4,column=0)
                Label(root7,text = 'Company Name').grid(row=5,column=0)
                Label(root7,text = 'Address').grid(row=6,column=0)
                Label(root7,text = 'City').grid(row=7,column=0)
                Label(root7,text = 'Pincode').grid(row=8,column=0)
                Label(root7,text = 'Website URL').grid(row=9,column=0)
                Label(root7,text = 'Date of Birth').grid(row=10,column=0)
                Label(root7,text = 'Select Phone Type',fg = 'Blue',font = 'Arial 14').grid(row=11,column=0)
                Label(root7,text = 'Phone Number').grid(row=12,column=0)
                Label(root7,text = 'Select Email Type:',fg = 'Blue',font = 'Arial 14').grid(row=13,column=0)
                Label(root7,text = 'Email Id').grid(row=14,column=0)
                #Button
                Button(root7,text='Update',bg = 'Black',fg = 'White',font = '30',command=update).grid(row=15,column=0)
                Button(root7,text='Close',bg = 'Black',fg = 'White',font = '30',command=close1).grid(row=15,column=2)
                vv1=IntVar()
                Radiobutton(root7,text='OFFICE',variable=vv1,value =1,tristatevalue='a').grid(row=11,column=1)
                Radiobutton(root7,text='HOME  ',variable=vv1,value =2,tristatevalue='a').grid(row=11,column=2)
                Radiobutton(root7,text='OTHER ',variable=vv1,value =3,tristatevalue='a').grid(row=11,column=3)
                vv2=IntVar()
                Radiobutton(root7,text='OFFICE  ',variable=vv2,value =1,tristatevalue='a').grid(row=13,column=1)
                Radiobutton(root7,text='PERSONAL',variable=vv2,value =2,tristatevalue='a').grid(row=13,column=2)
                con.commit()
            root3=Tk()
            root3.geometry('500x500')
            k1=lb2.get(a1[0])
            cur.execute('select fname,mname,lname,company,address,city,pin,website,dob,contact_type,phone_number,email_type,email_id from record,phone,email where fname=? and mname=? and lname=?',k1)
            m11=cur.fetchall()
            m11=m11[0] 
            lo1=Listbox(root3,height=15,width=50)
            lo1.pack()
            lo1.insert(0,"First Name: "+m11[0])
            lo1.insert(1,"Middle Name: "+m11[1])
            lo1.insert(2,"Last Name:"+m11[2])
            lo1.insert(3,"Company Name:"+m11[3])
            lo1.insert(4,"Address:"+m11[4])
            lo1.insert(5,"City:"+m11[5])
            lo1.insert(6,"Pin:"+str(m11[6]))
            lo1.insert(7,"Website:"+m11[7])
            lo1.insert(8,"DOB: "+m11[8])
            lo1.insert(9,"Contact Type:"+m11[9])
            lo1.insert(10,"Phone no.:"+str(m11[10]))
            lo1.insert(11,"Email Type:"+m11[11])
            lo1.insert(12,"Email id:"+m11[12])
            Button(root3,text="Close",bg = 'Black',fg = 'White',font = '30',command=root3.destroy).pack()
            Button(root3,text="Edit",bg = 'Black',fg = 'White',font = '30',command=edit_rec).pack()
            
        
    def get_text1(event2):
        lb2.delete(0, END)
        print m123.get()
        cur.execute('select fname,mname,lname from record where fname like "%'+m123.get()+'%" or mname like " %'+m123.get()+'%" or lname like " %'+m123.get()+'%" ')
        res1=cur.fetchall()
        for i in range(len(res1)):
            lb2.insert(i,res1[i])
            

    root4=Tk()
    root4.geometry('600x600')
    root4.bind('<Button-1>', curse2)
    Label(root4,text="Searching Phone Book",font="Arial 15",bg="light blue").pack()
    Label(root4,text="Enter Your Name").pack()
    m123=Entry(root4)
    m123.pack()
    m123.bind('<KeyRelease>',get_text1)
    lb2=Listbox(root4,height=30,width=80,fg="red",selectmode=SINGLE)
    lb2.pack()
    Button(root4,text="Close",bg = 'Black',fg = 'White',font = '30',command=root4.destroy).pack()
    root4.mainloop()
    

img=PhotoImage(file ='image11.gif')
#Labels
Label(root,image=img).grid(row=0,column=1) 
Label(root,text = '  Phone Book  ',font = 'Arial 20',fg = 'Blue').grid(row=1,column=1)
Label(root,text = 'First Name').grid(row=2,column=0)
Label(root,text = 'Middle Name').grid(row=3,column=0)
Label(root,text = 'Last Name').grid(row=4,column=0)
Label(root,text = 'Company Name').grid(row=5,column=0)
Label(root,text = 'Address').grid(row=6,column=0)
Label(root,text = 'City').grid(row=7,column=0)
Label(root,text = 'Pincode').grid(row=8,column=0)
Label(root,text = 'Website URL').grid(row=9,column=0)
Label(root,text = 'Date of Birth').grid(row=10,column=0)
Label(root,text = 'Select Phone Type',fg = 'Blue',font = 'Arial 14').grid(row=11,column=0)
Label(root,text = 'Phone Number').grid(row=12,column=0)
Label(root,text = 'Select Email Type:',fg = 'Blue',font = 'Arial 14').grid(row=13,column=0)
Label(root,text = 'Email Id').grid(row=14,column=0)
#Entry
e1 = Entry(root)
e1.insert(0,'')
e1.grid(row=2,column=1)
e2 = Entry(root)
e2.insert(0,'')
e2.grid(row=3,column=1)
e3 = Entry(root)
e3.insert(0,'')
e3.grid(row=4,column=1)
e4 = Entry(root)
e4.insert(0,'')
e4.grid(row=5,column=1)
e5 = Entry(root)
e5.insert(0,'')
e5.grid(row=6,column=1)
e6 = Entry(root)
e6.insert(0,'')
e6.grid(row=7,column=1)
e7 = Entry(root)
e7.insert(0,'')
e7.grid(row=8,column=1)
e8 = Entry(root)
e8.insert(0,'')
e8.grid(row=9,column=1)
e9 = Entry(root)
e9.insert(0,'')
e9.grid(row=10,column=1)
e10 = Entry(root)
e10.insert(0,'')
e10.grid(row=12,column=1)
e11 = Entry(root)
e11.insert(0,'')
e11.grid(row=14,column=1)

#Radio Button
v1=IntVar()
Radiobutton(root,text='OFFICE',variable=v1,value =1,tristatevalue='a').grid(row=11,column=1)
Radiobutton(root,text='HOME  ',variable=v1,value =2,tristatevalue='a').grid(row=11,column=2)
Radiobutton(root,text='OTHER ',variable=v1,value =3,tristatevalue='a').grid(row=11,column=3)
v2=IntVar()
Radiobutton(root,text='OFFICE  ',variable=v2,value =1,tristatevalue='a').grid(row=13,column=1)
Radiobutton(root,text='PERSONAL',variable=v2,value =2,tristatevalue='a').grid(row=13,column=2)
#Button
Button(root,text='Save',bg = 'Black',fg = 'White',font = '30',command=save).grid(row=15,column=0)
Button(root,text='Search',bg = 'Black',fg = 'White',font = '30',command=search).grid(row=15,column=1)
Button(root,text='Close',bg = 'Black',fg = 'White',font = '30',command=close).grid(row=15,column=2)
Button(root,text='Edit',bg = 'Black',fg = 'White',font = '30',command=edit).grid(row=15,column=3)
root.mainloop()

