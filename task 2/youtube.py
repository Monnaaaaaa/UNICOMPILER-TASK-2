from cgitb import text
from dataclasses import Field
from tkinter import *
from tkinter.font import BOLD
from tkinter import filedialog, messagebox
from pytube import YouTube,Playlist
import os

#Functionality Part--------------
def download():
    got_path=filedialog.askdirectory()
    link_url=text.get() #link text will be stored
    if check.get()==1 and check1.get()==3:

        yt=YouTube(link_url)
        yt.streams.get_lowest_resolution().download(got_path)
        messagebox.showinfo("Success",'Downloaded successfully')
        os.startfile(got_path)
    if check.get()==1 and check1.get()==4:
        yt=YouTube(link_url)
        yt.streams.get_highest_resolution().download(got_path)
        messagebox.showinfo("Success",'Downloaded successfully')
        os.startfile(got_path)

    if check.get()==2 and check1.get()==3:
        yt_playlist=Playlist(link_url)      #playlist class imported from pytube
        for videos in yt_playlist.videos:
            videos.streams.get_lowest_resolution().download(got_path)
        messagebox.showinfo("Success",'Downloaded the playlist successfully')
        os.startfile(got_path)

    if check.get()==2 and check1.get()==4:
        yt_playlist=Playlist(link_url)      #playlist class imported from pytube
        for videos in yt_playlist.videos:
            videos.streams.get_highest_resolution().download(got_path)
        messagebox.showinfo("Success",'Downloaded the playlist successfully')
        os.startfile(got_path)





#GUI PART--------
root = Tk()
root.title('Youtube Downloader')
root.config(bg='red3')
outerframe=Frame(root)
outerframe.grid(row=0,column=0,pady=30,padx=30)

#logolabel

logoimage =PhotoImage(file='logo.png')

logolabel=Label(outerframe,image=logoimage)
logolabel.grid(row=0,column=0,pady=20)  #grid is the way to display any label or buttons 


innerframe =LabelFrame(outerframe, text='DOWNLOAD',font=('arial black',12,'bold'))
innerframe.grid(row=1,column=0)

#single video
radioImage=PhotoImage(file='video.png')
check=IntVar()
videoradioButton =Radiobutton(innerframe,image=radioImage,text ='Single Video',compound=LEFT,font=('arial black',8,'bold'),relief=SOLID,variable=check,value=1)  #compund used to see image in left hand side of the text
videoradioButton.grid(row=0,column=0,padx=20,pady=20)

#playlist

radioImage1=PhotoImage(file='playlist.png')
videoradioButton1 =Radiobutton(innerframe,image=radioImage1,text ='Playlist',compound=LEFT,font=('arial black',8,'bold'),relief=SOLID,variable=check,value=2)  #compund used to see image in left hand side of the text
videoradioButton1.grid(row=0,column=1,padx=20,pady=20)

#Low resolution button
check1=IntVar()
lr_button= Radiobutton(innerframe,text='Low Resolution',font=('arial',10,BOLD),relief=SOLID, variable=check1,value=3)
lr_button.grid(row=2,column=0, padx=10,pady=10,)


#High resolution button
lr_button= Radiobutton(innerframe,text='High Resolution',font=('arial',10,BOLD),relief=SOLID, variable=check1,value=4)
lr_button.grid(row=2,column=1, padx=10,pady=10)


#Entry() class for field
text= StringVar()
url_entryField=Entry(outerframe,width=60,font=('arial',12,'bold'),justify=CENTER,textvariable=text,fg='gray')
url_entryField.grid(row=2,column=0,padx=20,pady=20)

text.set('Enter URL')

def click(event):
    url_entryField.delete(0,END)
    url_entryField.config(fg='black')
url_entryField.bind('<Button-1>',click)   #bind method used to perform action depending upon mouse click(event)
                                            #<Button-1> shows left click of mouse
#download button 
download_image=PhotoImage(file='download.png')
download_button= Button(outerframe,image=download_image,text='DOWNLOAD',
font=('aerial',14,'bold'),compound=LEFT,relief=SOLID,command=download)
download_button.grid(row=3,column=0,pady=20,)

root.mainloop()
