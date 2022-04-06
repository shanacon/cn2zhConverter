
import os
from tkinter.messagebox import RETRY
from zhconv import convert
def Convert(InputData, ST):
    ConvertData = convert(InputData,ST)
    return ConvertData

def ConvertAss(InputList, ST):
    ConvertData = ""
    for line in InputList:
        former = line.split(':')[0]
        if former == "Style" :
            style = line.split(':')[1].split(',')[0]
            ConvertData += line.replace(style, convert(style ,ST)) 
        elif former == "Dialogue" :
            ConvertData += convert(line,ST)
        else :
            ConvertData += line
    return ConvertData

def Output_Cover(ConvertData, FilePath) :
    try:
        with open(FilePath, "w", encoding='utf-8') as WriteF:
            WriteF.write(ConvertData)
        return True
    except:
        return False

def Output_NoCover(ConvertData, path, OutputPath):
    try:
        FileName = os.path.basename(path)
        with open(OutputPath + '/' + FileName, "w", encoding='utf-8') as WriteF:
            WriteF.write(ConvertData)
        return True
    except:
        return False