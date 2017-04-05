import os
import subprocess
import csv
import signal
import time
import re
from config import *
import datetime
st = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
csv_out = open('console-error-output-{}.csv'.format(st), 'w', encoding='utf-8')
writer = csv.writer(csv_out)
with open(inputFileLoc, 'r', encoding='utf-8') as csv_in:
	reader = csv.reader(csv_in)
	count = 0
	for row in reader:
		count += 1
		if count == 1:
			continue
		links = row[2]
		link = links.split(' ')[0]
		link.replace(' ', '')
		print("Processing user id:",  row[1])
		relevantLines = list()
		if link and link != "":
			if os.path.exists(logLoc):
				os.remove(logLoc)
			cmd = ' '.join([chromeLoc, \
				"--enable-logging", "--v=1", link])
			pro = subprocess.Popen(cmd, stdout=subprocess.PIPE) 
			time.sleep(sleepTime)
			pro.terminate()
			fin = open(logLoc, 'r')
			for line in fin.readlines():
				print(line)
				if "CONSOLE" in line:
					bits = line.split(']')
					secHalf = bits[1:]
					print(' '.join(secHalf))
					relevantLines.append(' '.join(secHalf))
			fin.close()
			time.sleep(1)
		writer.writerow([row[0], row[1], link, '|'.join(relevantLines)])
