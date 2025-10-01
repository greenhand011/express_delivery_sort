import re
import unicodedata
with open('data.txt','r',encoding="UTF-8")as f:
    text=f.read()

text=unicodedata.normalize("NFKC",text)
text=re.sub(r'(.)\1+',r'\1',text)
with open('data.txt','w',encoding="UTF-8")as f:
    f.write(text)
print("finish")