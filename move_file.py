import os,shutil
# .exe , .msi, .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx
to_dir = "C:/Users/yakka_ch7sh0s/OneDrive/Desktop/white hat jr.com/projects_python/project_111/doutuments_files"
from_dir = "C:/Users/yakka_ch7sh0s/OneDrive/Desktop/white hat jr.com/projects_python/project_111"
list_of_allFiles = os.listdir(from_dir)
for l in list_of_allFiles:
    name,ext = os.path.splitext(l)
    if(ext==''):
        continue
    if(ext in ['.csv', '.pdf' , '.xls' , '.xlsx' , '.ppt' , '.pptx','.doc']):
        s_path = from_dir+'/'+l
        d_path = to_dir
        if(os.path.exists(d_path)):
            shutil.move(s_path,d_path+'/'+l)
        else:
            os.makedirs(d_path)
            shutil.move(s_path,d_path+'/'+l)
