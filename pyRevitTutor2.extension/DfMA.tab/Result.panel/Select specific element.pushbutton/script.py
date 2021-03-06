from rpw.ui.forms import CommandLink, TaskDialog, SelectFromList, Alert
from Autodesk.Revit import UI
from Autodesk.Revit import DB
import xlwt
import xlrd
import clr

uidoc=__revit__.ActiveUIDocument
doc=uidoc.Document

clr.AddReference("System")
from System.Collections.Generic import List
element_list = List[DB.ElementId]()

wb=xlrd.open_workbook("test.xls")
sh1=wb.sheet_by_name("1")

rows=sh1.nrows
id_list=[]
explanation=[]
for i in range(rows):
    id_list.append(('Element '+str(int(sh1.cell_value(i,0)))))
    explanation.append(str(sh1.cell_value(i,1)))

value=SelectFromList('Check Result',id_list)

if value:
    Alert('Details',title='Details',header='Length should be less than 20')

element_list.Add(DB.ElementId(int(value.lstrip('Element'))))
uidoc.Selection.SetElementIds(element_list)
