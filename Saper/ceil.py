# coding=utf-8
import Tkinter
import os

class Ceil(object):
    """
    Класс ячейки
    """

    width = 35
    """ :type: int """

    height = 35
    """ :type: int """

    padding = 1
    """ :type: int """

    __numberInRow = 0

    __numberOnAllCeil = 0
    """ Номер ячейки по порядку, среди всех ячеек """

    __isMine = False
    __isOpen = False
    __numberMineAround = 0
    __userSelectIsMine = False
    __countMineAround = 0
    __obRow = False

    __eventRightClick = None
    __eventLeftClick = None

    def __init__(self,number_ceil_in_row):
        self.__numberInRow = int(number_ceil_in_row)

    def setMine(self,is_mine):
        """
        Задаём, что ячейка является миной
        :param is_mine:
        :return:
        """
        self.__isMine = type(is_mine) == bool and is_mine == True

    def isMine(self):
        """
        Проверка является ли ячейка миной
        :return:
        """
        return self.__isMine

    def setRow(self,obRow):
        """
        Задаём строчку ячейки
        :param obRow: Saper.row.Row
        :return:
        """
        self.__obRow = obRow

    def getRow(self):
        """
        :return:Saper.row.Row
        """
        return self.__obRow

    def setNumber(self, number_ceil):
        """
        Задать номер ячейки среди всех ячеек вообще
        :param number_ceil:
        :return:
        """
        self.__numberOnAllCeil = int(number_ceil)

    def getNumber(self):
        return self.__numberOnAllCeil

    def getNumberInRow(self):
        """
        Получить номер ячейки в строке
        :return:
        """
        return self.__numberInRow

    def open(self):
        """
        Открыть ячейку
        :return:
        """
        self.__isOpen = True

    def isOpen(self):
        return self.__isOpen

    def setUserSelectMine(self, is_mine):
        """
        Отметить что пользвоатель поставил сюда мину
        :param is_mine:
        :return:
        """
        if (type(self.__isOpen) == bool and self.__isOpen == False):
            self.__userSelectIsMine = (type(is_mine) == bool and is_mine == True)

    def isUserSelectMine(self):
        """
        Првоеряка поставил ли пользователь мину сюда или нет
        :return:
        """
        return self.__userSelectIsMine

    def setCountMineAround(self, count_mine):
        """
        Задаём кол-во мин в ячейки
        :param count_mine:
        :return:
        """
        self.__countMineAround = int(count_mine)

    def getCountMineAround(self):
        return self.__countMineAround

    def setParentFrame(self, frame):
        self.parentFrame = frame
        self.frame = Tkinter.Frame(self.parentFrame,width = self.width,height = self.height)
        self.button = Tkinter.Button(self.frame)
        self.button.bind('<Button-1>', self.leftclick)
        self.button.bind('<Button-3>', self.rightclick)
        self.lable = Tkinter.Label(self.frame)

    def leftclick(self,event):
        if self.__eventLeftClick:
            self.__eventLeftClick(self,event)

    def rightclick(self,event):
        if self.isOpen():
            return  False

        if self.__userSelectIsMine == False:
            curDir = os.path.dirname(os.path.abspath(__file__))
            flag_gif = curDir +  "/data/flag.gif"
            self.flagImage = Tkinter.PhotoImage(file=flag_gif,width=19, height=19)
            self.button.configure(image = self.flagImage,state = Tkinter.DISABLED,disabledforeground = "#00FF00")
            self.__userSelectIsMine = True
        else:
            self.button.configure(image = "",state = Tkinter.NORMAL)
            self.__userSelectIsMine = False

        if self.__eventRightClick:
            self.__eventRightClick(self,event)

    def structure(self):
        self.frame.grid(row = int(self.getRow().getNumber()),column = int(self.getNumberInRow()),padx = self.padding, pady = self.padding)
        self.button.grid(sticky = Tkinter.NSEW)
        self.frame.rowconfigure('all', minsize = self.height)
        self.frame.columnconfigure('all', minsize = self.width)

    def bind(self,event,function):
        if(event == "<Button-3>"):
            self.__eventRightClick = function
        elif (event == "<Button-1>"):
            self.__eventLeftClick = function
