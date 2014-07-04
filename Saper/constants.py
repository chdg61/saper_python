# coding=utf-8

# ------------------------------- MAIN ----------------------------------
# кол-во строк
COUNT_ROWS = 9

# кол-во столбцов
COUNT_COLUMNS = 9

# Отступ между ячейками
PADDING_BETWEEN_CEIL = 1

# Кол-во мин на поле
MINE_COUNT = 10

# размер ячейки
SIZE_CEIL = 25

# ------------------------------- GUI ----------------------------------
# название окна
WINDOW_TITLE = "Сапер"

# Высота информационной панели
WINDOW_TOOLBAR_HEIGHT = 50

# Цвет фона главного окна с полем
WINDOW_MAIN_FRAME_COLOR_BACKGROUND = "#DCDCDC"

# Название окна сообщений при проигрыше
GAME_OVER_WINDOW_TITLE = "Game Over"

# сообщение при проигрыше
GAME_OVER_MESSAGE = "Вы продули эту игру, поздравляю..."

# Название окна сообщений при выигрыше
WINNER_WINDOW_TITLE = "WINNER"

# сообщение при выигрыше
WINNER_MESSAGE = "Победа :)))"

# список цветов для каждой цифры которая обозначает бомбы вокруг
COLOR_CHAR = {1: "#222", 2: "#2f2", 3: "#f22", 4: "#22f", 5: "#220", 6: "#022", 7: "#202", 8: "#2H2"}

# цвет цифрвы по умолчанию
DEFAULT_COLOR_CHAR = '#2HH'

# шрифт и стиль цифры
STYLE_FONT_CEIL = 'sans 13 bold'

# ------------------------------- OTHER ----------------------------------
# Общее кол-во ячеек
COUNT_CEIL = COUNT_COLUMNS * COUNT_ROWS

# Общая ширина окна
WINDOW_WIDTH = SIZE_CEIL * COUNT_COLUMNS + 10 + (COUNT_COLUMNS * (PADDING_BETWEEN_CEIL * 2))

# Общая высота окна
WINDOW_HEIGHT = SIZE_CEIL * COUNT_ROWS + 10 + (COUNT_ROWS * (PADDING_BETWEEN_CEIL * 2)) + WINDOW_TOOLBAR_HEIGHT

# событие при клике на левую клавишу
EVENT_LEFT_CLICK = "<Button-1>"

# событие при клике на правую клавишу
EVENT_RIGHT_CLICK = "<Button-3>"

