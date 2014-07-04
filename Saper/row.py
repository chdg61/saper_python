# coding=utf-8
from Saper.ceil import Ceil

class Row(object):
    """
    Класс строк
    """

    number = 0

    def __init__(self,number_row):
        self.number = int(number_row)
        self.__listCeilList = []


    def createCeil(self, number_ceil):
        """
        Создаёт ячейку в строку
        :param number_ceil:
        :return:
        """

        number_ceil = int(number_ceil)

        self.__listCeilList.insert(number_ceil,Ceil(number_ceil))
        self.__listCeilList[number_ceil].setRow(self)
        return self.__listCeilList[number_ceil]


    def getCeil(self,number_ceil):
        """
        Получает объект ячейки в строке
        :param number_ceil:
        :return:
        """
        try:
            number_ceil = int(number_ceil)
            return self.__listCeilList[number_ceil]
        except:
            return False

    def getListCeil(self):
        """
        Возвращает объект списка ячеек
        :rtype Saper.ceil.Ceil[]
        :return:
        """
        return self.__listCeilList

    def getNumber(self):
        return int(self.number)