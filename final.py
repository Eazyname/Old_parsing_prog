from tkinter import *
import requests
import os


window = Tk()
window.geometry('500x200')
window.title("Auto Save")

window.tk.call('wm', 'iconphoto', window._w,PhotoImage(file='solvent.png'))

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

def clicked():
	link0 = txt0.get()
	link00 = int(txt00.get())
	link01 = txt01.get()
	name = txt1.get()
	path = txt2.get()
	n = int(txt3.get())

	url = [link0+str(i)+link01 for i in range(link00,n+1)]

	if os.path.isdir(path+name):
		os.chdir(path+name)
	else:
		os.mkdir(path+name)
		os.chdir(path+name)

	for x in url:
		save_data(get_name(x),get_file(x))



txt0 = Entry(window,width=30)#,state='disabled') #/убрать возможность ввода теста
txt0.grid(column = 0,row=1)
lbl = Label(window, text = "основа",font=("Arial",15))
lbl.grid(column=0, row=0)

txt00 = Entry(window,width=10)#,state='disabled') #/убрать возможность ввода теста
txt00.grid(column = 1,row=1)
txt00.insert(0, "1")
lbl = Label(window, text = "начало",font=("Arial",15))
lbl.grid(column=1, row=0)

txt01 = Entry(window,width=10)#,state='disabled') #/убрать возможность ввода теста
txt01.grid(column = 2,row=1)
lbl = Label(window, text = "формат",font=("Arial",15))
txt01.insert(0, ".jpg")
lbl.grid(column=2, row=0)


lbl = Label(window, text = "Ссылка",font=("Arial",15))
lbl.grid(column=3, row=1)

txt1 = Entry(window,width=30)
txt1.grid(column = 0,row=2)
lbl = Label(window, text = "Имя",font=("Arial",15))
lbl.grid(column=1, row=2)


txt2 = Entry(window,width=30)
txt2.grid(column = 0,row=3)
txt2.insert(0, "/home/alex/AutoSave/")

lbl = Label(window, text = "Путь",font=("Arial",15))
lbl.grid(column=1, row=3)

txt3 = Entry(window,width=30)
txt3.grid(column = 0,row=4)
lbl = Label(window, text = "Сколько",font=("Arial",15))
lbl.grid(column=1, row=4)



btn = Button(window, text="press", command=clicked,bg = "red")
btn.grid(column=1, row = 5)






window.mainloop()



