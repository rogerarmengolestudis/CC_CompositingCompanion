# //////////////////////////////////////////////////
# CC_CompositingCompanion - alignLeft.py
# //////////////////////////////////////////////////

import nuke

keyShortCut = "Left"

def _get_node_width(node):
    if node.Class() == 'BackdropNode':
        return int(node.knob('bdwidth').value())
    return node.screenWidth()

def align_nodes_left():
    selected = nuke.selectedNodes()
    if len(selected) < 2:
        nuke.message("Select at least 2 nodes to align.")
        return

    try:
        nuke.Undo().begin('Align Nodes Left')
        min_center_x = min(n.xpos() + _get_node_width(n) // 2 for n in selected)
        for n in selected:
            n.setXpos(min_center_x - _get_node_width(n) // 2)
    finally:
        nuke.Undo().end()

def run():
    align_nodes_left()