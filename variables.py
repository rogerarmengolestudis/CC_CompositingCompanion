# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - variables.py
# ////////////////////////////////////////////////////////////////////

import os

import sys
sys.dont_write_bytecode = True

class CCVariables:
    PLUGIN_DIR = os.path.dirname(__file__)
    ICONS_DIR = os.path.join(os.path.dirname(__file__), "icons")
    TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
    GIZMOS_DIR = os.path.join(os.path.dirname(__file__), "gizmos")
    DEFAULTS_DIR = os.path.join(os.path.dirname(__file__), "defaults")
    TOOLS_DIR = os.path.join(os.path.dirname(__file__), "tools")