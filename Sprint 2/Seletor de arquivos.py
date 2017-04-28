import os, shutil
os.chdir('C:\\Users\\')
a="jpg"
b="pdf"
for folderName, subfolders, filenames in os.walk('C:\\Users\\'):
    for filename in filenames:
        k=filename
        t=k[-3]+k[-2]+k[-1]
        if t==b:
            os.makedirs('C:\\PDF')
            shutil.move(os.path.join(folderName+"\\"+filename),'C:\\PDF')
        if t==a:
            os.makedirs('C:\\JPG')
            shutil.move(os.path.join(folderName+"\\"+filename),'C:\\JPG')
