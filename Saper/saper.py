# coding=utf-8
import random
from Saper.gui import GUI
from Saper.ceil import Ceil
from Saper.row import Row
from Saper.constants import *


class Saper(object):
    # Число проставленных мин пользователя
    count_selected_mine = 0

    def __init__(self, **args):

        # Номера ячеек которые содержат мины
        self.list_numbers_field_for_mine = []

        # Список объектов строк
        self.list_rows = []

        # Объект ячеек с расставленными пользователем минами
        self.list_ceil_on_selected_mine = []

        self.gui = GUI()

        self.gui.show_all_count_mine()

        # рассчет мин
        self.create_mine()

    def create_mine(self):
        """
        Создание поля случайных мин
        """

        # формируем случайные мины на поле
        self.create_random_mine()

        # self.__listRows = [Row(number_row) for number_row in range(0,COUNT_ROWS)]

        for number_row in range(0, COUNT_ROWS):
            self.list_rows.insert(number_row, Row(number_row))

            # пробегаем по строкам и создаём объекты ячеек
            for number_ceil in range(0, COUNT_COLUMNS):
                ceil = Ceil(number_ceil, self.gui.tk_frame_main)
                ceil.number_in_all = (number_row * COUNT_COLUMNS) + number_ceil + 1
                ceil.bind(EVENT_LEFT_CLICK, self.left_click)
                ceil.bind(EVENT_RIGHT_CLICK, self.right_click)

                self.list_rows[number_row].add_ceil(ceil)

                if ceil.number_in_all in self.list_numbers_field_for_mine:
                    ceil.is_mine = True

    def create_random_mine(self):
        """
        Формируем случайные мины на поле
        """

        for i in range(0, MINE_COUNT):
            self.list_numbers_field_for_mine.append(self.random_number_ceil_on_mine())

    def random_number_ceil_on_mine(self):
        """
        Генеририрует случайный номер ячейки где будет располагаться мина
        С проверкой его не вхождения в общую базу сгенерированных номеров
        :rtype: int
        """

        random_number_ceil = random.randint(1, COUNT_CEIL)

        if random_number_ceil in self.list_numbers_field_for_mine:
            return self.random_number_ceil_on_mine()
        else:
            return random_number_ceil

    def left_click(self, ceil, event=None):
        """
        Обработка действий при нажатии левой клавиши, открытие полей
        :type ceil: Ceil
        :type event: None or Tkinter.Event
        """

        count_mine = 0

        self.gui.timer_start()

        # если на ячейки стоит что мина
        if ceil.is_user_select_mine:
            return False

        # если ячейка является миной
        if ceil.is_mine:
            self.gui.game_over()
            return False

        list_around_ceil = self.find_around_ceil(ceil)

        for tmpCeil in list_around_ceil:
            if tmpCeil.is_mine:
                count_mine += 1

        ceil.count_mine_around = count_mine
        ceil.is_open = True

        # если ноль мин в ячейки
        if count_mine == 0:
            self.open_ceil_empty(ceil)
            for tmpCeil in list_around_ceil:
                if not tmpCeil.is_mine and not tmpCeil.is_user_select_mine and not tmpCeil.is_open:
                    self.left_click(tmpCeil)
        else:
            self.open_ceil(ceil)

    def right_click(self, ceil, event=None):
        """
        Обработка действий при нажатии правой клавиши, расстановка мин
        :type ceil: Ceil
        :type event: None or Tkinter.Event
        """

        if ceil.is_user_select_mine:
            self.add_selected_mine(ceil)
            self.check_selected_mine(True)
        else:
            self.delete_selected_mine(ceil)
            self.check_selected_mine(False)

    def find_around_ceil(self, ceil):
        """
        Находим ячейки рядом с текущей
        :type ceil: Ceil
        :rtype: list
        """

        list_ceil = []

        # смотрим левую ячейку
        try:
            if ceil.number_in_row > 0:
                tmp_ceil = ceil.row.get_ceil(ceil.number_in_row - 1)
                if tmp_ceil:
                    list_ceil.append(tmp_ceil)
        except:
            pass

        # смотрим правую ячейку
        try:
            tmp_ceil = ceil.row.get_ceil(ceil.number_in_row + 1)
            if tmp_ceil:
                list_ceil.append(tmp_ceil)
        except:
            pass

        # смотрим верхний ряд
        try:
            if ceil.row.number_row > 0:
                tmp_row = self.list_rows[ceil.row.number_row - 1]
                if tmp_row:
                    # смотрим левую верхнюю ячейку
                    try:
                        if ceil.number_in_row > 0:
                            tmp_ceil = tmp_row.get_ceil(ceil.number_in_row - 1)
                            if tmp_ceil:
                                list_ceil.append(tmp_ceil)
                    except:
                        pass

                    # смотрим среднюю верхнюю ячейку
                    try:
                        tmp_ceil = tmp_row.get_ceil(ceil.number_in_row)
                        if tmp_ceil:
                            list_ceil.append(tmp_ceil)
                    except:
                        pass

                    # смотрим правую верхнюю ячейку
                    try:
                        tmp_ceil = tmp_row.get_ceil(ceil.number_in_row + 1)
                        if tmp_ceil:
                            list_ceil.append(tmp_ceil)
                    except:
                        pass
        except:
            pass

        # смотрим нижний ряд
        try:
            tmp_row = self.list_rows[ceil.row.number_row + 1]
            if tmp_row:
                # смотрим левую нижнюю ячейку
                try:
                    if ceil.number_in_row > 0:
                        tmp_ceil = tmp_row.get_ceil(ceil.number_in_row - 1)
                        if tmp_ceil:
                            list_ceil.append(tmp_ceil)
                except:
                    pass

                # смотрим среднюю нижнюю ячейку
                try:
                    tmp_ceil = tmp_row.get_ceil(ceil.number_in_row)
                    if tmp_ceil:
                        list_ceil.append(tmp_ceil)
                except:
                    pass

                # смотрим правую нижнюю ячейку
                try:
                    tmp_ceil = tmp_row.get_ceil(ceil.number_in_row + 1)
                    if tmp_ceil:
                        list_ceil.append(tmp_ceil)
                except:
                    pass
        except:
            pass

        return list_ceil

    def open_ceil_empty(self, ceil):
        """
        Закрашиваем пустую ячейку
        :type ceil: Ceil
        """
        ceil.tk_button.destroy()
        ceil.tk_label['text'] = ""
        ceil.tk_label.grid()

    def open_ceil(self, ceil):
        """
        Закрашиваем ячейку с цифрой
        :type ceil: Ceil
        """

        ceil.tk_button.destroy()
        color_char = COLOR_CHAR.get(ceil.count_mine_around, DEFAULT_COLOR_CHAR)

        ceil.tk_label['text'] = ceil.count_mine_around
        ceil.tk_label['font'] = STYLE_FONT_CEIL
        ceil.tk_label['fg'] = color_char
        ceil.tk_label.grid()

    def add_selected_mine(self, ceil):
        """
        Добавляем ячейку в выбранные пользователем
        :type ceil: Ceil
        """
        self.list_ceil_on_selected_mine.append(ceil)

    def delete_selected_mine(self, ceil):
        """
        Удаляем ячейку из выбранных пользователем
        :type ceil: Ceil
        """
        try:
            self.list_ceil_on_selected_mine.remove(ceil)
        except:
            pass

    def check_selected_mine(self, is_mine):
        """
        учитывает число проставленных мин, для победы
        :type is_mine: bool
        """
        count_rules_mine = 0

        if is_mine:
            self.count_selected_mine += 1
            self.gui.show_selected_count_mine(self.count_selected_mine)
        elif not is_mine:
            self.count_selected_mine -= 1
            self.gui.show_selected_count_mine(self.count_selected_mine)

        # проверям кол-во проставленных и всего и проверяем на правильность
        if self.count_selected_mine == MINE_COUNT:
            for ceil in self.list_ceil_on_selected_mine:
                if ceil.is_mine and ceil.is_user_select_mine:
                    count_rules_mine += 1

            if count_rules_mine == MINE_COUNT:
                self.gui.game_winner()

    def grid(self):
        """
        Структурируем данные
        """
        self.gui.grid()

        for x, row in enumerate(self.list_rows):
            for y, ceil in enumerate(row.get_list_ceil()):
                ceil.grid()

    def show(self):
        """
        Показываем окно
        """
        self.grid()
        self.gui.show()