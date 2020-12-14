from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import io
import urllib.parse
import urllib.request
from tkinter import *
from PIL import ImageTk, Image 
from tkinter import ttk  

input_topic = input()

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome("C:/Users/perfu/Desktop/商程設/期末專案/chromedriver.exe", chrome_options=options)

chrome.get("https://lookbook.nu/")

wait = WebDriverWait(chrome, 20)

search = chrome.find_element_by_name('q')
search.send_keys(input_topic)
search.submit()

pos = 0  
m = 0 # 圖片編號 
for i in range(3):  
    pos += i*600 # 每次下滾500  
    js = "document.documentElement.scrollTop=%d" % pos  
    chrome.execute_script(js)  
    time.sleep(1)

soup = BeautifulSoup(chrome.page_source, 'lxml')
imgs = soup.find_all('img', {'class': 'thumbimage'})
srcs = []
for img in imgs:
    if img != 'None':
        small_pic = img.get('src')
        large_pic = small_pic.replace("small", "medium")
        srcs.append(large_pic)

chrome.close()


mainWindow = Tk()
mainWindow.title("What to wear")
w, h = mainWindow.maxsize()
mainWindow.geometry("{}x{}".format(w, h))
mainWindow.minsize(width=1000, height=1240)
mainWindow.attributes("-topmost", 1)


List_images = []
for i in range(len(srcs)):
    picture_url = "http:" + srcs[i]
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=picture_url, headers=headers)
    raw_data = urllib.request.urlopen(req).read()
    im = Image.open(io.BytesIO(raw_data))
    img = ImageTk.PhotoImage(im)
    List_images.append(img)

def forward(img_no): 
  
    # GLobal variable so that we can have 
    # access and change the variable 
    # whenever needed 
    global label 
    global button_forward 
    global button_back 
    global button_exit 
    label.grid_forget() 
  
    # This is for clearing the screen so that 
    # our next image can pop up 
    label = Label(image=List_images[img_no-1]) 
  
    # as the list starts from 0 so we are 
    # subtracting one 
    label.grid(row=1, column=0, columnspan=3) 
    button_for = Button(mainWindow, text="forward", command=lambda: forward(img_no+1)) 
  
    # img_no+1 as we want the next image to pop up 
    if img_no == len(List_images): 
        button_forward = Button(mainWindow, text="Forward", state=DISABLED) 
  
    # img_no-1 as we want previous image when we click 
    # back button 
    button_back = Button(mainWindow, text="Back", command=lambda: back(img_no-1)) 
  
    # Placing the button in new grid 
    button_back.grid(row=5, column=0) 
    button_exit.grid(row=5, column=1) 
    button_for.grid(row=5, column=2) 
  
  
def back(img_no): 
  
    # We willl have global variable to access these 
    # variable and change whenever needed 
    global label 
    global button_forward 
    global button_back 
    global button_exit 
    label.grid_forget() 
  
    # for clearing the image for new image to pop up 
    label = Label(image=List_images[img_no - 1]) 
    label.grid(row=1, column=0, columnspan=3) 
    button_forward = Button(mainWindow, text="forward", command=lambda: forward(img_no + 1)) 
    button_back = Button(mainWindow, text="Back", command=lambda: back(img_no - 1)) 
    print(img_no) 
  
    # whenever the first image will be there we will 
    # have the back button disabled 
    if img_no == 1: 
        button_back = Button(mainWindow, Text="Back", state=DISABLED) 
  
    label.grid(row=1, column=0, columnspan=3) 
    button_back.grid(row=5, column=0) 
    button_exit.grid(row=5, column=1) 
    button_for.grid(row=5, column=2) 


  
label = Label(image=List_images[0]) 
  
# We have to show the the box so this below line is needed 
label.grid(row=1, column=0, columnspan=3) 
  
# We will have three button back ,forward and exit 
button_back = Button(mainWindow, text="Back", command=back, state=DISABLED) 
  
# mainWindow.quit for closing the app 
button_exit = Button(mainWindow, text="Exit", command=mainWindow.quit) 
  
button_forward = Button(mainWindow, text="Forward", command=lambda: forward(1)) 
  
# grid function is for placing the buttons in the frame 
button_back.grid(row=5, column=0) 
button_exit.grid(row=5, column=1) 
button_forward.grid(row=5, column=2) 
  
mainWindow.mainloop()