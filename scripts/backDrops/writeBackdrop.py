# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - writeBackdrop.py
# ////////////////////////////////////////////////////////////////////




import json
import os

from variables import CCVariables
ccVars = CCVariables()

# ----- Directory paths -----
ICONS_DIR  = ccVars.ICONS_DIR
SCRIPTS_DIR = ccVars.SCRIPTS_DIR

PRESETS_PATH = os.path.join(SCRIPTS_DIR, 'backDrops', 'utils', 'backdrop_presets.json')


def _load() -> dict:
    if not os.path.exists(PRESETS_PATH):
        return {"presets": []}
    with open(PRESETS_PATH, "r") as f:
        return json.load(f)


def _save(data: dict):
    with open(PRESETS_PATH, "w") as f:
        json.dump(data, f, indent=4)


def list_presets():
    data = _load()
    for p in data["presets"]:
        print(f"  {p['name']:20s}  color={p['color']}  bold={p['bold']}  "
              f"italics={p['italics']}  size={p['size']}")
    return data["presets"]


def add_preset(name: str,
               color: str = "#3a3a3a",
               bold: bool = True,
               italics: bool = False,
               center: bool = True,
               bookmark: bool = True,
               size: int = 25):
    """Add or overwrite a preset entry."""
    data = _load()
    # Overwrite if name already exists
    data["presets"] = [p for p in data["presets"] if p["name"] != name]
    data["presets"].append({
        "name":     name,
        "color":    color,
        "bold":     bold,
        "italics":  italics,
        "center":   center,
        "bookmark": bookmark,
        "size":     size,
    })
    _save(data)


def remove_preset(name: str):
    """Remove a preset by name."""
    data = _load()
    before = len(data["presets"])
    data["presets"] = [p for p in data["presets"] if p["name"] != name]
    if len(data["presets"]) < before:
        _save(data)
        print(f"[preset_writer] Removed preset '{name}'")
    else:
        print(f"[preset_writer] Preset '{name}' not found")


def run():
    add_preset()


keyShortCut = 'Ctrl+Shift+Alt+B'
