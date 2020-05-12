# try:
if True:
    from win.reder import red
    from tkinter import *
    from tkinter import filedialog as fd
    from tkinter import messagebox as mb
    from time import sleep as sp
    import webbrowser as wb

    qestions = [{'count': 0}]
    flag_file = False

    # Дешифратор + переобразование в удобную форму
    red.chois()
    qestions = red.c

    if qestions == [{'count': 0}]:
        flag_file = False
    else:
        flag_file = TRUE
    if flag_file == True:
        try:
            count = (qestions[0]['count'])
        except:
            win = Tk()
            win.iconbitmap("icon.ico")
            win.withdraw
            mb.showerror('Ошибочка вышла', 'Данный тест повреждён или составлен неверно, попробуйте занаво')
            exit(28)
            win.mainloop()
        if count == 0:
            win = Tk()
            win.iconbitmap("icon.ico")
            win.withdraw
            mb.showerror('Ошибочка вышла', 'Данный тест пустой')
            exit(35)
            win.mainloop()
        elif count <= 0:
            win = Tk()
            win.iconbitmap("icon.ico")
            win.withdraw
            mb.showerror('Ошибочка вышла', 'Данный тест повреждён или составлен неверно, попробуйте занаво')
            exit(42)
            win.mainloop()
        elif count > 20:
            win = Tk()
            win.iconbitmap("icon.ico")
            win.withdraw
            mb.showerror('Ошибочка вышла', 'Данный тест слишком большой или произошла ошибка, попробуйте занаво')
            exit(49)
            win.mainloop()
        else:
            flag_c = 0
            for i in range(1, (count + 1)):
                try:
                    el = (qestions[i])[0]
                    number = el['n']
                    name = el['q']
                    answer = el['a']
                    a1 = answer[0]
                    a2 = answer[1]
                    a3 = answer[2]
                    a4 = answer[3]
                    c = el['c']
                    if number != i:
                        win = Tk()
                        win.iconbitmap("icon.ico")
                        win.withdraw
                        mb.showerror('Ошибочка вышла', 'Данный тест повреждён или составлен неверно, попробуйте занаво')
                        exit(69)
                        win.mainloop()

                    red.answerfill(number, name, a1, a2, a3, a4)
                    try:
                        if red.var == c:
                            flag_c += 1
                    except:
                        exit(77)

                except:
                    win = Tk()
                    win.iconbitmap("icon.ico")
                    win.withdraw()
                    mb.showerror('Ошибочка вышла', 'Данный тест повреждён или составлен неверно, попробуйте занав  о')
                    exit(84)
                    win.mainloop()
            if flag_c < (count // 2):
                res = 'полхой'
            elif flag_c > (count // 2) and flag_c < count:
                res = 'нормальный'
            elif flag_c == count:
                res = 'отличный'
            else:
                res = 'неопределённый'
            winc = Tk()
            winc.iconbitmap("icon.ico")
            winc.withdraw()
            mb.showinfo('Поздравляем, Вы оконьчили тест', 'Вы ответили верно на {} вопросов из {} вопросов, это {} результат.'.format(flag_c, count,res))
            url = 'https://www.donationalerts.com/widget/corona?token=NtUC9GH5XO7flPcoY6ZS'
            wb.open(url)
            winc.mainloop()
    else:
        win = Tk()
        win.iconbitmap("icon.ico")
        win.withdraw()
        mb.showerror('Ошибочка вышла', 'не удалось открыть тест или в программе произашла ошибка попробуйте заново')
        win.mainloop()
        exit(107)
    win = Tk()
    win.iconbitmap("icon.ico")
    win.destroy()
    win.mainloop()

# except:
#     win = Tk()
#     win.iconbitmap("icon.ico")
#     win.withdraw()
#     mb.showerror('Ошибочка вышла', 'в программе произашла ошибка попробуйте заново')
#     exit(118)
#     win.mainloop()
