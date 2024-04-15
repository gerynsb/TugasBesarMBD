from tkinter import* 
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB: 
        
    def __init__(self, root):
        self.root = root
        titlespace = ""
        self.root.title(102 * titlespace + "MySQL Connector")
        self.root.geometry('800x700+300+0')
        self.root.resizable(width=False, height=False)
            
        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg='cadet blue')
        MainFrame.grid()
            
        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)
            
        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, bg='cadet blue', relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=12, pady=9, relief=RIDGE)
        LeftFrame1.pack(side=TOP)
            
        RightFrame1= Frame(TopFrame3, bd=5, width=100, height=400, padx=2, bg='cadet blue', relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2,relief=RIDGE)
        RightFrame1a.pack(side=TOP)
            
        # Define Text Variables as instance attributes
        self.kode_pembayaran = StringVar()
        self.cash = StringVar()
        self.cicilan  = StringVar()
        
        # Functionality
        def iExit():
            iExit = tkinter.messagebox.askyesno("MySQL Conntion", "Confirm if you want to exit")     
            if iExit > 0 : 
                root.destroy()
                return
        
        def Reset() : 
            self.kode_pembayaran.set("")
            self.cash.set("")
            self.cicilan.set("")
            
        def addData() : 
            if self.kode_pembayaran.get() == "" or self.cash.get() == "": 
                tkinter.messagebox.showerror('Enter Correct Details')
            else: 
                sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
                cur = sqlCon.cursor()
                cur.execute("insert into pembayaran values (%s, %s, %s)",(
                self.kode_pembayaran.get(), 
                self.cash.get(),
                self.cicilan.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

        def DisplayData(): 
            sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("select * from pembayaran")
            result = cur.fetchall()
            if len(result) != 0 : 
                self.pembayaran_records.delete(*self.pembayaran_records.get_children())
                for row in result:
                    self.pembayaran_records.insert('', END,values = row)
                    
                sqlCon.commit()
                sqlCon.close()
        
        def pembayaranInfo(ev):
            viewInfo = self.pembayaran_records.focus()
            if viewInfo:
                pembayaranData = self.pembayaran_records.item(viewInfo)
                row = pembayaranData.get('values', [])
            if row : 
                self.kode_pembayaran.set(row[0])
                self.cash.set(row[1])
                self.cicilan.set(row[2])
                
        def update() : 
            sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("update pembayaran set cash = %s, cicilan = %s where kode_pembayaran = %s", (
                
                self.cash.get(),
                self.cicilan.get(),
                self.kode_pembayaran.get()
            ))
            
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully")
            
        def deleteDB(): 
            selected_item = self.pembayaran_records.selection()
            if selected_item: 
                self.pembayaran_records.delete(selected_item)
                
                sqlCon = pymysql.connect(host="localhost", port=3307, user="root", password="Dean642642#", database="tokokomputer")
                cur = sqlCon.cursor()
                cur.execute("delete from pembayaran where kode_pembayaran = %s", self.kode_pembayaran.get())
                
                sqlCon.commit()
                sqlCon.close()
                
                tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")
                
            else : 
                tkinter.messagebox.showinfo("Data Entry Form", "Please select a record to delete")
                
        def searchDB(): 
            try :
                sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
                cur = sqlCon.cursor()
                cur.execute("select * from pembayaran where kode_pembayaran=%s"%self.kode_pembayaran.get())
                
                row = cur.fetchone()
                
                self.kode_pembayaran.set(row[0])
                self.cash.set(row[1])
                self.cicilan.set(row[2])
  
                sqlCon.commit()
                
            except: 
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found")
                Reset()
                
            sqlCon.close()
            
        # Label Frame
        self.lbltitle=Label(TitleFrame, font=('arial', 40, 'bold'), text= "Toko Komputer", bd=7)
        self.lbltitle.grid(row=0, column=0,padx=132)
            
        self.lblkode_pembayaran=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Kode pembayaran', bd =7)
        self.lblkode_pembayaran.grid(row=1, column=0, padx= 5)
        self.entkode_pembayaran=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.kode_pembayaran)
        self.entkode_pembayaran.grid(row=1,column=1,sticky=W,padx=5)
            
        self.lblcash=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Cash', bd =7)
        self.lblcash.grid(row=2, column=0, padx= 5)
        self.entcash=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.cash)
        self.entcash.grid(row=2,column=1,sticky=W,padx=5)
            
        self.lblcicilan=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Alamat pembayaran', bd =7)
        self.lblcicilan.grid(row=3, column=0, padx= 5)
        self.entcicilan=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.cicilan)
        self.entcicilan.grid(row=3,column=1,sticky=W,padx=5)
        
        # Table Treeview
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        
        self.pembayaran_records=ttk.Treeview(LeftFrame, height=14, columns=("kode_pembayaran", "cash","cicilan"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.pembayaran_records.heading("kode_pembayaran",text = "Kode Pembayaran")
        self.pembayaran_records.heading("cash", text = "Cash")
        self.pembayaran_records.heading("cicilan", text = "Cicilan")
        
        self.pembayaran_records['show']='headings'
        
        self.pembayaran_records.column("kode_pembayaran", width = 70)
        self.pembayaran_records.column("cash", width = 100)
        self.pembayaran_records.column("cicilan", width = 100)
        
        self.pembayaran_records.pack(fill = BOTH, expand=1)
        self.pembayaran_records.bind("<ButtonRelease-1>", pembayaranInfo)
        
        # Buttons
        self.btnAddNew=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Add New', bd=4,pady=1, padx=24,
                              width=5, height=1, command=addData)
        self.btnAddNew.grid(row=0,column=0, padx=1)
        
        self.btnDisplay=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Display', bd=4,pady=1, padx=24,
                              width=5, height=2, command=DisplayData)
        self.btnDisplay.grid(row=1,column=0, padx=1)
        
        self.btnUpdate=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Update', bd=4,pady=1, padx=24,
                              width=5, height=2, command=update)
        self.btnUpdate.grid(row=2,column=0, padx=1)
        
        self.btnDelete=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Delete', bd=4,pady=1, padx=24,
                              width=5, height=2, command=deleteDB)
        self.btnDelete.grid(row=3,column=0, padx=1)
        
        self.btnSearch=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Search', bd=4,pady=1, padx=24,
                              width=5, height=2, command=searchDB)
        self.btnSearch.grid(row=4,column=0, padx=1)
        
        self.btnReset=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Reset', bd=4,pady=1, padx=24,
                              width=5, height=2, command=Reset)
        self.btnReset.grid(row=5,column=0, padx=1)
        
        self.btnExit=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Exit', bd=4,pady=1, padx=24,
                              width=5, height=1, command=iExit)
        self.btnExit.grid(row=6,column=0, padx=1)


if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
