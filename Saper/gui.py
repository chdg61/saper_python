# coding=utf-8
import tkMessageBox
import Tkinter

class MainGUI(Tkinter.Tk):

    __width = 500
    __height = 400

    __sizeX = 9
    __sizeY = 9

    __isStructureEnable = False

    TOOLBAR_HEIGHT = 50
    MAIN_COLOR_BACKGROUND = "#DCDCDC"

    # начало с 1й секунды
    __timeBegin = 1

    # ID интервала таймера
    __timerId = False

    def __init__(self,title = 'Saper',**args):
        Tkinter.Tk.__init__(self)

        self.__listCeil = []

        self.title(title)

        if("width" in args):
            self.__width = int(args['width'])
        if("height" in args):
            self.__height = int(args['height']) + self.TOOLBAR_HEIGHT

        self.geometry("%sx%s" % (self.__width,self.__height))

        if("size" in args):
            self.__sizeX = int(args['size'])
            self.__sizeY = int(args['size'])
        else:
            if("sizeX" in args):
                self.__sizeX = int(args['sizeX'])
            if("sizeY" in args):
                self.__sizeY = int(args['sizeY'])

        self.__createFrame()

    def __createFrame(self):
        self.frameToolBar = Tkinter.Frame(self,width = self.__width,height = self.TOOLBAR_HEIGHT, background = "grey",relief = Tkinter.GROOVE,border = 2)
        self.frameMain = Tkinter.Frame(self,width = self.__width,height = self.__height - self.TOOLBAR_HEIGHT, background = self.MAIN_COLOR_BACKGROUND,relief = Tkinter.GROOVE,border = 2)

        self.labeTimer = Tkinter.Label(self.frameToolBar,text = "0000")
        self.labeTimer.grid(row = 0,column = 0,sticky='nsew')

        self.labeButtonNew = Tkinter.Button(self.frameToolBar,text = "NEW")
        self.labeButtonNew.grid(row = 0,column = 1,sticky='nsew')

        self.labeCounter = Tkinter.Label(self.frameToolBar,text = "00/00")
        self.labeCounter.grid(row = 0,column = 2,sticky='nsew')

    def setAllCountMine(self,count_mine):
        self.count_mine = count_mine
        self.labeCounter['text'] = "00/%2d" % count_mine

    def setSelectedCountMine(self,selected_mine):
        self.labeCounter['text'] = "%2d/%2d" % (selected_mine,self.count_mine)

    def __gridCeilFrame(self):
        for x,listX in enumerate(self.__listCeil):
            for y,listY in enumerate(listX):
                listY['button'].grid()
                listY['frame'].grid(row = int(y),column = int(x),padx =2, pady =2)

    def timerStart(self):
        """
        Включает таймер игры
        :return:
        """
        if self.__timerId == False and self.__timeBegin == 1:
            self.__timer()

    def timerStop(self):
        """
        Выключает таймер игры
        :return:
        """
        if self.__timerId !=  False:
            self.labeTimer.after_cancel(self.__timerId)
            self.__timerId = False


    def __timer(self):
        self.labeTimer['text'] = "%0004d" % self.__timeBegin
        self.__timeBegin += 1
        self.__timerId = self.labeTimer.after(1000, self.__timer)

    def game_over(self):
        self.timerStop()
        tkMessageBox.showerror("Game Over", "Вы продули эту игру, поздравляю...")
        return False

    def game_winner(self):
        self.timerStop()
        tkMessageBox.showinfo("WINNER", "Победа :)))")
        return False


    def structure(self):
        self.frameToolBar.grid(row = 0, column = 0)
        widthLableToolBar = (float(self.__width - self.TOOLBAR_HEIGHT))/2.0
        self.frameToolBar.rowconfigure('all',minsize = self.TOOLBAR_HEIGHT)
        self.frameToolBar.columnconfigure(0,minsize = widthLableToolBar - 5)
        self.frameToolBar.columnconfigure(1,minsize = self.TOOLBAR_HEIGHT)
        self.frameToolBar.columnconfigure(2,minsize = widthLableToolBar - 5)
        self.frameMain.grid(row = 1, column = 0)
        self.__isStructureEnable = True

    def show(self):
        if self.__isStructureEnable == False:
            self.structure()

        self.mainloop()