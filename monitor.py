import speedtest 
import datetime 
import csv 

servers = []
threads = None
s = speedtest.Speedtest()

with open('test.csv', mode='w') as speedcsv:
  csv_writter = csv.DictWriter(speedcsv, fieldnames=['time', 'download speed', 'upload speed'])
  csv_writter.writeheader()
  while True:
    time = datetime.datetime.now().strftime("%H:%M:%S")
    download_speed = round((round(s.download(threads=threads)) / 1048576), 2)
    upload_speed = round((round(s.upload(threads=threads)) / 1048576), 2)
    csv_writter.writerow({
      'time': time,
      'download speed': download_speed,
      'upload speed': upload_speed
    })