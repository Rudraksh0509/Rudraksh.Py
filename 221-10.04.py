import os
import shutil

os.makedirs('subdir/new_subdir', exist_ok=True)
shutil.copy('students.csv', 'subdir/new_subdir/students_copy.csv')
print("File copied to new subdirectory.")
