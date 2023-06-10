'''
NGười viết: Lê THành VInh
MSSV: 2110940
Ngày viết: 19/04/2023
Mô tả: Báo cáo cuối kì: EDA Chess - phần Frame
'''

#  B1: Nạp thư viện
import cv2
import tkinter as tkVinh
import time
from PIL import Image
from tkinter import Canvas
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msgBox

# B2: Hàm khởi tạo Clips cắt Frames
def OpenFile():
    global filepath
    # Hộp thoại Mở thư mục 
    filepath = filedialog.askopenfilename(initialdir = "all", title = "Select a File", filetypes = (("mp4 files", "*.mp4"), ("all files", "*.*")))
    # Hiển thị đường dẫn file video
    txtPath.insert(0, filepath)

# B3: Hàm khởi tạo thư mục lưu Frames
def OpenFolder():
    global folderpath
    # Hộp thoại Mở thư mục 
    folderpath = filedialog.askdirectory()
    # Hiển thị đường dẫn thư mục lưu Frames
    txtFolder.insert(0, folderpath)


# B4: Hàm lưu Frames vào thư mục
def SaveFrames():
    # Mở video
    cap = cv2.VideoCapture(filepath)
    # Kiểm tra video có mở được hay không
    if (cap.isOpened()==False):
        msgBox.showerror("Error", "Không thể mở file video")
    count = 0
    # Đọc video
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Video', frame)
            cv2.imwrite(folderpath + "/frame%d.jpg" % count, frame)
            count += 1
            # Nhấn phím ESC để thoát
            if cv2.waitKey(25) & 0xFF == 27:
                break
        else:
            break
    # Đóng video
    cap.release()
    cv2.destroyAllWindows()

# B5: Hàm chọn thời gian bắt đầu cắt Frames (tính bằng s) lấy từ textbox
def StartCut():
    # Lấy giá trị từ textbox
    txtStart = txtStartCut.get()
    # Hiển thị giá trị
    print(txtStart)

# B6: Hàm chọn thời gian kết thúc cắt Frames (tính bằng s) lấy từ textbox
def EndCut():
    # Lấy giá trị từ textbox
    txtEnd = txtEndCut.get()
    # Hiển thị giá trị
    print(txtEnd)

# B7: Hàm lưu Frames cắt được vào thư mục với thời gian bắt đầu lấy từ txtStartCut và thời gian kết thúc lấy từ txtEndCut
def SaveFramesCut():
    # Mở video
    cap = cv2.VideoCapture(filepath)
    # Kiểm tra video có mở được hay không
    if (cap.isOpened()==False):
        msgBox.showerror("Error", "Không thể mở file video")
    count = 0
    # Đọc video trong khoảng thời gian cắt (khoảng thời gian bắt đầu và kết thúc)
    while (cap.isOpened()):
        star = int(txtStartCut.get())
        end = int(txtEndCut.get())
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Video', frame)
            if count >= star and count <= end:
                cv2.imwrite(folderpath + "/frame%d.jpg" % count, frame)
            count += 1
            # Nhấn phím ESC để thoát
            if cv2.waitKey(25) & 0xFF == 27:
                break
        else:
            break
    # Đóng video
    cap.release()
    cv2.destroyAllWindows()

# B8: Hàm xử lí ảnh lật dọc
def FlipVertical():
    # Mở video
    cap = cv2.VideoCapture(filepath)
    # Kiểm tra video có mở được hay không
    if (cap.isOpened()==False):
        msgBox.showerror("Error", "Không thể mở file video")
    count = 0
    # Đọc video
    while (cap.isOpened()):
        star = int(txtStartCut.get())
        end = int(txtEndCut.get())
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Video', frame)
            if count >= star and count <= end:
                cv2.imwrite(folderpath + "/frame%d.jpg" % count, cv2.flip(frame, 0))
            count += 1
            # Nhấn phím ESC để thoát
            if cv2.waitKey(25) & 0xFF == 27:
                break
        else:
            break
    # Đóng video
    cap.release()
    cv2.destroyAllWindows()

# B9: Hàm xử lí ảnh thêm màu cho ảnh
def AddColor():
    # Mở video
    cap = cv2.VideoCapture(filepath)
    # Kiểm tra video có mở được hay không
    if (cap.isOpened()==False):
        msgBox.showerror("Error", "Không thể mở file video")
    count = 0
    # Đọc video
    while (cap.isOpened()):
        star = int(txtStartCut.get())
        end = int(txtEndCut.get())
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Video', frame)
            if count >= star and count <= end:
                cv2.imwrite(folderpath + "/frame%d.jpg" % count, cv2.cvtColor(frame, cv2.COLOR_BGR2HSV))
            count += 1
            # Nhấn phím ESC để thoát
            if cv2.waitKey(25) & 0xFF == 27:
                break
        else:
            break
    # Đóng video
    cap.release()
    cv2.destroyAllWindows()


# Hàm khởi tạo form
def GUI():
    # Khởi tạo form
    form = tkVinh.Tk()
    # Đặt tiêu đề cho form
    form.title("84 - Lê THành Vinh")
    # Đặt kích thước cho form
    form.geometry("1280x720")
    # Khởi tạo các control trên form
    # Label
    lblPath = tkVinh.Label(form, text="Đường dẫn file video: ")
    lblPath.place(x=10, y=10)
    lblFolder = tkVinh.Label(form, text="Đường dẫn thư mục lưu Frames: ")
    lblFolder.place(x=10, y=40)
    lblStartCut = tkVinh.Label(form, text="Thời gian bắt đầu cắt Frames (Frames): ")
    lblStartCut.place(x=10, y=70)
    lblEndCut = tkVinh.Label(form, text="Thời gian kết thúc cắt Frames (Fames): ")
    lblEndCut.place(x=10, y=100)
    # Button
    btnPath = tkVinh.Button(form, text="Chọn file video", command=OpenFile)
    btnPath.place(x=500, y=10)
    btnFolder = tkVinh.Button(form, text="Chọn thư mục lưu Frames", command=OpenFolder)
    btnFolder.place(x=500, y=40)
    btnSaveFrames = tkVinh.Button(form, text="Lưu Frames All", command=SaveFrames)
    btnSaveFrames.place(x=10, y=130)
    btnSaveFramesCut = tkVinh.Button(form, text="Lưu Frames Cut", command=SaveFramesCut)
    btnSaveFramesCut.place(x=10, y=160)
    btnLatDoc = tkVinh.Button(form, text="Lật dọc các Frames", command=FlipVertical)
    btnLatDoc.place(x=10, y=190)
    btnAddColor = tkVinh.Button(form, text="Thêm màu cho các Frames", command=AddColor)
    btnAddColor.place(x=10, y=220)

    # Textbox
    global txtPath
    txtPath = tkVinh.Entry(form, width=50)
    txtPath.place(x=150, y=10)
    global txtFolder
    txtFolder = tkVinh.Entry(form, width=50)
    txtFolder.place(x=150, y=40)
    global txtStartCut
    txtStartCut = tkVinh.Entry(form, width=50)
    txtStartCut.place(x=150, y=70)
    global txtEndCut
    txtEndCut = tkVinh.Entry(form, width=50)
    txtEndCut.place(x=150, y=100)


    # Hiển thị form
    form.mainloop()


# Hàm chính
if __name__ == "__main__":
    GUI()

    


