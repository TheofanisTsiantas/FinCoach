# A helper class for setting some style options of Qt-elements

from PyQt5.QtWidgets import (
    QWidget,
    QLayout
)

def neutralize_widget_style(widget:QWidget):
    widget.setStyleSheet("border: 0px; margin: 0px")

def neutralize_layout_style(layout:QLayout):
    layout.setSpacing(0)
    layout.setContentsMargins(0, 0, 0, 0)