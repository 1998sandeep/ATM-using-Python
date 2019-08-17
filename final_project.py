from tkinter import *
import os
from tkinter import messagebox
import sqlite3

#*******************************************************************************************************
class all_in_one:
#******************************************
    global card_get
    global pin_get
    def quit(self):
        win1.destroy()
        win1.quit()

    def common_disp(self):                                           #for first display
        global win1
        win1 = Tk()
        Me = Menu(win1)
        win1.config(menu=Me)
        submenu = Menu(Me)
        Me.add_cascade(label="Help", menu=submenu)
        submenu.add_command(label="Quit...", command=self.quit)

        win1.title("Home Page....")
        win1.configure(background="light green")
        win1.geometry("1200x720")
        win1.resizable(False,False)
        #image set
        photo = PhotoImage(file="img1.png")
        l1 = Label(win1, image=photo)
        l1.place(x=280, y=70)#450

        #left buttons
        Button(win1, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)#x=270
        Button(win1, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win1, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win1, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #right buttons
        Button(win1, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun1).place(x=980, y=100)#x=1150
        Button(win1, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun2).place(x=980, y=200)
        Button(win1, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win1, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=400)
        #key buttons
        status = Label(win1, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        #*****

        Button(win1, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10).place(x=320, y=600)#x=490
        Button(win1, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_info1).place(x=530, y=600)#x=710
        Button(win1, text="ABOUT", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about1).place(x=740, y=600)#x=900
        win1.mainloop()
    #************************
    def fun1(self):
        win1.destroy()
        self.customer_pin_card()
    def fun2(self):
        win1.destroy()
        self.employee_disp()
    def fun_info1(self):
        win1.destroy()
        self.fun_info()
    def fun_about1(self):
        win1.destroy()
        self.fun_about()
    #********************************************************************************************************
                                                    #for entring pin and card menu
    def customer_pin_card(self):
        global win_pin
        win_pin = Tk()
        win_pin.title("Information Collection...")
        win_pin.configure(background="light green")
        win_pin.geometry("1200x720")
        win_pin.resizable(False,False)

        #image set
        photo = PhotoImage(file="img4.png")
        l1 = Label(win_pin, image=photo)
        l1.place(x=280, y=70)
        #left buttons
        Button(win_pin, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win_pin, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win_pin, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win_pin, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #***
        l2 = Label(win_pin, text="Enter Your Card",bg="white", font="Times 20")
        l2.place(x=330, y=200)
        l3 = Label(win_pin, text="Eeter Your Pin",bg="white", font="Times 20")
        l3.place(x=330, y=300)
        #entry box for deposit
        e1 = Entry(win_pin)
        e1.place(x=580, y=200, height=40, width=150)
        e2 = Entry(win_pin)
        e2.place(x=580, y=300, height=40, width=150)
        #**********#
        def fun_get():
            self.card_get = e1.get()
            self.pin_get = e2.get()
            connection = sqlite3.connect("database_1.db")
            conn = connection.cursor()
            data = conn.execute("SELECT * FROM CUSTOMER")
            for i in data:
                if i[0] == self.card_get and i[1] == self.pin_get:
                    messagebox.showinfo("INFO", "Successfully loged in....")
                    win_pin.destroy()
                    self.customer_disp()
                #break
            connection.commit()
            connection.close()
        #right buttons
        Button(win_pin, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win_pin, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win_pin, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win_pin, text="Button", font="Times 20",fg="yellow",bg="dark green", command=fun_get).place(x=980, y=400)
        #key buttons
        status = Label(win_pin, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win_pin, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal1).place(x=320, y=600)
        Button(win_pin, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_info2).place(x=530, y=600)
        Button(win_pin, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about2).place(x=740, y=600)



        win_pin.mainloop()
    def fun_cal1(self):
        win_pin.destroy()
        self.common_disp()
    def fun_info2(self):
        win_pin.destroy()
        self.fun_info()
    def fun_about2(self):
        win_pin.destroy()
        self.fun_about()
#*******************************************************************************************************
    def customer_disp(self):                                                #for customer menu
        global win
        win = Tk()
        win.title("Customer Menu...")
        win.configure(background="light green")
        win.geometry("1200x720")
        win.resizable(False, False)
        #image set
        photo = PhotoImage(file="logo1 - Copy.png")
        l1 = Label(win, image=photo)
        l1.place(x=280, y=70)
        #left buttons
        Button(win, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun_b1).place(x=100, y=100)
        Button(win, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #right buttons
        Button(win, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun_b5).place(x=980, y=100)
        Button(win, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun_b6).place(x=980, y=200)
        Button(win, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun_b7).place(x=980, y=300)
        Button(win, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun_b8).place(x=980, y=400)
        #key buttons
        status = Label(win, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal2).place(x=320, y=600)
        Button(win, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_info3).place(x=530, y=600)
        Button(win, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_about3).place(x=740, y=600)
        win.mainloop()
    def fun_cal2(self):
        win.destroy()
        self.common_disp()
        #****************
    def fun_b1(self):
        win.destroy()
        self.customer_pin_change()
    def fun_b5(self):
        win.destroy()
        self.customer_disp_deposit()
    def fun_b6(self):
        win.destroy()
        self.customer_disp_widhrew()
    def fun_b7(self):
        win.destroy()
        self.customer_check_balance()
    def fun_b8(self):
        win.destroy()
        self.customer_transfer()
    def fun_info3(self):
        win.destroy()
        self.fun_info()
    def fun_about3(self):
        win.destroy()
        self.fun_about()

    #**********************************************************************************************************
    def customer_disp_deposit(self):                                             #for deposit window
        global win3
        win3 = Tk()
        win3.configure(background="light green")
        win3.geometry("1200x720")
        win3.resizable(False,False)
        #image set
        photo = PhotoImage(file="img4.png")
        l1 = Label(win3, image=photo)
        l1.place(x=280, y=70)
        #left buttons
        Button(win3, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win3, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win3, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win3, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #***
        l2 = Label(win3, text="Enter Your Amount",bg="white",font="Times 30")
        l2.place(x=430, y=100)
        #entry box for deposit
        e_dep = Entry(win3)
        e_dep.place(x=515, y=200, height=50, width=200)
        #**************
        def fun_get():
            amt_deposit = int(e_dep.get())
            #print(amt_deposit)

            connection = sqlite3.connect("database_1.db")
            conn = connection.cursor()
            data = conn.execute("SELECT * FROM CUSTOMER")

            for i in data:
                if i[0] == self.card_get and i[1] == self.pin_get and amt_deposit >=0:
                    initial_amt = int(i[2])
                    total = int(amt_deposit) + int(i[2])
                    command = "UPDATE CUSTOMER SET Amount_cust=" + str(total) + " WHERE Card='" + str(i[0]) + "'"
                    conn.execute(command)
                    messagebox.showinfo("INFO","SUCCESSFULLY DEPOSIT....")
                    break
            connection.commit()
            #connection.close()
            # for updation in employee table
            if initial_amt!=total:
                data1 = conn.execute("SELECT * FROM EMPLOYEE")
                for j in data1:
                    total_amt = int(amt_deposit)+int(j[2])
                    command1 = "UPDATE EMPLOYEE SET Amount_empl=" + str(total_amt) + " WHERE ID='" + "Sandeep" + "'"
                    conn.execute(command1)

                    break
                connection.commit()

                connection.close()

        #right buttons
        Button(win3, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win3, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win3, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win3, text="Button", font="Times 20",fg="yellow",bg="dark green",command=fun_get).place(x=980, y=400)
        #key buttons
        status = Label(win3, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win3, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,comman=self.fun_cal3).place(x=320, y=600)
        Button(win3, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_info4).place(x=530, y=600)
        Button(win3, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about4).place(x=740, y=600)
        win3.mainloop()
    def fun_cal3(self):
        win3.destroy()
        self.common_disp()
    def fun_info4(self):
        win3.destroy()
        self.fun_info()
    def fun_about4(self):
        win3.destroy()
        self.fun_about()
    #********************************************************************************************************************
    #for widhrew
    def customer_disp_widhrew(self):                                        #for widtrew window
        global win4
        win4 = Tk()
        win4.configure(background="light green")
        win4.geometry("1200x720")
        win4.resizable(False, False)
        #image set
        photo = PhotoImage(file="img4.png")
        l1 = Label(win4, image=photo)
        l1.place(x=280, y=70)
        #left buttons
        Button(win4, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win4, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win4, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win4, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #***
        l2 = Label(win4, text="Enter Your Amount",bg="white", font="Times 30")
        l2.place(x=430, y=100)
        #entry box for deposit
        e1 = Entry(win4)
        e1.place(x=515, y=200, height=50, width=150)
        #******
        def fun_get():
            amt = e1.get()
            connection = sqlite3.connect("database_1.db")
            conn = connection.cursor()
            data = conn.execute("SELECT * FROM CUSTOMER")
            for i in data:
                if i[0] == self.card_get and i[1] == self.pin_get:
                    initial_amt = i[2]
                    total = int(i[2])-int(amt)
                    command = "UPDATE CUSTOMER SET Amount_cust=" + str(total) + " WHERE Card='" + str(i[0]) + "'"
                    # constrain for limit
                    if total >= 0:
                        conn.execute(command)
                        messagebox.showinfo("INFO", "SUCCESSFULLY Widhrewed...")
                    else:
                        messagebox.showinfo("INFO", "Limit exiting")
                    break
            connection.commit()
            #connection.close()
            # for updation in employee table
            if initial_amt!=total:
                data1 = conn.execute("SELECT * FROM EMPLOYEE")
                for j in data1:
                    total_amt = int(j[2])-int(amt)
                    command1 = "UPDATE EMPLOYEE SET Amount_empl=" + str(total_amt) + " WHERE ID='" + "Sandeep" + "'"
                    conn.execute(command1)

                    break
            connection.commit()
            connection.close()

        #right buttons
        Button(win4, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win4, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win4, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win4, text="Button", font="Times 20",fg="yellow",bg="dark green", command=fun_get).place(x=980, y=400)
        #key buttons
        status = Label(win4, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win4, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal4).place(x=320, y=600)
        Button(win4, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_info5).place(x=530, y=600)
        Button(win4, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about5).place(x=740, y=600)
        win4.mainloop()
    def fun_cal4(self):
        win4.destroy()
        self.common_disp()
    def fun_info5(self):
        win4.destroy()
        self.fun_info()
    def fun_about5(self):
        win4.destroy()
        self.fun_about()
    #*****************************************************************************************************
                                                                                #for check balance
    def customer_check_balance(self):
        global win_check
        win_check = Tk()
        win_check.configure(background="light green")
        win_check.geometry("1200x720")
        win_check.resizable(False, False)
        #image set
        photo = PhotoImage(file="img4.png")
        l1 = Label(win_check, image=photo)
        l1.place(x=280, y=70)
        #text
        l2 = Label(win_check, text="Balance",bg="white", font="Times 30")
        l2.place(x=530, y=100)
        #**
        def fun_get():
            #card_get = e1.get()
            #pin_get = e2.get()
            connection = sqlite3.connect("database_1.db")
            conn = connection.cursor()
            data = conn.execute("SELECT * FROM CUSTOMER")
            for i in data:
                if i[0] == self.card_get and i[1] == self.pin_get:
                    l3 = Label(win_check, text=i[2],bg="white", font="Times 30")
                    l3.place(x=580, y=200)
                    #win_pin.destroy()
            connection.commit()
            connection.close()

        #***
        #l3 = Label(win_check, text = bal, font="Times 30")
        #l3.place(x=700,y=150)
        #left buttons
        Button(win_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #right buttons
        Button(win_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win_check, text="Button", font="Times 20",fg="yellow",bg="dark green",command=fun_get).place(x=980, y=400)
        #key buttons
        status = Label(win_check, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win_check, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal5).place(x=320, y=600)
        Button(win_check, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_info6).place(x=530, y=600)
        Button(win_check, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about6).place(x=740, y=600)
        win_check.mainloop()
    def fun_cal5(self):
        win_check.destroy()
        self.common_disp()
    def fun_info6(self):
        win_check.destroy()
        self.fun_info()
    def fun_about6(self):
        win_check.destroy()
        self.fun_about()
    #****************************************************************************************************
                                                            #for transfer
    def customer_transfer(self):
        global win_trans
        win_trans = Tk()
        win_trans.configure(background="light green")
        win_trans.geometry("1200x720")
        win_trans.resizable(False,False)
        #image set
        photo = PhotoImage(file="img4.png")
        l1 = Label(win_trans, image=photo)
        l1.place(x=280, y=70)
        #left buttons
        Button(win_trans, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win_trans, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win_trans, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win_trans, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #***
        l2 = Label(win_trans, text="Enter Amount",bg="white", font="Times 20")
        l2.place(x=330, y=200)
        l3 = Label(win_trans, text="Enter Account No.",bg="white", font="Times 20")
        l3.place(x=330, y=300)
        #entry box for deposit
        e1 = Entry(win_trans)
        e1.place(x=580, y=200, height=40, width=150)
        e2 = Entry(win_trans)
        e2.place(x=580, y=300, height=40, width=150)
        #*************
        def fun_trans():
            amt = e1.get()
            connection = sqlite3.connect("database_1.db")
            conn = connection.cursor()
            data = conn.execute("SELECT * FROM CUSTOMER")
            for i in data:
                if i[0] == self.card_get and i[1] == self.pin_get:
                    initial_amt = i[2]
                    total = int(i[2])-int(amt)
                    command = "UPDATE CUSTOMER SET Amount_cust=" + str(total) + " WHERE Card='" + str(i[0]) + "'"
                    # constrain for limit
                    if total >= 0:
                        conn.execute(command)
                        messagebox.showinfo("INFO", "SUCCESSFULLY TRANSFERED....")
                    else:
                        messagebox.showinfo("INFO", "Limit exiting.....")
                    break
            connection.commit()
            #connection.close()
            # for updation in employee table
            if initial_amt!=total:
                data1 = conn.execute("SELECT * FROM EMPLOYEE")
                for j in data1:
                    total_amt = int(j[2])-int(amt)
                    command1 = "UPDATE EMPLOYEE SET Amount_empl=" + str(total_amt) + " WHERE ID='" + "Sandeep" + "'"
                    conn.execute(command1)
                    break
            connection.commit()
            connection.close()

        #right buttons
        Button(win_trans, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win_trans, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win_trans, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win_trans, text="Button", font="Times 20",fg="yellow",bg="dark green", command=fun_trans).place(x=980, y=400)
        #key buttons
        status = Label(win_trans, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win_trans, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal6).place(x=320, y=600)
        Button(win_trans, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_info7).place(x=530, y=600)
        Button(win_trans, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about7).place(x=740, y=600)
        win_trans.mainloop()
    def fun_cal6(self):
        win_trans.destroy()
        self.common_disp()
    def fun_info7(self):
        win_trans.destroy()
        self.fun_info()
    def fun_about7(self):
        win_trans.destroy()
        self.fun_about()
    #***********************************************************************************************************
                                                                                                #for chanage pin for customer
    def customer_pin_change(self):
        global win_change
        win_change = Tk()
        win_change.configure(background="light green")
        win_change.geometry("1200x720")
        win_change.resizable(False, False)
        #image set
        photo = PhotoImage(file="img4.png")
        l1 = Label(win_change, image=photo)
        l1.place(x=280, y=70)
        #***
        l2 = Label(win_change, text="Enter Previous Pin",bg="white", font="Times 20")
        l2.place(x=330, y=200)
        l3 = Label(win_change, text="Enter New Pin",bg="white", font="Times 20")
        l3.place(x=330, y=300)
        #entry box for deposit
        e1 = Entry(win_change)
        e1.place(x=580, y=200, height=40, width=150)
        e2 = Entry(win_change)
        e2.place(x=580, y=300, height=40, width=150)
        #****
        def fun_change():
            pre_pin = e1.get()
            new_pin = e2.get()
            connection = sqlite3.connect("database_1.db")
            conn = connection.cursor()
            data = conn.execute("SELECT * FROM CUSTOMER")
            for i in data:
                if i[0] == self.card_get and i[1] == self.pin_get and pre_pin != new_pin:
                    if pre_pin == self.pin_get:
                        command = "UPDATE CUSTOMER SET Pin=" + str(new_pin) + " WHERE Card='" + str(i[0]) + "'"
                        conn.execute(command)
                        messagebox.showinfo("INFO", "PIN SUCCESSFULLY CHANGED.......")
                    break
                #else:
                    #messagebox.showinfo("INFO","Wrong Credential......")
            connection.commit()
            connection.close()
        #left buttons
        Button(win_change, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win_change, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win_change, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win_change, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #right buttons
        Button(win_change, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win_change, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win_change, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win_change, text="Button", font="Times 20",fg="yellow",bg="dark green",command=fun_change).place(x=980, y=400)
        #key buttons
        status = Label(win_change, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win_change, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal7).place(x=320, y=600)
        Button(win_change, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_info8).place(x=530, y=600)
        Button(win_change, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about8).place(x=740, y=600)
        win_change.mainloop()
    def fun_cal7(self):
        win_change.destroy()
        self.common_disp()
    def fun_info8(self):
        win_change.destroy()
        self.fun_info()
    def fun_about8(self):
        win_change.destroy()
        self.fun_about()
    #********************************************************************************************************************************************************************************
    #********************************************************************************************************************************************************************************

                                                                        #for Employee
                                                                        #for first display window
    def employee_disp(self):
        global win_em_disp
        win_em_disp = Tk()
        win_em_disp.configure(background="light green")
        win_em_disp.geometry("1200x720")
        win_em_disp.resizable(False, False)
        #image set
        photo = PhotoImage(file="img4.png")
        l1 = Label(win_em_disp, image=photo)
        l1.place(x=280, y=70)
        #**************
        l2 = Label(win_em_disp, text="Enter Your Id",bg="white", font="Times 20")
        l2.place(x=330, y=200)
        l3 = Label(win_em_disp, text="Eeter Your pin",bg="white", font="Times 20")
        l3.place(x=330, y=300)
        #entry box for deposit
        global e1, e2
        e1 = Entry(win_em_disp)
        e1.place(x=580, y=200, height=40, width=150)
        e2 = Entry(win_em_disp)
        e2.place(x=580, y=300, height=40, width=150)
                #****

        #for id from database

        def get():          #for gating id and pin
            connection = sqlite3.connect("database_1.db")
            conn = connection.cursor()
            conn.execute('SELECT ID FROM EMPLOYEE')
            for i in conn.fetchall():
                id_data = i[0]
            #for pin from database
            conn.execute('SELECT Pin FROM EMPLOYEE')
            for j in conn.fetchall():
                pin_data = j[0]
            connection.commit()
            connection.close()
            #print("id = ",id_data)
            #print("pin = ",pin_data)
            id = e1.get()
            pin = e2.get()
            #win_em_disp.destroy()
            if id_data == id and pin_data == pin:
                messagebox.showinfo("INFO", "Welcome Mr. Admin")
                win_em_disp.destroy()
                self.employee_main_menu()
            else:
                messagebox.showinfo("INFO", "Wrong Credential")

        #left buttons

        Button(win_em_disp, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win_em_disp, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win_em_disp, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win_em_disp, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #right buttons
        Button(win_em_disp, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win_em_disp, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win_em_disp, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win_em_disp, text="Button", font="Times 20",fg="yellow",bg="dark green",command=get).place(x=980, y=400)
        #key buttons
        status = Label(win_em_disp, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        Button(win_em_disp, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal8).place(x=320, y=600)
        Button(win_em_disp, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_info9).place(x=530, y=600)
        Button(win_em_disp, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about9).place(x=740, y=600)
        #*******
        #*******
        win_em_disp.mainloop()
    def fun_cal8(self):
        win_em_disp.destroy()
        self.common_disp()
    def fun_info9(self):
        win_em_disp.destroy()
        self.fun_info()
    def fun_about9(self):
        win_em_disp.destroy()
        self.fun_about()
    #*********************************************************************************************
                                                            #for employee menu
    def employee_main_menu(self):
        global win_em_main
        win_em_main = Tk()
        win_em_main.configure(background="light green")
        win_em_main.geometry("1200x720")
        win_em_main.resizable(False,False)
        #image set
        photo = PhotoImage(file="em_main.png")
        l1 = Label(win_em_main, image=photo)
        l1.place(x=280, y=70)
        #left buttons
        Button(win_em_main, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win_em_main, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win_em_main, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win_em_main, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #right buttons
        Button(win_em_main, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun_em_addmoney).place(x=980, y=100)
        Button(win_em_main, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun_em_balance).place(x=980, y=200)
        Button(win_em_main, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun_em_addcust).place(x=980, y=300)
        Button(win_em_main, text="Button", font="Times 20",fg="yellow",bg="dark green", command=self.fun_em_delcust).place(x=980, y=400)
        #key buttons
        status = Label(win_em_main, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win_em_main, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal9).place(x=320, y=600)
        Button(win_em_main, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_info_10).place(x=530, y=600)
        Button(win_em_main, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about10).place(x=740, y=600)
        win_em_main.mainloop()
        #**************
    def fun_em_balance(self):
        win_em_main.destroy()
        self.employee_check()
    def fun_em_addmoney(self):
        win_em_main.destroy()
        self.employee_add_money()
    def fun_em_addcust(self):
        win_em_main.destroy()
        self.employee_add_cust()
    def fun_em_delcust(self):
        win_em_main.destroy()
        self.employee_delete_cust()
    def fun_cal9(self):
        win_em_main.destroy()
        self.common_disp()
    def fun_info_10(self):
        win_em_main.destroy()
        self.fun_info()
    def fun_about10(self):
        win_em_main.destroy()
        self.fun_about()
    #********************************************************************************************
                                                                        #employeee adding money
    def employee_add_money(self):
        global win_em_add_money
        win_em_add_money = Tk()
        win_em_add_money.configure(background="light green")
        win_em_add_money.geometry("1200x720")
        win_em_add_money.resizable(False, False)
        #image set
        photo = PhotoImage(file="img4.png")
        l1 = Label(win_em_add_money, image=photo)
        l1.place(x=280, y=70)
        #****
        l2 = Label(win_em_add_money, text="Enter Amount",bg="white", font="Times 30")
        l2.place(x=510, y=100)
        #entry box for deposit
        e1 = Entry(win_em_add_money)
        e1.place(x=515, y=200, height=50, width=150)
        #**********
        def fun_add():
            new = int(e1.get())
            connection = sqlite3.connect("database_1.db")
            conn=connection.cursor()
            conn.execute('SELECT Amount_empl FROM EMPLOYEE')
            for m in conn.fetchall():
                final_amt = new+m[0]
            command = "UPDATE EMPLOYEE SET Amount_empl=" + str(final_amt) + " WHERE ID='" + "Sandeep" + "'"
            conn.execute(command)
            messagebox.showinfo("INFO","Money Added Successfully....")
            connection.commit()
            connection.close()
        #left buttons
        Button(win_em_add_money, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win_em_add_money, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win_em_add_money, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win_em_add_money, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #right buttons
        Button(win_em_add_money, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win_em_add_money, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win_em_add_money, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win_em_add_money, text="Button", font="Times 20",fg="yellow",bg="dark green", command=fun_add).place(x=980, y=400)
        #key buttons
        status = Label(win_em_add_money, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win_em_add_money, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal10).place(x=320, y=600)
        Button(win_em_add_money, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_info11).place(x=530, y=600)
        Button(win_em_add_money, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about11).place(x=740, y=600)
        win_em_add_money.mainloop()
    def fun_cal10(self):
        win_em_add_money.destroy()
        self.common_disp()
    def fun_info11(self):
        win_em_add_money.destroy()
        self.fun_info()
    def fun_about11(self):
        win_em_add_money.destroy()
        self.fun_about()
    #******************************************************************************************************
                                                                    #for check balance
    def employee_check(self):
        global win_em_check
        win_em_check = Tk()
        win_em_check.configure(background="light green")
        win_em_check.geometry("1200x720")
        win_em_check.resizable(False,False)
        #image set
        photo = PhotoImage(file="img2.png")
        l1 = Label(win_em_check, image=photo)
        l1.place(x=280, y=70)
        #text
        l2 = Label(win_em_check, text="Balance",bg="white", font="Times 30")
        l2.place(x=530, y=100)
        #**
        #left buttons
        Button(win_em_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win_em_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win_em_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win_em_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #right buttons
        Button(win_em_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win_em_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win_em_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win_em_check, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=400)
        #key buttons
        status = Label(win_em_check, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win_em_check, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal11).place(x=320, y=600)
        Button(win_em_check, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_info12).place(x=530, y=600)
        Button(win_em_check, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about12).place(x=740, y=600)

        #********
        #for read of total amount
        global conn
        global connection
        connection = sqlite3.connect("database_1.db")
        conn = connection.cursor()
        conn.execute('SELECT Amount_empl from EMPLOYEE')
        for i in conn.fetchall():
            c = i[0]
        connection.commit()
        connection.close()
        l3 = Label(win_em_check, text=c,bg="white", font="Times 30")
        l3.place(x=545, y=200)
        win_em_check.mainloop()
    def fun_cal11(self):
        win_em_check.destroy()
        self.common_disp()
    def fun_info12(self):
        win_em_check.destroy()
        self.fun_info()
    def fun_about12(self):
        win_em_check.destroy()
        self.fun_about()
    #****************************************************************************************************
                                                            #for adding customer
    def employee_add_cust(self):
        global win_em_addcustomer
        win_em_addcustomer = Tk()
        win_em_addcustomer.configure(background="light green")
        win_em_addcustomer.geometry("1200x720")
        win_em_addcustomer.resizable(False, False)
        #image set
        photo = PhotoImage(file="img4.png")
        l1 = Label(win_em_addcustomer, image=photo)
        l1.place(x=280, y=70)
        #left buttons
        Button(win_em_addcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win_em_addcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win_em_addcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win_em_addcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #***
        l2 = Label(win_em_addcustomer, text="Enter Card No.",bg="white", font="Times 20")
        l2.place(x=330, y=200)
        l3 = Label(win_em_addcustomer, text="Enter Pin",bg="white", font="Times 20")
        l3.place(x=330, y=300)
        #entry box for deposit
        e1 = Entry(win_em_addcustomer)
        e1.place(x=580, y=200, height=40, width=150)
        e2 = Entry(win_em_addcustomer)
        e2.place(x=580, y=300, height=40, width=150)
        #****************#
        def fun_get():
            card = e1.get()
            pin = e2.get()
            initial_amt = 0
            connection = sqlite3.connect("database_1.db")
            conn = connection.cursor()
            a = "INSERT INTO CUSTOMER(Card, Pin, Amount_cust) VALUES(" + str(card) + ", " + str(pin) + ", " + str(initial_amt) + ")"
            conn.execute(a)
            messagebox.showinfo("INFO","CUSTOMER SUCCESSFULLY ADDED.............")
            connection.commit()
            connection.close()

        #right buttons
        Button(win_em_addcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win_em_addcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win_em_addcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win_em_addcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green", command=fun_get).place(x=980, y=400)
        #key buttons
        status = Label(win_em_addcustomer, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        Button(win_em_addcustomer, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal12).place(x=320, y=600)
        Button(win_em_addcustomer, text=" INFO  ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_info13).place(x=530, y=600)
        Button(win_em_addcustomer, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_about13).place(x=740, y=600)
        win_em_addcustomer.mainloop()
    def fun_cal12(self):
        win_em_addcustomer.destroy()
        self.common_disp()
    def fun_info13(self):
        win_em_addcustomer.destroy()
        self.fun_info()
    def fun_about13(self):
        win_em_addcustomer.destroy()
        self.fun_about()
    #****************************************************************************************************
                                                                #for delete customer
    def employee_delete_cust(self):
        global win_em_delcustomer
        win_em_delcustomer = Tk()
        win_em_delcustomer.configure(background="light green")
        win_em_delcustomer.geometry("1200x720")
        win_em_delcustomer.resizable(False, False)
        #image set
        photo = PhotoImage(file="img4.png")
        l1 = Label(win_em_delcustomer,image=photo)
        l1.place(x=280, y=70)
        #left buttons
        Button(win_em_delcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=100)
        Button(win_em_delcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=200)
        Button(win_em_delcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=300)
        Button(win_em_delcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=100, y=400)
        #***
        status = Label(win_em_delcustomer, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        l2 = Label(win_em_delcustomer, text="Enter Card No.", bg="white", font="Times 20")
        l2.place(x=330, y=250)
        #entry box for deposit
        e1 = Entry(win_em_delcustomer)
        e1.place(x=580, y=240, height=40, width=150)
        def fun_del():
            card = e1.get()
            connection = sqlite3.connect("database_1.db")
            conn=connection.cursor()
            command = "DELETE FROM CUSTOMER WHERE Card=" + str(card)
            conn.execute(command)
            messagebox.showinfo("INFO","CUSTOMER SUCCESSFULLY DELETED.....")
            connection.commit()
            connection.close()
        #right buttons
        Button(win_em_delcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=100)
        Button(win_em_delcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=200)
        Button(win_em_delcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green").place(x=980, y=300)
        Button(win_em_delcustomer, text="Button", font="Times 20",fg="yellow",bg="dark green", command=fun_del).place(x=980, y=400)
        Button(win_em_delcustomer, text="CANCEL", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_cal13).place(x=320, y=600)
        Button(win_em_delcustomer, text=". INFO   .", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10,command=self.fun_info14).place(x=530, y=600)
        Button(win_em_delcustomer, text=" ABOUT ", font="Times 20",fg="yellow",bg="dark green", padx=15, pady=10, command=self.fun_about14).place(x=740, y=600)
        win_em_delcustomer.mainloop()
    def fun_info14(self):
        win_em_delcustomer.destroy()
        self.fun_info()
    def fun_about14(self):
        win_em_delcustomer.destroy()
        self.fun_about()
    #for information about bank and atm
    def fun_info(self):
        global win_info
        win_info = Tk()
        win_info.title("Information....")
        win_info.configure(background='light green')
        win_info.geometry("1200x720")
        win_info.resizable(False, False)
        P1 = 'ATM BANK NAME :: PYBANK Pvt Ltd..'
        P2 = 'VERSION       :: 1.0'
        P3 = 'TECHNOLOGY    :: Python 3.6.2'
        def fun_home():
            win_info.destroy()
            self.common_disp()
        status = Label(win_info, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        Label(win_info, text=P1, fg='dark green',bg="light green", font="Times 40").place(x=100, y=100)
        Label(win_info, text=P2, fg='dark green',bg="light green", font="Times 40").place(x=100, y=250)
        Label(win_info, text=P3, fg='dark green',bg="light green", font="Times 40").place(x=100, y=400)
        Button(win_info,text="HOME", fg="dark green", bg="light green", font="Times 20", command=fun_home).place(x=1090, y=640)
        win_info.mainloop()
    #***********
    def fun_cal13(self):
        win_em_delcustomer.destroy()
        self.common_disp()
        #************************************
    def fun_about(self):
        global win_about
        win_about = Tk()
        win_about.title("About....")
        win_about.configure(background="light green")
        win_about.geometry("1200x720")
        win_about.resizable(FALSE,FALSE)
        p1 = "It is a python based ATM Management System Project which includes Tkinter, Sqlite3, Images, Lables, Buttons and so on....."
        p2 = "There is a three member team who created this ATM Management System . Description of Members is following given..........."
        p3 = "1. Sandeep kannaujiya"
        p4 = "Reg. No. :: 11712528"
        p5 = "2. Aman saxena"
        p6 = "Reg. No. :: 11712586"
        p7 = "3. Vishal singh"
        p8 = "Reg. No. :: 11706638"
        p_line="-------------------------------------------------------------------------------------------------------------------------"
        def fun_home():
            win_about.destroy()
            self.common_disp()
        status = Label(win_about, text="ATM Running........", bd=1,bg="dark green",fg="white", relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        Label(win_about, text=p1,bg="light green", fg='dark green', font="Times 16").place(x=100, y=100)
        Label(win_about, text=p2,bg="light green", fg='dark green', font="Times 16").place(x=100, y=150)
        Label(win_about, text=p_line,bg="light green", fg='dark green', font="Times 16").place(x=100, y=200)
        Label(win_about, text=p3,bg="light green", fg='dark green', font="Times 16").place(x=100, y=300)
        Label(win_about, text=p4,bg="light green", fg='dark green', font="Times 16").place(x=100, y=350)
        Label(win_about, text=p5,bg="light green", fg='dark green', font="Times 16").place(x=100, y=450)
        Label(win_about, text=p6,bg="light green", fg='dark green', font="Times 16").place(x=100, y=500)
        Label(win_about, text=p7,bg="light green", fg='dark green', font="Times 16").place(x=100, y=600)
        Label(win_about, text=p8,bg="light green", fg='dark green', font="Times 16").place(x=100, y=650)
        Button(win_about, text="HOME",bg="light green", fg='dark green', font="Times 16",command=fun_home).place(x=1110, y=640)
        win_about.mainloop()
    #***************************************************************************************************************
                                                        #for lamdba
    def __init__(self):
        os.system('espeak "{}"'.format('Welcome  To  pybank private lemited'))
        os.system('espeak "{}"'.format('version 2 . o'))
        os.system('espeak "{}"'.format("Created by Sandeep kannaujiya"))
        os.system('espeak "{}"'.format('Registration number 1 1 7 1 2 5 2 8 '))
 #****************************************************************************************************************
                                                # for database
        #global conn
        #global connection
        #connection = sqlite3.connect("database_1.db")
        #conn = connection.cursor()
                                                    #for customer
        #conn.execute("""CREATE TABLE CUSTOMER(Card varchar(40) PRIMARY KEY,Pin varchar(40),Amount_cust int)""")
                                                    #for employee
        #conn.execute("""CREATE TABLE EMPLOYEE(ID varchar(40),Pin varchar(40),Amount_empl int)""")
                                                    #for employee addintion
        #conn.execute('INSERT INTO EMPLOYEE VALUES("Sandeep", "123", 50000)')
        #connection.commit()
        #connection.close()
    def __del__(self):
        os.system('espeak "{}"'.format('Thank  You  for  using  Pybank'))
obj = all_in_one()              #object creating
#obj.customer_disp_widhrew()
#obj.employee_add_cust()
#obj.employee_delete_cust()
#obj.employee_check()
obj.common_disp()
#obj.fun_info()
#obj.fun_about()


