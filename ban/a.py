import os
import re

# Input for the directory name
zc = input("Enter directory name: ")
if not os.path.isdir(zc):
    os.mkdir(zc)

# Reading the HTML template
zcs = open("test/index.html", "r", encoding="utf-8").read()

# Text block with Telegram links
text2 = """
فروش سلف مراقب باشید نفروشه
t.me/+989396501229
t.me/+989225054528
اکانت فیک طرف
tg://openmessage?user_id=7374352774
""".replace('https://', '').replace('@', 't.me/').replace('t.me/+', '+').replace('+', 't.me/+')

# Finding and replacing links
for dasd in re.findall('t.me/(.*)', text2):
    text2 = text2.replace(f"t.me/{dasd}", f'<a href="https://t.me/{dasd}">t.me/{dasd}</a>')
for dasd in re.findall('tg://(.*)', text2):
    text2 = text2.replace(f"tg://{dasd}", f'<a href="tg://{dasd}">tg://{dasd}</a>')
zxc = input("Photo ")
dad=""
for dd in os.listdir(os.getcwd()+"/"+zc):
  if dd.split(".")[-1]=="jpg":
    dad+=f'            <img src="{dd}" alt="{dd}" class="active" onclick="openLightbox(this)">\n'
  if dd.split(".")[-1]=="mp4":
    dad+=f'            <video src="{dd}" controls onclick="openLightbox(this)"></video>\n'
if not dad:
  zcs = zcs.replace('{{text3}}','<img src="https://raw.githubusercontent.com/amirwolf5122/amirwolf5122.github.io/master/ban/back.jpg" alt="Image 1" class="active" onclick="openLightbox(this)">')

else:
  zcs = zcs.replace('            {{text3}}',dad)
with open(f"{zc}/index.html", "w", encoding="utf-8") as file:
    file.write(zcs.replace('{{text}}', text2))

#<img src="https://raw.githubusercontent.com/amirwolf5122/amirwolf5122.github.io/master/ban/back.jpg" alt="Image 1" class="active" onclick="openLightbox(this.src)">
#.replace(']]', '')