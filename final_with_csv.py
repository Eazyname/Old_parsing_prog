from tkinter import *
from tkinter import ttk
import requests
import os
from bs4 import BeautifulSoup as bs
import csv




allink = []


def get_file(url):
    response = requests.get(url, verify = True,stream=True, headers={'User-Agent': 'XYZ/3.0'} )
    return response

def save_data(name, file_data):
    file = open(name, 'wb') #Бинарный режим, изображение передається байтами
    for chunk in file_data.iter_content(16384): # Записываем в файл по блочно данные
        file.write(chunk)

def get_name(url):
    name = url.split('/')[-1]
    return name



def clicked_1():
	clerdatalinks = []
	sourse = txt0.get()
	with open(sourse) as fp:
		reader = csv.reader(fp)
		datalinks = [row for row in reader]
		for x in datalinks:
			if x not in clerdatalinks:
				clerdatalinks.append(x)
	return clicked(clerdatalinks)


def clicked(data):
	print(len(data))
	a = 1
	for element in data:
		print(element)
		print(a)
		a += 1
		pars = requests.get(element[0],stream = True, headers={'User-Agent': 'XYZ/3.0'})
		soup0 = bs(pars.text,"html.parser")
		
		NumberFoto = soup0.findAll('a',class_ = 'on-popunder page-numbers')
		Name = soup0.findAll('a',class_ = 'on-popunder', rel="category tag")
		NameSet = soup0.findAll('h2',class_ = 'main-title')
		
		if NumberFoto == []:
			print("ты что тупой,это не сет")
		else:
			link0 = element[0]             # Ссылка на сет
			name = Name[-1].text           # Имя модели
			path = txt2.get()              # Путь куда 
			n = int(NumberFoto[-1].text)   # Скольфо фото
			nameSet = NameSet[0].text      # Название сета
		
			FinallPath = path+name+'/'+nameSet

			if os.path.isdir(path+name):
				if os.path.isdir(FinallPath):
					print("Уже есть такая, ЛаЛ")
				else:
					os.mkdir(FinallPath)
					os.chdir(FinallPath)
					reqq(link0,n)
			else:
				os.makedirs(FinallPath)
				os.chdir(FinallPath)
				reqq(link0,n)


def reqq(link0,n):
	for x in range(1,n+1):
		url = link0 + "/" + str(x)
		page = requests.get(url,stream = True, headers={'User-Agent': 'XYZ/3.0'})
		soup = bs(page.text,"html.parser")
		allfoto = soup.findAll('img',class_ = 'blur')
		link = allfoto[0].get("src")
		save_data(get_name(link),get_file(link))


def clicked_2():
	link = txt00.get()
	name = txt11.get()
	path = txt22.get()
	n = int(txt33.get())
	link = link.split("jpg")[0]
	link = link[:-link[::-1].index("/")]

	url = [link+str(i)+".jpg" for i in range(1,n+1)]

	if os.path.isdir(path+name):
		os.chdir(path+name)
	else:
		os.mkdir(path+name)
		os.chdir(path+name)

	for x in url:
		save_data(get_name(x),get_file(x))



window = Tk()
window.geometry('500x200')
window.title("Auto Save")
window.tk.call('wm', 'iconphoto', window._w,PhotoImage(file='solvent.png'))


tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='CSV')  
tab_control.add(tab2, text='https://') 
tab_control.pack(expand=1, fill='both') 

#Для первого окна-----------------------
txt0 = Entry(tab1,width=30)
txt0.grid(column = 1,row=0)
lbl = Label(tab1, text = "Путь до CSV",font=("Arial",15))
lbl.grid(column=0, row=0)
txt0.insert(0, "/home/alex/AutoSave/Texts/")

txt2 = Entry(tab1,width=30)
txt2.grid(column = 1,row=2)
txt2.insert(0, "/home/alex/AutoSave/allFoto/")
lbl = Label(tab1, text = "Путь",font=("Arial",15))
lbl.grid(column=0, row=2)

btn = Button(tab1, text="press", command=clicked_1,bg = "red")
btn.grid(column=1, row = 3)

#Для второго окна------------------------
txt00 = Entry(tab2,width=30)
txt00.grid(column = 0,row=0)
lbl = Label(tab2, text = "Ссылка",font=("Arial",15))
lbl.grid(column=1, row=0)

txt11 = Entry(tab2,width=30)
txt11.grid(column = 0,row=1)
lbl = Label(tab2, text = "Имя",font=("Arial",15))
lbl.grid(column=1, row=1)

txt22 = Entry(tab2,width=30)
txt22.grid(column = 0,row=2)
txt22.insert(0, "/home/alex/AutoSave/allFoto/")
lbl = Label(tab2, text = "Путь",font=("Arial",15))
lbl.grid(column=1, row=2)

txt33 = Entry(tab2,width=30)
txt33.grid(column = 0,row=3)
lbl = Label(tab2, text = "Сколько",font=("Arial",15))
lbl.grid(column=1, row=3)


btn = Button(tab2, text="press", command=clicked_2,bg = "red")
btn.grid(column=1, row = 5)






window.mainloop()



