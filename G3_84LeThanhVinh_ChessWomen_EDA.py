'''
NGười viết: Lê THành VInh
MSSV: 2110940
Ngày viết: 19/04/2023
Mô tả: Báo cáo cuối kì: EDA Chess - phần EDA
'''
# B1: NẠP THƯ VIỆN
    # Speech
import speech_recognition as vinh84
from gtts import gTTS
import playsound
import re

    # tkinter
import tkinter as tkVinh
from tkinter import messagebox
from tkinter import ttk, filedialog
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns


    # thư viện OS (lập thư mục, files)
import os  # THƯ VIỆN OS MS. WINDOWS = Lập thư mục & lưu file

   # Nạp các thư viện cần thiết EDA
import numpy as np #Numeric Python: Thư viện về Đại số tuyến tính tính
import pandas as pd #Python Analytic on Data System: For data processing (Thư viện xử lý dữ liệu)
from scipy import stats # thư viện cung cấp các công cụ thống kê [statistics] sub-lib của science python [các công cụ khoa học] 
from sklearn import preprocessing # Thư viện tiền xử lý DL (XL ngoại lệ: Isolated)
from sklearn.feature_selection import SelectKBest, chi2 # Nạp hàm Thư viện phân tích dữ liệu thăm dò

# # B2: KHAI BÁO TÊN THƯ MỤC & FILE LƯU CÁC THÔNG TIN BÀI LÀM
# LeVinh84_FILE = "LeVinh84.mp3"  # lưu tên  file Input
# LeVinh84_DIR = 'Le_Vinh_84'     # Thư mục lưu các file [trên]

