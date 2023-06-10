'''
NGười viết: Lê THành VInh
MSSV: 2110940
Ngày viết: 19/04/2023
Mô tả: Báo cáo cuối kì: EDA Chess - Giao diện chính
'''

import tkinter as tkVinh
import customtkinter as ctk
from tkinter import *
from tkinter.font import Font
from CTkMessagebox import CTkMessagebox
import cv2
import PIL.Image, PIL.ImageTk
from PIL import ImageTk, Image
import tkinter.filedialog as filedialog
from PIL import Image
import os
import matplotlib.pyplot as plt
# import pygame,sys
# from pygame.locals import *
import random
# import BaiTuan.Tuan14_5 as game
import G3_84LeThanhVinh_ChessWomen_Frame as Frame
import G3_84LeThanhVinh_ChessWomen_Game as game
import G3_84LeThanhVinh_ChessWomen_EDA as eda

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green") 



class App(ctk.CTk):
    width = 650
    height = 366
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.iconbitmap("G3_84_LeThanhVinh_ChessWomen/Icon.ico")        
        self.title("84 - Lê Thành Vinh - EDA Chess")
        self.geometry("800x600")
        self.resizable(False, False)

        # Tạo Frame cho label giới thiệu
        self.frame = ctk.CTkFrame(self, width=800,height= 200, bg_color="#8FBC8F", border_width=1, border_color="#8FBC8F")
        self.frame.grid(row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # Tạo label giới thiệu
        self.label = ctk.CTkLabel(self.frame, text="84 LÊ THÀNH VINH, ĐỒ ÁN HỌC PHẦN: LẬP TRÌNH PYTHON EDA CHESS", font=ctk.CTkFont(size=17, weight="bold"), text_color="white", bg_color="#2F4F4F")
        # self.label.grid(row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="w")
        self.label.grid(row=0, column=3,padx=(80, 0), sticky="nsew")
        
        # tạo tabview
        self.tabview = ctk.CTkTabview(self, width=760, height=500, bg_color="#8FBC8F", border_width=3, border_color="#8FBC8F")        
        self.tabview.grid(row=3, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Giới thiệu")
        self.tabview.tab("Giới thiệu").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.add("EDA")
        self.tabview.tab("EDA").grid_columnconfigure(0, weight=1)
        self.tabview.add("Frame")
        self.tabview.tab("Frame").grid_columnconfigure(0, weight=1)
        self.tabview.add("Game")
        self.tabview.tab("Game").grid_columnconfigure(0, weight=1)

        # thêm hình nền cho tabview Giới thiệu
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = ctk.CTkImage(Image.open(current_path + "/G3_84_LeThanhVinh_ChessWomen/gioi_thieu.png"),
                                                  size=(self.width, self.height)) 
        self.bg_image_label = ctk.CTkLabel(self.tabview.tab("Giới thiệu"), image=self.bg_image, text=None)
        self.bg_image_label.grid(row=0, column=0, sticky="nsew")

        # thêm hình nền cho tabview EDA
        self.bg_image = ctk.CTkImage(Image.open(current_path + "/G3_84_LeThanhVinh_ChessWomen/eda.png"),
                                                    size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self.tabview.tab("EDA"), image=self.bg_image, text=None)
        self.bg_image_label.grid(row=0, column=0, sticky="nsew")

        # thêm hình nền cho tabview Frame
        self.bg_image = ctk.CTkImage(Image.open(current_path + "/G3_84_LeThanhVinh_ChessWomen/Frame.png"),
                                                    size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self.tabview.tab("Frame"), image=self.bg_image, text=None)
        self.bg_image_label.grid(row=0, column=0, sticky="nsew")

        # thêm hình nền cho tabview Game
        self.bg_image = ctk.CTkImage(Image.open(current_path + "/G3_84_LeThanhVinh_ChessWomen/Game.png"),
                                                    size=(self.width, self.height))
        self.bg_image_label = ctk.CTkLabel(self.tabview.tab("Game"), image=self.bg_image, text=None)
        self.bg_image_label.grid(row=0, column=0, sticky="nsew")

        # thêm button vào tabview Giới thiệu
        self.buttonGioiThieu = ctk.CTkButton(self.tabview.tab("Giới thiệu"), text="84 - Lê Thành Vinh", command=self.mo_GioiThieu, font=ctk.CTkFont(size=20, weight="bold", family="Segoe UI"))
        self.buttonGioiThieu.grid(row=1, column=0, padx=(300, 0), pady=(20, 0), sticky="w")


        # thêm button vào tabview Frame
        self.buttonFrame = ctk.CTkButton(self.tabview.tab("Frame"), text="Mở Frame", command=self.mo_Frame, font=ctk.CTkFont(size=20, weight="bold", family="Segoe UI"))
        self.buttonFrame.grid(row=1, column=0, padx=(300, 0), pady=(20, 0), sticky="w")

        # thêm button vào tabview EDA
        self.buttonEDA = ctk.CTkButton(self.tabview.tab("EDA"), text="Mở EDA", command=self.mo_EDA, font=ctk.CTkFont(size=20, weight="bold", family="Segoe UI"))
        self.buttonEDA.grid(row=1, column=0, padx=(300, 0), pady=(20, 0), sticky="w")

        # thêm button vào tabview Game
        self.buttonGame = ctk.CTkButton(self.tabview.tab("Game"), text="Mở Game", command=self.mo_Game, font=ctk.CTkFont(size=20, weight="bold", family="Segoe UI"))
        self.buttonGame.grid(row=1, column=0, padx=(300, 0), pady=(20, 0), sticky="w")

    def mo_GioiThieu(self):
        # Nếu nhấn vào thì sẽ xuất hiện messagebox
        CTkMessagebox(message="Được tạo bởi: 84 - Lê Thành Vinh (21110940) \n Đồ án học phần: Lập trình Python EDA Chess",
                  icon="check", option_1="Ok", title="Giới thiệu", font=ctk.CTkFont(size=16, family="Segoe UI"))
    
    def mo_Game(self):
        # Nếu button 1 được nhấn thì mở game
        game.main()

    def mo_EDA(self):
        # Nếu button 2 được nhấn thì mở EDA
        # eda.mainEDA()
        eda.mainEDA()

    def mo_Frame(self):
        # Nếu button 3 được nhấn thì mở Frame
        Frame.GUI()

if __name__ == "__main__":
    app = App()
    app.mainloop()