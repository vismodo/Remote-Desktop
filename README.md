# Python Remote Desktop

Aren't you tired of intructing a person on a call to use their computer? This project gives you a virtual touchpad and a field to type in!

## Prerequisites

* Python 3 (I used Python 3.9.0)
* Two or more computers running Windows / macOS / Linux
* All computers need to be connected to the same network

## Run on Repl.it

* Server Script: [![Run on Repl.it](https://repl.it/badge/github/vismodo/Remote-Desktop%20Server)](https://repl.it/github/vismodo/Remote-Desktop%20Server)
* Client Script: [![Run on Repl.it](https://repl.it/badge/github/vismodo/Remote-Desktop%20Client)](https://repl.it/github/vismodo/Remote-Desktop%20Client)

## Usage

* We first need to install the [`pyautogui`](https://pyautogui.readthedocs.io/en/latest/) module to control the cursor and keyboard. Launch <b>Command Prompt</b> or <b>Terminal</b> and type the following:

```
pip install pyautogui
```

* You now need to download [`server.py`](https://github.com/vismodo/Remote-Desktop/blob/main/server.py) onto one of the computers and [`client.py`](https://github.com/vismodo/Remote-Desktop/blob/main/client.py) to the rest.

* Now run [`server.py`](https://github.com/vismodo/Remote-Desktop/blob/main/server.py) on and note the IP address as well as the port that comes as an alert.

* On the other computers, run [`client.py`](https://github.com/vismodo/Remote-Desktop/blob/main/client.py). When it asks for the <b>Host IP Address and the Port</b>, type the details that you saw in the alert.

* On the computer running [`server.py`](https://github.com/vismodo/Remote-Desktop/blob/main/server.py), you should now see a tkinter window. This window is your virtual touchpad. Click inside the window, and as your cursor moves inside that window, the cursor will move simultaniosly on the client computers!
* You can adjust the window so that the touchpad can reach each end of the client computer. You can use <b>Control + l</b> for left click, <b>Control + r</b> for right click and <b>Control + d</b> for double click. I am working on adding dragging functionality to the touchpad too!

* To type text, click on the <b>'Text'</b> button from the menu of the touchpad. This should bring up a window. Use the text field to enter your text, and click on the <b>'Type Text'</b> button to type the text on the clients, <b>'Delete'</b> for 'backspace' and <b>'Enter'</b> for a new line.

## Authors

[vismodo](https://github.com/vismodo) : [vismaya.atreya@outlook.com](mailto:vismaya.atreya@outlook.com)

## Troubleshooting

1. <h3><b>Lag in the movement of the cursor</b></h3>This happens only if your network connection is unstable or slow.

2. <h3><b>The touchpad takes my complete screen, but it still does not access the clients complete screen</b></h3>Try changing the '2' of line 40 in server.py to a higher number, such as 3 or 4.

In the case that you found any other bugs in the code, create an issue or send an email to [vismaya.atreya@outlook.com](mailto:vismaya.atreya@outlook.com) and I will fix it as soon as possible.
