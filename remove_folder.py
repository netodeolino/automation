# -*- coding: UTF-8 -*-
import os

def removeFolder(folderPath):
  if os.path.exists(folderPath):
    os.rmdir(folderPath)
  else:
    print("The folder does not exist")
