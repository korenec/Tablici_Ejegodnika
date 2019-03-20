from tkinter import *


class PageOption(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        self.frames = {}
        list_page = [PageOne, PageTwo, PageThree]
        for F in list_page:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.button_level_water = Button(self, text='(1.2) Таблица среднесуточных уровней воды',
                                         command=lambda: controller.show_frame(PageTwo))
        self.button_level_water.pack()

        self.button_consumption = Button(self, text='(1.3) Таблица среднесуточных расходов воды')
        self.button_consumption.pack()


class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.button_level_water = Button(self, text='83026 р.Берда с.Захаровка',
                                         command=lambda: controller.show_frame(PageThree))
        self.button_level_water.pack()


class PageThree(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.scrolling = Scrollbar(self)   # Прокрутка экрана с правой стороны
        self.scrolling.grid(row=0, column=25, rowspan=31, sticky=N+S)

        self.number_day = Label(self, text='1', font='CourierNew 9')
        self.number_day.grid(row=1, column=0)

        self.january1 = Entry(self, width=9, bd=3)
        self.january1.grid(row=1, column=1)

        self.january2 = Entry(self, width=9, bd=3)
        self.january2.grid(row=2, column=1)

        self.january3 = Entry(self, width=9, bd=3)
        self.january3.grid(row=3, column=1)

        self.january4 = Entry(self, width=9, bd=3)
        self.january4.grid(row=4, column=1)

        self.january5 = Entry(self, width=9, bd=3)
        self.january5.grid(row=5, column=1)

        self.january6 = Entry(self, width=9, bd=3)
        self.january6.grid(row=6, column=1)

        self.january7 = Entry(self, width=9, bd=3)
        self.january7.grid(row=7, column=1)

        self.january8 = Entry(self, width=9, bd=3)
        self.january8.grid(row=8, column=1)

        self.january9 = Entry(self, width=9, bd=3)
        self.january9.grid(row=9, column=1)

        self.january10 = Entry(self, width=9, bd=3)
        self.january10.grid(row=10, column=1)

        self.january11 = Entry(self, width=9, bd=3)
        self.january11.grid(row=11, column=1)

        self.january12 = Entry(self, width=9, bd=3)
        self.january12.grid(row=12, column=1)

        self.january13 = Entry(self, width=9, bd=3)
        self.january13.grid(row=13, column=1)

        self.january14 = Entry(self, width=9, bd=3)
        self.january14.grid(row=14, column=1)

        self.january15 = Entry(self, width=9, bd=3)
        self.january15.grid(row=15, column=1)

        self.january16 = Entry(self, width=9, bd=3)
        self.january16.grid(row=16, column=1)

        self.january17 = Entry(self, width=9, bd=3)
        self.january17.grid(row=17, column=1)

        self.january18 = Entry(self, width=9, bd=3)
        self.january18.grid(row=18, column=1)

        self.january19 = Entry(self, width=9, bd=3)
        self.january19.grid(row=19, column=1)

        self.january20 = Entry(self, width=9, bd=3)
        self.january20.grid(row=20, column=1)

        self.january21 = Entry(self, width=9, bd=3)
        self.january21.grid(row=21, column=1)

        self.january22 = Entry(self, width=9, bd=3)
        self.january22.grid(row=22, column=1)

        self.january23 = Entry(self, width=9, bd=3)
        self.january23.grid(row=23, column=1)

        self.january24 = Entry(self, width=9, bd=3)
        self.january24.grid(row=24, column=1)

        self.january25 = Entry(self, width=9, bd=3)
        self.january25.grid(row=25, column=1)

        self.january26 = Entry(self, width=9, bd=3)
        self.january26.grid(row=26, column=1)

        self.january27 = Entry(self, width=9, bd=3)
        self.january27.grid(row=27, column=1)

        self.january28 = Entry(self, width=9, bd=3)
        self.january28.grid(row=28, column=1)

        self.january29 = Entry(self, width=9, bd=3)
        self.january29.grid(row=29, column=1)

        self.january30 = Entry(self, width=9, bd=3)
        self.january30.grid(row=30, column=1)

        self.january31 = Entry(self, width=9, bd=3)
        self.january31.grid(row=31, column=1)

        # february

        self.february1 = Entry(self, width=9, bd=3)
        self.february1.grid(row=1, column=3)

        self.february2 = Entry(self, width=9, bd=3)
        self.february2.grid(row=2, column=3)

        self.february3 = Entry(self, width=9, bd=3)
        self.february3.grid(row=3, column=3)

        self.february4 = Entry(self, width=9, bd=3)
        self.february4.grid(row=4, column=3)

        self.february5 = Entry(self, width=9, bd=3)
        self.february5.grid(row=5, column=3)

        self.february6 = Entry(self, width=9, bd=3)
        self.february6.grid(row=6, column=3)

        self.february7 = Entry(self, width=9, bd=3)
        self.february7.grid(row=7, column=3)

        self.february8 = Entry(self, width=9, bd=3)
        self.february8.grid(row=8, column=3)

        self.february9 = Entry(self, width=9, bd=3)
        self.february9.grid(row=9, column=3)

        self.february10 = Entry(self, width=9, bd=3)
        self.february10.grid(row=10, column=3)

        self.february11 = Entry(self, width=9, bd=3)
        self.february11.grid(row=11, column=3)

        self.february12 = Entry(self, width=9, bd=3)
        self.february12.grid(row=12, column=3)

        self.february13 = Entry(self, width=9, bd=3)
        self.february13.grid(row=13, column=3)

        self.february14 = Entry(self, width=9, bd=3)
        self.february14.grid(row=14, column=3)

        self.february15 = Entry(self, width=9, bd=3)
        self.february15.grid(row=15, column=3)

        self.february16 = Entry(self, width=9, bd=3)
        self.february16.grid(row=16, column=3)

        self.february17 = Entry(self, width=9, bd=3)
        self.february17.grid(row=17, column=3)

        self.february18 = Entry(self, width=9, bd=3)
        self.february18.grid(row=18, column=3)

        self.february19 = Entry(self, width=9, bd=3)
        self.february19.grid(row=19, column=3)

        self.february20 = Entry(self, width=9, bd=3)
        self.february20.grid(row=20, column=3)

        self.february21 = Entry(self, width=9, bd=3)
        self.february21.grid(row=21, column=3)

        self.february22 = Entry(self, width=9, bd=3)
        self.february22.grid(row=22, column=3)

        self.february23 = Entry(self, width=9, bd=3)
        self.february23.grid(row=23, column=3)

        self.february24 = Entry(self, width=9, bd=3)
        self.february24.grid(row=24, column=3)

        self.february25 = Entry(self, width=9, bd=3)
        self.february25.grid(row=25, column=3)

        self.february26 = Entry(self, width=9, bd=3)
        self.february26.grid(row=26, column=3)

        self.february27 = Entry(self, width=9, bd=3)
        self.february27.grid(row=27, column=3)

        self.february28 = Entry(self, width=9, bd=3)
        self.february28.grid(row=28, column=3)

        self.february29 = Entry(self, width=9, bd=3)
        self.february29.grid(row=29, column=3)

        self.february30 = Entry(self, width=9, bd=3)
        self.february30.grid(row=30, column=3)

        self.february31 = Entry(self, width=9, bd=3)
        self.february31.grid(row=31, column=3)





root = PageOption()
root.title('Заполнение таблиц ежегодника')
root.geometry('1024x600')


root.mainloop()
