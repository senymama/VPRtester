from tkinter import *
from tkinter import messagebox as mb

class entrys:
    def showenty(title='Поле ввода', mesenge='' , width=30, bd=2, state='normal'):
        def retern():
            text = entry.get()
            while text == 0:
                try:
                    text = float(text)
                    # if text < 1 or text > 10:
                    #     mb.showerror(message='Число должно быть в промежутке от 1 до 10')
                    #     win.destroy()
                except:
                    mb.showerror('Ошибочка вышла', 'должно быть введенно число')
            if text == '' or text == 0:
                pass
                mb.showwarning('Ошибочка вышла', "вы ничего не ввели")
            else:
                entrys.text = text
                entry.delete(0, END)
                win.destroy()

        win = Tk()
        win.iconbitmap("icon.ico")
        win.title(title)
        entry = Entry(width=width, bd=bd, state=state)
        Label(text=mesenge, width=35).grid(row=0)
        entry.grid(row=1)
        Button(text='Передать', command=retern).grid(row=2)
        win.bind()
        win.mainloop()
    def destroy(win):
        win.iconbitmap("icon.ico")
        win.destroy()
    def qest(number=1):
        qestion = []
        entrys.qestion = qestion
        entrys.numberasd = number
        def check():
            number = entrys.numberasd
            c = entrys.Casd
            win.title('Вопрос #{}'.format(number))
            try:
                a1, a2, a3, a4, name, c = e1.get(), e2.get(), e3.get(), e4.get(), entry.get(), var.get()
                entrys.Casd = c
            except:
                pass
            if a1 != '' and a2 != "" and a3 != '' and a4 != '' and name != '' and c != 0:
                q = {'n': number, 'q': name, 'a': [a1, a2, a3, a4], 'c': c}
                qestion = entrys.qestion
                qestion.append(q)
                entrys.qestion = qestion
                print(q)
                print('Вопрос #{}: {} Ответы на вопрос: 1.{} 2.{} 3.{} 4.{} Правильный ответ под номером {}'.format
                      (number, name, a1, a2, a3, a4, c))
                entry.delete(0, END)
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                number += 1
                win.title('Вопрос #{}'.format(number))
                var.set(0)
                entrys.destroy(win)
            else:
                if a1 == '' and a2 == "" and a3 == '' and a4 == '' and name == '' and c == 0:
                    mb.showwarning('Ошибочка вышла', "Обязательно заполнить все поля")
                elif a1 == "" or a2 == '' or a3 == "" or a4 == "":
                    mb.showerror('Ошибочка вышла', "Обязательно заполнить все поля для ответов")
                elif name == "":
                    mb.showwarning('Ошибочка вышла', "Обязательно заполнить поле для вопроса")
                elif c == '' or c == 0:
                    mb.showwarning('Ошибочка вышла', "Вы не выбрали правильный ответ")
                else:
                    mb.showwarning('Ошибочка вышла', "вы ничего не ввели")

        a1, a2, a3, a4, name = '', '', '', '', ''
        c = 0
        entrys.Casd = c
        win = Tk()
        win.iconbitmap("icon.ico")
        entrys.win = win
        # rbwin.withdraw()
        var = IntVar()
        var.set(0)
        r1 = Radiobutton(text="", variable=var, value=1)
        r2 = Radiobutton(text="", variable=var, value=2)
        r3 = Radiobutton(text="", variable=var, value=3)
        r4 = Radiobutton(text="", variable=var, value=4)
        r1.grid(row=3, column=2)
        r2.grid(row=4, column=2)
        r3.grid(row=5, column=2)
        r4.grid(row=6, column=2)
        win.title('Вопрос #{}'.format(number))
        # win.withdraw()
        entry = Entry(width=30, bd=2)
        Label(text="Введите вопрос").grid(row=0)
        entry.grid(row=1)
        e1 = Entry(width=30, bd=2)
        e2 = Entry(width=30, bd=2)
        e3 = Entry(width=30, bd=2)
        e4 = Entry(width=30, bd=2)
        Label(text="Введите Варианты ответа").grid(row=2)
        e1.grid(row=3)
        e2.grid(row=4)
        e3.grid(row=5)
        e4.grid(row=6)
        Button(text='Передать', command=check).grid(row=7)
        win.mainloop()
