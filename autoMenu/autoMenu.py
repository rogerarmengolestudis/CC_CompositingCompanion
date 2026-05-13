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

    path = os.path.join(ICONS_DIR, f"{filename}.png")

    if path is None:
        path = os.path.join(ICONS_DIR, "missingIcon.png")

    return path

def _label(raw_name):
    return raw_name.replace("_", " ")
 
 
def _load_template(path):
    """Paste a .nk template into the current Nuke script at the viewer centre"""
    nuke.nodePaste(path)
 
 
def _load_gizmo(name):
    """Create a gizmo node by class name (Nuke must have it on its plugin path)"""
    nuke.createNode(name)
 
 




# ////////////////////////////////////////////////////////////////////
# Menu item factory
# ////////////////////////////////////////////////////////////////////
 
def _make_template_command(path):
    return lambda p=path: _load_template(p)
 
 
def _make_gizmo_command(name):
    return lambda n=name: _load_gizmo(n)

    



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
            tb_ccMenu = toolbar.addMenu("CompositingCompanion", icon = _icon("2LoudCompoBuilder"))

            # ----- Templates submenu -----
            self._buildTemplatesMenu(tb_ccMenu)
            # ----- Gizmos submenu -----
            self._buildGizmosMenu(tb_ccMenu)
            # ----- External submenu -----
            self._buildExternalMenu(tb_ccMenu)

        except Exception as e:
            nuke.message("[CC] Error when building menu: {}".format(e))
            raise



    def _buildTemplatesMenu(self, parentMenu):
        """Build the "Templates" submenu"""
        templatesMenu = parentMenu.addMenu("CC_Templates", icon = _icon("templateIcon"))
        self._scanDirectory(self.templatesDir, templatesMenu, ".nk", _make_template_command)


    
    def _buildGizmosMenu(self, parentMenu):
        """Build the "Gizmos" submenu"""
        gizmosMenu = parentMenu.addMenu("CC_Gizmos", icon = _icon("gizmoIcon"))
        self._scanDirectory(self.gizmosDir, gizmosMenu, ".gizmo", _make_gizmo_command)
        self._scanDirectory(self.gizmosDir, gizmosMenu, ".nk", _make_template_command)
    


    def _buildExternalMenu(self, parentMenu):
        """Build the "External" submenu (for items that are not stored in the plugin folders)"""
        externalMenu = parentMenu.addMenu("External", icon = _icon("externalIcon"))
        self._scanDirectory(self.gizmosDir, externalMenu, ".gizmo", _make_gizmo_command)
        self._scanDirectory(self.gizmosDir, externalMenu, ".nk", _make_template_command)

    


    def _scanDirectory(self, directory, parentMenu, extension, commandFn):
        """Scan directory and create sub menus and items"""
        try:
            entries = sorted(os.listdir(directory))
        except OSError as e:
            nuke.message("[CC] Error accessing directory '{}': {}".format(directory, e))
            return
        
        for entry in entries:
            path = os.path.join(directory, entry)

            if os.path.isdir(path):

                # Get element basics
                sub_label = _label(entry)
                sub_icon = _icon(entry)

                # Create Submenu and scan it recursively
                sub_menu = parentMenu.addMenu(sub_label, icon=sub_icon)
                self._scanDirectory(path, sub_menu, extension, commandFn)
            
            if os.path.isfile(path) and entry.lower().endswith(extension):
                entry_name = entry[:-len(extension)]
                entry_label = _label(entry_name)
                entry_icon = _icon(entry_name)

                parentMenu.addCommand(entry_label, commandFn(path), icon=entry_icon)





