import tkinter as tk

class FilePanel:
    def __init__(self, window, BtnFont, EntryFont):
        self.OutputText = tk.Label(window, text ="請選擇輸出方式", font = BtnFont)
        self.OutputPlace = tk.Button(window, text ="選擇輸出資料夾", bg = "light blue", width = '15', height = '1', font = EntryFont)
        self.FileBtn = tk.Button(window, text ="選擇檔案", bg = "light blue", width = '10', height = '1', font = BtnFont)
        self.WillCover = tk.BooleanVar()
        self.WillCover_Btn = tk.Checkbutton(window, text='直接覆蓋原檔案', var = self.WillCover, font = EntryFont)
        ##
        self.WillCover_Btn.config(command = lambda:self.CoverEvent())

    def ShowUI(self):
        self.OutputText.place(x = 400, y = 150)
        self.FileBtn.place(x = 400, y = 50)
        self.WillCover_Btn.place(x = 400, y = 200)
        self.CoverEvent()
    
    def HideUI(self):
        self.OutputText.place_forget()
        self.OutputPlace.place_forget()
        self.FileBtn.place_forget()
        self.WillCover_Btn.place_forget()

    def CoverEvent(self):
        if self.WillCover.get() :
            self.OutputPlace.place_forget()
        else :
            self.OutputPlace.place(x = 400, y = 250)