import socket
import cv2
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox
import sys
import threading
import time

def rec_n_save():
	size = conn.recv(1024)
	print("Recieved")
	size_str = str(size,encoding="utf-8")
	file_size = int(size_str)
	has_size = 0
	f = open("db_new.png","wb")
	while True:
	    if file_size == has_size:
	        break
	    date = conn.recv(1024)
	    f.write(date)
	    has_size += len(date)
	f.close()

def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args) 
    # 守护 !!!
    t.setDaemon(True) 
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()

def display():
	def check():
		tkinter.messagebox.showinfo('提示', "成功通过了！")
		conn.sendall(bytes("恭喜你通过了！",encoding="utf-8"))
		top.destroy()



	def SHB():
		tkinter.messagebox.showinfo('提示', '他没有通过！')
		conn.sendall(bytes("对不起你没有通过！",encoding="utf-8"))
		top.destroy()

	rec_n_save()
	print('\a')
	top = Toplevel()
	top.geometry('2560x1600')
	top.title("确认界面")

	panel = Label(top)  # initialize image panel
	panel.pack(padx=10, pady=10)
	top.config(cursor="arrow")


	
	img=cv2.imread('db_new.png',1)
	cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
	current_image = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=current_image)


	panel.imgtk = imgtk
	panel.config(image=imgtk)
	btn1 = Button(top, text="通过！", command= check )
	btn1.pack(side="right", fill="y", expand=YES, padx=10, pady=10)
	btn2 = Button(top, text="不通过！", command= SHB )
	btn2.pack(side="left", fill="y", expand=YES, padx=10, pady=10)
	top.mainloop
	time.sleep(3)
	thread_it(display,)




try:
	sk = socket.socket()
	sk.bind(("127.0.0.1",39002))
	sk.listen(5)
except socket.error as msg:
	print(msg)	
	sys.exit(1)
print("Waiting for Connection...")
conn, addr = sk.accept()
root = Tk()
root.geometry('2560x1600')
root.title("欢迎界面")
root.config(cursor="arrow")
panel1 = Label(root,text="welcome",compound=CENTER,justify = CENTER) 
panel1.pack(expand=YES,anchor=N)

thread_it(display,)
	


root.mainloop()









