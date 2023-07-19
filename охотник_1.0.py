import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # эти библиотеки для формы
import webbrowser
import folium
import folium as folium
import winsound

def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения"):
        tk.destroy()  # всплывающее укно с нозванием и текстом

def show_message():
    label6["text"] = entry6.get()  # получаем введенный текст
    label5["text"] = entry5.get()
    label4["text"] = entry4.get()
    label3["text"] = entry3.get()
    label2["text"] = entry2.get()
    label1["text"] = entry1.get()

tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)  # при наступлении этого события, вызывается функция on_closing
tk.title("ОХОТНИК win_1.0")
tk.geometry("480x760")
tk.wm_attributes("-topmost", 1)  # поверх всех окон
tk.iconbitmap("gc.ico")  # добавление иконки приложения




entry1 = ttk.Entry()
entry1.pack(anchor=NE, padx=6, pady=6)
entry2 = ttk.Entry()
entry2.pack(anchor=NE, padx=6, pady=6)
entry3 = ttk.Entry()
entry3.pack(anchor=NE, padx=6, pady=6)
entry4 = ttk.Entry()
entry4.pack(anchor=NE, padx=6, pady=6)
entry5 = ttk.Entry()
entry5.pack(anchor=NE, padx=6, pady=6)
entry6 = ttk.Entry()
entry6.pack(anchor=NE, padx=6, pady=6)

btn = ttk.Button(text="Сохранить", command=show_message)
btn.pack(anchor=N, padx=6, pady=6)

label1 = ttk.Label()
label1.pack(anchor=NW, padx=6, pady=6)
label2 = ttk.Label()
label2.pack(anchor=NW, padx=6, pady=6)
label3 = ttk.Label()
label3.pack(anchor=NW, padx=6, pady=6)
label4 = ttk.Label()
label4.pack(anchor=NW, padx=6, pady=6)
label5 = ttk.Label()
label5.pack(anchor=NW, padx=6, pady=6)
label6 = ttk.Label()
label6.pack(anchor=NW, padx=6, pady=6)

lbl1 = Label(tk, text="ПОСТ№1", font=("Times New Roman", 28))
lbl1.place(x=20, y=15)

lbl2 = Label(tk, text="ПОСТ№2", font=("Times New Roman", 28))
lbl2.place(x=20, y=75)

lbl3 = Label(tk, text="ПОСТ№3", font=("Times New Roman", 28))
lbl3.place(x=20, y=140)

lbl4 = Label(tk, text="x=", font=("Times New Roman", 14))
lbl4.place(x=185, y=4)

lbl5 = Label(tk, text="y=", font=("Times New Roman", 14))
lbl5.place(x=185, y=37)

lbl5 = Label(tk, text="x=", font=("Times New Roman", 14))
lbl5.place(x=185, y=70)

lbl6 = Label(tk, text="y=", font=("Times New Roman", 14))
lbl6.place(x=185, y=103)

lbl7 = Label(tk, text="x=", font=("Times New Roman", 14))
lbl7.place(x=185, y=135)

lbl8 = Label(tk, text="y=", font=("Times New Roman", 14))
lbl8.place(x=185, y=170)

our_button = PhotoImage(file="test.png")    #добавляем картинку (кнопку)
our_button = our_button.subsample(2,2)      #маштабируем кнопку

#our_button2 = PhotoImage(file="knopka.png")    #добавляем картинку (кнопку)
#our_button2 = our_button.subsample(1,1)      #маштабируем кнопку

m = folium.Map(location=[47.5236, 36.6750], zoom_start=7) # НАЧАЛО КАРТЫ ЗДЕСЬ


x1=47.3827
y1=36.3850
x2=47.3736
y2=36.3750
x3=47.3538
y3=36.3541
x4=47.2336
y4=35.6750
q1='Пост№1',x1,y1
q2='Пост№2',x2,y2
q3='Пост№3',x3,y3
q4='Тестовая цель',x4,y4

