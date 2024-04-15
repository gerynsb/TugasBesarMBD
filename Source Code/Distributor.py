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
        self.id_distributor = StringVar()
        self.alamat_distributor = StringVar()
        
        # Functionality
        def iExit():
            iExit = tkinter.messagebox.askyesno("MySQL Conntion", "Confirm if you want to exit")     
            if iExit > 0 : 
                root.destroy()
                return
        
        def Reset() : 
            self.id_distributor.set("")
            self.alamat_distributor.set("")
            
        def addData() : 
            if self.id_distributor.get() == "" or self.alamat_distributor.get() == "": 
                tkinter.messagebox.showerror('Enter Correct Details')
            else: 
                sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
                cur = sqlCon.cursor()
                cur.execute("insert into distributor values (%s, %s)",(
                self.id_distributor.get(), 
                self.alamat_distributor.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

        def DisplayData(): 
            sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("select * from distributor")
            result = cur.fetchall()
            if len(result) != 0 : 
                self.distributor_records.delete(*self.distributor_records.get_children())
                for row in result:
                    self.distributor_records.insert('', END,values = row)
                    
                sqlCon.commit()
                sqlCon.close()
        
        def distributorInfo(ev):
            viewInfo = self.distributor_records.focus()
            if viewInfo:
                distributorData = self.distributor_records.item(viewInfo)
                row = distributorData.get('values', [])
            if row : 
                self.id_distributor.set(row[0])
                self.alamat_distributor.set(row[1])
                
        def update() : 
            sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("update distributor set alamat_distributor = %s where id_distributor = %s", (
                
                self.alamat_distributor.get(),
                self.id_distributor.get()
            ))
            
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully")
            
        def deleteDB(): 
            selected_item = self.distributor_records.selection()
            if selected_item: 
                self.distributor_records.delete(selected_item)
                
                sqlCon = pymysql.connect(host="localhost", port=3307, user="root", password="Dean642642#", database="tokokomputer")
                cur = sqlCon.cursor()
                cur.execute("delete from distributor where id_distributor = %s", self.id_distributor.get())
                
                sqlCon.commit()
                sqlCon.close()
                
                tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")
                
            else : 
                tkinter.messagebox.showinfo("Data Entry Form", "Please select a record to delete")
                
        def searchDB(): 
            try :
                sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
                cur = sqlCon.cursor()
                cur.execute("select * from distributor where id_distributor=%s"%self.id_distributor.get())
                
                row = cur.fetchone()
                
                self.id_distributor.set(row[0])
                self.alamat_distributor.set(row[1])
  
                sqlCon.commit()
                
            except: 
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found")
                Reset()
                
            sqlCon.close()
            
        # Label Frame
        self.lbltitle=Label(TitleFrame, font=('arial', 40, 'bold'), text= "Toko Komputer", bd=7)
        self.lbltitle.grid(row=0, column=0,padx=132)
            
        self.lblid_distributor=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Kode distributor', bd =7)
        self.lblid_distributor.grid(row=1, column=0, padx= 5)
        self.entid_distributor=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.id_distributor)
        self.entid_distributor.grid(row=1,column=1,sticky=W,padx=5)
            
        self.lblalamat_distributor=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'alamat_distributor', bd =7)
        self.lblalamat_distributor.grid(row=2, column=0, padx= 5)
        self.entalamat_distributor=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.alamat_distributor)
        self.entalamat_distributor.grid(row=2,column=1,sticky=W,padx=5)
        
        # Table Treeview
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        
        self.distributor_records=ttk.Treeview(LeftFrame, height=14, columns=("id_distributor", "alamat_distributor"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.distributor_records.heading("id_distributor",text = "Kode distributor")
        self.distributor_records.heading("alamat_distributor", text = "alamat_distributor")
        
        self.distributor_records['show']='headings'
        
        self.distributor_records.column("id_distributor", width = 70)
        self.distributor_records.column("alamat_distributor", width = 100)
        
        self.distributor_records.pack(fill = BOTH, expand=1)
        self.distributor_records.bind("<ButtonRelease-1>", distributorInfo)
        
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
