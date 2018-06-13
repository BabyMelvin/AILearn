from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, random

"""
        Tetris类创建游戏
        Boards是游戏主要逻辑
        Tetrominoe包含所有的砖块
        Shape是所有砖块的代码
"""


class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''initaiates applicaiton UI'''
        # TODO
        # self.board = Board(self)
        pass


class Board(object):
    msg2Statusbar = pyqtSignal(str)
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self):
        '''initates board'''
        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()

    def shapeAt(self, x, y):
        '''determines shape at the board postion'''
        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        '''set a shape at the board'''
        self.board[(y * Board.BoardWidth)] = shape

    def squareWidth(self):
        '''returns the width of one square'''
        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        '''return the height of one square'''
        return self.contentRect().height() // Board.BoardHeight

    def start(self):
        '''start game'''
        if self.isPaused:
            return
        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()
        self.msg2Statusbar.emit(str(self.numLinesRemoved))
        self.newPiece()
        self.timer.start(Board.Speed,self)


class Tetrominoe(object):
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


class Shape(object):
    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1)),
    )

    def __init__(self):
        self.coords = [[0, 0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape
        self.setShape(Tetrominoe.NoShape)

    def shape(self):
        '''return shape'''
        return self.pieceShape

    def setShape(self, shape):
        '''set a shape'''
        table = Shape.coordsTable
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]
        self.pieceShape = shape

    def setRandomShape(self):
        '''choose a random shape'''
        self.setShape(random.randint(1, 7))

    def x(self, index):
        '''return x coordinate'''
        return self.coords[index][0]

    def y(self, index):
        ''''return y coordinates'''
        return self.coords[index][1]

    def setX(self, index, x):
        '''set x coordinate'''
        self.coords[index][0] = x

    def setY(self, index, y):
        '''set y coordinate'''
        self.coords[index][1] = y

    def minX(self):
        '''return min x value'''
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])
        return m

    def maxX(self):
        ''' return max x value'''
        m = self.coords[0][0]
        for i in range(4):
            m = max((m, self.coords[i][0]))
        return m

    def minY(self):
        '''return min y value'''
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])
        return m

    def maxY(self):
        '''return max y value'''
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

    def rotateLeft(self):
        '''rotate shape to the left'''
        if self.pieceShape == Tetrominoe.SquareShape:
            return self
        result = Shape()
        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))
        return result

    def rotateRight(self):
        '''rotate shape to the right'''
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))
        return result
