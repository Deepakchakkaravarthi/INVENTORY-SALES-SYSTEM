# import modules
from tkinter import *
import tkinter.messagebox
import sqlite3


# class for font End UI
class Product:

    def __init__(self, root):

        # CREATE object reference instance of Database class as p

        p = Database()
        p.conn()

        self.root = root
        self.root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("1325x690")
        self.root.config(bg="grey")

        pId = StringVar()
        pName = StringVar()
        pPrice = StringVar()
        pQty = StringVar()
        pCompany = StringVar()
        pContact = StringVar()

        '''' lets call the database methods to perform database operations'''

        # function to close the product frame

        def close():
            print("Product : close method called ")
            close = tkinter.messagebox.askyesno("WAREHOUSE INVENTORY \ SALES MANAGEMENT SYSTEM")
            if close > 0:
                root.destroy()
                print("Product : close method finished\n")

            return

        #  function for clear / reset the widget

        def clear():
            print("Product : clear method called ")
            self.txtpID.delete(0, END)
            self.txtpName.delete(0, END)
            self.txtpPrice.delete(0, END)
            self.txtpQty.delete(0, END)
            self.txtpCompany.delete(0, END)
            self.txtpContact.delete(0, END)
            print("Product : clear method finished\n ")

        # function to save the product detials in database TABLE

        def insert():
            print("Product : insert method called ")
            if (len(pId.get()) != 0):
                p.insert(pId.get(), pName.get(), pQty.get(), pPrice.get(), pCompany.get(), pContact.get())
                ProductList.delete(0, END)
                ProductList.insert(END, pId.get(), pName.get(), pQty.get(), pPrice.get(), pCompany.get(),
                                   pContact.get())
                showInProductList()  # called showInproductlist method
            else:
                tkinter.messagebox.askyesno("WAREHOUSE INVENTORY \ SALES MANAGEMENT SYSTEM",
                                            "Really .... Enter Product Id")
                print("Product : insert method finished\n ")

        # function responsible to show product TABLE data to scrooll  productlist

        def showInProductList():
            print("Product : showInProductList method called ")
            ProductList.delete(0, END)
            for row in p.show():
                ProductList.insert(END, row, str(""))
                print("Product : showInProductList method finished\n ")

        # add to scroll bar

        def ProductRec(event):  # function to be called from scrollbar ProducList
            print("Product :  ProductRec method called ")
            global pd

            searchPd = ProductList.curselection()[0]
            pd = ProductList.get(searchPd)

            self.txtpID.delete(0, END)
            self.txtpID.insert(END, pd[0])

            self.txtpName.delete(0, END)
            self.txtpName.insert(END, pd[1])

            self.txtpPrice.delete(0, END)
            self.txtpPrice.insert(END, pd[2])

            self.txtpQty.delete(0, END)
            self.txtpQty.insert(END, pd[3])

            self.txtpCompany.delete(0, END)
            self.txtpCompany.insert(END, pd[4])

            self.txtpContact.delete(0, END)
            self.txtpContact.insert(END, pd[5])

            print('Product :  ProductRec method finished \n')

        # function to delete the data record from database TABLE

        def delete():
            print('Product :  delete method called')
            if (len(pId.get()) != 0):
                p.delete(pd[0])
                clear()
                showInProductList()
            print('Product : delete method finished \n')

        # search the record from database TABLE
        def search():
            print('Product : search method called')
            ProductList.delete(0, END)
            for row in p.search(pId.get(), pName.get(), pQty.get(), pPrice.get(), pCompany.get(), pContact.get()):
                ProductList.insert(END, row, str(""))
                print('Product : search method finished \n')

        # function to update the record
        def update():
            print("Product : update method called")
            if (len(pId.get()) != 0):
                print("pd[0]", pd[p])
                p.delete(pd[0])
            if (len(pId.get()) != 0):
                p.insert(pId.get(), pName.get(), pQty.get(), pPrice.get(), pCompany.get(), pContact.get())
            ProductList.delete(0, END)
            ProductList.insert(END, (pId.get(), pName.get(), pQty.get(), pPrice.get(), pCompany.get(), pContact.get()))
            print("Product : update method finished \n")

        MainFrame = Frame(self.root, bg="green")
        MainFrame.grid()

        HeadFrame = Frame(MainFrame, bd=1, padx=50, pady=10, bg='white', relief=RIDGE)
        HeadFrame.pack(side='top')
        self.ITitle = Label(HeadFrame, font=('arial', 50, 'bold'), fg='red',
                            text=' Warehouse Inventory Sales Purchase ', bg='white')
        self.ITitle.grid()

        operationFrame = Frame(MainFrame, bd=2, width=1300, height=60, padx=50, pady=20, bg='white',
                               relief=RIDGE)
        operationFrame.pack(side=BOTTOM)
        BodyFrame = Frame(MainFrame, bd=2, width=1290, height=400, padx=30, pady=20, bg='white',
                          relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)
        LeftBodyFrame = Frame(BodyFrame, bd=2, width=600, height=390, padx=20, pady=10, bg='yellow',
                              relief=RIDGE)
        LeftBodyFrame.pack(side=LEFT)
        RightBodyFrame = Frame(BodyFrame, bd=2, width=400, height=390, padx=20, pady=10, bg='yellow',
                               relief=RIDGE)
        RightBodyFrame.pack(side=RIGHT)

        '''''add the widgets to LeftBodyFrame'''

        self.LabelpID = Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Product Id: ",
                              padx=2, pady=2, bg='white', fg='blue')
        self.LabelpID.grid(row=0, column=0, sticky='w')
        self.txtpID = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=pId,
                            width=35)
        self.txtpID.grid(row=0, column=1, sticky='w')

        self.LabelpName = Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Product Name :",
                                padx=2, pady=2, bg='white', fg='blue')
        self.LabelpName.grid(row=1, column=0, sticky='w')
        self.txtpName = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=pName,
                              width=35)
        self.txtpName.grid(row=1, column=1, sticky='w')

        self.LabelpPrice = Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Product Price :",
                                 padx=2, pady=2, bg='white', fg='blue')
        self.LabelpPrice.grid(row=2, column=0, sticky='w')
        self.txtpPrice = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=pPrice,
                               width=35)
        self.txtpPrice.grid(row=2, column=1, sticky='w')

        self.LabelpQty = Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Product Qunantity",
                               padx=2, pady=2, bg='white', fg='blue')
        self.LabelpQty.grid(row=3, column=0, sticky='w')
        self.txtpQty = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=pQty,
                             width=35)
        self.txtpQty.grid(row=3, column=1, sticky='w')

        self.LabelpCompany = Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="MFG. Company :",
                                   padx=2, pady=2, bg='white', fg='blue')
        self.LabelpCompany.grid(row=4, column=0, sticky='w')
        self.txtpCompany = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=pCompany,
                                 width=35)
        self.txtpCompany.grid(row=4, column=1, sticky='w')

        self.LabelpContact = Label(LeftBodyFrame, font=('arial', 15, 'bold'), text="Company Contact :",
                                   padx=2, pady=2, bg='white', fg='blue')
        self.LabelpContact.grid(row=5, column=0, sticky='w')
        self.txtpContact = Entry(LeftBodyFrame, font=('arial', 20, 'bold'), textvariable=pContact,
                                 width=35)
        self.txtpContact.grid(row=5, column=1, sticky='w')

        self.labelpC1 = Label(LeftBodyFrame, padx=2, pady=2)
        self.labelpC1.grid(row=6, column=0, sticky='w')

        self.labelpC2 = Label(LeftBodyFrame, padx=2, pady=2)
        self.labelpC2.grid(row=7, column=0, sticky='w')

        self.labelpC3 = Label(LeftBodyFrame, padx=2, pady=2)
        self.labelpC3.grid(row=8, column=0, sticky='w')

        self.labelpC4 = Label(LeftBodyFrame, padx=2, pady=2)
        self.labelpC4.grid(row=9, column=0, sticky='w')

        '''' add scroll bar'''

        scroll = Scrollbar(RightBodyFrame)
        scroll.grid(row=0, column=1, sticky='ns')
        ProductList = Listbox(RightBodyFrame, width=40, height=16, font=('arial', 12, 'bold'),
                              yscrollcommand=scroll.set)
        # called above CREATEd productRec function of init
        ProductList.bind('<<ListboxSelect>>', ProductRec)
        ProductList.grid(row=0, column=0, padx=8)
        scroll.config(command=ProductList.yview)

        ''''  add the button to operation Frame '''

        self.buttonSaveData = Button(operationFrame, text='save', font=('arial', 18, 'bold')
                                     , height=1, width='10', bd=4, command=insert)
        self.buttonSaveData.grid(row=0, column=0)

        self.buttonShowData = Button(operationFrame, text='show', font=('arial', 18, 'bold')
                                     , height=1, width='10', bd=4, command=showInProductList)
        self.buttonShowData.grid(row=0, column=1)

        self.buttonClearData = Button(operationFrame, text='reset', font=('arial', 18, 'bold')
                                      , height=1, width='10', bd=4, command=clear)
        self.buttonClearData.grid(row=0, column=2)

        self.buttonDeleteData = Button(operationFrame, text='delete', font=('arial', 18, 'bold')
                                       , height=1, width='10', bd=4, command=delete)
        self.buttonDeleteData.grid(row=0, column=3)

        self.buttonUpdateData = Button(operationFrame, text='update', font=('arial', 18, 'bold')
                                       , height=1, width='10', bd=4)
        self.buttonUpdateData.grid(row=0, column=4)

        self.buttonSearchData = Button(operationFrame, text='search', font=('arial', 18, 'bold')
                                       , height=1, width='10', bd=4, command=search)
        self.buttonSearchData.grid(row=0, column=5)

        self.buttonClose = Button(operationFrame, text='close', font=('arial', 18, 'bold')
                                  , height=1, width='10', bd=4, command=close)
        self.buttonClose.grid(row=0, column=6)


