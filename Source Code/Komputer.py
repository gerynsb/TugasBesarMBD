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
        self.tipe = StringVar()
        self.thn_rilis = StringVar()
        self.warna  = StringVar()
        self.merk = StringVar()
        self.harga = StringVar()
        
        # Functionality
        def iExit():
            iExit = tkinter.messagebox.askyesno("MySQL Conntion", "Confirm if you want to exit")     
            if iExit > 0 : 
                root.destroy()
                return
        
        def Reset() : 
            self.tipe.set("")
            self.thn_rilis.set("")
            self.warna.set("")
            self.merk.set("")
            self.harga.set("")
            
        def addData():
            if self.tipe.get() == "" or self.thn_rilis.get() == "":
                tkinter.messagebox.showerror('Enter Correct Details')
            else:
                try:
                    sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
                    cur = sqlCon.cursor()
                    cur.execute("insert into komputer values (%s, %s, %s, %s, %s)", (
                        self.tipe.get(),
                        self.thn_rilis.get(),
                        self.warna.get(),
                        self.merk.get(),
                        self.harga.get(),
                    ))
                    sqlCon.commit()
                    sqlCon.close()
                    tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")
                    
                except pymysql.IntegrityError as e:
                    tkinter.messagebox.showerror("Data Entry Form", f"Failed to add record: {e}")

        def DisplayData(): 
            sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("select * from komputer")
            result = cur.fetchall()
            if len(result) != 0 : 
                self.komputer_records.delete(*self.komputer_records.get_children())
                for row in result:
                    self.komputer_records.insert('', END,values = row)
                    
                sqlCon.commit()
                sqlCon.close()
        
        def komputerInfo(ev):
            viewInfo = self.komputer_records.focus()
            if viewInfo:
                komputerData = self.komputer_records.item(viewInfo)
                row = komputerData.get('values', [])
            if row : 
                self.tipe.set(row[0])
                self.thn_rilis.set(row[1])
                self.warna.set(row[2])
                self.merk.set(row[3])
                self.harga.set(row[4])
                
        def update() : 
            sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("update komputer set thn_rilis = %s, warna = %s, merk = %s, harga = %s where tipe = %s", (
                
                self.thn_rilis.get(),
                self.warna.get(),
                self.merk.get(),
                self.harga.get(),
                self.tipe.get()
            ))
            
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully")
            
        def deleteDB(): 
            selected_item = self.komputer_records.selection()
            if selected_item: 
                self.komputer_records.delete(selected_item)
                
                sqlCon = pymysql.connect(host="localhost", port=3307, user="root", password="Dean642642#", database="tokokomputer")
                cur = sqlCon.cursor()
                cur.execute("delete from komputer where tipe = %s", self.tipe.get())
                
                sqlCon.commit()
                sqlCon.close()
                
                tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")
                
            else : 
                tkinter.messagebox.showinfo("Data Entry Form", "Please select a record to delete")
                
        def searchDB(): 
            try :
                sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
                cur = sqlCon.cursor()
                cur.execute("select * from komputer where tipe=%s"%self.tipe.get())
                
                row = cur.fetchone()
                
                self.tipe.set(row[0])
                self.thn_rilis.set(row[1])
                self.warna.set(row[2])
                self.merk.set(row[3])
                self.harga.set(row[3])
  
                sqlCon.commit()
                
            except: 
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found")
                Reset()
                
            sqlCon.close()
            
        # Label Frame
        self.lbltitle=Label(TitleFrame, font=('arial', 40, 'bold'), text= "Toko Komputer", bd=7)
        self.lbltitle.grid(row=0, column=0,padx=132)
            
        self.lbltipe=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Tipe Komputer', bd =7)
        self.lbltipe.grid(row=1, column=0, padx= 5)
        self.enttipe=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.tipe)
        self.enttipe.grid(row=1,column=1,sticky=W,padx=5)
            
        self.lblthn_rilis=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Tahun Rilis', bd =7)
        self.lblthn_rilis.grid(row=2, column=0, padx= 5)
        self.entthn_rilis=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.thn_rilis)
        self.entthn_rilis.grid(row=2,column=1,sticky=W,padx=5)
            
        self.lblwarna=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Warna Komputer', bd =7)
        self.lblwarna.grid(row=3, column=0, padx= 5)
        self.entwarna=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.warna)
        self.entwarna.grid(row=3,column=1,sticky=W,padx=5)
        
        self.lblmerk = Label(LeftFrame1, font=('arial', 12, 'bold'), text = 'Merk Komputer', bd=7)
        self.lblmerk.grid(row=4, column=0, padx= 5)
        self.entmerk=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.merk)
        self.entmerk.grid(row=4,column=1,sticky=W,padx=5)
        
        self.lblharga = Label(LeftFrame1, font=('arial', 12, 'bold'), text = 'Harga Komputer', bd=7)
        self.lblharga.grid(row=5, column=0, padx= 5)
        self.entharga=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.harga)
        self.entharga.grid(row=5,column=1,sticky=W,padx=5)
        
        # Table Treeview
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        
        self.komputer_records=ttk.Treeview(LeftFrame, height=14, columns=("tipe", "thn_rilis","warna", "merk", "harga"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.komputer_records.heading("tipe",text = "Tipe Komputer")
        self.komputer_records.heading("thn_rilis", text = "Tahun Rilis")
        self.komputer_records.heading("warna", text = "Warna Komputer")
        self.komputer_records.heading("merk", text = "Merk Komputer")
        self.komputer_records.heading("harga", text = "Harga Komputer")
        
        self.komputer_records['show']='headings'
        
        self.komputer_records.column("tipe", width = 70)
        self.komputer_records.column("thn_rilis", width = 100)
        self.komputer_records.column("warna", width = 100)
        self.komputer_records.column("merk", width = 70)
        self.komputer_records.column("harga", width = 70)
        
        self.komputer_records.pack(fill = BOTH, expand=1)
        self.komputer_records.bind("<ButtonRelease-1>", komputerInfo)
        
        # Buttons
        self.btnAddNew=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Add New', bd=4,pady=1, padx=24,
                              width=5, height=2, command=addData)
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
                              width=5, height=2, command=iExit)
        self.btnExit.grid(row=6,column=0, padx=1)


if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
