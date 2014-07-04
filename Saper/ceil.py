# coding=utf-8
import Tkinter
import os
from Saper.constants import *


class Ceil(object):
    """
    Класс ячейки
    """

    number_in_row = 0

    number_in_all = 0
    """ Номер ячейки по порядку, среди всех ячеек """

    is_mine = False
    is_open = False

    is_user_select_mine = False
    """ Поставил ли пользователь сюда мину или нет """

    count_mine_around = 0
    """ кол-во мин вокруг ячейки """

    _row = None
    """ :type: Saper.Row """

    event_right_click = None
    event_left_click = None

    def __init__(self, number_in_row, tk_frame_parent):
        """
        :param number_in_row: Номер в строке
        :type number_in_row:  int
        :param tk_frame_parent: Основной Frame Tkinter
        :type tk_frame_parent:  Tkinter.Frame
        """
        self.number_in_row = int(number_in_row)

        self.tk_frame = Tkinter.Frame(tk_frame_parent, width=SIZE_CEIL, height=SIZE_CEIL)
        self.tk_button = Tkinter.Button(self.tk_frame)
        self.tk_button.bind(EVENT_LEFT_CLICK, self.left_click)
        self.tk_button.bind(EVENT_RIGHT_CLICK, self.right_click)
        self.tk_label = Tkinter.Label(self.tk_frame)

    @property
    def row(self):
        """
        :rtype: Saper.Row
        """
        return self._row

    @row.setter
    def row(self, row):
        """
        Задаём строчку ячейки
        :type row: Saper.Row
        """
        self._row = row

    def left_click(self, event):
        if self.event_left_click:
            self.event_left_click(self, event)

    def right_click(self, event):
        if self.is_open:
            return False

        if not self.is_user_select_mine:
            self.tk_button.configure(image=self.get_image_flag(), state=Tkinter.DISABLED, disabledforeground="#00FF00")
            self.is_user_select_mine = True
        else:
            self.tk_button.configure(image="", state=Tkinter.NORMAL)
            self.is_user_select_mine = False

        if self.event_right_click:
            self.event_right_click(self, event)

    @classmethod
    def get_image_flag(cls):
        try:
            return cls.tk_image_flag
        except:
            current_directory = os.path.dirname(os.path.abspath(__file__))
            flag_gif = current_directory + "/data/flag.gif"
            cls.tk_image_flag = Tkinter.PhotoImage(file=flag_gif, width=19, height=19)
            return cls.tk_image_flag

    def grid(self):
        self.tk_frame.grid(row=int(self.row.number_row), column=int(self.number_in_row), padx=PADDING_BETWEEN_CEIL,
                           pady=PADDING_BETWEEN_CEIL)
        self.tk_button.grid(sticky=Tkinter.NSEW)
        self.tk_frame.rowconfigure('all', minsize=SIZE_CEIL)
        self.tk_frame.columnconfigure('all', minsize=SIZE_CEIL)

    def bind(self, event, function):
        if event == EVENT_RIGHT_CLICK:
            self.event_right_click = function
        elif event == EVENT_LEFT_CLICK:
            self.event_left_click = function
