from google import search
import csv

output = csv.writer(open("output.csv","w"))    # <= 500 hits
output1 = csv.writer(open("output1.csv","w")) # >500 hits
count = 0
for url in search("Royal Enfield Reviews", stop = 20):
	print(url)
