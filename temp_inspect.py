import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
path = Path('D:/work/projects/data x projects/New folder/ROW_DATA.xlsx')
with zipfile.ZipFile(path) as z:
    rel = ET.fromstring(z.read('xl/workbook.xml'))
    ns = {'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    sheets = [(s.attrib['name'], s.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')) for s in rel.findall('.//x:sheets/x:sheet', ns)]
    print(sheets)
    wbrel = ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    ids = {r.attrib['Id']: r.attrib['Target'] for r in wbrel.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship')}
    print([(name, ids[rid]) for name,rid in sheets])
