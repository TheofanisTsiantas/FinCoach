#
import numpy as np

from Views.vh1000_Figure_Canvas import MplCanvas
from Views.vh1001_View_Styles import GRAPHICS_FONT_SIZE
from Helpers import Categories

def View_Expense_Evolution_Graph(title:str, transactions:dict ={}):
    canvas = MplCanvas()
    max_exp = 0;
    if transactions=={}:
        # Dummy plot to ensure legend is visible even prior to reading data
        canvas.axes.text(0.1, 0.5, "Import a month, to see the stats", fontsize=GRAPHICS_FONT_SIZE)
        canvas.axes.set_xticks([])
        canvas.axes.set_yticks([])
    else:
        singleMonth = True;
        for cat,cat_expense_per_month in transactions.items():
            if len(cat_expense_per_month[0])>1:
                singleMonth = False;
                break;

        if  singleMonth:
            it = 1;
            for cat,cat_expense_per_month in transactions.items():
                expense_in_thousands = [v/1000 for v in cat_expense_per_month[1]];
                if expense_in_thousands:
                    max_exp = max(max_exp, max(expense_in_thousands))
                canvas.axes.bar(it,expense_in_thousands,label=cat)
                it = it+1;
                canvas.axes.set_xlabel("Expense type", fontsize=GRAPHICS_FONT_SIZE)
        else:
            canvas.axes.clear();
            for cat,cat_expense_per_month in transactions.items():
                expense_in_thousands = [v/1000 for v in cat_expense_per_month[1]];
                if expense_in_thousands:
                    max_exp = max(max_exp, max(expense_in_thousands))
                canvas.axes.plot(cat_expense_per_month[0],expense_in_thousands,label=cat)
                canvas.axes.set_xlabel("Month-year", fontsize=GRAPHICS_FONT_SIZE)
        canvas.axes.set_ylabel("Expenses [kCHF]", fontsize=GRAPHICS_FONT_SIZE)
        canvas.axes.set_title(title, fontsize=GRAPHICS_FONT_SIZE)
        canvas.axes.grid(True)
        canvas.axes.set_yticks(np.arange(0.0, max_exp, 0.5))        
        leg = canvas.axes.legend(ncol=1,
                             loc='upper left',            # anchor point on the legend
                             bbox_to_anchor=(-0.5, 1.),  # position in axes coordinates
                             borderaxespad=0)
        leg.set_draggable(True)
        canvas.fig.subplots_adjust(bottom=2*GRAPHICS_FONT_SIZE/100, top=9*GRAPHICS_FONT_SIZE/100, left=3*GRAPHICS_FONT_SIZE/100, right=0.95)
    return canvas

def Month_Expense_Graph(title:str, expense_distribution:dict = {}):
    # expense_distribution:dict --> { CATEGORY : XX% of monthly cost }
    canvas = MplCanvas()

    if expense_distribution == {}:
        canvas.axes.text(0.1, 0.5, "Select a month (after importing), to see the stats", fontsize=GRAPHICS_FONT_SIZE)
        canvas.axes.set_xticks([])
        canvas.axes.set_yticks([])
    else:
        canvas.axes.set_title(title, fontsize=GRAPHICS_FONT_SIZE)
        canvas.axes.pie(list(expense_distribution.values()),  labels=list(expense_distribution.keys()), labeldistance=None, 
                    shadow=False, startangle=90)
        legend_labels = []
        for key,item in expense_distribution.items():
            legend_labels.append(str(key)+": "+str(item)+"%")
            leg = canvas.axes.legend(legend_labels,
                             loc='upper left',            # anchor point on the legend
                             bbox_to_anchor=(-0.15, 1.),  # position in axes coordinates
                             borderaxespad=0)
            leg.set_draggable(True)

        canvas.axes.axis('equal')  # Equal aspect ratio makes the pie circular.
    return canvas