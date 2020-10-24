import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv

times = []
download = []
upload = []

with open('test.csv', 'r') as csvfile:
  plots = csv.reader(csvfile, delimiter = ',')
  next(csvfile)
  for row in plots:
    if row != []:
      times.append(str(row[0]))
      download.append(float(row[1]))
      upload.append(float(row[2]))
    else:
      continue
    
plt.figure()
plt.plot(times, download, label = "download speed", color='r')
plt.plot(times, upload, label = "upload speed", color='b')
plt.xlabel("time")
plt.ylabel("speed in Mb/s")
plt.title("internet speed")
plt.legend()
plt.savefig("test_graph.jpg", bbox_inches = "tight")