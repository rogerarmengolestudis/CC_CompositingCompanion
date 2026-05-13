# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - menu.py
# ////////////////////////////////////////////////////////////////////

from autoMenu import autoMenu
from variables import CCVariables
ccVars = CCVariables()

from defaults import nodeDefaults

nodeDefaults





menuOperations = autoMenu.CCMenuBuilder(ccVars.PLUGIN_DIR)

menuOperations.createCCMenu(pluginRoot=ccVars.PLUGIN_DIR)

print("[CC] Compositing Companion plugin initialized successfully.")