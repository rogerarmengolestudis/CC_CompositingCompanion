# //////////////////////////////////////////////////
# CC_CompositingCompanion - alignRight.py
# //////////////////////////////////////////////////

import nuke

import sys
sys.dont_write_bytecode = True

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
        max_center_x = max(n.xpos() + _get_node_width(n) // 2 for n in selected)
        for n in selected:
            n.setXpos(max_center_x - _get_node_width(n) // 2)
    finally:
        nuke.Undo().end()

def run():
    align_nodes_right()