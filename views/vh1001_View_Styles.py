# A helper class for setting some style options of Qt-elements

from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLayout,
    QPushButton,
    QLabel
)

# ----------------------------------------------------------------
#                              WIDGET 
def neutral_widget_style(widget:QWidget):
    widget.setStyleSheet("border: 0px; margin: 0px; background-color: white;")

def small_round_widget_corners(widget:QWidget):
    widget.setStyleSheet(widget.styleSheet() + "; border-radius: 5px;")

def medium_round_widget_corners(widget:QWidget):
    widget.setStyleSheet(widget.styleSheet() + "; border-radius: 40px;")
# ----------------------------------------------------------------

# ----------------------------------------------------------------
#                         SCROLLABLE AREA 
def scrollable_area_style(area:QScrollArea):
    area.setStyleSheet("border: 0px white solid; margin: 5px; background-color: white; border-radius: 5px;")
# ----------------------------------------------------------------

# ----------------------------------------------------------------
#                             LAYOUT 
def neutral_layout_style(layout:QLayout):
    layout.setSpacing(0)
    layout.setContentsMargins(0, 0, 0, 0)

def small_margin_layout_style(layout:QLayout):
    layout.setContentsMargins(1, 1, 1, 1)

def medium_margin_layout_style(layout:QLayout):
    layout.setContentsMargins(5, 5, 5, 5)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
#                              QLABEL 
def add_label_left_padding_style(label:QLabel):
    label.setStyleSheet(label.styleSheet() + "; margin-left: 5px;")
# ----------------------------------------------------------------

# ----------------------------------------------------------------
#                            BUTTON 
def import_button_style(button:QPushButton):
    button.setStyleSheet("background-color: #e8d8ac; border-radius: 8px;padding:5px; border: 1px solid grey;")