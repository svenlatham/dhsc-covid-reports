import urllib.request
import pyexcel as pe
import json
import re
import datetime

with open('sources.txt') as src_file:
    for line in src_file:
        resp = urllib.request.urlopen(line)
        ods = resp.read()
        data = pe.get_sheet(file_type="ods", file_content=ods)
        #print(data)
        date = None
        for row in data.row:
            if (row[0] == 'Region'):
                # This is the header, so we'll use this to parse out the date
                m = re.search('(\d+) ([A-Za-z]+) (\d{4})', row[10])
                if m != None:
                    dt_week = datetime.datetime.strptime(m.group(0), '%d %B %Y')
                    date = dt_week.date()
                else:
                    print("Could not parse %s" % row[10])
            elif (row[1] != ''):
                if date == None:
                    raise "Date has not been parsed yet"
                output = (str(date), row[0], row[1], row[2].strip(), row[3], row[5], row[7], row[9])
                print(output)

