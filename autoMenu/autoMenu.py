# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - autoMenu.py
# ////////////////////////////////////////////////////////////////////

import nuke
import os
import re

from variables import CCVariables
ccVars = CCVariables()

# ----- Directory paths -----
ICONS_DIR  = ccVars.ICONS_DIR
TEMPLATES_DIR = ccVars.TEMPLATES_DIR
GIZMOS_DIR = ccVars.GIZMOS_DIR

# ///////////////////////////////////////////////////////////////////
# Helpers
# ///////////////////////////////////////////////////////////////////

def _icon(filename):
    """Return the absolute path for an icon file, or None if it doesn't exist."""

    path = os.path.join(ICONS_DIR, filename)
    return path if os.path.isfile(path) else None
    



# ////////////////////////////////////////////////////////////////////
# Menu builder
# ////////////////////////////////////////////////////////////////////

class CCMenuBuilder:

    def __init__(self, pluginRoot):
        self.pluginRoot  = pluginRoot
        self.templatesDir = os.path.join(pluginRoot, "templates")
        self.gizmosDir    = os.path.join(pluginRoot, "gizmos")
        self.iconsDir     = os.path.join(pluginRoot, "icons")
 
        # Register gizmos dirs with Nuke
        if os.path.isdir(self.gizmosDir):
            nuke.pluginAddPath(self.gizmosDir)

    def createCCMenu(self, pluginRoot):
        """
        Build the Compositing Companion menu.
        """

        try:
            toolbar = nuke.menu("Nodes")
            tb_ccMenu = toolbar.addMenu("CompositingCompanion", icon = _icon("2LoudCompoBuilder.png"))

            # ----- Templates submenu -----
            self._buildTemplatesMenu(tb_ccMenu)
            # ----- Gizmos submenu -----
            self._buildGizmosMenu(tb_ccMenu)
            
        except Exception as e:
            nuke.message("[CC] Error when building menu: {}".format(e))

    def _buildTemplatesMenu(self, parentMenu):
        """Build the "Templates" submenu"""

        parentMenu.addCommand("Estofat")
        parentMenu.addCommand("Puré")
    
    def _buildGizmosMenu(self, parentMenu):
        """Build the "Gizmos" submenu"""

        parentMenu.addCommand("Patata")
        parentMenu.addCommand("Ceba")


