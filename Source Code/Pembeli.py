from tkinter import* 
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB: 
        
    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(102 * titlespace + "MySQL Connector")
        self.root.geometry('800x700+300+0')
        self.root.resizable(width=False, height = False)
            
        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg='cadet blue')
        MainFrame.grid()
            
        TitleFrame = Frame (MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row = 0, column =0)
        TopFrame3 = Frame(MainFrame,bd = 5, width = 770, height = 500, relief = RIDGE)
        TopFrame3.grid(row = 1, column=0)
            
        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, bg='cadet blue', relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width =600, height = 180, padx=12, pady=9, relief=RIDGE)
        LeftFrame1.pack(side=TOP)
            
        RightFrame1= Frame(TopFrame3, bd=5, width=100, height= 400, padx=2, bg='cadet blue', relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2,relief=RIDGE)
        RightFrame1a.pack(side=TOP)
            
        #============================================Define Text Variable==================================================================
        id_pelanggan = StringVar()
        nama_pelanggan = StringVar()
        alamat_pelanggan  = StringVar()
        noTelp_pelanggan = StringVar()  
        # ===========================================Functionality============================================================
        def iExit() : 
            iExit = tkinter.messagebox.askyesno("MySQL Condition", "Confirm if you want to exit")     
            if iExit > 0 : 
                root.destroy()
                return
        
        def Reset() : 
            self.entid_pelanggan.delete(0, END)
            self.entnama_pelanggan.delete(0, END)
            self.entalamat_pelanggan.delete(0, END)
            self.entnoTelp_pelanggan.delete(0, END)
            
        def addData() : 
            if id_pelanggan.get() == "" or nama_pelanggan.get() == "": 
                tkinter.messagebox.showerror('Enter Correct Details')
            else: 
                sqlCon = pymysql.connect(host = 'localhost', port = 3307, user = 'root', password = 'Dean642642#',
                                         database = 'tokokomputer')
                cur = sqlCon.cursor()
                cur.execute("insert into pembeli values (%s, %s, %s, %s)",(
                id_pelanggan.get(), 
                nama_pelanggan.get(),
                alamat_pelanggan.get(),
                noTelp_pelanggan.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

        def DisplayData(): 
            sqlCon = pymysql.connect(host = 'localhost', port = 3307, user = 'root', password = 'Dean642642#',
                                         database = 'tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("select * from pembeli")
            result = cur.fetchall()
            if len(result) != 0 : 
                self.pelanggan_records.delete(*self.pelanggan_records.get_children())
                for row in result:
                    self.pelanggan_records.insert('', END,values = row)
                    
                sqlCon.commit()
                sqlCon.close()
        
        def PelangganInfo(ev):
            viewInfo = self.pelanggan_records.focus()
            if viewInfo:
                pembeliData = self.pelanggan_records.item(viewInfo)
                row = pembeliData.get('values', [])
            if row : 
                id_pelanggan.set(row[0]), 
                nama_pelanggan.set(row[1]),
                alamat_pelanggan.set(row[2]),
                noTelp_pelanggan.set(row[3])
                
        def update() : 
            sqlCon = pymysql.connect(host = 'localhost', port = 3307, user = 'root', password = 'Dean642642#',
                                        database = 'tokokomputer')
            cur = sqlCon.cursor()
            cur.execute("update pembeli set nama_pelanggan = %s, alamat_pelanggan = %s, noTelp_pelanggan = %s where id_pelanggan = %s", (
                
                id_pelanggan.get(), 
                nama_pelanggan.get(),
                alamat_pelanggan.get(),
                noTelp_pelanggan.get()
            ))
            
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully")
            
        def deleteDB(): 
            selected_item = self.pelanggan_records.selection()
            if selected_item: 
                self.pelanggan_records.delete(selected_item)
                
                sqlCon = pymysql.connect(host="localhost", port=3307, user="root", password="Dean642642#", database="tokokomputer")
                cur = sqlCon.cursor()
                cur.execute("delete from pembeli where id_pelanggan = %s", id_pelanggan.get())
                
                sqlCon.commit()
                sqlCon.close()
                
                tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")
                
            else : 
                tkinter.messagebox.showinfo("Data Entry Form", "Please select a record to delete")
                
        def searchDB(): 
            try :
                sqlCon = pymysql.connect(host = 'localhost', port = 3307, user = 'root', password = 'Dean642642#',
                                         database = 'tokokomputer')
                cur = sqlCon.cursor()
                cur.execute("select * from pembeli where id_pelanggan=%s"%id_pelanggan.get())
                
                row = cur.fetchone()
                
                id_pelanggan.set(row[0]), 
                nama_pelanggan.set(row[1]),
                alamat_pelanggan.set(row[2]),
                noTelp_pelanggan.set(row[3])
                
                sqlCon.commit()
                
            except: 
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found")
                Reset()
                
            sqlCon.close()
            
        # ===========================================Label Frame==============================================================
        self.lbltitle=Label(TitleFrame, font=('arial', 40, 'bold'), text= "Toko Komputer", bd=7)
        self.lbltitle.grid(row=0, column=0,padx=132)
            
        self.lblid_pelanggan=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Id Pelanggan', bd =7)
        self.lblid_pelanggan.grid(row=1, column=0, padx= 5)
        self.entid_pelanggan=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=id_pelanggan)
        self.entid_pelanggan.grid(row=1,column=1,sticky=W,padx=5)
            
        self.lblnama_pelanggan=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Nama Pelanggan', bd =7)
        self.lblnama_pelanggan.grid(row=2, column=0, padx= 5)
        self.entnama_pelanggan=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=nama_pelanggan)
        self.entnama_pelanggan.grid(row=2,column=1,sticky=W,padx=5)
            
        self.lblalamat_pelanggan=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'Alamat Pelanggan', bd =7)
        self.lblalamat_pelanggan.grid(row=3, column=0, padx= 5)
        self.entalamat_pelanggan=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=alamat_pelanggan)
        self.entalamat_pelanggan.grid(row=3,column=1,sticky=W,padx=5)
            
        self.lblnoTelp_pelanggan=Label(LeftFrame1,font=('arial', 12, 'bold'), text = 'No Telepon', bd =7)
        self.lblnoTelp_pelanggan.grid(row=4, column=0, padx= 5)
        self.entnoTelp_pelanggan=Entry(LeftFrame1,font=('arial', 12, 'bold'), bd=5, width=44,justify='left',textvariable=noTelp_pelanggan)
        self.entnoTelp_pelanggan.grid(row=4,column=1,sticky=W,padx=5)
        
        # ==========================================Table Treeview================================================================================
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        
        self.pelanggan_records=ttk.Treeview(LeftFrame, height=14, columns=("id_pelanggan", "nama_pelanggan","alamat_pelanggan",
                                                                           "noTelp_pelanggan"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.pelanggan_records.heading("id_pelanggan",text = "Id Pelanggan")
        self.pelanggan_records.heading("nama_pelanggan", text = "Nama Pelanggan")
        self.pelanggan_records.heading("alamat_pelanggan", text = "Alamat Pelanggan")
        self.pelanggan_records.heading("noTelp_pelanggan", text = "No Telepon")
        
        self.pelanggan_records['show']='headings'
        
        self.pelanggan_records.column("id_pelanggan", width = 70)
        self.pelanggan_records.column("nama_pelanggan", width = 100)
        self.pelanggan_records.column("alamat_pelanggan", width = 100)
        self.pelanggan_records.column("noTelp_pelanggan", width = 70)
        
        self.pelanggan_records.pack(fill = BOTH, expand=1)
        self.pelanggan_records.bind("<ButtonRelease-1>", PelangganInfo)
        
        # =================================================Button==============================================================================
        self.btnAddNew=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Add New', bd=4,pady=1, padx=24,
                              width=5, height=2, command=addData).grid(row=0,column=0, padx=1)
        
        self.btnDisplay=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Display', bd=4,pady=1, padx=24,
                              width=5, height=2, command=DisplayData).grid(row=1,column=0, padx=1)
        
        self.btnUpdate=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Update', bd=4,pady=1, padx=24,
                              width=5, height=2, command=update).grid(row=2,column=0, padx=1)
        
        self.btnDelete=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Delete', bd=4,pady=1, padx=24,
                              width=5, height=2, command=deleteDB).grid(row=3,column=0, padx=1)
        
        self.btnSearch=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Search', bd=4,pady=1, padx=24,
                              width=5, height=2, command=searchDB).grid(row=4,column=0, padx=1)
        
        self.btnReset=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Reset', bd=4,pady=1, padx=24,
                              width=5, height=2, command = Reset).grid(row=5,column=0, padx=1)
        
        self.btnExit=Button(RightFrame1a, font=('arial', 16, 'bold'), text='Exit', bd=4,pady=1, padx=24,
                              width=5, height=1, command=iExit).grid(row=6,column=0, padx=1)


        
        
if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
        