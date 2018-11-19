# Dicom-Filtering
Filters dicom based on slice thickness and series ID and save useful information in a new csv file. Also remove corrupt or null dicom files.

Follow the simple steps:
1. Put all the .py files in a folder.
2. Create two folders. 'junk' and 'Repo'.
3. Change the source code for required slice thickness. 
4. Run Main.py file only.
5. Input name of the dicom files that needed to be filtered when asked.

The code is able to do the following steps:
1. Rename the Dicom files.
2. List all the important Dicom tags into a csv file.
3. Separate the usable Dicom into another folder based on SeriesID (considering Slice thickness <=2 and pixel spacing <= 1).
4. Each Series ID is assigned to each folder within the institute folder and the folders are named as A,B,C,D and so on.
5. Finally listing all the filtered data into another CSV file.
