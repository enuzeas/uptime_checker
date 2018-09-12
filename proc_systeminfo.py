import os
import re
import datetime
#server = ['10.12','10.13','10.22','10.23','10.31','10.32','10.33','10.34','10.41','10.42','10.43','10.44']
import json
import shutil
'''serverdict = {'CMS1':'192.168.10.12',
          'CMS2':'192.168.10.13',
          'DB1':'192.168.10.22',
          'DB2':'192.168.10.23',
          'TC1':'192.168.10.31',
          'TC2':'192.168.10.32',
          'TC3':'192.168.10.33',
          'TC4':'192.168.10.34',
          'CA1':'192.168.10.41',
          'CA2':'192.168.10.42',
          'TM1':'192.168.10.43',
          'TM2':'192.168.10.44',
          'TM3':'192.168.10.45',
          'TM4':'192.168.10.46',
          'TM5':'192.168.10.47',
          'TM6':'192.168.10.48',
          'QC1':'192.168.10.61',
          'QC2':'192.168.10.62',
          'IF1':'192.168.20.32',
              'IF2':'192.168.20.33',
              'AD1':'192.168.20.12',
              'AD2':'192.168.20.13',
              'SH1':'192.168.20.22',
              'SH2':'192.168.20.23',
              'WAS1':'192.168.30.12',
              'WAS2':'192.168.30.13'
              }
'''

p = re.compile('[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}, [가-힣]{2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}')


with open('C:/server.json') as f:
    serverdict = json.load(f)

length  = len(serverdict['Server'])
def server(index):
    command = ('systeminfo /s %s ' %serverdict["Server"][index].get("IP") +
               '/U %s ' %serverdict["Server"][index].get("ID") +
               '/p %s ' %serverdict["Server"][index].get("Pass") +
               '| find "부트"')
    process = os.popen(command)
    preprocess = process.read()
    filtered = p.findall(preprocess)

    def lapsetime(filtered):
        format = '%Y-%m-%d, %p %H:%M:%S'

        now = datetime.datetime.now()
        string = " ".join(filtered)
        ancestero = string.replace(u'오전', 'AM')
        postero = ancestero.replace(u'오후', 'PM')

        time = datetime.datetime.strptime(postero, format)

        lapse = now - time

        return lapse

    sentence = ('Server Name is %s ' %serverdict["Server"][index].get("Name"), 'address is %s' %serverdict["Server"][index].get("IP"), 'and uptime is %s' %str(lapsetime(filtered)))
    return sentence




print('Processing....')
filename = 'uptime_'+ datetime.datetime.now().strftime('%Y-%m-%d %H%M')+'.txt'
f = open(filename, 'a')
f.write('Uptime Listup\n')
f.write('Recoreded at ' + str(datetime.datetime.today()))
f.write('\n')
f.write('\n')
for i in range(len(serverdict['Server'])):
    f.write(str(server(i)))
    print(str(server(i)))
    f.write('\n')
print('end of printing')
f.write('\n')
f.write('\n')
f.close()

spath = "/"
dpath = "//192.168.105.63/tech_share/Files/uptimechk/"
shutil.move(filename, dpath+filename)


