from tkinter import *
import cv2
from PIL import Image,ImageTk
import socket
import os
import tkinter.messagebox

def show():

	def photo():
		camera = cv2.VideoCapture(0)    #摄像头
		success,img = camera.read()  # 从摄像头读取照片
		if success:
			cv2.imwrite('/Users/Bonds/Desktop/project/'+'0.png',img)
			tkinter.messagebox.showinfo('提示', "Already Sent!")
			top.destroy()
			transfer()
			



	def transfer():

		size = os.stat("0.png").st_size
		obj.sendall(bytes(str(size),encoding="utf-8"))

		with open("0.png","rb") as f:
			for line in f:
				obj.sendall(line)

		ret_bytes1 = obj.recv(1024)
		ret_str1 = str(ret_bytes1,encoding="utf-8")
		tkinter.messagebox.showinfo('提示', ret_str1)

	def back():
		top.destroy()

	def video_loop():
		success, img = camera.read()  # 从摄像头读取照片
		if success:
			cv2.waitKey(1)
			cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)#转换颜色从BGR到RGBA
			current_image = Image.fromarray(cv2image)#将图像转换成Image对象
			imgtk = ImageTk.PhotoImage(image=current_image)
			panel.imgtk = imgtk
			panel.config(image=imgtk)
			root.after(1, video_loop)


	camera = cv2.VideoCapture(0)    #摄像头

	top = Toplevel()
	top.geometry('2560x1600')
	top.title("拍照界面")

	panel = Label(top)  # initialize image panel
	panel.pack(padx=10, pady=10)
	top.config(cursor="arrow")

	video_loop()
	btn3 = Button(top, text="拍照", command= photo )
	btn3.pack(side="right", fill="none", expand=YES, padx=10, pady=10)
	btn4 = Button(top, text="返回", command= back )
	btn4.pack(side="left", fill="none", expand=YES, padx=10, pady=10)
	






	top.mainloop()
	# 当一切都完成后，关闭摄像头并释放所占资源

	camera.release()
	cv2.destroyAllWindows()

obj = socket.socket()
obj.connect(("127.0.0.1",39002))



root = Tk()
root.title("选择界面")
root.geometry("2560x1600")
root.config(cursor="arrow")
panel1 = Label(root,text="请问您要找？",compound=CENTER,justify = CENTER)  
panel1.pack(expand=YES,anchor=N)
btn1 = Button(root, text="ABC", command= show )
btn1.pack(side="right", fill="none", expand=YES, padx=10, pady=10)
btn2 = Button(root, text="BCD", command= show )
btn2.pack(side="left", fill="none", expand=YES, padx=10, pady=10)
root.mainloop()












