from Main_1 import root
import os.path
from datetime import datetime
import pydicom as dicom
import csv

start_time = datetime.now()
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
            
with open('junk/Full_Filtered_File.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["Folder Name","Institution Name","Manufacturer","Patient's Name","Patient's ID","Patient's Sex","Patient Birth Date",
                             "Study Description","Physician Name","Modality","Study UID","Series UID","SliceThickness",
                             "Study ID","Rows","Columns","Pixel Spacing"])
       

        for dcm_file in dcm_files:
            ds = dicom.read_file(dcm_file)
            fileName = dcm_file.split("\\")
            spamwriter.writerow([fileName[1], ds.get("InstitutionName", "None"),ds.get("Manufacturer", "None"), ds.get("PatientName", "None"), ds.get("PatientID", "None"),
                                 ds.get("PatientSex", "None"), ds.get("PatientBirthDate", "None") ,ds.get("StudyDescription", "None"),ds.get("ReferringPhysicianName", "None"),
                                 ds.get("Modality", "None"),ds.get("StudyInstanceUID", "None"), ds.get("SeriesInstanceUID", "None"), ds.get("SliceThickness", "None"),
                                 ds.get("StudyID", "None"),ds.get("Rows", "None"), ds.get("Columns", "None"),ds.get("PixelSpacing", "None") ])
 
for path, subdirs, files in os.walk(root, topdown=False):
    try:
        os.rmdir(path) #to delete empty folders in the directory
    except OSError as ex:
        print(ex)
    
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

os.remove('junk/Ignore_Junk.csv',dir_fd=None)