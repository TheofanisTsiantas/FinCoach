#

from Views.vh1000_Figure_Canvas import MplCanvas
from Views.vh1001_View_Styles import GRAPHICS_FONT_SIZE

def View_Expense_Evolution_Graph(title:str):
    canvas = MplCanvas()
    canvas.axes.plot([0, 1, 2, 10], [10, 1, 20, 3])
    canvas.axes.set_ylabel("Expenses [CHF]", fontsize=GRAPHICS_FONT_SIZE)
    canvas.axes.set_xlabel("Month-year", fontsize=GRAPHICS_FONT_SIZE)
    canvas.axes.set_title(title, fontsize=GRAPHICS_FONT_SIZE)
    canvas.fig.subplots_adjust(bottom=2*GRAPHICS_FONT_SIZE/100, top=9*GRAPHICS_FONT_SIZE/100, left=8*GRAPHICS_FONT_SIZE/1000, right=0.95)

    return canvas

def Month_Expense_Graph(title:str):
    canvas = MplCanvas()

    # Example pie chart data
    labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # "explode" the 2nd slice
    canvas.axes.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
    canvas.axes.axis('equal')  # Equal aspect ratio makes the pie circular.

    #canvas.axes.set_ylabel("Expenses [CHF]", fontsize=GRAPHICS_FONT_SIZE)
    #canvas.axes.set_xlabel("Month-year", fontsize=GRAPHICS_FONT_SIZE)
    canvas.axes.set_title(title, fontsize=GRAPHICS_FONT_SIZE)
    #canvas.fig.subplots_adjust(bottom=2*GRAPHICS_FONT_SIZE/100, top=9*GRAPHICS_FONT_SIZE/100, left=8*GRAPHICS_FONT_SIZE/1000, right=0.95)

    return canvas