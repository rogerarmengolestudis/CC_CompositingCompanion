# //////////////////////////////////////////////////
# CC_CompositingCompanion - node_align.py
# //////////////////////////////////////////////////

import nuke



def _getSelectedNodes():
    sel = nuke.selectedNodes()
    if len(sel) < 2:
        nuke.message('Please select at least 2 nodes to align.')
        return None

    return sel

def _selBounds(node):
    x = node.xpos()
    y = node.ypos()
    w = node.screenWidth()
    h = node.screenHeight()

    return (x, y, w, h)

def alignNodes(mode="center"):
    nodes = _getSelectedNodes()

    if not nodes:
        nuke.message('No nodes selected for alignment.')

    bounds = {n: _selBounds(n) for n in nodes}

# continuar aqui <-------------------------------------------------------!!!!!!!!!!!!!, fer operacions de aliniació :) 


