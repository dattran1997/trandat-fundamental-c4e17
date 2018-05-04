from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
#open connect
conn =  urlopen(url)
#đọc data
raw_data =conn.read()
#decode
text = raw_data.decode('utf8')
#clone file html cua trang web
# vinamilk_file = open("vinamilk.html","wb")
# vinamilk_file.write(raw_data)
# vinamilk_file.close()
#
soup = BeautifulSoup(text,"html.parser")
table = soup.find("table",id="tableContent")

row_content = table.find_all("tr")

for tr in row_content:
    title = tr.td
    print(title)
    print('----------------------------------')
