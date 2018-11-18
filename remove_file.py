# -*- coding: UTF-8 -*-
import os

def removeFile(filePath):
  if os.path.exists(filePath):
    os.remove(filePath)
  else:
    print("The file does not exist")
