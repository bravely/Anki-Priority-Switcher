'''
author: @quaunaut
Adds an easier way to assign priorities of selected cards to the card browser.
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ankiqt import mw
from anki.hooks import addHook
from anki.cards import Card

def setupMenu(editor):
   prioVeryHigh = QAction("Set Priority to Very High", editor)
   prioVeryHigh.setEnabled(True)
   prioVeryHigh.setText("Set Priority to Very High")
   prioVeryHigh.setToolTip(_("Set Priority to Very High"))
   editor.connect(prioVeryHigh, SIGNAL("triggered()"), lambda e=editor: priorityVeryHigh(e))
   
   prioHigh = QAction("Set Priority to High", editor)
   prioHigh.setEnabled(True)
   prioHigh.setText("Set Priority to High")
   prioHigh.setToolTip(_("Set Priority to High"))
   editor.connect(prioHigh, SIGNAL("triggered()"), lambda e=editor: priorityHigh(e))
      
   prioLow = QAction("Set Priority to Low", editor)
   prioLow.setEnabled(True)
   prioLow.setText("Set Priority to Low")
   prioLow.setToolTip(_("Set Priority to Low"))
   editor.connect(prioLow, SIGNAL("triggered()"), lambda e=editor: priorityLow(e))
   
   prioNormal = QAction("Reset Priority to Normal", editor)
   prioNormal.setEnabled(True)
   prioNormal.setText("Reset Priority to Normal")
   prioNormal.setToolTip(_("Reset Priority to Normal"))
   editor.connect(prioNormal, SIGNAL("triggered()"), lambda e=editor: priorityNormal(e))
   
   editor.dialog.menuActions.addSeparator()
   prioritySubMenu = editor.dialog.menuActions.addMenu('&Priority Switcher')
   prioritySubMenu.addAction(prioVeryHigh)
   prioritySubMenu.addAction(prioHigh)
   prioritySubMenu.addAction(prioLow)
   prioritySubMenu.addAction(prioNormal)


# Since Anki doesn't provide access to the HasTag() function, I essentially have to just delete and recreate the tags for each instance.

def priorityVeryHigh(editor):
    editor.deleteTags(tags="PriorityVeryHigh", label=False)
    editor.deleteTags(tags="PriorityHigh", label=False)
    editor.deleteTags(tags="PriorityLow", label=False)
    editor.addTags(tags="PriorityVeryHigh", label=False,)

def priorityHigh(editor):
    editor.deleteTags(tags="PriorityVeryHigh", label=False)
    editor.deleteTags(tags="PriorityHigh", label=False)
    editor.deleteTags(tags="PriorityLow", label=False)
    editor.addTags(tags="PriorityHigh", label=False,)

def priorityLow(editor):
    editor.deleteTags(tags="PriorityVeryHigh", label=False)
    editor.deleteTags(tags="PriorityHigh", label=False)
    editor.deleteTags(tags="PriorityLow", label=False)
    editor.addTags(tags="PriorityLow", label=False,)

def priorityNormal(editor):
    editor.deleteTags(tags="PriorityVeryHigh", label=False)
    editor.deleteTags(tags="PriorityHigh", label=False)
    editor.deleteTags(tags="PriorityLow", label=False)

addHook("editor.setupMenus", setupMenu)
mw.registerPlugin("Priority Switcher", 19)
