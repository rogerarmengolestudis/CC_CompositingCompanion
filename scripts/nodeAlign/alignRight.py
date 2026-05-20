# //////////////////////////////////////////////////
# CC_CompositingCompanion - alignRight.py
# //////////////////////////////////////////////////

import nuke

keyShortCut = "Right"

def _get_node_width(node):
    if node.Class() == 'BackdropNode':
        return int(node.knob('bdwidth').value())
    return node.screenWidth()

def align_nodes_right():
    selected = nuke.selectedNodes()
    if len(selected) < 2:
        nuke.message("Select at least 2 nodes to align.")
        return

    try:
        nuke.Undo().begin('Align Nodes Right')
        max_right = max(n.xpos() + _get_node_width(n) for n in selected)
        for n in selected:
            n.setXpos(max_right - _get_node_width(n))
    finally:
        nuke.Undo().end()

def run():
    align_nodes_right()