import os, sys
import pygame, pgu
from pgu import gui

app = gui.App()
e = gui.Button("This is a test button!")
quitBtn = gui.Button("Quit")
labelColor = (255,255,255)

mainTable = gui.Table()

mainTable.tr()
mainTable.td(gui.Label("Tic-Tac-Toe", color=labelColor))
mainTable.tr()
mainTable.td(e)
mainTable.tr()
mainTable.td(quitBtn)

quitBtn.connect(gui.CLICK, app.quit)
app.connect(gui.QUIT, app.quit)
app.run(mainTable)
