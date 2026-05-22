# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - backDropFunction.py
# ////////////////////////////////////////////////////////////////////

import os
import nuke

import colorsys
import random

def selectedNodes():
    """Returns a list of currently selected nodes in the Nuke script."""
    return nuke.selectedNodes()


def createBackDrop(data):
    padding, font_size, default_z_order = 100, 42, -10
    
    nodes = selectedNodes()

    color = data.get('color',"#3a3a3a")
    color = color.lstrip('#')
    r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
    backDrop_color = (r << 24) | (g << 16) | (b << 8) | 0xFF

    
    x_min = min(node.xpos() for node in nodes)
    y_min = min(node.ypos() for node in nodes)
    x_max = max(node.xpos() + node.screenWidth() for node in nodes)
    y_max = max(node.ypos() + node.screenHeight() for node in nodes)
    
    bd = nuke.createNode('BackdropNode')
    bd.setXpos(x_min - padding)
    bd.setYpos(y_min - padding)
    bd.knob('bdwidth').setValue(x_max - x_min + 2 * padding)
    bd.knob('bdheight').setValue(y_max - y_min + 2 * padding)
    bd.knob('note_font_size').setValue(font_size)
    bd.knob('z_order').setValue(default_z_order)
    bd.knob('tile_color').setValue(backDrop_color)
    bd.knob('appearance').setValue('Fill')
    bd.knob('bookmark').setValue(data.get('bookmark', False))
    
    bd.selectNodes(True)
    bd['selected'].setValue(True)