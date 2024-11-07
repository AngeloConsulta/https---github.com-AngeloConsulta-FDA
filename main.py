from tkinter import *
import sqlite3


# connectto the database

conn = sqlite3.connect('database.db')

#cursor to move around the database
c= conn.cursor()


# Tkinter Windows

class Application:
    def __init__(self, master):
        self.master = master

        # Creating frames  in the master
        self.left = Frame( master, width=800, height= 720, bg='lightgreen')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        #labels for the windows
        self.heading = Label(self.left, text="Food & Drug Administration", font=('arial 40 bold'), fg='black' , bg= 'lightgreen')
        self.heading.place(x=0, y=0)

        #patients name
        self.name = Label(self.left, text="Patient's Name", font=('arial 18 bold'), fg='black',  bg='lightgreen')
        self.name.place (x=0, y=100)

        #patients age
        self.age = Label(self.left, text="Age", font=('arial 18 bold'), fg='black',  bg='lightgreen')
        self.age.place (x=0, y=140)

        #Gender
        self.gender = Label(self.left, text="Gender", font=('arial 18 bold'), fg='black',  bg='lightgreen')
        self.gender.place (x=0, y=180)

        #Location
        self.location = Label(self.left, text="Location", font=('arial 18 bold'), fg='black',  bg='lightgreen')
        self.location.place (x=0, y=220)

        #appointment time
        self.time = Label(self.left, text="Time", font=('arial 18 bold'), fg='black',  bg='lightgreen')
        self.time.place (x=0, y=260)

         #Type of vaccine
        self.vaccine = Label(self.left, text="Type of Vaccine", font=('arial 18 bold'), fg='black',  bg='lightgreen')
        self.vaccine.place (x=0, y=300)

        #Entries for all labels
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=300, y=110)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=300, y=150)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=300, y=190)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=300, y=230)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=300, y=270)

        self.vaccine_ent = Entry(self.left, width=30)
        self.vaccine_ent.place(x=300, y=310)

        #Button to perforn a command
        self.submit = Button(self.left, text= "Submit",  font=('arial 12 bold'),width=20,  bg='steelblue', command=self.submit)
        self.submit.place(x=320, y=350)

        
    #Function to call when the submit button is clicked
    def submit(self):
        #getting the users input

        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.vaccine_ent.get()


#creating the object

root = Tk()
b = Application(root)

#resolution of the windows
root.geometry("1200x720+0+0")

# preventing the resize feature

root.resizable(False, False)

#end the loop
root.mainloop()



