# from tkinter import * #Thêm thư viện Tkinter
# win = Tk() #Tạo cửa sổ chính của Tk
# win.title("Ví dụ của SpinBox") # đặt tiêu đề cho cửa sổ
# win.geometry("300x200") #Đặt kích thước của cửa sổ
# w = Label(win, text ='Nhóm 13 K21406', fg="navy blue",font = "50")
# #sử dụng widget Label để hiển thị thông báo, fg: màu của foreground
# w.pack() #phương thức pack để tổ chức widget theo khối
# sp = Spinbox(win, from_= 0, to = 62) #Sử dụng widget SpinBox chọn từ 0 đến 50
# sp.pack()
# win.mainloop() #Gọi vòng lặp vô tận để hiện thị cửa sổ

# from tkinter import *  #Thêm thư viện Tkinter
# window = Tk()  #Tạo cửa sổ chính của Tk
# window.title("Ví dụ PanedWindow")  # Thêm tiêu đề cho cửa sổ
# window.geometry("300x200")  #Đặt kích thước của cửa sổ
# pane = PanedWindow(window, orient=VERTICAL) #Tạo paned( khung giao diện ), dùng tùy chọn orient để đặt các cửa sổ con theo hướng từ trên xuống dưới.
# pane.pack(fill=BOTH, expand=True) #fill=both sẽ giãn widget ra theo chiều ngang và rộng, tức là chiếm toàn bộ không gian cửa sổ, expand=1 lấp đầy cửa sổ
# # Thêm một số Label widget trên panedwindow
# row1 = Label(pane, text="Nhãn 1", bg="forest green") #Chỉ định màu nền cho widget
# pane.add(row1)
# row2 = Label(pane, text="Nhãn 2", bg="orange red")
# pane.add(row2)
# row3 = Label(pane, text="Nhãn 3", bg="RoyalBlue2")
# pane.add(row3)
# window.mainloop()#Gọi vòng lặp vô tận để hiện thị cửa sổ

from tkinter import *    #Thêm thư viện Tkinter
win = Tk()  #Tạo cửa sổ chính của Tk
win.title("Ví dụ của LabelFrame")
win.geometry("300x200")  #Đặt kích thước của cửa sổ
labelframe = LabelFrame(win, text="K21406") # sử dụng widget labelframe tạo đường viền cho nội dung trong Label dưới
labelframe.pack(fill="both", expand="yes")
 #fill=both sẽ giãn widget ra theo chiều ngang và rộng, tức là chiếm toàn bộ không gian cửa sổ, expand=”yes”, khi được đặt “yes” widget sẽ mở rộng để lấp đầy bất kỳ khoảng trống nào.
label = Label(labelframe, text="Nhóm 13")
label.pack()  #phương thức pack() để tổ chức widget theo khối

win.mainloop()  #Gọi vòng lặp vô tận để hiện thị cửa sổ

from tkinter import *  #Thêm thư viện Tkinter
from tkinter import messagebox #Thêm module messagebox từ thư viện Tkinter
win = Tk()  #Tạo cửa sổ chính của Tk
win.title("Ví dụ của MessageBox")
win.geometry("200x200")  #Đặt kích thước của cửa sổ
messagebox.showwarning("Cảnh báo!","Đây là một cảnh báo") #sử dụng widget messagebox() để hiển thị thông báo
win.mainloop()  #Gọi vòng lặp vô tận để hiện thị cửa sổ



