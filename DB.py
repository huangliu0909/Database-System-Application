from tkinter import *
from tkinter import ttk
import pymysql
import tkinter as tk

# 连接database
conn = pymysql.connect(host="127.0.0.1", user="root",password="332099",database="project-1",charset="utf8")
cursor = conn.cursor()


def inputNullError():
    rootError = Tk()
    theLabel = tk.Label(rootError, text="you have not input !", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    rootError.mainloop()


def inputWrong():
    rootInputWrong = Tk()
    theLabel = tk.Label(rootInputWrong, text="you have input sth wrong !", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    rootInputWrong.mainloop()

def showNum(num):
    rootNum = Tk()
    #  t = "the book(s) you need: "
    if len(num) == 0:
        theLabel = tk.Label(rootNum, text="Not Found", justify=LEFT, padx=10)
        theLabel.pack(side=TOP)
    else:
        theLabel = tk.Label(rootNum, text="the book(s) you need: ", justify=LEFT, padx=10)
        theLabel.pack(side=TOP)

        columns = ("BookID", "BookName", "BookPrice", "Author", "BookStyle", "Publisher");
        treeview = ttk.Treeview(rootNum, height=18, show="headings", columns=columns)  # 表格
        treeview.column("BookID", width=200, anchor='center')
        treeview.column("BookName", width=200, anchor='center')
        treeview.column("BookPrice", width=200, anchor='center')
        treeview.column("Author", width=200, anchor='center')
        treeview.column("BookStyle", width=200, anchor='center')
        treeview.column("Publisher", width=200, anchor='center')
        treeview.heading("BookID", text="BookID")
        treeview.heading("BookName", text="BookName")
        treeview.heading("BookPrice", text="BookPrice")
        treeview.heading("Author", text="Author")
        treeview.heading("BookStyle", text="BookStyle")
        treeview.heading("Publisher", text="Publisher")
        treeview.pack(side=LEFT, fill=BOTH)
        for i in range(len(num)):  # 写入数据
            treeview.insert('', i, values=list(num[i]))
    rootNum.mainloop()


def user():
    def show():
        s = []
        if e1.get() is not "":
            s1 = e1.get()
            print("书名:<< % s>>" % e1.get())
            s.append("BookName = \"% s\"" % s1)
        if e2.get() is not "":
            s2 = e2.get()
            print("出版社:<< % s>>" % e2.get())
            s.append("Publisher = \"% s\"" % s2)
        if e3.get() is not "":
            s3 = e3.get()
            print("作者:<< % s>>" % e3.get())
            s.append("Author = \"% s\"" % s3)
        if e4.get() is not "":
            s4 = e4.get()
            print("风格:<< % s>>" % e4.get())
            s.append("BookStyle = \"% s\"" % s4)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        sql = "select BookID, BookName, BookPrice, Author, BookStyle,Publisher from book where "
        for i in range(len(s)):
            if i == 0:
                sql += s[0]
            else:
                sql += " and "
                sql += s[i]
        # 执行SQL语句
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(list(results))
        showNum(list(results))

    root = Tk()
    Label(root, text="书名:").grid(row=0)
    Label(root, text="出版社:").grid(row=1)
    Label(root, text="作者:").grid(row=2)
    Label(root, text="风格:").grid(row=3)
    e1 = Entry(root)
    e2 = Entry(root)
    e3 = Entry(root)
    e4 = Entry(root)
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)
    e3.grid(row=2, column=1, padx=10, pady=5)
    e4.grid(row=3, column=1, padx=10, pady=5)
    Button(root, text="完成", width=10, command=show).grid(row=4, column=0, sticky=W, padx=10, pady=5)
    Button(root, text="退出", width=10, command=root.quit()).grid(row=4, column=1, sticky=E, padx=10, pady=5)
    mainloop()


def updateSuccess():
    rootUpdateSuccess = Tk()
    theLabel = tk.Label(rootUpdateSuccess, text="change successfully~", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    rootUpdateSuccess.mainloop()

def manager(name, flag, id, code):
    def personal():

        def personalCode():
            def show():
                ee = e.get()
                sql = " update manager set CODE= \"%s\"  where ManagerId = %s" % (ee,id)
                cursor.execute(sql)
                cursor.fetchall()
                updateSuccess()

            rootPersonalCode = Tk()
            theLabel = tk.Label(rootPersonalCode, text="CODE", justify=LEFT, padx=10)
            theLabel.pack(side=TOP)
            Label(rootPersonalCode, text="change to:").pack()
            e = Entry(rootPersonalCode)
            e.pack()
            Button(rootPersonalCode, text="完成", width=10, command=show).pack()
            rootPersonalCode.mainloop()

        def personalTele():
            def show():
                ee = e.get()
                sql = " update manager set ManagerTele=%s where ManagerId = %s" % (ee, id)
                cursor.execute(sql)
                cursor.fetchall()
                showManager()
                updateSuccess()

            rootPersonalTele = Tk()
            theLabel = tk.Label(rootPersonalTele, text="TELEPHONE", justify=LEFT, padx=10)
            theLabel.pack(side=TOP)
            Label(rootPersonalTele, text="change to:").pack()
            e = Entry(rootPersonalTele)
            e.pack()
            Button(rootPersonalTele, text="完成", width=10, command=show).pack()
            rootPersonalTele.mainloop()

        def personalStorageId():
            def show():
                ee = e.get()
                sql = " update manager set StorageId=%s where ManagerId = %s" % (ee, id)
                cursor.execute(sql)
                cursor.fetchall()
                showManager()
                updateSuccess()

            rootPersonalStorageId = Tk()
            theLabel = tk.Label(rootPersonalStorageId, text="StorageId", justify=LEFT, padx=10)
            theLabel.pack(side=TOP)
            Label(rootPersonalStorageId, text="change to:").pack()
            e = Entry(rootPersonalStorageId)
            e.pack()
            Button(rootPersonalStorageId, text="完成", width=10, command=show).pack()
            rootPersonalStorageId.mainloop()

        rootPersonal = Tk()
        theLabel = tk.Label(rootPersonal, text="PERSONAL STAFF", justify=LEFT, padx=10)
        theLabel.pack(side=TOP)
        Button(rootPersonal, text="update code", width=30, command=personalCode).pack()
        Button(rootPersonal, text="update telephone number ", width=30, command=personalTele).pack()
        Button(rootPersonal, text="update storageId ", width=30, command=personalStorageId).pack()

        rootPersonal.mainloop()

    def searchBook():
        def show():
            q = entry1.get().split(" ")
            r = []
            for i in range(len(q)):
                sql = "select * from book natural join storage where storage.StorageId = book.StorageId and BookId = \"% s\"" % q[i]
                cursor.execute(sql)
                r.append(list(cursor.fetchall())[0])
            rootShowSearch = Tk()
            theLabel = tk.Label(rootShowSearch, text="the book(s) you need: ", justify=LEFT, padx=10)
            theLabel.pack(side=TOP)
            columns = ("BookID",  "Publisher",  "BookName", "BookNum", "BookPrice", "Author", "BookStyle",  "StorageName")
            treeview = ttk.Treeview(rootShowSearch, height=18, show="headings", columns=columns)  # 表格
            for i in range(len(columns)):
                treeview.column(columns[i], width=100, anchor='center')
            for i in range(len(columns)):
                treeview.heading(columns[i], text=columns[i])
            treeview.pack(side=LEFT, fill=BOTH)
            for i in range(len(r)):  # 写入数据
                x = list(r[i])
                y = []
                for j in range(len(x)):
                    if j > 0:
                        y.append(x[j])
                treeview.insert('', i, values=y)
            rootShowSearch.mainloop()

        rootsearch = Tk()
        label0 = tk.Label(rootsearch, text="SEARCH FOR BOOK")
        label0.grid(row=0, column=0)
        label1 = tk.Label(rootsearch, text="please input BookId(s):")
        label1.grid(row=1, column=0)
        entry1 = tk.Entry(rootsearch)
        entry1.grid(row=1, column=1)
        Button(rootsearch, text="完成", width=10, command=show).grid(row=2, column=1, sticky=W, padx=10, pady=5)
        rootsearch.mainloop()

    def searchBuy():

        def searchByBook():

            def show():
                q = entry1.get().split(" ")
                r = []
                for i in range(len(q)):
                    sql = "select BuyId, BuyNum , BuyTime,ClientName,ClientTele from buy natural join client where buy.ClientId = client.ClientId and BookId = \"% s\"" % q[i]
                    cursor.execute(sql)
                    c = list(cursor.fetchall())
                    for j in range(len(c)):
                        r.append(list(c[j]))
                print(r)
                showByBook = Tk()
                theLabel = tk.Label(showByBook, text="the info you need: ", justify=LEFT, padx=10)
                theLabel.pack(side=TOP)
                columns = ("BuyId", "BuyNum ", "BuyTime ", "ClientName", "ClientTele")
                treeview = ttk.Treeview(showByBook, height=18, show="headings", columns=columns)  # 表格
                for i in range(len(columns)):
                    if i == 2:
                        treeview.column(columns[i], width=200, anchor='center')
                    else:
                        treeview.column(columns[i], width=100, anchor='center')
                for i in range(len(columns)):
                    treeview.heading(columns[i], text=columns[i])
                treeview.pack(side=LEFT, fill=BOTH)
                for i in range(len(r)):  # 写入数据
                    treeview.insert('', i, values=r[i])
                showByBook.mainloop()

            searchByBook = Tk()
            label0 = tk.Label(searchByBook, text="SEARCH BY BOOK")
            label0.grid(row=0, column=0)
            label1 = tk.Label(searchByBook, text="please input BookId(s):")
            label1.grid(row=1, column=0)
            entry1 = tk.Entry(searchByBook)
            entry1.grid(row=1, column=1)
            Button(searchByBook, text="完成", width=10, command=show).grid(row=2, column=1, sticky=W, padx=10, pady=5)
            searchByBook.mainloop()

        def searchByClient():
            def showSearchByClient():
                name = entry1.get()
                tele = entry2.get()
                id = entry3.get()
                if id == "":
                    if name is "":
                        inputNullError()
                    else:
                        sql = "select ClientId from client where ClientName = \"% s\" " % name
                        cursor.execute(sql)
                        c = list(cursor.fetchall())
                        if len(c) == 1:
                            id = list(c[0])[0]
                        else:
                            if tele == "":
                                inputNullError()
                            else:
                                sql = "select ClientId from client where ClientName = \"% s\" and  ClientTele = % s" % (name , tele)
                                cursor.execute(sql)
                                id = list(list(cursor.fetchall())[0])[0]
                sql = "select ClientId, BookId, BuyNum, BuyTime from buy where ClientId = \"% s\" " % id
                cursor.execute(sql)
                r = list(cursor.fetchall())
                print(r)
                showSearchByClient = Tk()
                theLabel = tk.Label(showSearchByClient, text="the info you need: ", justify=LEFT, padx=10)
                theLabel.pack(side=TOP)
                columns = ("ClientId", "BookId", "BuyNum", "BuyTime")
                treeview = ttk.Treeview(showSearchByClient, height=18, show="headings", columns=columns)  # 表格
                for i in range(len(columns)):
                    if i == len(columns) - 1:
                        treeview.column(columns[i], width=200, anchor='center')
                    else:
                        treeview.column(columns[i], width=100, anchor='center')
                for i in range(len(columns)):
                    treeview.heading(columns[i], text=columns[i])
                treeview.pack(side=LEFT, fill=BOTH)
                for i in range(len(r)):  # 写入数据
                    treeview.insert('', i, values=r[i])
                    showSearchByClient.mainloop()

            searchByClient = Tk()
            label0 = tk.Label(searchByClient, text="SEARCH BY CLIENT")
            label0.grid(row=0, column=0)
            label1 = tk.Label(searchByClient, text="please input Name:")
            label1.grid(row=1, column=0)
            entry1 = tk.Entry(searchByClient)
            entry1.grid(row=1, column=1)
            label2 = tk.Label(searchByClient, text="please input tele:")
            label2.grid(row=2, column=0)
            entry2 = tk.Entry(searchByClient)
            entry2.grid(row=2, column=1)
            label3 = tk.Label(searchByClient, text="please input id:")
            label3.grid(row=3, column=0)
            entry3 = tk.Entry(searchByClient)
            entry3.grid(row=3, column=1)
            Button(searchByClient, text="完成", width=10, command=showSearchByClient).grid(row=4, column=1, sticky=W, padx=10, pady=5)
            searchByClient.mainloop()

        rootSearchBuy = Tk()
        theLabel = tk.Label(rootSearchBuy, text="HOW TO SEARCH", justify=LEFT, padx=10)
        theLabel.pack(side=TOP)
        Button(rootSearchBuy, text="BY BOOK", width=30, command=searchByBook).pack()
        Button(rootSearchBuy, text="BY CLIENT", width=30, command=searchByClient).pack()
        rootSearchBuy.mainloop()

    rootManager = Tk()
    s = "Hello, " + name + "!"
    if flag == 1:
        s += "\nplease update your code~\n"
    theLabel = tk.Label(rootManager, text=s, justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    Button(rootManager, text="personal staff", width=100, command=personal).pack()
    Button(rootManager, text="search for book ", width=100, command=searchBook).pack()
    Button(rootManager, text="search purchase info ", width=100, command=searchBuy).pack()
    Button(rootManager, text="insert info ", width=100, command=insert).pack()
    Button(rootManager, text="all in all", width=100, command=showEntity).pack()
    rootManager.mainloop()


def check():
    def show():
        if e1.get() is not "":
            s1 = e1.get()
            sql = "select CODE, ManagerName from manager where ManagerId = \"% s\"" % s1
            cursor.execute(sql)
            results = cursor.fetchall()
            code = list(list(results)[0])[0]
            name = list(list(results)[0])[1]
            print(code)
            if code is not None:
                if e2.get() is not "":
                    s2 = e2.get()
                    if code == s2:
                        manager(name, 0, s1, code)
                    else:
                        inputWrong()
                else:
                    inputNullError()
            else:
                # 如果数据库中没有设置密码，则直接进入
                if name is not None:
                    manager(name, 1, s1, code)
                else:
                    inputWrong()
        else:
            inputNullError()
    rootCheck = Tk()
    Label(rootCheck, text="your id:").grid(row=0)
    Label(rootCheck, text="your code:").grid(row=1)
    e1 = Entry(rootCheck)
    e2 = Entry(rootCheck)
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2.grid(row=1, column=1, padx=10, pady=5)
    Button(rootCheck, text="确认", width=10, command=show).grid(row=4, column=0, sticky=W, padx=10, pady=5)
    Button(rootCheck, text="退出", width=10, command=rootCheck.quit()).grid(row=4, column=1, sticky=E, padx=10, pady=5)
    mainloop()

def whoRU():
    rootWho = Tk()
    theLabel = tk.Label(rootWho, text="welcome to the Book Search System", justify=LEFT, padx=100)
    theLabel.pack(side=TOP)
    Button(rootWho, text="user", width=100, command=user).pack()
    Button(rootWho, text="manager", width=100, command=check).pack()
    mainloop()

def insertSuccess():
    rootInsertSuccess = Tk()
    theLabel = tk.Label(rootInsertSuccess, text="insert successfully~", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    rootInsertSuccess.mainloop()


def insertClient():
    def show():
        s1 = e1.get()
        s2 = e2.get()
        s3 = e3.get()
        sql = "INSERT INTO client (ClientId ,ClientName ,ClientTele) VALUES(%s,\"%s\",%s);" % (s1, s2, s3)
        cursor.execute(sql)
        showClient()
    rootInserClient = Tk()
    label0 = tk.Label(rootInserClient, text="INSERT CLIENT")
    label0.grid(row=0, column=0)
    Label(rootInserClient, text="id:").grid(row=1, column=0, padx=10, pady=5)
    Label(rootInserClient, text="name:").grid(row=2, column=0, padx=10, pady=5)
    Label(rootInserClient, text="tele:").grid(row=3, column=0, padx=10, pady=5)
    e1 = Entry(rootInserClient)
    e2 = Entry(rootInserClient)
    e3 = Entry(rootInserClient)
    e1.grid(row=1, column=1, padx=10, pady=5)
    e2.grid(row=2, column=1, padx=10, pady=5)
    e3.grid(row=3, column=1, padx=10, pady=5)
    Button(rootInserClient, text="完成", width=10, command=show).grid(row=4, column=0, sticky=W, padx=10, pady=5)
    rootInserClient.mainloop()


def insertManager():
    # ManagerName | ManagerTele | ManagerId | StorageId | CODE
    def show():
        s1 = e1.get()
        s2 = e2.get()
        s3 = e3.get()
        s4 = e4.get()
        s5 = e5.get()
        sql = "INSERT INTO manager (ManagerName ,ManagerTele ,ManagerId, StorageId,CODE ) VALUES(\"%s\",%s,%s,%s,\"%s\");" % (s1, s2, s3, s4, s5)
        cursor.execute(sql)
        showManager()
    rootInserManager = Tk()
    label0 = tk.Label(rootInserManager, text="INSERT MANAGER")
    label0.grid(row=0, column=0)
    Label(rootInserManager, text="ManagerName:").grid(row=1, column=0, padx=10, pady=5)
    Label(rootInserManager, text="ManagerTele:").grid(row=2, column=0, padx=10, pady=5)
    Label(rootInserManager, text="ManagerId:").grid(row=3, column=0, padx=10, pady=5)
    Label(rootInserManager, text="StorageId:").grid(row=4, column=0, padx=10, pady=5)
    Label(rootInserManager, text="CODE:").grid(row=5, column=0, padx=10, pady=5)
    e1 = Entry(rootInserManager)
    e2 = Entry(rootInserManager)
    e3 = Entry(rootInserManager)
    e4 = Entry(rootInserManager)
    e5 = Entry(rootInserManager)
    e1.grid(row=1, column=1, padx=10, pady=5)
    e2.grid(row=2, column=1, padx=10, pady=5)
    e3.grid(row=3, column=1, padx=10, pady=5)
    e4.grid(row=4, column=1, padx=10, pady=5)
    e5.grid(row=5, column=1, padx=10, pady=5)
    Button(rootInserManager, text="完成", width=10, command=show).grid(row=6, column=0, sticky=W, padx=10, pady=5)
    rootInserManager.mainloop()


def insertBook():
    #  BookId | Publisher | BookName | BookNum | BookPrice | Author | BookStyle | StorageId |
    def show():
        s1 = e1.get()
        s2 = e2.get()
        s3 = e3.get()
        s4 = e4.get()
        s5 = e5.get()
        s6 = e6.get()
        s7 = e7.get()
        s8 = e8.get()
        sql = "INSERT INTO book (BookId ,Publisher ,BookName, BookNum,BookPrice,  Author, BookStyle, StorageId) " \
              "VALUES(%s,\"%s\",\"%s\",%s,%s,\"%s\",\"%s\",%s);" % (s1, s2, s3, s4, s5, s6, s7, s8)
        cursor.execute(sql)
        showBook()
    rootInserBook = Tk()
    label0 = tk.Label(rootInserBook, text="INSERT BOOK")
    label0.grid(row=0, column=0)
    Label(rootInserBook, text="BookId:").grid(row=1, column=0, padx=10, pady=5)
    Label(rootInserBook, text="Publisher:").grid(row=2, column=0, padx=10, pady=5)
    Label(rootInserBook, text="BookName:").grid(row=3, column=0, padx=10, pady=5)
    Label(rootInserBook, text="BookNum:").grid(row=4, column=0, padx=10, pady=5)
    Label(rootInserBook, text="BookPrice:").grid(row=5, column=0, padx=10, pady=5)
    Label(rootInserBook, text="Author:").grid(row=6, column=0, padx=10, pady=5)
    Label(rootInserBook, text="BookStyle:").grid(row=7, column=0, padx=10, pady=5)
    Label(rootInserBook, text="StorageId:").grid(row=8, column=0, padx=10, pady=5)
    e1 = Entry(rootInserBook)
    e2 = Entry(rootInserBook)
    e3 = Entry(rootInserBook)
    e4 = Entry(rootInserBook)
    e5 = Entry(rootInserBook)
    e6 = Entry(rootInserBook)
    e7 = Entry(rootInserBook)
    e8 = Entry(rootInserBook)
    e1.grid(row=1, column=1, padx=10, pady=5)
    e2.grid(row=2, column=1, padx=10, pady=5)
    e3.grid(row=3, column=1, padx=10, pady=5)
    e4.grid(row=4, column=1, padx=10, pady=5)
    e5.grid(row=5, column=1, padx=10, pady=5)
    e6.grid(row=6, column=1, padx=10, pady=5)
    e7.grid(row=7, column=1, padx=10, pady=5)
    e8.grid(row=8, column=1, padx=10, pady=5)
    Button(rootInserBook, text="完成", width=10, command=show).grid(row=9, column=0, sticky=W, padx=10, pady=5)
    rootInserBook.mainloop()


def insertStorage():
    def show():
        # | StorageId | StorageName
        s1 = e1.get()
        s2 = e2.get()
        sql = "INSERT INTO storage (StorageId ,StorageName ) VALUES(%s,\"%s\");" % (s1, s2)
        cursor.execute(sql)
        showStorage()
    rootInserStorage = Tk()
    label0 = tk.Label(rootInserStorage, text="INSERT STORAGE")
    label0.grid(row=0, column=0)
    Label(rootInserStorage, text="StorageId:").grid(row=1, column=0, padx=10, pady=5)
    Label(rootInserStorage, text="StorageName:").grid(row=2, column=0, padx=10, pady=5)
    e1 = Entry(rootInserStorage)
    e2 = Entry(rootInserStorage)
    e1.grid(row=1, column=1, padx=10, pady=5)
    e2.grid(row=2, column=1, padx=10, pady=5)
    Button(rootInserStorage, text="完成", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)

    rootInserStorage.mainloop()


def insertManagement():
    def show():
        #  ManagementId | ManagerId | BookId
        s1 = e1.get()
        s2 = e2.get()
        s3 = e3.get()
        sql = "INSERT INTO management (ManagementId ,ManagerId, BookId ) VALUES(%s,%s,%s);" % (s1, s2, s3)
        cursor.execute(sql)
        showManagement()
    rootInserManagemen = Tk()
    label0 = tk.Label(rootInserManagemen, text="INSERT MANAGEMENT")
    label0.grid(row=0, column=0)
    Label(rootInserManagemen, text="ManagementId:").grid(row=1, column=0, padx=10, pady=5)
    Label(rootInserManagemen, text="ManagerId:").grid(row=2, column=0, padx=10, pady=5)
    Label(rootInserManagemen, text="BookId:").grid(row=3, column=0, padx=10, pady=5)
    e1 = Entry(rootInserManagemen)
    e2 = Entry(rootInserManagemen)
    e3 = Entry(rootInserManagemen)
    e1.grid(row=1, column=1, padx=10, pady=5)
    e2.grid(row=2, column=1, padx=10, pady=5)
    e3.grid(row=3, column=1, padx=10, pady=5)
    Button(rootInserManagemen, text="完成", width=10, command=show).grid(row=4, column=0, sticky=W, padx=10, pady=5)
    rootInserManagemen.mainloop()


def insertBuy():
    def show():
        #  | BuyId | ClientId | BookId | BuyNum | BuyTime
        s1 = e1.get()
        s2 = e2.get()
        s3 = e3.get()
        s4 = e4.get()
        s5 = e5.get()
        sql = "INSERT INTO buy (BuyId ,ClientId, BookId, BuyNum ,BuyTime) VALUES(%s,%s,%s,%s,\"%s\");" % (s1, s2, s3, s4, s5)
        cursor.execute(sql)
        showBuy()
    rootInserBuy = Tk()
    label0 = tk.Label(rootInserBuy, text="INSERT BUY")
    label0.grid(row=0, column=0)
    Label(rootInserBuy, text="BuyId:").grid(row=1, column=0, padx=10, pady=5)
    Label(rootInserBuy, text="ClientId:").grid(row=2, column=0, padx=10, pady=5)
    Label(rootInserBuy, text="BookId:").grid(row=3, column=0, padx=10, pady=5)
    Label(rootInserBuy, text="BuyNum:").grid(row=4, column=0, padx=10, pady=5)
    Label(rootInserBuy, text="BuyTime:").grid(row=5, column=0, padx=10, pady=5)
    e1 = Entry(rootInserBuy)
    e2 = Entry(rootInserBuy)
    e3 = Entry(rootInserBuy)
    e4 = Entry(rootInserBuy)
    e5 = Entry(rootInserBuy)
    e1.grid(row=1, column=1, padx=10, pady=5)
    e2.grid(row=2, column=1, padx=10, pady=5)
    e3.grid(row=3, column=1, padx=10, pady=5)
    e4.grid(row=4, column=1, padx=10, pady=5)
    e5.grid(row=5, column=1, padx=10, pady=5)
    Button(rootInserBuy, text="完成", width=10, command=show).grid(row=6, column=0, sticky=W, padx=10, pady=5)
    rootInserBuy.mainloop()


def insert():
    rootInput = Tk()
    theLabel = tk.Label(rootInput, text="welcome to the insert System", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    Button(rootInput, text="client", width=10, command=insertClient).pack()
    Button(rootInput, text="manager", width=10, command=insertManager).pack()
    Button(rootInput, text="book", width=10, command=insertBook).pack()
    Button(rootInput, text="storage", width=10, command=insertStorage).pack()
    Button(rootInput, text="management", width=10, command=insertManagement).pack()
    Button(rootInput, text="buy", width=10, command=insertBuy).pack()
    mainloop()


def showClient():
    rootShowUser = Tk()
    sql = "select * from  client"
    cursor.execute(sql)
    r = list(cursor.fetchall())
    print(r)
    theLabel = tk.Label(rootShowUser, text="CLIENT ", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    columns = ("ClientId", "ClientName", "ClientTele")
    treeview = ttk.Treeview(rootShowUser, height=18, show="headings", columns=columns)  # 表格
    for i in range(len(columns)):
        if i == len(columns) - 1:
            treeview.column(columns[i], width=200, anchor='center')
        else:
            treeview.column(columns[i], width=100, anchor='center')
    for i in range(len(columns)):
        treeview.heading(columns[i], text=columns[i])
    treeview.pack(side=LEFT, fill=BOTH)
    for i in range(len(r)):  # 写入数据
        treeview.insert('', i, values=r[i])
    rootShowUser.mainloop()


def showManager():
    rootShowManager = Tk()
    sql = "select  ManagerName, ManagerTele, ManagerId , StorageId from  manager"
    cursor.execute(sql)
    r = list(cursor.fetchall())
    print(r)
    theLabel = tk.Label(rootShowManager, text="MANAGER ", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    columns = ("ManagerName", "ManagerTele", "ManagerId","StorageId")
    treeview = ttk.Treeview(rootShowManager, height=18, show="headings", columns=columns)  # 表格
    for i in range(len(columns)):
        if i == len(columns) - 1:
            treeview.column(columns[i], width=200, anchor='center')
        else:
            treeview.column(columns[i], width=100, anchor='center')
    for i in range(len(columns)):
        treeview.heading(columns[i], text=columns[i])
    treeview.pack(side=LEFT, fill=BOTH)
    for i in range(len(r)):  # 写入数据
        treeview.insert('', i, values=r[i])
    rootShowManager.mainloop()


def showBook():
    rootSHowBook = Tk()
    sql = "select * from  book"
    cursor.execute(sql)
    r = list(cursor.fetchall())
    print(r)
    theLabel = tk.Label(rootSHowBook, text="BOOK ", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    columns = ("BookId", "Publisher", "BookName", "BookNum", "BookPrice", "Author", "BookStyle", "StorageId")
    treeview = ttk.Treeview(rootSHowBook, height=18, show="headings", columns=columns)  # 表格
    for i in range(len(columns)):
        if i == len(columns) - 1:
            treeview.column(columns[i], width=200, anchor='center')
        else:
            treeview.column(columns[i], width=100, anchor='center')
    for i in range(len(columns)):
        treeview.heading(columns[i], text=columns[i])
    treeview.pack(side=LEFT, fill=BOTH)
    for i in range(len(r)):  # 写入数据
        treeview.insert('', i, values=r[i])
    rootSHowBook.mainloop()

def showStorage():
    rootShowStorage = Tk()
    sql = "select * from  storage"
    cursor.execute(sql)
    r = list(cursor.fetchall())
    print(r)
    theLabel = tk.Label(rootShowStorage, text="STORAGE ", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    columns = ( "StorageId", "StorageName")
    treeview = ttk.Treeview(rootShowStorage, height=18, show="headings", columns=columns)  # 表格
    for i in range(len(columns)):
        if i == len(columns) - 1:
            treeview.column(columns[i], width=200, anchor='center')
        else:
            treeview.column(columns[i], width=100, anchor='center')
    for i in range(len(columns)):
        treeview.heading(columns[i], text=columns[i])
    treeview.pack(side=LEFT, fill=BOTH)
    for i in range(len(r)):  # 写入数据
        treeview.insert('', i, values=r[i])
    rootShowStorage.mainloop()

def showManagement():
    rootShowManagement= Tk()
    sql = "select ManagerId, BookId from  management;"
    cursor.execute(sql)
    r = list(cursor.fetchall())
    print(r)
    theLabel = tk.Label(rootShowManagement, text="MANAGEMENT ", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    columns = ("ManagerId", "BookId")
    treeview = ttk.Treeview(rootShowManagement, height=18, show="headings", columns=columns)  # 表格
    for i in range(len(columns)):
        if i == len(columns) - 1:
            treeview.column(columns[i], width=200, anchor='center')
        else:
            treeview.column(columns[i], width=100, anchor='center')
    for i in range(len(columns)):
        treeview.heading(columns[i], text=columns[i])
    treeview.pack(side=LEFT, fill=BOTH)
    for i in range(len(r)):  # 写入数据
        treeview.insert('', i, values=r[i])
    rootShowManagement.mainloop()


def showBuy():
    rootShowBuy = Tk()
    sql = "select  ClientId , BookId , BuyNum , BuyTime from  buy"
    cursor.execute(sql)
    r = list(cursor.fetchall())
    print(r)
    theLabel = tk.Label(rootShowBuy, text="BUY ", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    columns = ("ClientId "," BookId ", "BuyNum", "BuyTime")
    treeview = ttk.Treeview(rootShowBuy, height=18, show="headings", columns=columns)  # 表格
    for i in range(len(columns)):
        if i == len(columns) - 1:
            treeview.column(columns[i], width=200, anchor='center')
        else:
            treeview.column(columns[i], width=100, anchor='center')
    for i in range(len(columns)):
        treeview.heading(columns[i], text=columns[i])
    treeview.pack(side=LEFT, fill=BOTH)
    for i in range(len(r)):  # 写入数据
        treeview.insert('', i, values=r[i])
    rootShowBuy.mainloop()


def showEntity():
    rootShowEntity = Tk()
    theLabel = tk.Label(rootShowEntity, text="welcome to the ShowALL System", justify=LEFT, padx=10)
    theLabel.pack(side=TOP)
    Button(rootShowEntity, text="client", width=10, command=showClient).pack()
    Button(rootShowEntity, text="manager", width=10, command=showManager).pack()
    Button(rootShowEntity, text="book", width=10, command=showBook).pack()
    Button(rootShowEntity, text="storage", width=10, command=showStorage).pack()
    Button(rootShowEntity, text="management", width=10, command=showManagement).pack()
    Button(rootShowEntity, text="buy", width=10, command=showBuy).pack()

    mainloop()

whoRU()
cursor.close()
# 关闭数据库连接
conn.close()


