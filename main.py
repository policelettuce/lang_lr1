from sys import exit

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
    global FLLW_A_dd
    global pointer
    c = getchar()
    while True:                     #Крутимся в этой функции, пока не найдем какой-то отличный от "a" символ
        if c != "a":                #По грамматике мы можем иметь сколько угодно символов "a" подряд
            if c not in FLLW_A_dd:  #Если нашли отличный от "а" символ:
                error()             #1) Он не принадлежит FLLW(A) - слово не валидное
            else:                   #2) Он принадлежит FLLW(A) - выходим из этой функции в некст
                pointer -= 1
                return
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
    global FLLW_B_dd
    global pointer
    c = getchar()
    while True:
        if c != "b":
            if c not in FLLW_B_dd:
                error()
            else:
                pointer -= 1
                return
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
    global FLLW_C_dd
    global pointer
    c = getchar()
    while True:
        if c != "c":
            if c not in FLLW_C_dd:
                error()
            else:
                pointer -= 1
                return
        c = getchar()


def getchar():
    global pointer
    global str1
    c = str1[pointer]
    pointer += 1
    return c


def error():
    print("ERROR OCCURRED\nstr: ", str1, "\npointer value: ", pointer, "\n")
    print(str1 + " is not a part of No4 grammar")
    exit()


if __name__ == "__main__":
    FLLW_A_dd = ["$", "b"]
    FLLW_B_dd = ["$"]
    FLLW_C_dd = ["b"]
    global pointer
    global str1
    print("Enter a line like abaa$, where $ - EOF symbol")
    str1 = input()
    pointer = 0
    S()
    print("Success!", str1, "is a part of No4 grammar")
