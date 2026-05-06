# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - menu.py
# ////////////////////////////////////////////////////////////////////

from autoMenu import autoMenu
from variables import CCVariables
ccVars = CCVariables()
menuOperations = autoMenu.CCMenuBuilder(ccVars.PLUGIN_DIR)

menuOperations.createCCMenu(pluginRoot=ccVars.PLUGIN_DIR)