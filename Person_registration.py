
from tkinter import *
import mysql.connector
from tkinter import messagebox as msg
from pymysql import *
con=mysql.connector.connect(host="localhost", user="root",password="Your_password")
cur=con.cursor(buffered=True)
 
 #You can give any name as data-base name .
try:
    cur.execute("use ducat")
except:
    cur.execute("create database ducat")
    cur.execute("use ducat")

try:
    cur.execute("describe persons")
except:
    cur.execute("create table persons(id int primary key auto_increment, name varchar(40), age int, gender varchar(7), email varchar(30), mobile varchar(30))")
    

class myregistration(Frame):
    def __init__(self,master):

        super().__init__(master)
       
        #labels for table
        self.l1=Label(self, text="Name")
        self.l2=Label(self, text="Age")
        self.l3=Label(self, text="Gender")
        self.l4=Label(self, text="Email")
        self.l5=Label(self, text="Mobile Number: ")

        # creating new lable and for delete 
        self.l6=Label(self, text= "ID-NO : ")
        self.l6.grid(row=0, column=3)
        
        #creating entry for delete option 
        self.t6=Entry(self)
        self.t6.grid(row=0, column=4)

        #creating lable for search. To find specific data 
        self.l7=Label(self,text="Email-Id")  
        self.l7.grid(row=0, column=5)

        #creating entry for search 
        self.t7=Entry(self)
        self.t7.grid(row=0, column=6)

        #aLL label grid
        self.l1.grid(row=0, column=0)
        self.l2.grid(row=1, column=0)
        self.l3.grid(row=2, column=0)
        self.l4.grid(row=3, column=0)
        self.l5.grid(row=4, column=0)
        
        # table entry
        self.t1=Entry(self)
        self.t2=Entry(self)
        self.t3=Entry(self)
        self.t4=Entry(self)
        self.t5=Entry(self)
          
        #table entry grid
        self.t1.grid(row=0,column=1) 
        self.t2.grid(row=1,column=1)
        self.t3.grid(row=2,column=1)
        self.t4.grid(row=3,column=1)
        self.t5.grid(row=4,column=1)
        
        #Button to Submit entry in the table
        self.B1=Button(self, text="Submit",command=self.Registration)

        #Button to show all data in the table
        self.B2=Button(self, text="Fatch-All",command=self.fetch_data)

        #creating a delete button 
        self.B3=Button(self,text="Delete",command=self.Delete )
        self.B3.grid(row=2,column=4)

        #creating a search button
        self.B4=Button(self,text="Search",command=self.Search )
        self.B4.grid(row=2,column=6) 

        self.B1.grid(row=8,column=0)
        self.B2.grid(row=8,column=1)

        self.pack()
    
    #creating function for Search

    def Search(self):

        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="your_data_base_name"
          )
        cursor= con.cursor()
        email=self.t7.get()
        cursor.execute("SELECT * FROM persons where(email='%s')"%(email))
        results = cursor.fetchall()

        # create new window to display fetched data
        new_window = Toplevel()
        new_window.title("Search by email ")

        #label name according to mysql table and grid
    
        l1 = Label(new_window, text="ID")
        l1.grid(row=0, column=0)

        l2 = Label(new_window, text="Name")
        l2.grid(row=0, column=1)

        l3 = Label(new_window, text="Age")
        l3.grid(row=0, column=2)

        l4 = Label(new_window, text="Gender")
        l4.grid(row=0, column=3)

        l5 = Label(new_window, text="Email")
        l5.grid(row=0, column=4)

        l6 = Label(new_window, text="Mobile")
        l6.grid(row=0, column=5)
        # creating a loop to call all data in mysql table through index, row 
        for index, row in enumerate(results):

            ID = Label(new_window, text=row[0])
            ID.grid(row=index + 2, column=0) #row=index is gap between rows

            Name = Label(new_window, text=row[1])
            Name.grid(row=index + 2, column=1)

            Age = Label(new_window, text=row[2])
            Age.grid(row=index + 2, column=2)
 
            Gender = Label(new_window, text=row[3])
            Gender.grid(row=index + 2, column=3)
 
            Email = Label(new_window, text=row[4])
            Email.grid(row=index + 2, column=4)

            Mobile = Label(new_window, text=row[5])
            Mobile.grid(row=index + 2, column=5)
        con.close()

    #function for fetching whole data.
    
    def fetch_data(self):

        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Your_password",
        database="your_data_base_name"
          )
        cursor= con.cursor()

        cursor.execute(f"SELECT * FROM persons ")
        results = cursor.fetchall()

        # create new window to display fetched data
        new_window = Toplevel()
        new_window.title("Fetched Data")
    
        l1 = Label(new_window, text="ID")
        l1.grid(row=0, column=0)

        l2 = Label(new_window, text="Name")
        l2.grid(row=0, column=1)

        l3 = Label(new_window, text="Age")
        l3.grid(row=0, column=2)

        l4 = Label(new_window, text="Gender")
        l4.grid(row=0, column=3)

        l5 = Label(new_window, text="Email")
        l5.grid(row=0, column=4)

        l6 = Label(new_window, text="Mobile")
        l6.grid(row=0, column=5)

        for index, row in enumerate(results):

            ID = Label(new_window, text=row[0])
            ID.grid(row=index + 1, column=0)

            Name = Label(new_window, text=row[1])
            Name.grid(row=index + 1, column=1)

            Age = Label(new_window, text=row[2])
            Age.grid(row=index + 1, column=2)
 
            Gender = Label(new_window, text=row[3])
            Gender.grid(row=index + 1, column=3)
 
            Email = Label(new_window, text=row[4])
            Email.grid(row=index + 1, column=4)

            Mobile = Label(new_window, text=row[5])
            Mobile.grid(row=index + 1, column=5)
        con.close()

  #function for registration 

    def Registration(self):
        con=connect(db='data_base_name',user='root',password='your_password',host='localhost')
        cur=con.cursor()
        name=self.t6.get()
        age=int(self.t2.get())
        gender=self.t3.get()
        email=self.t4.get()
        mobile=self.t5.get()
        i=cur.execute(f"insert into persons(name, age, gender, email, mobile) values('{self.t1.get()}','{self.t2.get()}','{self.t3.get()}','{self.t4.get()}','{self.t5.get()}')")
        con.commit()
        if(i==1):
            msg.showinfo('Confiramtion','Recorded ') 
            self.t1.delete(0,'end')
            self.t2.delete(0,'end')
            self.t3.delete(0,'end')
            self.t4.delete(0,'end')
            self.t5.delete(0,'end')
            self.t1.focus()
            
            con.close()

    def Delete(self):
        con=connect(db='Your_data_base_name',user='root',password='Your_password',host='localhost')
        cur=con.cursor()
        Id=int(self.t6.get())
        j=cur.execute("delete from persons where id=%d"%(Id))
        con.commit()
        if(j==1):
            msg.showinfo('Confiramtion','Deleted!!! ') 
            self.t6.delete(0,'end')
            self.t6.focus()
            
            con.close()

root=Tk()
ob=myregistration(root)
root.geometry("700x300")
root.title("Person Registration Portal")
root.mainloop()
