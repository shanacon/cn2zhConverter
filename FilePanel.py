import tkinter as tk
from tkinter import filedialog
from zhconv import convert
from ConvertEvent import *
import os

class FilePanel:
    def __init__(self, window, BtnFont, EntryFont):
        self.OutputText = tk.Label(window, text ="請選擇輸出方式", font = BtnFont)
        self.OutputPlace = tk.Button(window, text ="選擇輸出資料夾", bg = "light blue", width = '15', height = '1', font = EntryFont)
        self.FileBtn = tk.Button(window, text ="選擇檔案", bg = "light blue", width = '10', height = '1', font = BtnFont)
        self.WillCover = tk.BooleanVar()
        self.WillCover_Btn = tk.Checkbutton(window, text='直接覆蓋原檔案', var = self.WillCover, font = EntryFont)
        self.ExecuteBtn = tk.Button(window, text='開始轉換', bg = "light blue", font = BtnFont)
        self.ToSim = tk.BooleanVar()
        self.ToSim_Btn = tk.Checkbutton(window, text='轉換成簡體字', var = self.ToSim, font = EntryFont)
        self.ToTrd = tk.BooleanVar()
        self.ToTrd_Btn = tk.Checkbutton(window, text='轉換成繁體字', var = self.ToTrd, font = EntryFont)
        #
        self.FileText = tk.Label(window, text ="", font = EntryFont)
        self.OutputFText = tk.Label(window, text ="", font = EntryFont)
        #
        self.Pathreg = ""
        self.Outputreg = ""
        self.Coverreg = False
        self.STreg = ""
        ##
        self.WillCover_Btn.config(command = lambda:self.CoverEvent())
        self.FileBtn.config(command = lambda:self.ChooseFile())
        self.ExecuteBtn.config(command = lambda:self.ConvertAction())
        self.OutputPlace.config(command = lambda:self.ChooseOutput())
        self.ToTrd_Btn.config(command = lambda:self.ChooseTrd())
        self.ToSim_Btn.config(command = lambda:self.ChooseSim())

    def ShowUI(self):
        self.OutputText.place(x = 400, y = 150)
        self.FileBtn.place(x = 400, y = 50)
        self.WillCover_Btn.place(x = 400, y = 200)
        self.ExecuteBtn.place(x = 400, y = 325)
        self.FileText.place(x = 600, y = 62)
        self.ToSim_Btn.place(x = 220, y = 340)
        self.ToTrd_Btn.place(x = 220, y = 290)
        self.CoverEvent()
    
    def HideUI(self):
        self.OutputText.place_forget()
        self.OutputPlace.place_forget()
        self.FileBtn.place_forget()
        self.WillCover_Btn.place_forget()
        self.ExecuteBtn.place_forget()
        self.FileText.place_forget()
        self.OutputFText.place_forget()
        self.ToSim_Btn.place_forget()
        self.ToTrd_Btn.place_forget()

    def CoverEvent(self):
        if self.WillCover.get() :
            self.OutputPlace.place_forget()
            self.OutputFText.place_forget()
            self.Coverreg = True
        else :
            self.OutputPlace.place(x = 400, y = 250)
            self.OutputFText.place(x = 600, y = 253)
            self.Coverreg = False
    
    def ChooseFile(self):
        file_path = filedialog.askopenfilename()
        if file_path != "":
            if os.path.splitext(file_path)[1] == '.txt' or  os.path.splitext(file_path)[1] == '.lrc' or  os.path.splitext(file_path)[1] == '.ass' or os.path.splitext(file_path)[1] == '.srt'  :
                self.FileText.config(text = os.path.basename(file_path))
                self.Pathreg = file_path
    
    def ChooseOutput(self):
        self.Outputreg = filedialog.askdirectory()
        if self.Outputreg != "":
            self.OutputFText.config(text = self.Outputreg)

    def ConvertAction(self):
        if self.Pathreg == "" :
            self.FileText.config(text = "請選擇欲轉換的檔案！")
            return
        if not self.Coverreg and self.Outputreg == "":
            self.OutputFText.config(text = "請選擇輸出資料夾！")
            return
        if os.path.splitext(self.Pathreg)[1] == '.txt' or  os.path.splitext(self.Pathreg)[1] == '.lrc' or  os.path.splitext(self.Pathreg)[1] == '.srt' :
            LoadF = open(self.Pathreg, "r" , encoding='utf-8')
            ConvertData = Convert(LoadF.read(), self.STreg)
        if os.path.splitext(self.Pathreg)[1] == '.ass':
            LoadF = open(self.Pathreg, "r" , encoding='utf-8')
            lines = LoadF.readlines()
            ConvertData = ConvertAss(lines, self.STreg)
        if self.Coverreg :
            status = Output_Cover(ConvertData, self.Pathreg)
        else :
            status = Output_NoCover(ConvertData, self.Pathreg, self.Outputreg)
        if status:
            self.Initial()
            self.FileText.config(text = "轉換完成")
        else :
            self.FileText.config(text = "轉換錯誤")

    def Initial(self):
        self.FileText.config(text = "")
        self.OutputFText.config(text = "")
        self.Pathreg = ""
        self.Outputreg = ""

    def ChooseSim(self):
        if self.ToSim.get() :
            self.ToTrd.set(False)
            self.STreg = "zh-cn"
    
    def ChooseTrd(self):
        if self.ToTrd.get() :
            self.ToSim.set(False)
            self.STreg = "zh-tw"

