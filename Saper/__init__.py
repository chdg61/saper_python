# coding=utf-8
import random
import gui
from Saper.ceil import Ceil
from Saper.row import Row

__author__ = 'chdg61'
__version__ = "0.1"



def show():
    saper = Saper()
    saper.show()



class Saper(object):

    # кол-во строк
    __rows = 9

    # кол-во столбцов
    __cols = 9

    # отступ поля
    __padding = 1

    # кол-во мин
    __mine_count = 10

    # размер ячейки
    __size_ceil = 25

    # Номера ячеек которые содержат мины
    __listNumbersFieldForMine = []

    # Список объектов строк
    __listRows = []

    # Объект ячеек с расставленными пользователем минами
    __selectedMineCeil = []

    # Число проставленных мин пользователя
    __countSelectetMine = 0

    def __init__(self,**args):

        # кол-во строк
        if 'rows' in args and type(args['rows']) == int:
            self.__rows = int(args['rows'])

        # кол-во столбцов
        if 'cols' in args and type(args['cols']) == int:
            self.__cols = int(args['cols'])

        # отступ поля
        if 'padding' in args and type(args['padding']) == int:
            self.__padding = int(args['padding'])

        # кол-во мин
        if 'mine_count' in args and type(args['mine_count']) == int:
            self.__mine_count = int(args['mine_count'])

        # размер ячейки
        if 'size_ceil' in args and type(args['size_ceil']) == int:
            self.__size_ceil = int(args['size_ceil'])

        # Общее число ячеек
        self.__count_ceil = self.__cols * self.__rows

        # Общая ширина
        self.__widthWindow = self.__size_ceil * self.__cols + 10 + (self.__cols * (self.__padding*2))

        # Общая высота
        self.__heightWindow = self.__size_ceil * self.__rows + 10 + (self.__rows * (self.__padding*2))

        self.__gui = gui.MainGUI("Сапер",width = self.__widthWindow,height = self.__heightWindow,sizeX = self.__cols,sizeY = self.__rows)

        self.__gui.setAllCountMine(self.__mine_count)

        Ceil.width = self.__size_ceil
        Ceil.height = self.__size_ceil
        Ceil.padding = self.__padding

        # рассчет мин
        self.createMine()

    def createMine(self):
        """
        Создание поля случайных мин
        :return:
        """

        # формируем случайные мины на поле
        self.__createRandomMineArray()

        # создаём объекты строк
        # self.__listRows = [SaperRow(number_row) for number_row in range(0,self.__rows)]

        for number_row in range(0,self.__rows):
            self.__listRows.insert(number_row,Row(number_row))
            # пробегаем по строкам и создаём объекты ячеек
            for number_ceil in range(0,self.__cols):
                ceil = self.__listRows[number_row].createCeil(number_ceil)
                ceil.setNumber((number_row * self.__cols) + number_ceil + 1)
                ceil.setParentFrame(self.__gui.frameMain)
                ceil.bind("<Button-1>",self.leftClick)
                ceil.bind("<Button-3>",self.rightClick)

                if (ceil.getNumber() in self.__listNumbersFieldForMine):
                    ceil.setMine(True)


    def __createRandomMineArray(self):
        """
        Формируем случайные мины на поле
        :return:
        """

        for i in range(0,self.__mine_count):
            self.__listNumbersFieldForMine.append(self.__randomNumberCeilOnMine())


    def __randomNumberCeilOnMine(self):
        """
        Генеририрует случайный номер ячейки где будет располагаться мина
        С проверкой его не вхождения в общую базу сгенерированных номеров
        :return:
        """

        # randomNumberCeil = math.floor(random.randint() * this._countСeil)
        randomNumberCeil = random.randint(1,self.__count_ceil)

        if randomNumberCeil in self.__listNumbersFieldForMine:
            return self.__randomNumberCeilOnMine()
        else:
            return randomNumberCeil


    def leftClick(self,ceil,event = None):
        """
        Обработка действий при нажатии левой клавиши, открытие полей
        :param ceil: Saper.ceil.Ceil
        """

        countMine = 0

        obRow = ceil.getRow()

        self.__gui.timerStart()

        # если на ячейки стоит что мина
        if ceil.isUserSelectMine():
            return False

        # если ячейка является миной
        if ceil.isMine():
            self.__gameOver()
            return False


        listAroundCeil = self.__findAroundCeil(ceil)
        for tmpCeil in listAroundCeil:
            if tmpCeil.isMine():
                countMine+= 1

        ceil.setCountMineAround(countMine)
        ceil.open()


        # если ноль мин в ячейки
        if countMine == 0:
            self.__openCeilEmpty(ceil)
            for tmpCeil in listAroundCeil:
                if tmpCeil.isMine() == False and tmpCeil.isUserSelectMine() == False and tmpCeil.isOpen() == False:
                    self.leftClick(tmpCeil)
        else:
            self.__openCeil(ceil)

    def rightClick(self,ceil,event = None):
        if ceil.isUserSelectMine():
            self.__addSelectedMine(ceil)
            self.__checkSelectedMine(True)
        else:
            self.__deleteSelectedMine(ceil)
            self.__checkSelectedMine(False)


    def __findAroundCeil(self,obCeil):
        """
        Находим ячейки рядом с текущей
        :param obCeil: Saper.ceil.Ceil
        :return:
        """

        listCeil = []
        countMine = 0

        # смотрим левую ячейку
        try:
            if obCeil.getNumberInRow() > 0:
                _ceil = obCeil.getRow().getCeil(obCeil.getNumberInRow() - 1)
                if _ceil:
                    listCeil.append(_ceil)
        except:
            pass

        # смотрим правую ячейку
        try:
            _ceil = obCeil.getRow().getCeil(obCeil.getNumberInRow() + 1)
            if _ceil:
                listCeil.append(_ceil)
        except:
            pass

        # смотрим верхний ряд
        try:
            if obCeil.getRow().getNumber() > 0:
                _row = self.__listRows[obCeil.getRow().getNumber() - 1]
                if _row:
                    # смотрим левую верхнюю ячейку
                    try:
                        if obCeil.getNumberInRow() > 0:
                            _ceil = _row.getCeil(obCeil.getNumberInRow() - 1)
                            if _ceil:
                                listCeil.append(_ceil)
                    except:
                        pass

                    # смотрим среднюю верхнюю ячейку
                    try:
                        _ceil = _row.getCeil(obCeil.getNumberInRow())
                        if _ceil:
                            listCeil.append(_ceil)
                    except:
                        pass

                    # смотрим правую верхнюю ячейку
                    try:
                        _ceil = _row.getCeil(obCeil.getNumberInRow() + 1)
                        if _ceil:
                            listCeil.append(_ceil)
                    except:
                        pass
        except:
            pass

        # смотрим нижний ряд
        try:
            _row = self.__listRows[obCeil.getRow().getNumber() + 1]
            if _row:
                # смотрим левую нижнюю ячейку
                try:
                    if obCeil.getNumberInRow() > 0:
                        _ceil = _row.getCeil(obCeil.getNumberInRow() - 1)
                        if _ceil:
                            listCeil.append(_ceil)
                except:
                    pass

                # смотрим среднюю нижнюю ячейку
                try:
                    _ceil = _row.getCeil(obCeil.getNumberInRow())
                    if _ceil:
                        listCeil.append(_ceil)
                except:
                    pass

                # смотрим правую нижнюю ячейку
                try:
                    _ceil = _row.getCeil(obCeil.getNumberInRow() + 1)
                    if _ceil:
                        listCeil.append(_ceil)
                except:
                    pass
        except:
            pass

        return listCeil

    def __openCeilEmpty(self,obCeil):
        """
        Закрашиваем пустую ячейку
        """
        obCeil.button.destroy()
        obCeil.lable['text'] = ""
        obCeil.lable.grid()

    def __openCeil(self,obCeil):
        """
        Закрашиваем ячейку с цифрой
        """

        obCeil.button.destroy()
        count_mine_around = obCeil.getCountMineAround()
        color_char = {
            1:"#222",
            2:"#2f2",
            3:"#f22",
            4:"#22f",
            5:"#220",
            6:"#022",
            7:"#202",
            8:"#2H2"
        }.get(count_mine_around,"#2HH")

        obCeil.lable['text'] = count_mine_around
        obCeil.lable['font'] = "sans 13 bold"
        obCeil.lable['fg'] = color_char
        obCeil.lable.grid()

    def __addSelectedMine(self,ceil):
        """
        Добавляем ячейку в выбранные пользователем
        """
        self.__selectedMineCeil.append(ceil)

    def __deleteSelectedMine(self,ceil):
        """
        Удаляем ячейку из выбранных пользователем
        """
        try:
            self.__selectedMineCeil.remove(ceil)
        except:
            pass

    def __checkSelectedMine(self,is_mine):
        """
        учитывает число проставленных мин, для победы
        """
        _countRulesMine = 0

        if is_mine == True:
            self.__countSelectetMine+= 1
            self.__gui.setSelectedCountMine(self.__countSelectetMine)
        elif is_mine == False:
            self.__countSelectetMine-= 1
            self.__gui.setSelectedCountMine(self.__countSelectetMine)


        # проверям кол-во проставленных и всего и проверяем на правильность
        if self.__countSelectetMine == self.__mine_count:
            for ceil in self.__selectedMineCeil:
                if ceil.isMine() and ceil.isUserSelectMine():
                    _countRulesMine+= 1

            if _countRulesMine == self.__mine_count:
                self.__winner()

    def __gameOver(self):
        self.__gui.game_over()

    def __winner(self):
        self.__gui.game_winner()

    def structure(self):
        for x, obRow in enumerate(self.__listRows):
            for y, obCeil in enumerate(obRow.getListCeil()):
                obCeil.structure()

    def show(self):
        self.__gui.structure()
        self.structure()
        self.__gui.show()