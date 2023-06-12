import speedtest as st 
from termcolor import colored
choices = [
    'UP',
    'DOWN',
    'PING',
    'ALL'
]

color = 'yellow'
userinput = str(input('>>> ')).upper()
speed = st.Speedtest()


def check_download_speed():
    msg = f'Checking download speed...'
    print(colored(msg,color))
    down = speed.download()
    print(f'Your current download speed: {round(down / 1000 / 1000, 1)} Mbit/s\n')
    
    
    
def check_upload_speed():
    msg = f'Checking upload speed...'
    print(colored(msg,color))
    up = speed.upload()
    print(f'Your current upload speed: {round(up / 1000 / 1000, 1)} Mbit/s\n')
    
    
def check_ping():
    msg = f'Checking ping...'
    print(colored(msg,color))
    servers = []
    speed.get_servers(servers)
    server = speed.get_best_server()
    print(f'Your current ping: {server["latency"]} ms\n')


if userinput in choices:
    if userinput == 'UP':
        check_upload_speed()
    elif userinput == 'DOWN':
        check_download_speed()
    elif userinput == 'PING':
        check_ping()
    elif userinput == 'ALL':
        check_download_speed()
        check_upload_speed()
        check_ping()
else:
    print('Invalid choice')
    
