from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")


        # =============================================Variables=====================================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address_var=StringVar()
        self.city_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar() 
        self.finallprice_var=StringVar()


        lbltitle=Label(self.root,text="LIBRARY MANAGEMNT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)

        # =============================================DataFrameLeft==================================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",bd=12,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        lblMember=Label(DataFrameLeft,font=("arial",12,"bold"),text="Member Type",padx=2,pady=6,bg="powder blue")
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,state="readonly",
                               font=("arial",12,"bold"),width=27)
        comMember['value']=("Admin Staff", "Lecturer", "Student")
        comMember.current(0)
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN No:",padx=2,bg="powder blue")
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry (DataFrameLeft,font=("arial",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry (DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="First Name:",padx=2,pady=4,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry (DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Last Name:",padx=2,pady=4,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry (DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)

        lblAddress=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address:",padx=2,pady=4,bg="powder blue")
        lblAddress.grid(row=5,column=0,sticky=W)
        txtAddress=Entry (DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address_var,width=29)
        txtAddress.grid(row=5,column=1)

        lblCity=Label(DataFrameLeft,font=("arial",12,"bold"),text="City:",padx=2,pady=4,bg="powder blue")
        lblCity.grid(row=6,column=0,sticky=W)
        txtCity=Entry (DataFrameLeft,font=("arial",13,"bold"),textvariable=self.city_var,width=29)
        txtCity.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Post Code:",padx=2,pady=4,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry (DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=4,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry (DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        txtMobile.grid(row=8,column=1)

        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",padx=2,pady=4,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry (DataFrameLeft,font=("arial",12,"bold"),textvariable=self.bookid_var,width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=4,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry (DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Author Name:",padx=2,pady=4,bg="powder blue")
        lblAuthor.grid(row=2,column=2,sticky=W)
        txtAuthor=Entry (DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=29)
        txtAuthor.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=4,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowqd=Entry (DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        txtDateBorrowqd.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=4,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry (DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Book:",padx=2,pady=4,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry (DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook_var,width=29)
        txtDaysOnBook.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=4,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry (DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lateratefine_var,width=29)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=4,bg="powder blue")
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry (DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue_var,width=29)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=4,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry (DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finallprice_var,width=29)
        txtActualPrice.grid(row=8,column=3)

        # =============================================DataFrameRight=================================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",
                                  bd=12,relief=RIDGE,font=("ariel",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=540,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16, padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1, sticky="ns")

        listBoooks=['Clean Code','The Pragmatic Programmer','Design Patterns: Elements of Reusable Object-Oriented Software','Introduction to Algorithms',
                    'Artificial Intelligence: A Modern Approach','Structure and Interpretation of Computer Programs','Code Complete',
                    'Refactoring: Improving the Design of Existing Code','The C Programming Language','Effective Java','Programming Pearls',
                    'Patterns of Enterprise Application Architecture','Operating System Concepts','The Mythical Man-Month','Domain-Driven Design',
                    'The Art of Computer Programming','Head First Design Patterns','Computer Networks','Practical Object-Oriented Design in Ruby','You Donâ€™t Know JS'
                                                                                    ]
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if x == "Clean Code":
                self.bookid_var.set("BKID8371")
                self.booktitle_var.set("Clean Code")
                self.author_var.set("Robert C. Martin")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.1800")

            elif x == "The Pragmatic Programmer":
                self.bookid_var.set("BKID4920")
                self.booktitle_var.set("The Pragmatic Programmer")
                self.author_var.set("Andrew Hunt & David Thomas")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2200")

            elif x == "Design Patterns: Elements of Reusable Object-Oriented Software":
                self.bookid_var.set("BKID1059")
                self.booktitle_var.set("Design Patterns: Elements of Reusable Object-Oriented Software")
                self.author_var.set("Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.3000")

            elif x == "Introduction to Algorithms":
                self.bookid_var.set("BKID7634")
                self.booktitle_var.set("Introduction to Algorithms")
                self.author_var.set("Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.3500")

            elif x == "Artificial Intelligence: A Modern Approach":
                self.bookid_var.set("BKID2187")
                self.booktitle_var.set("Artificial Intelligence: A Modern Approach")
                self.author_var.set("Stuart Russell & Peter Norvig")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.3200")

            elif x == "Structure and Interpretation of Computer Programs":
                self.bookid_var.set("BKID3492")
                self.booktitle_var.set("Structure and Interpretation of Computer Programs")
                self.author_var.set("Harold Abelson, Gerald Jay Sussman")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2800")

            elif x == "Code Complete":
                self.bookid_var.set("BKID6805")
                self.booktitle_var.set("Code Complete")
                self.author_var.set("Steve McConnell")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2000")

            elif x == "Refactoring: Improving the Design of Existing Code":
                self.bookid_var.set("BKID1543")
                self.booktitle_var.set("Refactoring: Improving the Design of Existing Code")
                self.author_var.set("Martin Fowler")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2500")

            elif x == "The C Programming Language":
                self.bookid_var.set("BKID9276")
                self.booktitle_var.set("The C Programming Language")
                self.author_var.set("Brian W. Kernighan & Dennis M. Ritchie")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.1800")

            elif x == "Effective Java":
                self.bookid_var.set("BKID4061")
                self.booktitle_var.set("Effective Java")
                self.author_var.set("Joshua Bloch")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2300")

            elif x == "Programming Pearls":
                self.bookid_var.set("BKID5839")
                self.booktitle_var.set("Programming Pearls")
                self.auther_var.set("Jon Bentley")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.1700")

            elif x == "Patterns of Enterprise Application Architecture":
                self.bookid_var.set("BKID2710")
                self.booktitle_var.set("Patterns of Enterprise Application Architecture")
                self.author_var.set("Martin Fowler")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2700")

            elif x == "Operating System Concepts":
                self.bookid_var.set("BKID7498")
                self.booktitle_var.set("Operating System Concepts")
                self.author_var.set("Abraham Silberschatz, Peter Baer Galvin, Greg Gagne")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2600")

            elif x == "The Mythical Man-Month":
                self.bookid_var.set("BKID6324")
                self.booktitle_var.set("The Mythical Man-Month")
                self.author_var.set("Frederick P. Brooks Jr.")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.1900")

            elif x == "Domain-Driven Design":
                self.bookid_var.set("BKID1987")
                self.booktitle_var.set("Domain-Driven Design")
                self.author_var.set("Eric Evans")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2400")

            elif x == "The Art of Computer Programming":
                self.bookid_var.set("BKID8540")
                self.booktitle_var.set("The Art of Computer Programming")
                self.author_var.set("Donald E. Knuth")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.4000")

            elif x == "Head First Design Patterns":
                self.bookid_var.set("BKID3106")
                self.booktitle_var.set("Head First Design Patterns")
                self.author_var.set("Eric Freeman, Elisabeth Robson, Bert Bates, Kathy Sierra")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2100")

            elif x == "Computer Networks":
                self.bookid_var.set("BKID4759")
                self.booktitle_var.set("Computer Networks")
                self.author_var.set("Andrew S. Tanenbaum")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.75")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2200")

            elif x == "Practical Object-Oriented Design in Ruby":
                self.bookid_var.set("BKID5203")
                self.booktitle_var.set("Practical Object-Oriented Design in Ruby")
                self.author_var.set("Sandi Metz")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.2000")

            elif x == "You Donâ€™t Know JS":
                self.bookid_var.set("BKID6872")
                self.booktitle_var.set("You Donâ€™t Know JS")
                self.author_var.set("Kyle Simpson")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.1600")



        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBoooks:
            listBox.insert(END,item)

        # =============================================Buttons Frame=================================================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data", font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)


        # =============================================Information Frame=================================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        Table_frame=Frame(FrameDetails,bd=12,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL) 
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table = ttk.Treeview(Table_frame, columns=("membertype", "prnno", "title", "firstname", "lastname", "address",
                                                      "city", "postid", "mobile", "bookid", "booktitle", "author", "dateborrowed",
                                                      "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"),xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)



        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address",text="Address1")
        self.library_table.heading("city",text="Address2") 
        self.library_table.heading("postid",text="Post Id")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title") 
        self.library_table.heading("author",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine") 
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address",width=100)
        self.library_table.column("city",width=100) 
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100) 
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100) 
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):

        conn=mysql.connector.connect(host="localhost", username="root", password="H@4anPORdan", database="hasandb")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address_var.get(),
                                                                                                                self.city_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finallprice_var.get()
                                                                                                                ))
        
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Member Has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="H@4anPORdan", database="hasandb")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address=%s,City=%s,PostId=%s,Mobile=%s,BookId=%s,BookTitle=%s,Author=%s,DateBorrowed=%s,DateDue=%s,Days=%s,LateReturnFine=%s,DateOverDue=%s,FinalPrice=%s where PRN_NO=%s",(
                                                                                                                self.member_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address_var.get(),
                                                                                                                self.city_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finallprice_var.get(),
                                                                                                                self.prn_var.get()
                                                                                                                ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Memeber has been Updated")

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="H@4anPORdan", database="hasandb")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from library")
        rows=my_cursor.fetchall()
        if len(rows) !=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in  rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self. lastname_var.set(row[4]),
        self.address_var.set(row[5]),
        self.city_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finallprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END, "Member Type:\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No:\t\t"+ self.id_var.get() + "\n")
        self.txtBox.insert(END, "FirstName:\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "LastName:\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1:\t\t"+ self.address_var.get() + "\n")
        self.txtBox.insert(END, "Address2:\t\t"+ self.city_var.get() + "\n")
        self.txtBox.insert(END, "Post Code:\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No:\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID: \t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Auther:\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END, "DateBorrowed:\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "DateDue:\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "DaysOnBook:\t\t" + self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END , "LateRateFine:\t\t"+ self.lateratefine_var.get() + "\n")
        self.txtBox.insert(END, "DateOverDue:\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END, "FinallPrice:\t\t"+ self.finallprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address_var.set(""),
        self.city_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.lateratefine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finallprice_var.set("")
        self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library managemnt System", "Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error", "First Selct the Member")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="H@4anPORdan", database="hasandb")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute (query, value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Memeber has been Deleted")

if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()