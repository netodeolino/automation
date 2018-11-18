# -*- coding: UTF-8 -*-
import os

def createFolder(folderPathAndName):
  if not os.path.exists(folderPathAndName):
    os.makedirs(folderPathAndName)