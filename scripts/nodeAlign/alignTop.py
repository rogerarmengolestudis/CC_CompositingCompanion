# //////////////////////////////////////////////////
# CC_CompositingCompanion - alignTop.py
# //////////////////////////////////////////////////

import nuke

keyShortCut = "Up"

def align_nodes_top():
    selected = nuke.selectedNodes()
    if len(selected) < 2:
        nuke.message("Select at least 2 nodes to align.")
        return

    try:
        nuke.Undo().begin('Align Nodes Top')
        min_y = min(n.ypos() for n in selected)
        for n in selected:
            n.setYpos(min_y)
    finally:
        nuke.Undo().end()

def run():
    align_nodes_top()