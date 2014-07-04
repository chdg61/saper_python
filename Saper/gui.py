# coding=utf-8
import tkMessageBox
import Tkinter
from Saper.constants import *


class GUI(object, Tkinter.Tk):
    is_grid = False

    _time_begin = 1
    """ начало с 1й секунды """

    _timer_id = False
    """ ID интервала таймера """

    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.title(WINDOW_TITLE)
        self.geometry("%sx%s" % (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.tk_frame_toolbar = Tkinter.Frame(self, width=WINDOW_WIDTH, height=WINDOW_TOOLBAR_HEIGHT, background="grey",
                                              relief=Tkinter.GROOVE, border=2)

        self.tk_frame_main = Tkinter.Frame(self, width=WINDOW_WIDTH, height=(WINDOW_HEIGHT - WINDOW_TOOLBAR_HEIGHT),
                                           background=WINDOW_MAIN_FRAME_COLOR_BACKGROUND, relief=Tkinter.GROOVE,
                                           border=2)

        self.tk_label_timer = Tkinter.Label(self.tk_frame_toolbar, text="0000")
        self.tk_label_timer.grid(row=0, column=0, sticky=Tkinter.NSEW)

        self.tk_label_button_new = Tkinter.Button(self.tk_frame_toolbar, text="NEW")
        self.tk_label_button_new.grid(row=0, column=1, sticky=Tkinter.NSEW)

        self.tk_label_counter = Tkinter.Label(self.tk_frame_toolbar, text="00/00")
        self.tk_label_counter.grid(row=0, column=2, sticky=Tkinter.NSEW)

    def show_all_count_mine(self):
        """
        Показываем общее число мин на панели
        """
        self.tk_label_counter['text'] = "00/%2d" % MINE_COUNT

    def show_selected_count_mine(self, selected_mine):
        """
        Показываем расставленное число мин на панели
        :type selected_mine: int
        """
        self.tk_label_counter['text'] = "%2d/%2d" % (selected_mine, MINE_COUNT)

    def timer_start(self):
        """
        Включает таймер игры
        """
        if not self._timer_id and self._time_begin == 1:
            self.timer()

    def timer_stop(self):
        """
        Выключает таймер игры
        """
        if self._timer_id:
            self.tk_label_timer.after_cancel(self._timer_id)
            self._timer_id = False

    def timer(self):
        self.tk_label_timer['text'] = "%0004d" % self._time_begin
        self._time_begin += 1
        self._timer_id = self.tk_label_timer.after(1000, self.timer)

    def game_over(self):
        """
        Показываем окно с поражением
        :return:
        :rtype: bool
        """
        self.timer_stop()
        tkMessageBox.showerror(GAME_OVER_WINDOW_TITLE, GAME_OVER_MESSAGE)
        return False

    def game_winner(self):
        """
        Показываем окно с победой
        :return:
        :rtype: bool
        """
        self.timer_stop()
        tkMessageBox.showinfo(WINNER_WINDOW_TITLE, WINNER_MESSAGE)
        return False

    def grid(self):
        super(GUI, self).grid()
        self.tk_frame_toolbar.grid(row=0, column=0)

        self.tk_frame_toolbar.rowconfigure('all', minsize=WINDOW_TOOLBAR_HEIGHT)

        width_label_toolbar = (float(WINDOW_WIDTH - WINDOW_TOOLBAR_HEIGHT)) / 2.0
        self.tk_frame_toolbar.columnconfigure(0, minsize=width_label_toolbar - 5)
        self.tk_frame_toolbar.columnconfigure(1, minsize=WINDOW_TOOLBAR_HEIGHT)
        self.tk_frame_toolbar.columnconfigure(2, minsize=width_label_toolbar - 5)

        self.tk_frame_main.grid(row=1, column=0)
        self.is_grid = True

    def show(self):
        if not self.is_grid:
            self.grid()
        self.mainloop()