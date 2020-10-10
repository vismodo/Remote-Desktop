#!/usr/bin/env python
# Server.py of 'Remote Desktop'
import socket # For network connections
import tkinter as tk # To create a graphical user interface
from tkinter.messagebox import showinfo # To give alerts
from random import randint # To pick a random number

def type_box():
    tp_fr = tk.Tk()
    tp_fr.title('Python Remote Keyboard')
    bx_txt = tk.Entry(tp_fr, width=100)
    bx_txt.pack()
    send_but =tk.Button(tp_fr, text="Type Text", command=lambda:conn.send(('cde:'+bx_txt.get()).encode()))
    del_but =tk.Button(tp_fr, text="Delete", command=lambda:conn.send(('del'.encode())))
    nl_but =tk.Button(tp_fr, text="Enter", command=lambda:conn.send(('nl'.encode())))
    del_but.pack()
    send_but.pack()
    nl_but.pack()
    tp_fr.mainloop()
port = random.randint(1000, 10000)
k = tk.Tk()
showinfo('Control Data','Host = '+socket.gethostbyname(socket.gethostname())+'\nPort = '+str(port))
k.destroy()
root = tk.Tk()
root.title('Python Remote Trackpad')
root.geometry('960x540')
global x, y, data
host = socket.gethostname()

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(2)
conn, address = server_socket.accept()
print("Connection from: " + str(address))
x = 10
y = 10
def motion(event):
    x, y = event.x, event.y
    data = conn.recv(1024).decode()
    data = str(x*2)+' '+str(y*2)
    conn.send(data.encode())
root.bind('<Motion>', motion)
print(10)
cde = ''
def a(o):
    conn.send('click'.encode())
def r(o):
    conn.send('rclick'.encode())
def d(o):
    conn.send('dclick'.encode())
root.bind('<Control-l>', a)
root.bind('<Control-r>', r)
root.bind('<Control-d>', d)
menubar = tk.Menu(root)
menubar.add_command(label="Type", command=type_box)
root.config(menu = menubar)
root.mainloop()
# Created by vismodo: https://github.com/vismodo/
# Email: vismaya.atreya@outlook.com
# Repository: https://github.com/vismodo/Remote-Desktop (Remote Desktop)
# Python Version: 3.9
