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
        self.seriProduk = StringVar()
        self.tgl_pemesanan = StringVar()
        
        # Functionality
        def iExit():
            iExit = tkinter.messagebox.askyesno("MySQL Conntion", "Confirm if you want to exit")     
            if iExit > 0 : 
                root.destroy()
                return
        
        def Reset() : 
            self.seriProduk.set("")
            self.tgl_pemesanan.set("")
            
        def addData() : 
            if self.seriProduk.get() == "" or self.tgl_pemesanan.get() == "": 
                tkinter.messagebox.showerror('Enter Correct Details')
            else: 
                sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
                cur = sqlCon.cursor()
                cur.execute("insert into pesanan values (%s, %s)",(
                self.seriProduk.get(), 
                self.tgl_pemesanan.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

        def DisplayData(): 
            sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("select * from pesanan")
            result = cur.fetchall()
            if len(result) != 0 : 
                self.pesanan_records.delete(*self.pesanan_records.get_children())
                for row in result:
                    self.pesanan_records.insert('', END,values = row)
                    
                sqlCon.commit()
                sqlCon.close()
        
        def pesananInfo(ev):
            viewInfo = self.pesanan_records.focus()
            if viewInfo:
                pesananData = self.pesanan_records.item(viewInfo)
                row = pesananData.get('values', [])
            if row : 
                self.seriProduk.set(row[0])
                self.tgl_pemesanan.set(row[1])
                
        def update() : 
            sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("update pesanan set tgl_pemesanan = %s where seriProduk = %s", (
                
                self.tgl_pemesanan.get(),
                self.seriProduk.get()
            ))
            
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully")
            
        def deleteDB(): 
            selected_item = self.pesanan_records.selection()
            if selected_item: 
                self.pesanan_records.delete(selected_item)
                
                sqlCon = pymysql.connect(host="localhost", port=3307, user="root", password="Dean642642#", database="tokokomputer")
                cur = sqlCon.cursor()
                cur.execute("delete from pesanan where seriProduk = %s", self.seriProduk.get())
                
                sqlCon.commit()
                sqlCon.close()
                
                tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")
                
            else : 
                tkinter.messagebox.showinfo("Data Entry Form", "Please select a record to delete")
                
        def searchDB(): 
            try :
                sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
                cur = sqlCon.cursor()
                cur.execute("select * from pesanan where seriProduk=%s"%self.seriProduk.get())
                
                row = cur.fetchone()
                
                self.seriProduk.set(row[0])
                self.tgl_pemesanan.set(row[1])
  
                sqlCon.commit()
                
            except: 
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found")
                Reset()
                
            sqlCon.close()
            
        # Label Frame
        self.lbltitle=Label(TitleFrame, font=('arial', 40, 'bold'), text= "Toko Komputer", bd=7)
        self.lbltitle.grid(row=0, column=0,padx=132)
            
        self.lblseriProduk=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Kode pesanan', bd =7)
        self.lblseriProduk.grid(row=1, column=0, padx= 5)
        self.entseriProduk=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.seriProduk)
        self.entseriProduk.grid(row=1,column=1,sticky=W,padx=5)
            
        self.lbltgl_pemesanan=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'tgl_pemesanan', bd =7)
        self.lbltgl_pemesanan.grid(row=2, column=0, padx= 5)
        self.enttgl_pemesanan=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.tgl_pemesanan)
        self.enttgl_pemesanan.grid(row=2,column=1,sticky=W,padx=5)
        
        # Table Treeview
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        
        self.pesanan_records=ttk.Treeview(LeftFrame, height=14, columns=("seriProduk", "tgl_pemesanan"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.pesanan_records.heading("seriProduk",text = "Kode pesanan")
        self.pesanan_records.heading("tgl_pemesanan", text = "tgl_pemesanan")
        
        self.pesanan_records['show']='headings'
        
        self.pesanan_records.column("seriProduk", width = 70)
        self.pesanan_records.column("tgl_pemesanan", width = 100)
        
        self.pesanan_records.pack(fill = BOTH, expand=1)
        self.pesanan_records.bind("<ButtonRelease-1>", pesananInfo)
        
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
