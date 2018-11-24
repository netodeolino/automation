# -*- coding: UTF-8 -*-
from crontab import CronTab

cronPrintDateTime = CronTab(user='netodeolino')

job = cronPrintDateTime.new(command='python /home/netodeolino/GitHub/Variados/automation/write_utils.py')
job.minute.every(1)
 
cronPrintDateTime.write()

# cronPrintDateTime.remove_all()