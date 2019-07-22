# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 00:33:37 2018

@author: SONY
"""

import urllib.request
import sys
from tkinter import *
#import tkinter

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self,master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self,master)
        #reference to the master widget, which is the tk window
        self.master = master
        #with that, we want to then run init_window, which doesn't yet exist
        self.mywindow_init()
    
    #Creation of init_window
    def mywindow_init(self):
        # changing the title of our master widget   
        self.master.title("MyDictionary")
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH,expand=1)
        # creating a button instance
        mybutton=Button(self,text='Search',command=self.client_search)
        mybutton.place(x=190,y=160)
        
        myTextbox = Entry(root,textvariable=mvar)
        myTextbox.place(x=150,y=130)
        
        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")
        edit.add_command(label="Show Text", command=self.showText)


        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)
        
                
    def client_exit(self):
        exit()
        
    def showText(self):
        text = Label(self, text="Hey there good lookin!")   
        text.pack()
    
    def client_search(self):
        try:
            sw = mvar.get()
            sw=str('define'+'+'+sw)
            sw=sw.replace(' ','+')
            url=str('https://www.google.com/search?q='+str(sw))
            head = {}
            head['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req=urllib.request.Request(url,headers=head)
            resp=urllib.request.urlopen(req)
            reqdata=resp.read()
            defop=str(reqdata).split('dfn',1)[1].split('span',3)[1].replace('>',' ').rstrip('</')
            mlabel=Label(root,text=defop).pack()
        except Exception as e:
            errortext='Sorry! Cannot find this word in my diectionary!! Try again...'
            mlabel=Label(root,text=errortext).pack()
            
 # root window created. Here, that would be the only window, but
# you can later have windows within windows.       
root = Tk()
root.geometry("400x350")
mvar=StringVar()
#creation of an instance
app = Window(root)
root.mainloop()