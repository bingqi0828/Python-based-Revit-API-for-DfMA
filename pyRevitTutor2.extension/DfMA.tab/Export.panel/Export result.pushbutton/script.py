from Autodesk.Revit import UI
from rpw.ui.forms import CommandLink
import xlwt

wb=xlwt.Workbook()
sh1=wb.add_sheet("1")

uidoc=__revit__.ActiveUIDocument
doc=uidoc.Document

id_list=uidoc.Selection.GetElementIds()
element_list=[]
i=0

for each in id_list:
    element=doc.GetElement(each)
    id=element.LookupParameter("ElementID")
    length=element.LookupParameter("Length")
    area=element.LookupParameter("Area")
    sh1.write(i,0,id.AsInteger())
    sh1.write(i,1,length.AsDouble())
    sh1.write(i,2,area.AsDouble())
    print ((id.AsInteger(),length.AsDouble(),area.AsDouble()))
    element_list.append((id.AsInteger(),length.AsDouble(),area.AsDouble()))
    i=i+1
    
wb.save("test.xls")
