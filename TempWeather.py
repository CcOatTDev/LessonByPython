from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from urllib.request import urlopen 
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

def checkweather(id):

    url = 'https://www.tmd.go.th/province.php?id=' + id
    # id 2  => Chiang Mai
    print(url)
    webopen = req(url)
    #print(webopen)
    page_html = webopen.read()
    #print(page_html)
    webopen.close()
    page_soup = soup(page_html,"html.parser")
    #print(page_soup)
    data = page_soup.find_all('td',{'class','strokeme'})
    #print(data)
    links = page_soup.find_all('img',alt=True)

    for i in links:
        #print(i)
        if i['alt'] == "ภาพจังหวัด":
            srcimg = i['src']
            title = i['title']
            break
    
    links = page_soup.find_all('a',href=True)
    for i in links:
        print(i)
        #print(i[0].text.strip())
    #print(links)

    province = page_soup.find_all('span',{'class','title'})
    provincename = province[0].text.strip()
    provincename = "อุณหภูมิ"+ provincename + "ตอนนี้"
    #print(provincename)
    L0.configure(text = provincename)
    L0.text = provincename

    temp = data[0].text
    temptext.set(temp)
    germandict(srcimg,title)

def germandict(sourceimg,title):
    sourceimg = "https://www.tmd.go.th" + sourceimg
    #Voc = Toplevel()
    #print("Open img "+ sourceimg)
    img = Image.open(urlopen(sourceimg))
    photo = ImageTk.PhotoImage(img)
    #print(img)
    #print(photo)
    width, height = img.size
    #print(img)

    #label = Label(GUI,image=photo)
    #label.image = photo
    #label.pack()

    #photoTemp=photo
    #print(photoTemp)
 
    imgbox.configure(image = photo)
    imgbox.image = photo
 
    #translate = Label(GUI,text = title)
    #translate.config(font=("Courier",44))
    #translate.pack(ipady=20)
    #Voc.mainloop()

GUI = Tk()
GUI.title('CGM48 Temp')
GUI.geometry('500x550')

temptext = StringVar()

L0 = ttk.Label(GUI , text="อุณหภูมิตอนนี้" , font = {'TH Satabun New',25})
L0.pack(padx=10,pady=10)

L1= ttk.Label(GUI,textvariable=temptext, foreground='green',font={'tohama',25})
L1.pack(padx=10,pady=10)

B1 = ttk.Button(GUI,text='เชียงราย', command=lambda:checkweather(str(1)))
B1.pack(padx=10,pady=10)

B2 = ttk.Button(GUI,text='เชียงใหม่', command=lambda:checkweather(str(2)))
B2.pack(padx=10,pady=20)

photoTemp = PhotoImage()
imgbox = Label(GUI,image=photoTemp)
imgbox.image = photoTemp
imgbox.pack()



GUI.mainloop()