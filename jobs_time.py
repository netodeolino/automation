# -*- coding: UTF-8 -*-
import time
from main import main

def job():
  main()

if __name__ == '__main__':
  while True:
    job()
    time.sleep(10)
    # 10 seconds