import time 
from datetime import datetime as dt 

# Host files
# etc/hosts
host_linux= '/etc/hosts'
host_temp= 'hosts'
redirect= '127.0.0.1'

website_list = [
    'www.facebook.com',
    'facebook.com',
    'www.tn.com.ar',
    'tn.com.ar',
    'www.lanacion.com.ar',
    'lanacion.com.ar',
    'www.clarin.com.ar',
    'clarin.com.ar'
]

hora_inicio= 9
hora_fin = 0

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, hora_inicio) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, hora_fin):
        print('trabajando')
        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        print('descansando')
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(1)