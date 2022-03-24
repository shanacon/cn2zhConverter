import tkinter as tk
import tkinter.font as font

window = tk.Tk()
##      font
BtnFont = font.Font(size=20)
EntryFont = font.Font(size=14)
##      button
###     main
FileMode = tk.Button(window, text ="按照檔案", bg = "light blue", width = '10', height = '1', font = BtnFont)
FileMode.place(x = 50, y = 70)
FolderMode = tk.Button(window, text ="按照資料夾", bg = "light blue", width = '10', height = '1', font = BtnFont)
FolderMode.place(x = 50, y = 270)
OutputPlace = tk.Button(window, text ="選擇輸出資料夾", bg = "light blue", width = '15', height = '1', font = EntryFont)
OutputPlace.place(x = 400, y = 270)

###    file
FileBtn = tk.Button(window, text ="選擇檔案", bg = "light blue", width = '10', height = '1', font = BtnFont)

###    folder
FolderBtn = tk.Button(window, text ="選擇資料夾", bg = "light blue", width = '10', height = '1', font = BtnFont)

##      Label
OutputText = tk.Label(window, text ="請選擇輸出方式", font = BtnFont)

##      checkbox
WillCover = tk.BooleanVar()
WillCover_Btn = tk.Checkbutton(window, text='直接覆蓋原檔案', var=WillCover, font = EntryFont)

###     folder
ActiveAss = tk.BooleanVar()
ActiveAss_Btn = tk.Checkbutton(window, text='轉換.ass檔案', var=ActiveAss, font = EntryFont)
ActiveLrc = tk.BooleanVar()
ActiveLrc_Btn = tk.Checkbutton(window, text='轉換.lrc檔案', var=ActiveLrc, font = EntryFont)
ActiveTxt = tk.BooleanVar()
ActiveTxt_Btn = tk.Checkbutton(window, text='轉換.txt檔案', var=ActiveTxt, font = EntryFont)

##      BtnEvent
FileMode.config(command = lambda:FileUI())
FolderMode.config(command = lambda:FolderUI())
WillCover_Btn.config(command = lambda:CoverEvent())
##      method
def FileUI():
    HideUI()
    FileBtn.place(x = 400, y = 50)
    OutputText.place(x = 400, y = 150)
    WillCover_Btn.place(x = 400, y = 200)

def FolderUI():
    HideUI()
    FolderBtn.place(x = 400, y = 50)
    OutputText.place(x = 400, y = 150)
    WillCover_Btn.place(x = 400, y = 200)
    ActiveAss_Btn.place(x = 600, y = 25)
    ActiveLrc_Btn.place(x = 600, y = 75)
    ActiveTxt_Btn.place(x = 600, y = 125)
    
def HideUI():
    FileBtn.place_forget()
    FolderBtn.place_forget()
    OutputText.place_forget()
    WillCover_Btn.place_forget()
    ActiveAss_Btn.place_forget()
    ActiveLrc_Btn.place_forget()
    ActiveTxt_Btn.place_forget()

def CoverEvent():
    if WillCover.get() :
        OutputPlace.place_forget()
    else :
        OutputPlace.place(x = 400, y = 250)
##
FileUI()
window.title('cn2zh')
window.geometry("1000x400+500+300")
window.mainloop()