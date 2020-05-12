# try:
if True:
    from win.wi import entrys
    from tkinter import *
    from tkinter import filedialog as fd
    from tkinter import messagebox as mb


    def extractText():
        try:
            win = Tk()
            win.withdraw()
            win.iconbitmap("icon.ico")

            file = fd.asksaveasfilename(defaultextension=".test", filetypes=(("TEST files", "*.test"),
                                                    ("All files", "*.*")))
            s = str(qestions)
            with open(file, 'w', encoding='utf-8') as data:
                data.write(s)
            win.mainloop()
        except FileNotFoundError:
            pass


    ans = 0
    flag_ans = 0
    while( ans < 1 or ans > 20 ) and flag_ans < 3:
        try:
            entrys.text = 0
            flag_ans += 1
            entrys.showenty(title='Поле ввода', mesenge='Введите число от 1 до 20', width=10, bd=4, state='normal')
            ans = int(entrys.text)
            print(ans)
        except:
            win = Tk()
            win.withdraw
            win.iconbitmap("icon.ico")
            mb.showerror('Ошибочка вышла', 'Произошла ошибка, попробуйте заново')
            exit()
            win.mainloop()
    if ans == 0:
        exit()


    qestions = [{'count':ans}]
    for i in range(1, (ans+1)):
        print(i)
        entrys.qest(i)

        qestions.append(entrys.qestion)
    print(qestions)

    win = Tk()
    win.withdraw()
    win.iconbitmap("icon.ico")
    extractText()
    mb.showinfo('Инфо для пользователя', 'Сохраненно успешно')
# except:
#     mb.showerror('Ошибочка вышла', 'В программе произошла ошибка попробуйте заново')