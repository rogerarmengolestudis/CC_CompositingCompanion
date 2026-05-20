# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - backDropFunction.py
# ////////////////////////////////////////////////////////////////////

import os
import nuke

import colorsys
import random




def randomColor():
    h = random.random()
    s = 0.5
    l = random.uniform(0.3, 0.5)
    
    # HLS to RGB
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return '#{:02x}{:02x}{:02x}'.format(int(r*255), int(g*255), int(b*255))

