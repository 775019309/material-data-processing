import re
f = open("log")
log = f.read()
f.close()
number = re.findall(r'(?<=\"band_gap": )\S+', log)
f = open("gap_NO.txt",'a+')
for each in number:
    each = each.replace(",","")
    each = each.replace('}','')
    each = each.replace(']','')
    f.write(each + '\n')
f.close()
