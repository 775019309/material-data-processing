import os

def dircount(DIR):
    return len(os.listdir(DIR))

with open("log") as f:
   read_log = f.read()
   a = read_log.split()
   count = dircount("total")
   for each in a:
      if 'mvc-' in each or 'mp-' in each:
         count = count + 1
         each = each.replace(',','')
         each = each.replace('"','')
         os.system("curl https://www.materialsproject.org/rest/v2/materials/" + each + \
                   "/vasp/cif?API_KEY=XXX >" + each)   # Please add the API_KEY  
         each_read = open(each)
         string1 = each_read.read()
         string2 = string1.replace("\\n","\r\n")
         cif = str(count) + ".cif"
         os.system("touch " + cif)
         each_write = open(cif, "a+")
         each_write.write(string2)
         each_write.close()
         os.system("sed -i '$d' " + cif)  
         os.system("rm " + each)
os.system("sed -i '1d' *.cif")
os.system("sed -i '1i\# pymatgen' *.cif")
os.system("mv *.cif total/")
