# //////////////////////////////////////////////////
# CC_CompositingCompanion - distributeHorizontal.py
# //////////////////////////////////////////////////

import nuke

keyShortCut = "*"

def _get_node_width(node):
    if node.Class() == 'BackdropNode':
        return int(node.knob('bdwidth').value())
    return node.screenWidth()

def distribute_horizontal():
    selected = nuke.selectedNodes()
    if len(selected) < 3:
        nuke.message("Select at least 3 nodes to distribute.")
        return

    try:
        nuke.Undo().begin('Distribute Nodes Horizontal')
        sorted_nodes = sorted(selected, key=lambda n: n.xpos())
        left_x = sorted_nodes[0].xpos()
        right_x = sorted_nodes[-1].xpos() + _get_node_width(sorted_nodes[-1])
        total_width = sum(_get_node_width(n) for n in sorted_nodes)
        spacing = (right_x - left_x - total_width) / (len(sorted_nodes) - 1)
        current_x = left_x
        for n in sorted_nodes:
            n.setXpos(int(round(current_x)))
            current_x += _get_node_width(n) + spacing
    finally:
        nuke.Undo().end()

def run():
    distribute_horizontal()