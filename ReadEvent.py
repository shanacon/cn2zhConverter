import chardet

def ReadData(path):
    text = open(path, 'rb').read()
    LoadF = open(path, "r" , encoding = chardet.detect(text)["encoding"])
    return LoadF.readlines()