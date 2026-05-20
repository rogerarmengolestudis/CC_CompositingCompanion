# //////////////////////////////////////////////////
# CC_CompositingCompanion - distributeVertical.py
# //////////////////////////////////////////////////

import nuke

keyShortCut = "Shift+*"

def _get_node_height(node):
    if node.Class() == 'BackdropNode':
        return int(node.knob('bdheight').value())
    return node.screenHeight()

def distribute_vertical():
    selected = nuke.selectedNodes()
    if len(selected) < 3:
        nuke.message("Select at least 3 nodes to distribute.")
        return

    try:
        nuke.Undo().begin('Distribute Nodes Vertical')
        sorted_nodes = sorted(selected, key=lambda n: n.ypos())
        top_y = sorted_nodes[0].ypos()
        bottom_y = sorted_nodes[-1].ypos() + _get_node_height(sorted_nodes[-1])
        total_height = sum(_get_node_height(n) for n in sorted_nodes)
        spacing = (bottom_y - top_y - total_height) / (len(sorted_nodes) - 1)
        current_y = top_y
        for n in sorted_nodes:
            n.setYpos(int(round(current_y)))
            current_y += _get_node_height(n) + spacing
    finally:
        nuke.Undo().end()

def run():
    distribute_vertical()