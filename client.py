#!/usr/bin/env python
# Client.py of 'Remote Desktop'

import pyautogui as pg
import socket

host = input('Host: ')  # as both code is running on same pc
port = int(input('Port: '))  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

message = 'done'
while True:
    try:
        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response
            if data == 'click':
                pg.click(x, y)
            elif data == 'del':
                pg.typewrite(['backspace'])
            elif data.startswith('cde:'):
                pg.write(data.replace('cde:', ''))
            elif data=='rclick':
                pg.click(button='right')
            elif data=='dclick':
                pg.click(clicks=2)
            elif data=='nl':
                pg.typewrite(['enter'])
            else:
                x = int(data.split(' ')[0])
                y = int(data.split(' ')[1])
                pg.moveTo(x, y)  # show in terminal
            message = 'done' # again take input

        client_socket.close()  # close the connection
    except:
        pass
# Created by vismodo: https://github.com/vismodo/
# Email: vismaya.atreya@outlook.com
# Repository: https://github.com/vismodo/Remote-Desktop (Remote Desktop)
# Python Version: 3.9
