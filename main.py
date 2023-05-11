def S():
    c = getchar()                   #в этой грамматике все строки начинаются с "a"
    if c != "a":
        error()
    S_dash()
    c = getchar()
    if c != '$':                    # $ - символ конца строки
        error()


def S_dash():
    c = getchar()
    if c == "b":
        A()
    elif c == "c":
        A()
        B()
    elif c == "a":
        C()
        B()
    else:
        error()


def A():
    c = getchar()
    if c != "a":                    #если мы встретили нетерминал "А" - сначала точно идет терминал "а"
        error()
    A_doubledash()


def A_dash():                       #unused lol, оставил для вида
    c = getchar()                   #A' - промежуточный этап между итерациями A''
    if c != "a":                    #поэтому single-dash функции в коде мы полностью скипаем
        error()
    A_doubledash()


def A_doubledash():                 #В данной грамматике мы можем добавить сколько угодно "а", но только идущих подряд
    c = getchar()                   # A > aA'' > aA' > aaA'' > aaA' > aaaA''... > aaae
    while c != "e":                 #"e" - эпсилон
        if c != "a":                #проходим через символы "a", пока не найдем "е"
            error()                 #нашли "е" - функция А() закончилась
        c = getchar()


def B():
    c = getchar()
    if c != "b":
        error()
    B_doubledash()


def B_dash():
    c = getchar()
    if c != "b":
        error()
    B_doubledash()


def B_doubledash():                 #аналогично функции А()
    c = getchar()
    while c != "e":
        if c != "b":
            error()
        c = getchar()


def C():
    c = getchar()
    if c != "c":
        error()
    C_doubledash()


def C_dash():
    c = getchar()
    if c != "c":
        error()
    C_doubledash()


def C_doubledash():                 #аналогично функции A()
    c = getchar()
    while c != "e":
        if c != "c":
            error()
        c = getchar()


def getchar():
    global pointer
    global str1
    c = str1[pointer]
    pointer += 1
    return c


def error():
    print("ERROR OCCURRED\nstr: ", str1, "\npointer value: ", pointer)
    raise Exception()


if __name__ == "__main__":
    global pointer
    global str1
    print("Enter a line like abaae$, where $ - EOF symbol")
    str1 = input()
    pointer = 0
    S()
    print("Success!", str1, "is a part of №4 grammar")
