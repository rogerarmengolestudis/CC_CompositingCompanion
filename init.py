# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - init.py
# ////////////////////////////////////////////////////////////////////

import nuke
import os

from variables import CCVariables
ccVars = CCVariables()

# Path registration
PLUGIN_DIR = ccVars.PLUGIN_DIR
ICONS_DIR  = ccVars.ICONS_DIR
DEFAULTS_DIR = ccVars.DEFAULTS_DIR

nuke.pluginAddPath(PLUGIN_DIR)
nuke.pluginAddPath(ICONS_DIR)

#nuke.pluginAddPath(DEFAULTS_DIR)

