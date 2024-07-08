from tkinter import* #for creating graphic user interface
from tkinter import ttk  #(themed tk) we use ttk for modern widgets like buttons, labels, and other GUI elements
from PIL import Image,ImageTk #helps for image processing in gui
from tkinter import messagebox #for displaying messages

class CA: #i used CA here to represent CyberOps Automation
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0') #This is my screen resolution
        self.root.title('CyberOps Automation') 
        self.root.iconbitmap('images/icon.ico')        
        
        #Title and logos
        title=Label(self.root,text='CyberOps  Automation',font=('Lucida Handwriting',70,'bold'),bg='#1178bd',fg='#ffd414')
        title.place(x=0,y=0,width=1366,height=130)        
        
        #for imporving the overall design of gui we use some images
        self.frame1 = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        self.frame1.place(x=0, y=130, width=1366, height=196)
        self.images = ['images/1.jpg','images/2.jpg','images/3.jpg','images/4.jpg','images/5.jpg','images/6.jpg','images/7.jpg','images/logo.png']
        self.image_labels = []
        self.load_images()
        self.animate()
    def load_images(self):
        self.image_objects = []
        for idx, img_path in enumerate(self.images):
            image = Image.open(img_path)
            image = image.resize((196, 196), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            label = Label(self.frame1, image=photo)
            label.image = photo
            label.place(x=idx * 196, y=0, width=196, height=196)
            self.image_labels.append(label)
            self.image_objects.append((label, photo, idx * 196))
    def animate(self):
        for idx, (label, photo, current_x) in enumerate(self.image_objects):
            new_x = current_x - 1
            label.place_configure(x=new_x)
            self.image_objects[idx] = (label, photo, new_x)
            if new_x <= -196: 
                label.place_configure(x=1366) 
                self.image_objects[idx] = (label, photo, 1366)  
        self.root.after(10, self.animate)         
        """
        #creating various input fields for the user to enter        
        frame2=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame2.place(x=10,y=200,width=1336,height=495)        
        frame2_1=LabelFrame(frame2,bd=2,relief=RIDGE,text='Cybersecurity Alerts',font=("Garamond",15,'bold'),fg='dark green',bg='white')
        frame2_1.place(x=10,y=10,width=1316,height=238)        
        b1=Label(frame2_1,text='Case ID :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b1.grid(row=0,column=0,padx=2,sticky=W,pady=2)
        b11=ttk.Entry(frame2_1,textvariable=self.var_case_id,width=20,font=("Times New Roman",10,'bold'))        
        b11.grid(row=0,column=1,padx=2,sticky=W,pady=2)        
        b2=Label(frame2_1,text='Victim Name :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b2.grid(row=1,column=0,padx=2,sticky=W,pady=2)
        b22=ttk.Entry(frame2_1,textvariable=self.var_victim_name,width=20,font=("Times New Roman",10,'bold'))        
        b22.grid(row=1,column=1,padx=2,sticky=W,pady=2)      
        b3=Label(frame2_1,text='Victim Gender :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b3.grid(row=2,column=0,padx=2,sticky=W,pady=2)
        frame3_1=Frame(frame2_1,bd=1,relief=RIDGE,bg='white',highlightbackground="grey", highlightthickness=1)
        frame3_1.place(x=120,y=56,width=146,height=30)
        b33_male=Radiobutton(frame3_1,variable=self.var_victim_gender,text='M',value='male',font=("Arial",10,'bold'),bg='white')
        b33_male.grid(row=0,column=0,pady=0,padx=10,sticky=W)
        b33_female=Radiobutton(frame3_1,variable=self.var_victim_gender,text='F',value='female',font=("Arial",10,'bold'),bg='white')
        b33_female.grid(row=0,column=1,pady=0,padx=10,sticky=W)        
        b4=Label(frame2_1,text='Victim Details :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b4.grid(row=3,column=0,padx=2,sticky=W,pady=10)
        b44=ttk.Entry(frame2_1,textvariable=self.var_victim_details,width=20,font=("Times New Roman",10,'bold'))        
        b44.grid(row=3,column=1,padx=2,sticky=W,pady=3)        
        b5=Label(frame2_1,text='Date of incident :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b5.grid(row=4,column=0,padx=2,sticky=W,pady=2)
        def show_calendar(event):
            top = Toplevel(root)
            top.iconbitmap('images/icon.ico')
            cal = Calendar(top, selectmode='day', year=2023, month=1, day=1)
            cal.pack(fill='both', expand=True)            
            def select_date():
                selected_date = cal.get_date()
                b55.configure(state='normal')
                b55.delete(0, END)
                b55.insert(0, selected_date)
                b55.configure(state='readonly') 
                top.destroy()            
            ok_button = ttk.Button(top, text="OK", command=select_date)
            ok_button.pack(pady=10)        
        b55 = ttk.Entry(frame2_1,textvariable=self.var_date_of_incident,width=20, font=("Times New Roman", 10, 'bold'))
        b55.grid(row=4, column=1, padx=2, sticky=W, pady=2)
        b55.bind('<Button-1>', show_calendar)        
        b6=Label(frame2_1,text='Type of cybercrime :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b6.grid(row=0,column=2,padx=2,sticky=W,pady=2)
        b66=ttk.Entry(frame2_1,textvariable=self.var_type_of_cybercrime,width=20,font=("Times New Roman",10,'bold'))
        b66.grid(row=0,column=3,padx=2,sticky=W,pady=2)        
        b7=Label(frame2_1,text='Type of cyberattack :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b7.grid(row=1,column=2,padx=2,sticky=W,pady=2)
        b77=ttk.Entry(frame2_1,textvariable=self.var_type_of_cyberattack,width=20,font=("Times New Roman",10,'bold'))
        b77.grid(row=1,column=3,padx=2,sticky=W,pady=2)        
        b8=Label(frame2_1,text='Impact Assessment :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b8.grid(row=2,column=2,padx=2,sticky=W,pady=2)
        b88=ttk.Entry(frame2_1,textvariable=self.var_impact_assessment,width=20,font=("Times New Roman",10,'bold'))
        b88.grid(row=2,column=3,padx=2,sticky=W,pady=2)        
        b9=Label(frame2_1,text='IP address :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b9.grid(row=3,column=2,padx=2,sticky=W,pady=2)
        b99=ttk.Entry(frame2_1,textvariable=self.var_ip_address,width=20,font=("Times New Roman",10,'bold'))
        b99.grid(row=3,column=3,padx=2,sticky=W,pady=2)
        b10=Label(frame2_1,text='Device Information :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b10.grid(row=4,column=2,padx=2,sticky=W,pady=2)
        b1010=ttk.Entry(frame2_1,textvariable=self.var_device_information,width=20,font=("Times New Roman",10,'bold'))
        b1010.grid(row=4,column=3,padx=2,sticky=W,pady=2)    
        b11=Label(frame2_1,text='Related Incident :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b11.grid(row=0,column=4,padx=2,sticky=W,pady=2)
        b1111=ttk.Entry(frame2_1,textvariable=self.var_related_incident,width=20,font=("Times New Roman",10,'bold'))
        b1111.grid(row=0,column=5,padx=2,sticky=W,pady=2)        
        b12=Label(frame2_1,text='Suspect Name :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b12.grid(row=1,column=4,padx=2,sticky=W,pady=2)
        b1212=ttk.Entry(frame2_1,textvariable=self.var_suspect_name,width=20,font=("Times New Roman",10,'bold'))
        b1212.grid(row=1,column=5,padx=2,sticky=W,pady=2)
        b13=Label(frame2_1,text='Suspect Gender :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b13.grid(row=2,column=4,padx=2,sticky=W,pady=2)
        frame3_2=Frame(frame2_1,bd=1,relief=RIDGE,bg='white',highlightbackground="grey", highlightthickness=1)
        frame3_2.place(x=677,y=56,width=146,height=30)
        b1313_male=Radiobutton(frame3_2,variable=self.var_suspect_gender, text='M',value='Male',font=("Arial",10,'bold'),bg='white')
        b1313_male.grid(row=0,column=0,pady=0,padx=10,sticky=W)
        b1313_female=Radiobutton(frame3_2,variable=self.var_suspect_gender, text='F',value='Female',font=("Arial",10,'bold'),bg='white')
        b1313_female.grid(row=0,column=1,pady=0,padx=10,sticky=W)           
        b14=Label(frame2_1,text='Suspect Details :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b14.grid(row=3,column=4,padx=2,sticky=W,pady=2)
        b1414=ttk.Entry(frame2_1,textvariable=self.var_suspect_details,width=20,font=("Times New Roman",10,'bold'))
        b1414.grid(row=3,column=5,padx=2,sticky=W,pady=2)        
        b15=Label(frame2_1,text='Status :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b15.grid(row=4,column=4,padx=2,sticky=W,pady=2)
        self.var_status = StringVar(frame2_1)
        self.var_status.set("SELECT ▼")
        b1515 = OptionMenu(frame2_1,self.var_status, "ONGOING", "CLOSED", "PENDING")
        b1515.configure(font=("Arial", 8,'bold'), bg='white',highlightthickness=1, highlightbackground='grey',activebackground='white',indicatoron=0)
        b1515['menu'].configure(font=("Times New Roman", 10, 'bold'), bg='white')
        b1515.grid(row=4, column=5, padx=2, pady=2, sticky=W)
        
        #save,update,delete,clear buttons creation        
        bf=Frame(frame2_1,bd=2,relief=RIDGE,bg='white')
        bf.place(x=3,y=160,width=613,height=45)        
        bt1=Button(bf,command=self.save_data,text='SAVE',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt1.grid(row=0,column=0,padx=3,pady=3)
        bt2=Button(bf,command=self.update_data,text='UPDATE',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt2.grid(row=0,column=1,padx=3,pady=3)
        bt3=Button(bf,command=self.delete_data,text='DELETE',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt3.grid(row=0,column=2,padx=3,pady=3)
        bt4=Button(bf,command=self.clear_data,text='CLEAR',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt4.grid(row=0,column=3,padx=3,pady=3)
        
        #an image has been incorporated on the right side of the screen to enhance the GUI and eliminate its vacant appearance
        i4=Image.open('images/i2.jpg')
        i4=i4.resize((472,222), Image.LANCZOS)
        self.i44=ImageTk.PhotoImage(i4)
        self.i444=Label(frame2_1,image=self.i44)
        self.i444.place(x=840,y=-10,width=472,height=222)
        
        #search and display area has been implemented in the GUI to facilitate record retrieval and viewing
        frame2_2=LabelFrame(frame2,bd=2,relief=RIDGE,text='Cybersecurity Alert Dashboard',font=("Garamond",15,'bold'),fg='dark green',bg='white')
        frame2_2.place(x=10,y=248,width=1316,height=238)        
        frame2_2_1=LabelFrame(frame2_2,bd=2,relief=RIDGE,text='Search Record',font=("Lucida Sans Unicode",11,'bold'),fg='black',bg='white')
        frame2_2_1.place(x=0,y=0,width=1306,height=50)
        sb=Label(frame2_2_1,text='Search By',font=("Georgia",10,'bold'),bg='yellow',fg='black')
        sb.grid(row=0,column=0,padx=4,sticky=W)
        
        '''once again two images has been incorporated on the right side 
        of the screen to enhance the GUI and eliminate its vacant appearance'''
        design2=Image.open('images/design2.png')
        design2=design2.resize((200,35), Image.LANCZOS)
        self.design22=ImageTk.PhotoImage(design2)
        self.design222=Label(frame2_2_1,image=self.design22)
        self.design222.place(x=950,y=-8,width=200,height=35)        
        design1=Image.open('images/design1.png')
        design1=design1.resize((40,29), Image.LANCZOS)
        self.design11=ImageTk.PhotoImage(design1)
        self.design111=Label(frame2_2_1,image=self.design11)
        self.design111.place(x=1047,y=-5,width=40,height=29)        
        
        #the search options have been set up, you can search by Case ID, IP address, or status or you can see
        #all the records by using show all button
        self.var_1_search=StringVar()        
        dd1=ttk.Combobox(frame2_2_1,textvariable=self.var_1_search,font=("Georgia",9,'bold'),width=17,state='readonly')
        dd1['value']=('Select Option','Case_ID','IP_address','Status')
        dd1.current(0)
        dd1.grid(row=0,column=1,padx=4,sticky=W)        
        self.var_2_search=StringVar()
        searchtxt=ttk.Entry(frame2_2_1,textvariable=self.var_2_search,width=17,font=("Georgia",9,'bold'))
        searchtxt.grid(row=0,column=2,padx=4,sticky=W)        
        searchbn=Button(frame2_2_1,command=self.search_data,text='SEARCH',font=("Georgia",9,'bold'),bg='#fee01c',width=17,fg='black')
        searchbn.grid(row=0,column=3,padx=4,sticky=W)        
        all1=Button(frame2_2_1,command=self.get_data,text='SHOW ALL',font=("Georgia",9,'bold'),bg='#fee01c',width=17,fg='black')
        all1.grid(row=0,column=4,padx=4,sticky=W)
        
        #a table area has been set up to display records
        #in case of numerous records, scroll bars are available for navigation      
        table_frame=Frame(frame2_2,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=50,width=1306,height=162)     
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)        
        self.details_table=ttk.Treeview(table_frame,column=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)        
        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)
        
        #various column names have been designated for the table, each with appropriate widths specified
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Ebrima',10,'bold'))        
        self.details_table.heading('1',text='Case ID')
        self.details_table.heading('2',text='Victim Name')
        self.details_table.heading('3',text='Victim Gender')
        self.details_table.heading('4',text='Victim Details')
        self.details_table.heading('5',text='Date of incident')
        self.details_table.heading('6',text='Type of cybercrime')
        self.details_table.heading('7',text='Type of cyberattack')
        self.details_table.heading('8',text='Impact Assessment')
        self.details_table.heading('9',text='IP address')
        self.details_table.heading('10',text='Device Information')
        self.details_table.heading('11',text='Related Incident')
        self.details_table.heading('12',text='Suspect Name')
        self.details_table.heading('13',text='Suspect Gender')
        self.details_table.heading('14',text='Suspect Details')
        self.details_table.heading('15',text='Status')        
        self.details_table['show']='headings'        
        self.details_table.column('1',width=75)
        self.details_table.column('2',width=150)
        self.details_table.column('3',width=110)
        self.details_table.column('4',width=220)
        self.details_table.column('5',width=135)
        self.details_table.column('6',width=160)
        self.details_table.column('7',width=150)
        self.details_table.column('8',width=150)
        self.details_table.column('9',width=130)
        self.details_table.column('10',width=160)
        self.details_table.column('11',width=135)
        self.details_table.column('12',width=150)
        self.details_table.column('13',width=130)
        self.details_table.column('14',width=220)
        self.details_table.column('15',width=75)        
        self.details_table.pack(fill=BOTH,expand=1)
            
        #get_cursor method is implemented for retrieving and displaying selected row data
        #get_data method is implemented here for fetching all records
        self.details_table.bind("<ButtonRelease>",self.get_cursor)        
        self.get_data()
        
    #this function is created to save cybersecurity incident data 
    #to a SQLite database after validation, showing errors or success messages accordingly 
    def save_data(self):
        if self.var_case_id.get() == "" or self.var_victim_name.get() == "" or \
           self.var_victim_gender.get() == "" or self.var_victim_details.get() == "" or \
           self.var_date_of_incident.get() == "" or self.var_type_of_cybercrime.get() == "" or \
           self.var_type_of_cyberattack.get() == "" or self.var_impact_assessment.get() == "" or \
           self.var_ip_address.get() == "" or self.var_device_information.get() == "" or \
           self.var_related_incident.get() == "" or self.var_suspect_name.get() == "" or \
           self.var_suspect_gender.get() == "" or self.var_suspect_details.get() == "" or \
           self.var_status.get() == "SELECT ▼":
            messagebox.showerror('Error', 'ALL ENTRIES ARE MANDATORY')
        else:
            try:
                self.cursor.execute('''
                    INSERT INTO cybersecurity (Case_ID, Victim_Name, Victim_Gender, Victim_Details, 
                                              Date_of_incident, Type_of_cybercrime, Type_of_cyberattack, 
                                              Impact_Assessment, IP_Address, Device_Information, Related_Incident, 
                                              Suspect_Name, Suspect_Gender, Suspect_Details, Status) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                                   (self.var_case_id.get(), self.var_victim_name.get(), self.var_victim_gender.get(),
                                    self.var_victim_details.get(), self.var_date_of_incident.get(),
                                    self.var_type_of_cybercrime.get(), self.var_type_of_cyberattack.get(),
                                    self.var_impact_assessment.get(), self.var_ip_address.get(),
                                    self.var_device_information.get(), self.var_related_incident.get(),
                                    self.var_suspect_name.get(), self.var_suspect_gender.get(),
                                    self.var_suspect_details.get(), self.var_status.get()))
                self.con.commit()
                self.get_data()
                self.clear_data()
                messagebox.showinfo('Success', 'CYBERSECURITY ALERT SUCCESSFULLY DEPLOYED')
            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')
                
    #this function is created for fetching all the data from SQLite
    def get_data(self):
        self.cursor.execute('SELECT * FROM cybersecurity')
        data = self.cursor.fetchall()
        if len(data) != 0:
            self.details_table.delete(*self.details_table.get_children())
            for row in data:
                self.details_table.insert('', END, values=row)
            self.con.commit()
        
    #this function retrieves and displays data from a selected row in table widget and also
    #setting corresponding entry fields for editing or viewing purposes.    
    def get_cursor(self,event=""):
        cursor_row=self.details_table.focus()
        content=self.details_table.item(cursor_row)
        data=content['values']
        self.var_case_id.set(data[0])
        self.var_victim_name.set(data[1])
        self.var_victim_gender.set(data[2])
        self.var_victim_details.set(data[3])
        self.var_date_of_incident.set(data[4])
        self.var_type_of_cybercrime.set(data[5])
        self.var_type_of_cyberattack.set(data[6])
        self.var_impact_assessment.set(data[7])
        self.var_ip_address.set(data[8])
        self.var_device_information.set(data[9])
        self.var_related_incident.set(data[10])
        self.var_suspect_name.set(data[11])
        self.var_suspect_gender.set(data[12])
        self.var_suspect_details.set(data[13])
        self.var_status.set(data[14])
        
    #this function updates data in SQLite after validation, 
    #confirming with the user before executing and displaying appropriate messages for success or errors.
    def update_data(self):
        if (self.var_case_id.get() == "" or self.var_victim_name.get() == "" or
            self.var_victim_gender.get() == "" or self.var_victim_details.get() == "" or
            self.var_date_of_incident.get() == "" or self.var_type_of_cybercrime.get() == "" or
            self.var_type_of_cyberattack.get() == "" or self.var_impact_assessment.get() == "" or
            self.var_ip_address.get() == "" or self.var_device_information.get() == "" or
            self.var_related_incident.get() == "" or self.var_suspect_name.get() == "" or
            self.var_suspect_gender.get() == "" or self.var_suspect_details.get() == "" or
            self.var_status.get() == "SELECT ▼"):
            messagebox.showerror('Error', 'ALL ENTRIES ARE MANDATORY')
        else:
            try:            
                case_id = self.var_case_id.get()
                self.cursor.execute('SELECT * FROM cybersecurity WHERE Case_ID=?', (case_id,))
                data = self.cursor.fetchone()
                if data is None:
                    messagebox.showerror('Error', 'Case ID does not exist. Please enter a valid Case ID.')
                else:                    
                    update = messagebox.askyesno('Update', 'Would you like to confirm UPDATING this record?')
                    if update:                      
                        self.cursor.execute('''
                            UPDATE cybersecurity SET Victim_Name=?, Victim_Gender=?, Victim_Details=?, 
                            Date_of_incident=?, Type_of_cybercrime=?, Type_of_cyberattack=?, Impact_Assessment=?, 
                            IP_Address=?, Device_Information=?, Related_Incident=?, Suspect_Name=?, Suspect_Gender=?, 
                            Suspect_Details=?, Status=?
                            WHERE Case_ID=?''',
                            (self.var_victim_name.get(), self.var_victim_gender.get(), self.var_victim_details.get(),
                            self.var_date_of_incident.get(), self.var_type_of_cybercrime.get(),
                            self.var_type_of_cyberattack.get(), self.var_impact_assessment.get(), self.var_ip_address.get(),
                            self.var_device_information.get(), self.var_related_incident.get(), self.var_suspect_name.get(),
                            self.var_suspect_gender.get(), self.var_suspect_details.get(), self.var_status.get(),
                            case_id))
                        self.con.commit()                        
                        print(f"Record with Case ID '{case_id}' updated successfully.")                        
                        self.get_data()                        
                        self.clear_data()                        
                        messagebox.showinfo('Success', 'Record updated successfully')
            except Exception as es:
                messagebox.showerror('Error', f'Error updating record: {str(es)}')
                      
    #this function deletes a SQLite record after verifying all necessary fields are filled
    #confirming with the user, it then displays messages indicating success or errors based on the outcome
    def delete_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'Please select a record to delete')
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Confirm DELETION of this record?')
                if delete:
                    self.cursor.execute('DELETE FROM cybersecurity WHERE Case_ID=?', (self.var_case_id.get(),))
                    self.con.commit()
                    self.get_data()
                    self.clear_data()
                    messagebox.showinfo('Success', 'Record deleted successfully')
            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')
     
    #this function is used to clear or reset the input data in entry fields            
    def clear_data(self):
        self.var_case_id.set("")
        self.var_victim_name.set("")
        self.var_victim_gender.set("")
        self.var_victim_details.set("")
        self.var_date_of_incident.set("")
        self.var_type_of_cybercrime.set("")
        self.var_type_of_cyberattack.set("")
        self.var_impact_assessment.set("")
        self.var_ip_address.set("")
        self.var_device_information.set("")
        self.var_related_incident.set("")
        self.var_suspect_name.set("")
        self.var_suspect_gender.set("")
        self.var_suspect_details.set("")
        self.var_status.set("SELECT ▼")
        
    #this function searches a SQLite database using user-specified criteria
    #presenting matching results in a table widget or handling errors as needed.
    def search_data(self):
        if self.var_1_search.get() == "":
            messagebox.showerror('Error', 'ALL ENTRIES ARE MANDATORY')
        else:
            try:
                if self.var_1_search.get() == 'Case_ID':
                    column = 'Case_ID'
                elif self.var_1_search.get() == 'IP_address':
                    column = 'IP_address'
                elif self.var_1_search.get() == 'Status':
                    column = 'Status'
                else:
                    messagebox.showerror('Error', 'Invalid search criteria')
                    return                
                sql = f"SELECT * FROM cybersecurity WHERE {column} LIKE ?"
                self.cursor.execute(sql, ('%' + self.var_2_search.get() + '%',))                
                rows = self.cursor.fetchall()
                if len(rows) != 0:
                    self.details_table.delete(*self.details_table.get_children())
                    for i in rows:
                        self.details_table.insert('', 'end', values=i)
                else:
                    messagebox.showinfo('Info', 'No records found')                
            except Exception as es:
                messagebox.showerror('Error', f'Due to {str(es)}')      """ 
                              
#this code initializes a tkinter application
#creates an instance of the CA class, and starts the main event loop for GUI interaction.
if __name__=="__main__":
    root=Tk()
    obj=CA(root)
    root.mainloop()
        