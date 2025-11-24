# A helper class for setting some style options of Qt-elements

from PyQt5.QtWidgets import (
    QWidget,
    QScrollArea,
    QLayout,
    QPushButton,
    QLabel
)

GRAPHICS_BKG_COLOR = "#D1E5F4"
GRAPHICS_FONT_SIZE = 10

# ----------------------------------------------------------------
#                              WIDGET 
def set_bkg_color_graphic_widget_style(widget:QWidget):
    widget.setStyleSheet(widget.styleSheet() + "; background-color: "+GRAPHICS_BKG_COLOR+";")

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

def save_button_style(button:QPushButton):
    button.setStyleSheet("background-color: #ADD8E6; border-radius: 8px;padding:5px; border: 1px solid grey;")