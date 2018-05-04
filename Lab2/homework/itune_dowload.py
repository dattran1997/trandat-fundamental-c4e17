from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.apple.com/itunes/charts/songs"

conn = urlopen(url)
#open connect
raw_data = conn.read()
#decode
text = raw_data.decode("utf8")
# chuyen data ve text
soup =BeautifulSoup(text,"html.parser")

div = soup.find("div",id="main")
#tim tat ca li trong list
li_list = div.find_all("li")

item_list = []

for li in li_list:
    a = li.h3.a
    title = a.string
    item_list.append(title)
#print(item_list)


#download form youtube
from youtube_dl import YoutubeDL
song_num = len(item_list)

option={
    'default_search':'ytsearch',
    'max_downloads':song_num #download 1 vieo trong ca list
}

dl = YoutubeDL(option)
dl.download(item_list)