# os.makedirs(LeVinh84_DIR, exist_ok=True)
class EDA:
    def __init__(self, form):
        self.form = form

        self.form.title("Phân tích dữ liệu EDA - Lê Thành Vinh 84")
        self.form.geometry("800x650")
        self.form.resizable(False, False)
        self.form.configure(bg='#90EE90')

        # # Tạo canvas với chiều rộng và chiều cao giống với cửa sổ gốc
        # canvas = tkVinh.Canvas(form, width=800, height=450)
        # canvas.pack()

        # # Load ảnh nền và tạo widget ảnh
        # img = Image.open("Images/EDAform.png")
        # bg_image = ImageTk.PhotoImage(img)
        # canvas.create_image(0, 0, image=bg_image, anchor="nw")
        # canvas.place(relwidth=1, relheight=1)

        self.frame_treeview = tkVinh.Frame(form)
        self.frame_treeview.place(x=20, y=100, width=760, height=300, bordermode='outside')

        # Tạo thanh cuộn ngang bên trên cho treeview
        self.scroll = ttk.Scrollbar(self.frame_treeview, orient='horizontal')
        self.scroll.place(x=0, y=280, width=760, height=20)

        # Tạo treeview
        self.table = ttk.Treeview(self.frame_treeview, xscrollcommand=self.scroll.set, height=10)
        self.table.place(x=0, y=0, width=760, height=280)

        # Thiết lập kết nối giữa thanh cuộn và treeview
        self.scroll.config(command=self.table.xview)       

        # KHởi tạo sẵn treeview
        self.df = pd.read_csv('G3_84LeThanhVinh_ChessWomen.csv')
        self.table.delete(*self.table.get_children())
        self.table["column"] = list(self.df.columns)
        self.table["show"] = "headings"
        for column in self.table["column"]:
            self.table.heading(column, text=column)
        # thêm 20 dòng đầu tiên
        df_rows = self.df.to_numpy().tolist()
        for row in df_rows[:20]:
            self.table.insert("", "end", values=row)

        # Button chọn file
        self.btn_file = tkVinh.Button(form, text='Chọn file',width=10,font= Font(family="Segoe UI", size=12, weight="bold"), command=self.open_file)
        self.btn_file.place(x=10, y=10)

        # Button xử lý cột null
        self.btn_cot_null = tkVinh.Button(form, text='Xử lý cột null',width=15,font= Font(family="Segoe UI", size=12, weight="bold"), command=self.columns_null)
        self.btn_cot_null.place(x=140, y=10)

        # Button xử lý dòng null (NaN)
        self.btn_dong_null = tkVinh.Button(form, text='Xử lý dòng null',width=15,font= Font(family="Segoe UI", size=12, weight="bold"), command=self.rows_null)
        self.btn_dong_null.place(x=300, y=10)

        # Button tạo ma trận z-core
        self.btn_zcore = tkVinh.Button(form, text='z-core',width=15,font= Font(family="Segoe UI", size=12, weight="bold"), command=self.zcore)
        self.btn_zcore.place(x=140, y=50)

        # Button chuẩn hóa (rời rạc hóa)
        self.btn_chuan_hoa = tkVinh.Button(form, text='Chuẩn hóa',width=15,font= Font(family="Segoe UI", size=12, weight="bold"), command=self.chuan_hoa)
        self.btn_chuan_hoa.place(x=300, y=50)

        # Label đồ thị
        self.label_do_thi = tkVinh.Label(form, text='Đồ thị',font= Font(family="Segoe UI", size=12, weight="bold"), bg='#8FBC8F')
        self.label_do_thi.place(x=520, y=10)

        # Button vẽ đồ thị (rời rạc vẽ đồ thị)
        self.btn_histogram = tkVinh.Button(form, text='Histogram',width=7,font= Font(family="Segoe UI", size=8, weight="bold"), command=self.histogram)
        self.btn_histogram.place(x=520, y=50)

        # Button vẽ đồ thị Phân tán
        self.btn_chuan_hoa = tkVinh.Button(form, text='Phân tán',width=7,font= Font(family="Segoe UI", size=8, weight="bold"), command=self.phan_tan)
        self.btn_chuan_hoa.place(x=580, y=50)

        # Button vẽ đồ thị quạt (Pie)
        self.btn_quat = tkVinh.Button(form, text='Pie',width=7,font= Font(family="Segoe UI", size=8, weight="bold"), command=self.pie)
        self.btn_quat.place(x=640, y=50)

        # Button vẽ đồ thị 3D scatter
        self.btn_scatter = tkVinh.Button(form, text='3D Scatter',width=7,font= Font(family="Segoe UI", size=8, weight="bold"), command=self.scatter_3d)
        self.btn_scatter.place(x=700, y=50)

        # Label Voice
        self.label_voice = tkVinh.Label(form, text='Voice',font= Font(family="Segoe UI", size=12, weight="bold"), bg='white')
        self.label_voice.place(x=10, y=420)
        # Label nội dung Voice
        self.label_dung_voice = tkVinh.Label(form, text='1. Mở file \n 2. Xử lý cột null \n 3. Xử lý dòng null \n 4. z-core \n 5. Chuẩn hóa \n 6. Histogram (Biểu đồ) \n 7. Phân tán (Biểu đồ) \n 8. Pie (Biểu đồ) \n 9. 3D Scatter',font= Font(family="Segoe UI", size=12, weight="bold"), bg='#8FBC8F')
        self.label_dung_voice.place(x=100, y=420)

        # Button Voice
        self.btn_voice = tkVinh.Button(form, text='Nói',width=10,font= Font(family="Segoe UI", size=12, weight="bold"), command=self.voice)
        self.btn_voice.place(x=400, y=420)

        # Label nhận diện giọng nói
        self.label_nhan_dien = tkVinh.Label(form, text='Nhận diện giọng nói',font= Font(family="Segoe UI", size=12, weight="bold"), bg='#8FBC8F')
        self.label_nhan_dien.place(x=400, y=460)

        # Button xác nhận giọng nói
        self.btn_nhan_dien = tkVinh.Button(form, text='Xác nhận',width=10,font= Font(family="Segoe UI", size=12, weight="bold"), command=self.submit_voice)
        self.btn_nhan_dien.place(x=400, y=500)

        self.form.mainloop()

    def open_file(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        if filename:
            try:
                filename = r"{}".format(filename)
                df = pd.read_csv(filename)
            except ValueError:
                messagebox.showerror("Thông báo", "File không đúng định dạng")
        
        self.table.delete(*self.table.get_children())
        self.table["column"] = list(df.columns)
        self.table["show"] = "headings"
        for column in self.table["column"]:
            self.table.heading(column, text=column)
        # thêm 20 dòng đầu tiên
        df_rows = df.to_numpy().tolist()
        for row in df_rows[:20]:
            self.table.insert("", "end", values=row)

    def columns_null(self):
        # Xử lý cột null
        df = self.df
        df = df.drop(['Fide id','Name','Federation','Gender','Year_of_birth','Title','Inactive_flag'],axis=1)
        self.table.delete(*self.table.get_children())
        self.table["column"] = list(df.columns)
        self.table["show"] = "headings"
        for column in self.table["column"]:
            self.table.heading(column, text=column)
        # thêm 20 dòng đầu tiên
        df_rows = df.to_numpy().tolist()
        for row in df_rows[:20]:
            self.table.insert("", "end", values=row)

    def rows_null(self):
        # Xử lý dòng null (NaN)
        df = self.df
        df = df.drop(['Fide id','Name','Federation','Gender','Year_of_birth','Title','Inactive_flag'],axis=1)
        df = df.dropna(how='any')
        # Xử lý dòng null (NaN)
        self.table.delete(*self.table.get_children())
        self.table["column"] = list(df.columns)
        self.table["show"] = "headings"
        for column in self.table["column"]:
            self.table.heading(column, text=column)
        # thêm 20 dòng đầu tiên
        df_rows = df.to_numpy().tolist()
        for row in df_rows[:20]:
            self.table.insert("", "end", values=row)

    def zcore(self):
        df = self.df
        df = df.drop(['Fide id','Name','Federation','Gender','Year_of_birth','Title','Inactive_flag'],axis=1)
        df = df.dropna(how='any')

        z = np.abs(stats.zscore(df._get_numeric_data()))
        df = df[(z < 3).all(axis=1)]
        self.table.delete(*self.table.get_children())
        self.table["column"] = list(z.columns)
        self.table["show"] = "headings"
        for column in self.table["column"]:
            self.table.heading(column, text=column)
        # thêm 20 dòng đầu tiên
        z_rows = z.to_numpy().tolist()
        for row in z_rows[:20]:
            self.table.insert("", "end", values=row)

    def chuan_hoa(self):
        df = self.df
        df = df.drop(['Fide id','Name','Federation','Gender','Year_of_birth','Title','Inactive_flag'],axis=1)
        df = df.dropna(how='any')
        scaler = preprocessing.MinMaxScaler()
        scaler.fit(df)
        df = pd.DataFrame(scaler.transform(df), index=df.index, columns=df.columns) 
        self.table.delete(*self.table.get_children())
        self.table["column"] = list(df.columns)
        self.table["show"] = "headings"
        for column in self.table["column"]:
            self.table.heading(column, text=column)
        # thêm 20 dòng đầu tiên
        df_rows = df.to_numpy().tolist()
        for row in df_rows[:20]:
            self.table.insert("", "end", values=row)

    def histogram(self):
        df = self.df
        df = df.drop(['Fide id','Name','Federation','Gender','Year_of_birth','Title','Inactive_flag'],axis=1)
        df = df.dropna(how='any')

        z = np.abs(stats.zscore(df._get_numeric_data()))
        df = df[(z < 3).all(axis=1)]

        # Vẽ biểu đồ phân phối từ z-core
        fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

        sns.distplot(df['Standard_Rating'], ax=axs[0])
        sns.distplot(df['Rapid_rating'], ax=axs[1])
        sns.distplot(df['Blitz_rating'], ax=axs[2])

        plt.subplots_adjust(wspace=0.3)
        plt.show()

    def phan_tan(self):
        df = self.df
        df = df.drop(['Fide id','Name','Federation','Gender','Year_of_birth','Title','Inactive_flag'],axis=1)
        df = df.dropna(how='any')

        z = np.abs(stats.zscore(df._get_numeric_data()))
        df = df[(z < 3).all(axis=1)]

        # Vẽ biểu đồ phân phối từ z-core với scatter
        fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

        sns.scatterplot(x='Standard_Rating', y='Rapid_rating', data=df, ax=axs[0])
        sns.scatterplot(x='Standard_Rating', y='Blitz_rating', data=df, ax=axs[1])
        sns.scatterplot(x='Rapid_rating', y='Blitz_rating', data=df, ax=axs[2])

        plt.subplots_adjust(wspace=0.3)
        plt.show()

    def pie(self):
        df = self.df
        df = df.drop(['Fide id','Name','Federation','Gender','Year_of_birth','Title','Inactive_flag'],axis=1)
        df = df.dropna(how='any')

        z = np.abs(stats.zscore(df._get_numeric_data()))
        df = df[(z < 3).all(axis=1)]

        # Sắp xếp lại theo thứ tự giảm dần
        z = z.sort_values(by=['Standard_Rating'], ascending=False)

        # Vẽ biểu đồ phân phối từ z-core với pie
        fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

        z['Standard_Rating'].value_counts().plot.pie(ax=axs[0], autopct='%.2f')
        z['Rapid_rating'].value_counts().plot.pie(ax=axs[1], autopct='%.2f')
        z['Blitz_rating'].value_counts().plot.pie(ax=axs[2], autopct='%.2f')

        plt.subplots_adjust(wspace=0.3)
        plt.show()

    def scatter_3d(self):
        df = self.df
        df = df.drop(['Fide id','Name','Federation','Gender','Year_of_birth','Title','Inactive_flag'],axis=1)
        df = df.dropna(how='any')

        z = np.abs(stats.zscore(df._get_numeric_data()))
        df = df[(z < 3).all(axis=1)]

        # Vẽ biểu đồ phân phối từ z-core với scatter 3D
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(df['Standard_Rating'], df['Rapid_rating'], df['Blitz_rating'], c='skyblue', s=60)

        ax.view_init(30, 185)
        plt.show()

    # def voice(self):
    #     r_vinh84 = vinh84.Recognizer()
    #     with vinh84.Microphone() as source:
    #         text_audio = r_vinh84.record(source, duration=5)
    #         try: 
    #             text_audio = r_vinh84.recognize_google(text_audio, language="vi-VN")
    #             self.label_nhan_dien.config(text=text_audio)
    #             self.label_nhan_dien.update()
    #         except:
    #             self.label_nhan_dien.config(text="Không nhận dạng được")
    #             self.label_nhan_dien.update()
    def voice(self):
        r_vinh84 = vinh84.Recognizer()
        with vinh84.Microphone() as source:
            text_audio = r_vinh84.record(source, duration=5)
            try:
                text_audio = r_vinh84.recognize_google(text_audio, language="vi-VN")
                # Tìm kiếm các số trong đoạn văn bản đã nhận dạng
                numbers = re.findall(r'\d+', text_audio)
                # Nếu tìm thấy ít nhất một số, hiển thị số đầu tiên lên nhãn
                if len(numbers) > 0:
                    self.label_nhan_dien.config(text=numbers[0])
                else:
                    self.label_nhan_dien.config(text="Không nhận dạng được số")
                    self.label_nhan_dien.update()
            except:
                self.label_nhan_dien.config(text="Không nhận dạng được")
                self.label_nhan_dien.update()

    def submit_voice(self):
        if self.label_nhan_dien.cget("text") == "Không nhận dạng được":
            messagebox.showinfo("Thông báo", "Không nhận dạng được")
        elif self.label_nhan_dien.cget("text") == "1":
            self.open_file()
        elif self.label_nhan_dien.cget("text") == "2":
            self.columns_null()
        elif self.label_nhan_dien.cget("text") == "3":
            self.rows_null()
        elif self.label_nhan_dien.cget("text") == "4":
            self.zcore()
        elif self.label_nhan_dien.cget("text") == "5":
            self.chuan_hoa()
        elif self.label_nhan_dien.cget("text") == "6":
            self.histogram()
        elif self.label_nhan_dien.cget("text") == "7":
            self.phan_tan()
        elif self.label_nhan_dien.cget("text") == "8":
            self.pie()
        elif self.label_nhan_dien.cget("text") == "9":
            self.scatter_3d()
        else:
            messagebox.showinfo("Thông báo", "Không nhận dạng được")

def mainEDA():
    EDA(tkVinh.Tk())

if __name__ == '__main__':
    mainEDA()