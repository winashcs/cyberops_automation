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
        self.root.after(25, self.animate)         

        #creating selection interface for the user to select from various options   
        frame2=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame2.place(x=0,y=326,width=1366,height=379)   
        frame2_1=LabelFrame(frame2,bd=2,relief=RIDGE,bg='white')
        frame2_1.place(x=5,y=12,width=620,height=350)    
        
        #creating interface for the user to display the selected function
        frame2_2=LabelFrame(frame2,bd=2,relief=RIDGE,bg='white')
        frame2_2.place(x=735,y=12,width=620,height=350)    
       
#this code initializes a tkinter application
#creates an instance of the CA class, and starts the main event loop for GUI interaction.
if __name__=="__main__":
    root=Tk()
    obj=CA(root)
    root.mainloop()
        