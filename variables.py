# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - variables.py
# ////////////////////////////////////////////////////////////////////

import os

class CCVariables:
    PLUGIN_DIR = os.path.dirname(__file__)
    ICONS_DIR = os.path.join(os.path.dirname(__file__), "icons")
    TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
    GIZMOS_DIR = os.path.join(os.path.dirname(__file__), "gizmos")