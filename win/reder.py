from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd


class red:
    def answerfill(n ,name, a1, a2, a3, a4):
        def retern():
            red.var = var.get()
            win.destroy()
        win = Tk()
        win.iconbitmap("icon.ico")
        win.title('Вопрос #{}'.format(n))
        qe =Label(text=name).grid(row=0, columnspan=2)
        l1 = Label(text=a1).grid(row=1, column=1, sticky='w')
        l2 = Label(text=a2).grid(row=2, column=1, sticky='w')
        l3 = Label(text=a3).grid(row=3, column=1, sticky='w')
        l4 = Label(text=a4).grid(row=4, column=1, sticky='w')
        var = IntVar()
        var.set(0)
        r1 = Radiobutton(text="1.", variable=var, value=1).grid(row=1, column=0, sticky='w')
        r2 = Radiobutton(text="2.", variable=var, value=2).grid(row=2, column=0, sticky='w')
        r3 = Radiobutton(text="3.", variable=var, value=3).grid(row=3, column=0, sticky='w')
        r4 = Radiobutton(text="4.", variable=var, value=4).grid(row=4, column=0, sticky='w')
        Button(text='Следующий вопрос', command=retern).grid(row=5)
        win.mainloop()

    def insertText(flag_):
        qestions = [{'count': 0}]
        win = Tk()
        win.iconbitmap("icon.ico")
        win.withdraw()
        flag = 0
        while qestions == [{'count': 0}] and flag < 1:
            try:

                file_name = fd.askopenfilename(filetypes=(("TEST files", "*.test"),
                                                          ("All files", "*.*")))
                with open(file_name, 'r', encoding='utf-8') as f:
                    s = f.read()
                    qestions = eval(s)
            except:
                pass
                # mb.showerror('Ошибочка вышла', 'Данный тест повреждён или составлен неверно')
            flag += 1
        win.destroy()
        return qestions


    def showenty(title='Поле ввода', mesenge='Введите код теста сюда', width=30, bd=2, state='normal'):
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
                red.text = text
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
    def chois(title='Поле выбора', width=30, bd=2, state='normal'):
        def retern():
            chois = var.get()
            print(chois)

            if chois == '' or chois == 0:
                mb.showwarning('Ошибочка вышла', "вы ничего не ввели")
            elif chois == 'o' or chois == 'c' or chois == 'e':
                if chois == 'e':
                    exit()
                elif chois == 'c':
                    win.destroy()
                    red.showenty()
                    red.c = red.text
                elif chois == 'o':
                    red.c = red.insertText(5)
                    win.destroy()
                    # exit()
            elif chois != 'o' or chois != 'c' or chois != 'e':
                mb.showerror('Ошибочка вышла', "вы ошиблись")
            else:
                mb.showerror('Ошибочка вышла', "Произошла ошибка, попробуйте заново")
                exit()


        win = Tk()
        win.iconbitmap("icon.ico")
        win.title(title)
        var = StringVar()
        var.set(5)
        r1 = Radiobutton(text="o", variable=var, value='o', command=retern).grid(row=0, column=1, sticky='w')
        r2 = Radiobutton(text="c", variable=var, value='c', command=retern).grid(row=1, column=1, sticky='w')
        r3 = Radiobutton(text="e", variable=var, value='e', command=retern).grid(row=2, column=1, sticky='w')
        Label(text='Если вы хотите открыть тест нажмите o').grid(row=0)
        Label(text='Если вы хотите вставить код текста нажмите c').grid(row=1)
        Label(text='Если ван надо выключить программу нажмите e').grid(row=2)
        win.bind()
        win.mainloop()