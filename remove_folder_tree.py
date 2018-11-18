# -*- coding: UTF-8 -*-
import shutil

def removeFolderInTree(folderPath):
  try:
    shutil.rmtree(folderPath)
  except Exception as e:
    print e
