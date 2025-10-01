with open('data.txt','r',encoding="UTF-8")as f:
    text=f.read()

text=text.replace("'",'"')

with open('data.txt','w',encoding="UTF-8")as f:
    f.write(text)
print("finish")