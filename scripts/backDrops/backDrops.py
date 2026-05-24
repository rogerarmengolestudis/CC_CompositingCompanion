# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - backDrops.py
# ////////////////////////////////////////////////////////////////////

import os
import nuke


keyShortCut = 'Ctrl+B'

def run():
    print('[CC] Backdrop creator starting')
    nodes = nuke.selectedNodes()
    if not nodes:
        nuke.message("Please select at least one node to create a backdrop.")
        return
    else:
        from scripts.backDrops.utils_bkdrp import backDropUI
        backDropUI.show_floating()



