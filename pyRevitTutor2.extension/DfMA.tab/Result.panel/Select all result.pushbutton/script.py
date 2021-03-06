from Autodesk.Revit import UI
from Autodesk.Revit import DB
import xlwt
import xlrd
import clr

clr.AddReference("System")
from System.Collections.Generic import List
uidoc=__revit__.ActiveUIDocument
doc=uidoc.Document


element_list = List[DB.ElementId]()

wb=xlrd.open_workbook("test.xls")
sh1=wb.sheet_by_name("1")

rows=sh1.nrows
for i in range(rows):
    element_list.Add(DB.ElementId(sh1.cell_value(i,0)))


uidoc.Selection.SetElementIds(element_list)
