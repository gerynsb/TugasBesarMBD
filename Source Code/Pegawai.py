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
        self.id_pegawai = StringVar()
        self.nama_pegawai = StringVar()
        self.alamat  = StringVar()
        self.noTelp_pegawai = StringVar()
        self.jabatan = StringVar()
        self.gaji = StringVar()
        
        # Functionality
        def iExit():
            iExit = tkinter.messagebox.askyesno("MySQL Conntion", "Confirm if you want to exit")     
            if iExit > 0 : 
                root.destroy()
                return
        
        def Reset() : 
            self.id_pegawai.set("")
            self.nama_pegawai.set("")
            self.alamat.set("")
            self.noTelp_pegawai.set("")
            self.jabatan.set("")
            self.gaji.set("")
            
        def addData():
            if self.id_pegawai.get() == "" or self.nama_pegawai.get() == "":
                tkinter.messagebox.showerror('Enter Correct Details')
            else:
                try:
                    sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokopegawai')
                    cur = sqlCon.cursor()
                    cur.execute("insert into pegawai values (%s, %s, %s, %s, %s)", (
                        self.id_pegawai.get(),
                        self.nama_pegawai.get(),
                        self.alamat.get(),
                        self.noTelp_pegawai.get(),
                        self.jabatan.get(),
                        self.gaji.get()
                    ))
                    sqlCon.commit()
                    sqlCon.close()
                    tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")
                    
                except pymysql.IntegrityError as e:
                    tkinter.messagebox.showerror("Data Entry Form", f"Failed to add record: {e}")

        def DisplayData(): 
            sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("select * from pegawai")
            result = cur.fetchall()
            if len(result) != 0 : 
                self.pegawai_records.delete(*self.pegawai_records.get_children())
                for row in result:
                    self.pegawai_records.insert('', END,values = row)
                    
                sqlCon.commit()
                sqlCon.close()
        
        def pegawaiInfo(ev):
            viewInfo = self.pegawai_records.focus()
            if viewInfo:
                pegawaiData = self.pegawai_records.item(viewInfo)
                row = pegawaiData.get('values', [])
            if row : 
                self.id_pegawai.set(row[0])
                self.nama_pegawai.set(row[1])
                self.alamat.set(row[2])
                self.noTelp_pegawai.set(row[3])
                self.jabatan.set(row[4])
                self.gaji.set(row[5])
                
        def update() : 
            sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("update pegawai set nama_pegawai = %s, alamat = %s, noTelp_pegawai = %s, jabatan = %s, gaji = %s where id_pegawai = %s", (
                
                self.nama_pegawai.get(),
                self.alamat.get(),
                self.noTelp_pegawai.get(),
                self.jabatan.get(),
                self.gaji.get(),
                self.id_pegawai.get()
            ))
            
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully")
            
        def deleteDB(): 
            selected_item = self.pegawai_records.selection()
            if selected_item: 
                self.pegawai_records.delete(selected_item)
                
                sqlCon = pymysql.connect(host="localhost", port=3307, user="root", password="Dean642642#", database="tokokomputer")
                cur = sqlCon.cursor()
                cur.execute("delete from pegawai where id_pegawai = %s", self.id_pegawai.get())
                
                sqlCon.commit()
                sqlCon.close()
                
                tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")
                
            else : 
                tkinter.messagebox.showinfo("Data Entry Form", "Please select a record to delete")
                
        def searchDB(): 
            try :
                sqlCon = pymysql.connect(host='localhost', port=3307, user='root', password='Dean642642#', database='tokokomputer')
                cur = sqlCon.cursor()
                cur.execute("select * from pegawai where id_pegawai=%s"%self.id_pegawai.get())
                
                row = cur.fetchone()
                
                self.id_pegawai.set(row[0])
                self.nama_pegawai.set(row[1])
                self.alamat.set(row[2])
                self.noTelp_pegawai.set(row[3])
                self.jabatan.set(row[3])
                self.gaji.set(row[4])
  
                sqlCon.commit()
                
            except: 
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found")
                Reset()
                
            sqlCon.close()
            
        # Label Frame
        self.lbltitle=Label(TitleFrame, font=('arial', 40, 'bold'), text= "Toko Komputer", bd=7)
        self.lbltitle.grid(row=0, column=0,padx=132)
            
        self.lblid_pegawai=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Id pegawai', bd =7)
        self.lblid_pegawai.grid(row=1, column=0, padx= 5)
        self.entid_pegawai=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.id_pegawai)
        self.entid_pegawai.grid(row=1,column=1,sticky=W,padx=5)
            
        self.lblnama_pegawai=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Nama Pegawai', bd =7)
        self.lblnama_pegawai.grid(row=2, column=0, padx= 5)
        self.entnama_pegawai=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.nama_pegawai)
        self.entnama_pegawai.grid(row=2,column=1,sticky=W,padx=5)
            
        self.lblalamat=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Alamat Pegawai', bd =7)
        self.lblalamat.grid(row=3, column=0, padx= 5)
        self.entalamat=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.alamat)
        self.entalamat.grid(row=3,column=1,sticky=W,padx=5)
        
        self.lblnoTelp_pegawai = Label(LeftFrame1, font=('arial', 12, 'bold'), text = 'Telp Pegawai', bd=7)
        self.lblnoTelp_pegawai.grid(row=4, column=0, padx= 5)
        self.entnoTelp_pegawai=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.noTelp_pegawai)
        self.entnoTelp_pegawai.grid(row=4,column=1,sticky=W,padx=5)
        
        self.lbljabatan = Label(LeftFrame1, font=('arial', 12, 'bold'), text = 'Jabatan Pegawai', bd=7)
        self.lbljabatan.grid(row=5, column=0, padx= 5)
        self.entjabatan=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.jabatan)
        self.entjabatan.grid(row=5,column=1,sticky=W,padx=5)
        
        self.lblgaji = Label(LeftFrame1, font=('arial', 12, 'bold'), text = 'Gaji Pegawai', bd=7)
        self.lblgaji.grid(row=5, column=0, padx= 5)
        self.entgaji=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=self.gaji)
        self.entgaji.grid(row=5,column=1,sticky=W,padx=5)
        
        # Table Treeview
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        
        self.pegawai_records=ttk.Treeview(LeftFrame, height=14, columns=("id_pegawai", "nama_pegawai","alamat", "noTelp_pegawai", "jabatan", "gaji"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.pegawai_records.heading("id_pegawai",text = "id_pegawai pegawai")
        self.pegawai_records.heading("nama_pegawai", text = "Tahun Rilis")
        self.pegawai_records.heading("alamat", text = "alamat pegawai")
        self.pegawai_records.heading("noTelp_pegawai", text = "noTelp_pegawai pegawai")
        self.pegawai_records.heading("jabatan", text = "jabatan pegawai")
        self.pegawai_records.heading("gaji", text = "gaji pegawai")
        
        self.pegawai_records['show']='headings'
        
        self.pegawai_records.column("id_pegawai", width = 70)
        self.pegawai_records.column("nama_pegawai", width = 100)
        self.pegawai_records.column("alamat", width = 100)
        self.pegawai_records.column("noTelp_pegawai", width = 70)
        self.pegawai_records.column("jabatan", width = 70)
        self.pegawai_records.column("gaji", width = 70)
        
        self.pegawai_records.pack(fill = BOTH, expand=1)
        self.pegawai_records.bind("<ButtonRelease-1>", pegawaiInfo)
        
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
