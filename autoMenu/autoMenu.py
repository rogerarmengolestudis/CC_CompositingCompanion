# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - autoMenu.py
# ////////////////////////////////////////////////////////////////////

import nuke
import os
import re

from variables import CCVariables
ccVars = CCVariables()

# ----- Directory paths -----





# ///////////////////////////////////////////////////////////////////
# Helpers
# ///////////////////////////////////////////////////////////////////


    



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

