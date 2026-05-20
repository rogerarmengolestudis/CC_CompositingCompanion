# ////////////////////////////////////////////////////////////////////
# CC_CompositingCompanion - backDropUI.py
# ////////////////////////////////////////////////////////////////////

import os
import sys
import platform

sys.dont_write_bytecode = True  # Avoid writing .pyc files


try:
    from PySide2 import QtWidgets, QtCore, QtGui
except ImportError:
    from PySide6 import QtWidgets, QtCore, QtGui


import nuke
import nukescripts



# ---------------------------------------------------------------------------
# Main Panel Widget
# ---------------------------------------------------------------------------

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setWindowTitle("BackDroper - Compositing Companion")

        self.resize(400, 5000)

        self._build_ui()
        self._connect_signals()

    # ------------------------------------------------------------------
    # UI Construction
    # ------------------------------------------------------------------

    def _build_ui(self):
        root_layout = QtWidgets.QVBoxLayout(self)
        root_layout.setContentsMargins(8, 8, 8, 8)
        root_layout.setSpacing(6)

        # ---- Header label ----
        self.header_label = QtWidgets.QLabel("Back Droper")
        self.header_label.setStyleSheet("font-weight: bold; font-size: 20px;") # disabeled:  color: #33cc70;

        root_layout.addWidget(self.header_label)
        root_layout.addWidget(self._make_separator())

        # ---- Name input row ----
        input_row = QtWidgets.QHBoxLayout()
        input_row.addWidget(QtWidgets.QLabel("Name:"))

        self.name_field = QtWidgets.QLineEdit()
        self.name_field.setPlaceholderText("Enter backdrop name...")

        input_row.addWidget(self.name_field)
        root_layout.addLayout(input_row)

        # ---- Format Layout ----
        format_layout = QtWidgets.QHBoxLayout()

        self.center_check = QtWidgets.QCheckBox("Center")
        self.center_check.setChecked(True) 

        self.bold_check = QtWidgets.QCheckBox("Bold")
        self.bold_check.setChecked(True) 

        self.italics_check = QtWidgets.QCheckBox("Italics")

        self.bookmark_check = QtWidgets.QCheckBox("Bookmark")
        self.bookmark_check.setChecked(True) 

        self.size_spb = QtWidgets.QSpinBox()
        self.size_spb.setRange(0, 200)
        self.size_spb.setSingleStep(5)
        self.size_spb.setValue(25)

        self.size_text = QtWidgets.QLabel("Size")

        format_layout.addWidget(self.center_check)
        format_layout.addWidget(self.bold_check)
        format_layout.addWidget(self.italics_check)
        format_layout.addWidget(self.bookmark_check)
        format_layout.addWidget(self.size_spb)
        format_layout.addWidget(self.size_text)

        root_layout.addLayout(format_layout)


        root_layout.addWidget(self._make_separator())

        # ---- Action buttons ----
        btn_row = QtWidgets.QHBoxLayout()
        self.create_btn = QtWidgets.QPushButton("Create")
        self.save_btn = QtWidgets.QPushButton("Save")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        btn_row.addWidget(self.create_btn)
        btn_row.addWidget(self.save_btn)
        btn_row.addWidget(self.cancel_btn)
        root_layout.addLayout(btn_row)

    def _make_separator(self):
        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        return line

    # ------------------------------------------------------------------
    # Signal Connections
    # ------------------------------------------------------------------

    def _connect_signals(self):
        self.create_btn.clicked.connect(self._on_run)
        self.cancel_btn.clicked.connect(self._on_reset)

    # ------------------------------------------------------------------
    # Slots / Logic
    # ------------------------------------------------------------------

    def _on_run(self):
        name = self.name_field.text().strip()
        mode = self.mode_combo.currentText()
        enabled = self.enable_check.isChecked()

        self.log(f"Running — name={name!r}, mode={mode!r}, enabled={enabled}")

        # ---- Put your Nuke logic here ----
        # Example: iterate selected nodes
        selected = nuke.selectedNodes()
        if not selected:
            self.log("No nodes selected.")
            return

        for node in selected:
            self.log(f"  Processing: {node.name()} ({node.Class()})")
            # node['label'].setValue(name)  # example knob access

    def _on_reset(self):
        self.name_field.clear()
        self.mode_combo.setCurrentIndex(0)
        self.enable_check.setChecked(False)
        self.log_output.clear()

    def log(self, message: str):
        """Append a line to the log area and echo to Nuke's script editor."""
        self.log_output.appendPlainText(message)
        print(f"[MyPanel] {message}")



# ---------------------------------------------------------------------------
# Floating dialog (alternative / quick-launch)
# ---------------------------------------------------------------------------

def show_floating():
    """Open as a standalone floating window (useful during development)."""
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    dialog = QtWidgets.QDialog()
    dialog.setWindowTitle("BackDroper - Compositing Companion")
    dialog.setMinimumWidth(500)
    
    layout = QtWidgets.QVBoxLayout(dialog)
    layout.addWidget(Window())
    dialog.exec_()



# ---------------------------------------------------------------------------
# Dev entry point — run directly in Script Editor for quick iteration
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    show_floating()