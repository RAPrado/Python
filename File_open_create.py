#Reference : https://www.pythontutorial.net/python-basics/python-create-text-file/

#Create a text file
f = open ('file_name.txt,'w',encoding='utf-8')

#where
#'w' – open a file for writing, and if the file doesn’t exist, the open() function creates a new file. Otherwise, it’ll overwrite the contents of the existing file.
#'a' – open a file for append new lines.
#'x' – open a file for exclusive creation, and if the file exists, the open() function raises an error (FileExistsError). Otherwise, it’ll create the text file.

#Record the information in file
f.write('Infomation' +  '\n') #Insert a break line

f.close() #Close the file
