import requests
from bs4 import BeautifulSoup
from tkinter import *

root=Tk()
root.geometry("1920x1080")
root.title("Price Finder")

#URL of product to find price of

URL='https://www.amazon.in/Kingston-SSDNow-Internal-SA400S37-240GIN/dp/B079TH8YZQ/ref=sr_1_1?keywords=ssd&qid=1575484680&sr=8-1'

#header to get info about your browser
headers={"User-Agents":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

page=requests.get(URL, headers=headers)

soup=BeautifulSoup(page.content, 'html.parser')

title=soup.find(id="productTitle").get_text()
price=soup.find(id="priceblock_ourprice").get_text()

label=Label(root, font=('arial',50),text = "Price Finder").place(x = 500,y = 50)


sv=StringVar(root)
label1=Label(root,textvar = sv,font=(50)).place(x = 100,y = 200)

#function to get title of product

def Title():
   sv.set(title.strip())
   

b=Button(root,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="Product",command=Title)
b.place(x=100,y=650)


sv1=StringVar(root)
label2=Label(root,textvar = sv1,font=(50)).place(x = 100,y = 400)

#function to get title of product

def Price():
 sv1.set("Rs"+price[1:7])

b1=Button(root,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="Price",command=Price)
b1.place(x=300,y=650)
 

root.mainloop()
