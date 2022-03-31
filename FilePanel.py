import tkinter as tk
from tkinter import filedialog
from zhconv import convert
import os

class FilePanel:
    def __init__(self, window, BtnFont, EntryFont):
        self.OutputText = tk.Label(window, text ="請選擇輸出方式", font = BtnFont)
        self.OutputPlace = tk.Button(window, text ="選擇輸出資料夾", bg = "light blue", width = '15', height = '1', font = EntryFont)
        self.FileBtn = tk.Button(window, text ="選擇檔案", bg = "light blue", width = '10', height = '1', font = BtnFont)
        self.WillCover = tk.BooleanVar()
        self.WillCover_Btn = tk.Checkbutton(window, text='直接覆蓋原檔案', var = self.WillCover, font = EntryFont)
        self.ExecuteBtn = tk.Button(window, text='開始轉換', bg = "light blue", font = BtnFont)
        #
        self.FileText = tk.Label(window, text ="", font = EntryFont)
        self.OutputFText = tk.Label(window, text ="", font = EntryFont)
        #
        self.Pathreg = ""
        self.Folderreg = ""
        self.Coverreg = False
        ##
        self.WillCover_Btn.config(command = lambda:self.CoverEvent())
        self.FileBtn.config(command = lambda:self.ChooseFile())
        self.ExecuteBtn.config(command = lambda:self.Convert())
        self.OutputPlace.config(command = lambda:self.ChooseOutput())

    def ShowUI(self):
        self.OutputText.place(x = 400, y = 150)
        self.FileBtn.place(x = 400, y = 50)
        self.WillCover_Btn.place(x = 400, y = 200)
        self.ExecuteBtn.place(x = 400, y = 325)
        self.FileText.place(x = 600, y = 62)
        self.CoverEvent()
    
    def HideUI(self):
        self.OutputText.place_forget()
        self.OutputPlace.place_forget()
        self.FileBtn.place_forget()
        self.WillCover_Btn.place_forget()
        self.ExecuteBtn.place_forget()
        self.FileText.place_forget()
        self.OutputFText.place_forget()

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
        self.Folderreg = filedialog.askdirectory()
        if self.Folderreg != "":
            self.OutputFText.config(text = self.Folderreg)

    def Convert(self):
        if not self.Coverreg and self.Folderreg == "":
            self.OutputFText.config(text = "請選擇輸出資料夾！")
            return
        if os.path.splitext(self.Pathreg)[1] == '.txt' or  os.path.splitext(self.Pathreg)[1] == '.lrc' or  os.path.splitext(self.Pathreg)[1] == '.srt' :
            LoadF = open(self.Pathreg, "r" , encoding='utf-8')
            ConvertData = convert(LoadF.read(),'zh-tw')
            if self.Coverreg :
                self.Output_Cover(ConvertData)
            else :
                self.Output_NoCover(ConvertData)
        if os.path.splitext(self.Pathreg)[1] == '.ass':
            LoadF = open(self.Pathreg, "r" , encoding='utf-8')
            lines = LoadF.readlines()
            ConvertData = ""
            for line in lines:
                former = line.split(':')[0]
                if former == "Style" :
                    style = line.split(':')[1].split(',')[0]
                    ConvertData += line.replace(style, convert(style ,'zh-tw')) 
                elif former == "Dialogue" :
                    ConvertData += convert(line,'zh-tw')
                else :
                    ConvertData += line
            if self.Coverreg :
                self.Output_Cover(ConvertData)
            else :
                self.Output_NoCover(ConvertData)

    def Output_Cover(self, ConvertData):
        with open(self.Pathreg, "w", encoding='utf-8') as WriteF:
            WriteF.write(ConvertData)

    def Output_NoCover(self, ConvertData):
        FileName = os.path.basename(self.Pathreg)
        with open(self.Folderreg + '/' + FileName, "w", encoding='utf-8') as WriteF:
            WriteF.write(ConvertData)
