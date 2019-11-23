# file_management using python
File Management using the python os and shutil Module
<hr>

Problem: 
I have 25k photos and videos which include various file format(like .json, .jpeg, .jpg, .png, mov, .mp4, .pdf).
I want to delete the .json files and arrange video and photos in structure(my photos and video includes Screenrecorder, Screenshot, Snapchat/Photos, Snapchat/Video, PDF, GIF, Quotes, Collage, etc).

if I want to move 3 GB of data then windows will take at least 1 minute, the big task is to do bifurcation in the required structure.

<hr>

Solution:
So I decided to use python as my tool to manage, and here is the solution...

  # -*- coding: utf-8 -*-
  """
  Created on Sat Nov 23 21:08:41 2019
  @author: preya
  """

  import os
  import shutil

  #path which contains files it may be inside sub folders
  data = 'C:/Data/Home/Google Photos'
  new_data = 'C:/Data/Home/takeout-20191022T082710Z-002/Takeout/Google Photos'
  #converting the path into the required format
  #data.replace('\\','/')
  #an empty list to append the file's full path
  file_paths = []
  #loop to get append file_paths 
  for root, directories, files in os.walk(new_data):
      for filename in files:
          # Join the two strings in order to form the full filepath.
          filepath = os.path.join(root, filename)
          #to append
          file_paths.append(filepath)

  #to remove files extention with .json and move other to data path
  for i in file_paths:
      i.replace('\\','/')
      #to delete the json files
      if(".json" in i):
          i.replace('\\','/')
          os.remove(i)

  #furter bifurcation into folders
  for i in file_paths:
      #to delete the json files
      if("Screenrecorder" in i):
          try:
              shutil.move(i, (data+"/Screenrecorder"))
          except:
              #to comeout from duplication erroe
              print(i)
      elif("Screenshot" in i):
          try:
              shutil.move(i, "C:/Data/Home/Google Photos/Screenshot")
          except:
              #to comeout from duplication erroe
              print(i)
      elif("Snapchat" in i):
          if(".MP4" in i or ".MOV" in i or ".mp4" in i or ".mov" in i):
              try:
                  shutil.move(i, "C:/Data/Home/Google Photos/Snapchat/Photos")
              except:
                  #to comeout from duplication erroe
                  print(i)
          else:
              try:
                  shutil.move(i, "C:/Data/Home/Google Photos/Snapchat/Video")
              except:
                  #to comeout from duplication erroe
                  print(i)
      elif(".MP4" in i or ".MOV" in i or ".mp4" in i or ".mov" in i ):
          try:
              shutil.move(i, data+"/Videos")
          except:
              #to comeout from duplication erroe
              print(i)
      elif(".pdf" in i or ".PDF" in i):
          try:
              shutil.move(i, data+"/PDF")
          except:
              #to comeout from duplication erroe
              print(i)
      elif(".gif" in i):
          try:
              shutil.move(i, data+"/GIF")
          except:
              #to comeout from duplication erroe
              print(i) 
      elif("amsuccess" in i):
          try:
              shutil.move(i, data+"/Quotes")
          except:
              #to comeout from duplication erroe
              print(i) 
      elif("COLLAGE" in i):
          try:
              shutil.move(i, data+"/Collage")
          except:
              #to comeout from duplication erroe
              print(i) 
      elif(".jpg" in i or ".JPG" in i or ".png" in i or ".jpeg" in i or ".mov" in i ):
          try:
              shutil.move(i, data+"/Photo")
          except:
              #to comeout from duplication erroe
              print(i) 
      else:
          try:
              shutil.move(i, data+"/Photos")
          except:
              #to comeout from duplication erroe
              print(i)
