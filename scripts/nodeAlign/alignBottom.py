# //////////////////////////////////////////////////
# CC_CompositingCompanion - alignBottom.py
# //////////////////////////////////////////////////

import nuke

keyShortCut = "Down"

def _get_node_height(node):
    if node.Class() == 'BackdropNode':
        return int(node.knob('bdheight').value())
    return node.screenHeight()

def align_nodes_bottom():
    selected = nuke.selectedNodes()
    if len(selected) < 2:
        nuke.message("Select at least 2 nodes to align.")
        return

    try:
        nuke.Undo().begin('Align Nodes Bottom')
        max_bottom = max(n.ypos() + _get_node_height(n) for n in selected)
        for n in selected:
            n.setYpos(max_bottom - _get_node_height(n) // 2)
    finally:
        nuke.Undo().end()

def run():
    align_nodes_bottom()