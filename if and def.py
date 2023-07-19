m=["апельсин ","обезьяна ","банан ","вишня ","BAR ","7 "]
from random import randint
s=int(input("Введите сумму, которую хотите поставить"))
l=1
while s>=0 and l==1:
    a = int(randint(0, 5))
    x = m[a]
    b = int(randint(0, 5))
    y = m[b]
    c = int(randint(0, 5))
    z = m[c]
    K = []
    K.append(x)
    K.append(y)
    K.append(z)
    print(K)
    if a == b and b == c and a == c:
        if a == 5:
            print("ДЖЕКПОТ!!!")
            s = s * 1000000
        else:
            print("ВЫИГРЫШ")
            s = s * 5
    else:
        print("ПРОИГРЫШ")
        s = s - 100
    print("У ВАС НА СЧЕТУ", s, "РУБЛЕЙ")
    q = "s"
    q1 = "ы"
    w = input()
    if w == q or w == q1:
        l = 1
    else:
        l=0
if s<0:
    print("У ВАС НА СЧЕТУ НЕ ДОСТАТОЧНО СРЕДСТВ")












