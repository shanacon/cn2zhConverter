import tkinter as tk
from FolderPanel import *
from FilePanel import *
from zhconv import convert

class MainPanel:
    def __init__(self, window, BtnFont, EntryFont):
        self.FileMode = tk.Button(window, text ="按照檔案", bg = "light blue", width = '10', height = '1', font = BtnFont)
        self.FolderMode = tk.Button(window, text ="按照資料夾", bg = "light blue", width = '10', height = '1', font = BtnFont)
        ##
        self.filepanel = FilePanel(window, BtnFont, EntryFont)
        self.folderpanel = FolderPanel(window, BtnFont, EntryFont)
        ##
        self.FileMode.config(command = lambda:self.ShowFileUI())
        self.FolderMode.config(command = lambda:self.ShowFolderUI())
        ##
        self.ShowUI()
    def ShowUI(self):
        self.FileMode.place(x = 50, y = 50)
        self.FolderMode.place(x = 50, y = 250)

    def ShowFileUI(self):
        self.folderpanel.HideUI()
        self.filepanel.ShowUI()

    def ShowFolderUI(self):
        self.filepanel.HideUI()
        self.folderpanel.ShowUI()