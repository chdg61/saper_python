# coding=utf-8
from Saper.ceil import Ceil


class Row(object):
    """
    Класс строк
    """
    number_row = 0

    def __init__(self, number_row):
        """
        :param number_row: Номер строки
        :type number_row: int
        """
        self.number_row = int(number_row)
        self.list_ceil = []

    def add_ceil(self, ceil):
        """
        Добавляет ячейку в строку
        :param ceil: ячейка
        :type ceil: Ceil
        :rtype: Ceil
        """
        self.list_ceil.insert(ceil.number_in_row, ceil)
        self.list_ceil[ceil.number_in_row].row = self
        return self.list_ceil[ceil.number_in_row]

    def get_ceil(self, number_ceil):
        """
        Получает объект ячейки в строке
        :type number_ceil: int
        :rtype: bool or Ceil
        """
        try:
            number_ceil = int(number_ceil)
            return self.list_ceil[number_ceil]
        except:
            return False

    def get_list_ceil(self):
        """
        Возвращает список ячеек строки
        :rtype list
        """
        return self.list_ceil