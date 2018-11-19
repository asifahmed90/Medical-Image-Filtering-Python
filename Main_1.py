
import os
dir = os.getcwd()
print (dir)
dir2 = os.chdir('C:/Users/immersivetouch/Desktop/')
print (dir2)

print ("Hello, World!")


import os.path
import pydicom as dicom
import csv
import shutil
import string

alpha = string.ascii_uppercase


root = input("Enter Directory Name: ")
#path = os.path.join(root, "targetdirectory")
i=1


for path, subdirs, files in os.walk(root):
    for name in files:
        if not name.endswith ('.dcm'):
            os.rename(os.path.join(path, name), os.path.join(path,'MR000'+ str(i)+'.dcm'))
            i=i+1
            print('initial path --->> \n',str(os.path.join(path, name)))
            print('New Path --->> \n', str(os.path.join(path,'MR000'+ str(i)+'.dcm')))

dcm_files = []
for path, dirs, files in os.walk(root):
    for names in files:
        if names.endswith(".dcm"):
            dcm_files.append(os.path.join(path, names))
            
#print (dcm_files)
            
with open('junk/Full_Complete_File.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["Folder Name","Institution Name","Manufacturer","Patient's Name","Patient's ID","Patient's Sex","Patient Birth Date",
                             "Study Description","Physician Name","Modality","Study UID","Series UID","SliceThickness",
                             "Study ID","Rows","Columns","Pixel Spacing"])
        series = dict()
        temp = 0
        #temp = 'A'
        #i=1
        folder_temp = "NULL"

        for dcm_file in dcm_files:
            ds = dicom.read_file(dcm_file, force='True')
            fileName = dcm_file.split("\\")
            spamwriter.writerow([fileName[1], ds.get("InstitutionName", "None"),ds.get("Manufacturer", "None"), ds.get("PatientName", "None"), ds.get("PatientID", "None"),
                                 ds.get("PatientSex", "None"), ds.get("PatientBirthDate", "None") ,ds.get("StudyDescription", "None"),ds.get("ReferringPhysicianName", "None"),
                                 ds.get("Modality", "None"),ds.get("StudyInstanceUID", "None"), ds.get("SeriesInstanceUID", "None"), ds.get("SliceThickness", "None"),
                                 ds.get("StudyID", "None"),ds.get("Rows", "None"), ds.get("Columns", "None"),ds.get("PixelSpacing", "None") ])

            folder = fileName[1]
            #print (folder)
            
            if ((ds.get("SliceThickness", "None") == 'None') or (ds.get("PixelSpacing", "None") == 'None')):
                shutil.move(dcm_file, 'Repo')

            elif (ds.get("SliceThickness", "None") > 2):
                shutil.move(dcm_file, 'Repo')
                
            else:
                pass
                if (folder != folder_temp):
                    temp = 0
                    folder_temp = folder
                    
                dummy = ds.get("SeriesInstanceUID", "None")
                dummy2 = (root+'/'+ fileName[1] +'/' + alpha[temp])
                
                if dummy not in list(series.keys()):
                    series.update({dummy:dummy2})
                    print (series)
                    temp += 1
                    
                    os.makedirs(dummy2,exist_ok=True)
                    
                    try:
                        shutil.move(dcm_file,dummy2)
                    except OSError:
                        pass
                        
                else:
                    dummy3 = series[dummy]
                    #shutil.move(dcm_file, dummy3)
                    try:
                        shutil.move(dcm_file,dummy3)
                    except OSError:
                        pass
 
               
        

