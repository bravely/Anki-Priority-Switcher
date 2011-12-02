'''
author: @quaunaut
Adds an easier way to assign priorities of selected cards to the card browser.
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ankiqt import mw
from anki.hooks import addHook
from anki.cards import Card

# Constants. Change these if you change the tags for your priorities.

PRIORITYVERYHIGH = "PriorityVeryHigh"
PRIORITYHIGH = "PriorityHigh"
PRIORITYLOW = "PriorityLow"

# Menu and UI Stuffs.
def setupMenu(editor):
   prioVeryHigh = QAction("Set Priority to Very High", editor)
   prioVeryHigh.setEnabled(True)
   prioVeryHigh.setText("Set Priority to Very High")
   editor.connect(prioVeryHigh, SIGNAL("triggered()"), lambda e=editor: priorityVeryHigh(e))
   
   prioHigh = QAction("Set Priority to High", editor)
   prioHigh.setEnabled(True)
   prioHigh.setText("Set Priority to High")
   editor.connect(prioHigh, SIGNAL("triggered()"), lambda e=editor: priorityHigh(e))
      
   prioLow = QAction("Set Priority to Low", editor)
   prioLow.setEnabled(True)
   prioLow.setText("Set Priority to Low")
   editor.connect(prioLow, SIGNAL("triggered()"), lambda e=editor: priorityLow(e))
   
   prioNormal = QAction("Reset Priority to Normal", editor)
   prioNormal.setEnabled(True)
   prioNormal.setText("Reset Priority to Normal")
   editor.connect(prioNormal, SIGNAL("triggered()"), lambda e=editor: priorityNormal(e))
   
   editor.dialog.menuActions.addSeparator()
   prioritySubMenu = editor.dialog.menuActions.addMenu('&Priority Switcher')
   prioritySubMenu.addAction(prioVeryHigh)
   prioritySubMenu.addAction(prioHigh)
   prioritySubMenu.addAction(prioLow)
   prioritySubMenu.addAction(prioNormal)

# The core workings of the plugin.
# Since Anki doesn't provide access to the HasTag() function, I essentially have to just delete and recreate the tags for each instance.
def priorityVeryHigh(editor):
    editor.deleteTags(tags=PRIORITYVERYHIGH, label=False)
    editor.deleteTags(tags=PRIORITYHIGH, label=False)
    editor.deleteTags(tags=PRIORITYLOW, label=False)
    editor.addTags(tags=PRIORITYVERYHIGH, label=False,)

def priorityHigh(editor):
    editor.deleteTags(tags=PRIORITYVERYHIGH, label=False)
    editor.deleteTags(tags=PRIORITYHIGH, label=False)
    editor.deleteTags(tags=PRIORITYLOW, label=False)
    editor.addTags(tags=PRIORITYHIGH, label=False,)

def priorityLow(editor):
    editor.deleteTags(tags=PRIORITYVERYHIGH, label=False)
    editor.deleteTags(tags=PRIORITYHIGH, label=False)
    editor.deleteTags(tags=PRIORITYLOW, label=False)
    editor.addTags(tags=PRIORITYLOW, label=False,)

def priorityNormal(editor):
    editor.deleteTags(tags=PRIORITYVERYHIGH, label=False)
    editor.deleteTags(tags=PRIORITYHIGH, label=False)
    editor.deleteTags(tags=PRIORITYLOW, label=False)

addHook("editor.setupMenus", setupMenu)
mw.registerPlugin("Priority Switcher", 19)