def click_button():

    m.add_child(
        folium.Marker(
            location=[x4, y4],
            popup=q4,
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(m))
    m.save('name.html')
    print("xорошо")
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    winsound.PlaySound("*", winsound.SND_ALIAS)
    output_file = "name.html"
    webbrowser.open(output_file, new=2)

#def www():
   # print(label1["text"])
   # print(label2["text"])
   # print(label3["text"])
   # print(label4["text"])
   # print(label5["text"])
   # print(label6["text"])

Button(tk, image=our_button, highlightthickness=0, bd=0, command = click_button).place(x=130, y=240)

#Button(tk, image=our_button2, highlightthickness=0, bd=0, command = www).place(x=130, y=450)


m.add_child(
    folium.Marker(
    location=[x1, y1],
    popup=q1,
    icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m))

m.add_child(
    folium.Marker(
    location=[x2, y2],
    popup=q2,
    icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m))

m.add_child(
    folium.Marker(
    location=[x3, y3],
    popup=q3,
    icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m))

# ИНФА
image = PhotoImage(file="info45.png")


label = Label(tk, image=image)
#label.pack()

# РАСЧЕТЫ

xxx = 111.3 * math.cos(math.radians((x2+x1)/2)) # один градус равен этому числу в км. по широте
yyy = 111.4

# AB
yAB = x2-x1 # разность x в координатах
xAB = y2-y1 # разyность y в координатах
xryyy = xAB * xxx # расстояние  x в километрах
yrxxx = yAB * yyy # расстояние y в километрах
xryyy2 = xryyy * xryyy # в степени
yrxxx2 = yrxxx * yrxxx # в степени
ABB = xryyy2 + yrxxx2 # сумма
AB = math.sqrt(ABB) # корень из

#BC
yBC = x3-x2 # разность x в координатах
xBC = y3-y2 # разyность y в координатах
xryyyBC = xBC * xxx # расстояние  x в километрах
yrxxxBC = yBC * yyy # расстояние y в километрах
xryyy2BC = xryyyBC * xryyyBC # в степени
yrxxx2BC = yrxxxBC * yrxxxBC # в степени
BCC = xryyy2BC + yrxxx2BC # сумма
BC = math.sqrt(BCC) # корень из

yAC = x3-x1 # разность x в координатах
xAC = y3-y1 # разyность y в координатах
xryyyAC = xAC * xxx # расстояние  x в километрах
yrxxxAC = yAC * yyy # расстояние y в километрах
xryyy2AC = xryyyAC * xryyyAC # в степени
yrxxx2AC = yrxxxAC * yrxxxAC # в степени
ACC = xryyy2AC + yrxxx2AC # сумма
AC = math.sqrt(ACC) # корень из

#ЗДЕСЬ НЕОБХОДИМО СДЕЛАТЬ КОРЕКТИРОВКУ ПОСТРОЕНИЯ В ОДНУ ЛИНИЮ ТРЕТЬЕЙ КООРДИНАТЫ
zzz = xAB*yAC/yAB # расстояние корректировки
y5 = y1 + zzz


yCC1 = x3 # разность x в координатах
xCC1 = y5-y3 # разyность y в координатах
xryyyCC1 = xCC1 * xxx # расстояние  x в километрах
yrxxxCC1 = yCC1 * yyy # расстояние y в километрах
xryyy2CC1 = xryyyCC1 * xryyyCC1 # в степени
yrxxx2CC1 = yrxxxCC1 * yrxxxCC1 # в степени
CC1 = xryyy2CC1 + yrxxx2CC1 # сумма
CCC1 = math.sqrt(CC1) # корень из


q5='Корректировка',x3,y5
m.add_child(
    folium.Marker(
    location=[x3, y5],
    popup=q5,
    icon=folium.Icon(color="green", icon="info-sign"),
    ).add_to(m))




a = AB
b = BC
c = AC
k = CCC1 # корректировка в КМ
v = 0.331 # скорость звука.


print(a)
print(b)
print(c)
print(zzz)



#dt1 = tb-ta
#dt2 = tc-ta

dt1 = 78.381 # ПРИМЕР Тест
dt2 = 0.000000001  # ПРИМЕР Тест

a1 = 2*v*dt1
a2 = 2*v*dt2
b1 = 2*a
b2 = 2*(a+b)
c1 = (a*a)-((v*dt1)*(v*dt1))
c2 = ((a+b)*(a+b))-((v*dt2)*(v*dt2))

xx2 = ((c2*a1)-(a2*c1))/((a1*b2)-(a2*b1))
xx1 = (c1-(b1*xx2))/a1
d = xx1

cosX = ((c1-(a1*d))/(b1*d))
cosX2 = math.acos(cosX)
cosX3 = math.fabs(cosX) # из минуса в плюс
l=math.acos(cosX3)*(180/math.pi) # из радианов в градусы

#print(a)
#print(b)
#print(d)
#print(l)

m.save('name.html')
tk.mainloop()