# back end database operations

class Database():
    def conn(self):
        print("Database : connection method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "CREATE TABLE if not EXISTS product(pid integer primary key,pname text,price text,qty text,company text,contact text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database : connection method finished\n")

    def insert(self, pid, name, price, qty, company, contact):
        print("Database : insert method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "insert into product values(?,?,?,?,?,?)"
        cur.execute(query, (pid, name, price, qty, company, contact))
        con.commit()
        con.close()
        print("Database : insert method finished\n")

    def show(self):
        print("Database : show method called")
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        query = "select * from product"
        cur.execute(query)
        rows = cur.fetchall()
        con.close()
        print("Database : show method finished\n")
        return rows

    def delete(self, pid):
        print("Database : delete method called ", pid)
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("delete from product where pid=?", (pid,))
        con.commit()
        con.close()
        print(pid, " Database : delete method finished\n")

    def search(self, pid="", name="", price="", qty="", company="", contact=""):
        print("Database : search method called ", pid)
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("select * from poduct where pid=? or pname=? or \
		price=? or qty=? or company=? or contact=? ", (pid, name, price, qty, company, contact))
        row = cur.fetchall()
        con.clase()
        print(pid, " Database : search method finished\n")
        return row

    def update(self, pid="", name="", price="", qty="", company="", contact=""):
        print("Database : update method called ", pid)
        con = sqlite3.connect("inventory.db")
        cur = con.cursor()
        cur.execute("update product set pid=? or pname=? or \
		price=? or qty=? or company=? or contact=? where pid=? ",
                    (pid, name, price, qty, company, contact, pid))
        con.commit()
        con.close()
        print(pid, " Database : update method finished\n")


if __name__ == '__main__':
    root = Tk()
    application = Product(root)
    root.mainloop()














