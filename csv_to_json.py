# -*- coding: UTF-8 -*-
import pandas

def convert(csvPathName, newJsonPathName):
  try:
    df = pandas.read_csv(csvPathName)
    df.to_json(newJsonPathName, orient='records')
  except Exception as e:
    print e
