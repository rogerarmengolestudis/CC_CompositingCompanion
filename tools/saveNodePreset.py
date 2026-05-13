# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - saveNodePreset.py
# ////////////////////////////////////////////////////////////////////

import nuke
import os

from collections import OrderedDict

from variables import CCVariables
ccVars = CCVariables()

# Where to save
def get_output_path():
    dir = os.path.join(ccVars.PLUGIN_DIR, "defaults", "nodeDefaults.py")
    return dir
 
 
# Knobs to always skip (internal / non-user knobs)
SKIP_KNOBS = {
    "name", "xpos", "ypos", "selected",
    "cached", "disable", "dope_sheet", "bookmark",
    "postage_stamp", "postage_stamp_frame",
}
 
 
def collect_presets(node):
    """Return list of (node_class, knob_name, value_str) for changed knobs."""
    cls = node.Class()
    presets = []
 
    # Create a temporary fresh node of the same class to compare defaults
    try:
        tmp = nuke.createNode(cls, inpanel=False)
    except Exception:
        nuke.message("Could not create a temp node for: " + cls)
        return presets
 
    for knob_name, knob in node.knobs().items():
        if knob_name in SKIP_KNOBS:
            continue
        if knob_name.startswith("_"):
            continue
 
        # Only handle knobs that have a simple string-representable value
        try:
            current = knob.toScript()
            default = tmp[knob_name].toScript()
        except Exception:
            continue
 
        if current != default and current.strip() != "":
            presets.append((cls, knob_name, current))
 
    nuke.delete(tmp)
    return presets
 
 
def save_presets():

    # Get Node Info
    node = nuke.selectedNode()
    if not node:
        nuke.message("Select at least one node first.")
        return
    
    nodeName = node.Class()

    all_presets = []
    all_presets.extend(collect_presets(node))
 
    if not all_presets:
        nuke.message("No knob differences found vs factory defaults.")
        return
    
    # Get path
    output_path = get_output_path()
 
    # Group by node class for readable output
    groups = OrderedDict()
    for cls, knob, value in all_presets:
        groups.setdefault(cls, []).append((knob, value))
 
    # Structure File
    lines = []
    lines.append("")
    for cls, knobs in groups.items():
        lines.append("# " + cls)
        for knob, value in knobs:
            # Escape any quotes inside the value
            safe_value = value.replace("\\", "\\\\").replace('"', '\\"')
            lines.append('nuke.knobDefault("{}.{}", "{}")'.format(cls, knob, safe_value))
        lines.append("")
 
    with open(output_path, "a") as f:
        f.write("\n".join(lines))
 
    nuke.message("Saved {} preset(s) to:\n{}".format(len(all_presets), output_path))

save_presets()