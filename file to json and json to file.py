import os

new_data = 'C:\\Users\\Preyash Patel\\Desktop\\project'

file_paths = []
#loop to get append file_paths 
for root, directories, files in os.walk(new_data):
    for filename in files:
        # Join the two strings in order to form the full filepath.
        filepath = os.path.join(root, filename)
        #to append
        file_paths.append(filepath)
            

data = {}        
for i in file_paths[50:100]:
    try:
        file1 = open(i,"r")
        data[i[39:]] = file1.readlines() 
        file1.close()
    except:
        pass


#storing the all data
import json
file1 = open("data.json","w")
json.dump(data, file1)
file1.close()

#there is total 120 files
#so here is trick to make files from one json file
import os
os.mkdir("Project")

file1 = open("data.json","r")
jsonData = file1.readlines() 
file1.close()

dicData = eval(jsonData[0])
listOfFile = dicData.keys()

for i in listOfFile:
    if len(i.split("\\")) == 1:
        file1 = open("Project\\" + i,"w")
        file1.writelines(dicData[i])
        file1.close()
    elif len(i.split("\\")) == 2:
        try:
            try:
                os.mkdir("Project\\"+i.split("\\")[0])
            except:
                pass
            file1 = open("Project\\" + i,"w")
            file1.writelines(dicData[i])
            file1.close()
        except:
            print("File Erroe in writing path: ", i)
    elif len(i.split("\\")) == 3:
        try:
            try:
                os.mkdir("Project\\"+ i.split("\\")[0])
            except:
                pass
            try:
                os.mkdir("Project\\"+i.split("\\")[0]+i.split("\\")[1])
            except:
                pass
            file1 = open("Project\\" + i,"w")
            file1.writelines(dicData[i])
            file1.close()
        except:
            print("File Erroe in writing path: ", i)