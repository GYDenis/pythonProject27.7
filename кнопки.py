import tkinter
import webbrowser
from tkinter import *
from tkinter import messagebox  # эти библиотеки для формы
from tkinter import ttk

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения"):
        tk.destroy()  # всплывающее укно с нозванием и текстом

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)  # при наступлении этого события, вызывается функция on_closing
tk.title("Мое приложение")  # заголовок
tk.resizable(0, 0)  # чтобы нельзя было поменять размеры приложения

tk.wm_attributes("-topmost", 1)  # поверх всех окон

tk.iconbitmap("icon.ico")  # добавление иконки приложения



canvas = Canvas(tk, width=700, height=700, bg="grey", highlightthickness=5)  # размер области, цвет, ширина рамки
x1 = Entry(tk)
x1.place(x=50, y=50, height=20, width=150)
x1.get()


y1 = ttk.Entry().pack(anchor=CENTER, padx=8, pady= 8),
x2 = ttk.Entry().pack(anchor=CENTER, padx=8, pady= 8),
y2 = ttk.Entry().pack(anchor=CENTER, padx=8, pady= 8),
x3 = ttk.Entry().pack(anchor=CENTER, padx=8, pady= 8),
y3 = ttk.Entry().pack(anchor=CENTER, padx=8, pady= 8)




def www():
    print(x1)




our_button = PhotoImage(file="knopka.png")    #добавляем картинку (кнопку)
our_button = our_button.subsample(2,2)      #маштабируем кнопку

our_button2 = PhotoImage(file="knopka.png")    #добавляем картинку (кнопку)
our_button2 = our_button.subsample(1,1)      #маштабируем кнопку


#Button(tk, image=our_button, highlightthickness=0, bd=0, command= lambda: print("КНОПКА НАЖАТА")).place(x=130, y=150)








canvas.pack()  # запаковали кэнвас


#canvas.create_text(150, 150, text="ПРИВЕТ", font=("Arial", 30))  # текст


#ttk.Entry().pack(anchor=E, padx=8, pady= 8)




import folium
import winsound


m = folium.Map(location=[47.5236, 36.6750], zoom_start=7)



x1=47.9236
y1=36.6750
x2=47.5236
y2=36.6750
x3=47.1236
y3=36.6750
x4=47.2236
y4=35.6750
q4='Тестовая цель',x4,y4


#folium.Marker([59.938732, 30.316229], popup='a_', tooltip=a).add_to(m)
#folium.Marker([59.998732, 30.396229], popup='b_', tooltip=b).add_to(m)
#folium.Marker([69.001645, 103.694781], popup='c_', tooltip=c).add_to(m)


#Button(tk, image=our_button, highlightthickness=0, bd=0, command= lambda: print("КНОПКА НАЖАТА")).place(x=130, y=150)
def click_button():

    m.add_child(
        folium.Marker(
            location=[x4, y4],
            popup=q4,
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(m))
    m.save('name.html')
    print("чщорошо")
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    winsound.PlaySound("*", winsound.SND_ALIAS)
    output_file = "name.html"
    webbrowser.open(output_file, new=2)





Button(tk, image=our_button, highlightthickness=0, bd=0, command = click_button).place(x=130, y=150)

Button(tk, image=our_button2, highlightthickness=0, bd=0, command = www).place(x=580, y=150)

#folium.Marker([59.938732, 30.316229], popup="Camp Muir").add_to(m)
m.add_child(
    folium.Marker(
    location=[x1, y1],
    popup="пост№1",
    icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m))

m.add_child(
    folium.Marker(
    location=[x2, y2],
    popup="пост№2",
    icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m))

m.add_child(
    folium.Marker(
    location=[x3, y3],
    popup="пост№3",
    icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m))







m.save('name.html')

tk.mainloop()  # запускает эти приложения

