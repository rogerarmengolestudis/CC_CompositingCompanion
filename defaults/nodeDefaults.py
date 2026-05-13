import nuke



# Shuffle2
nuke.knobDefault("Shuffle2.label", "[value in1]")

# Crop
nuke.knobDefault("Crop.crop", "false")

# STMap
nuke.knobDefault("STMap.uv", "rgb")

# Viewer
nuke.knobDefault("Viewer.hide_input", "true")
