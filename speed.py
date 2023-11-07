import speedtest as st 
from termcolor import colored
import colors


choices = [
    'UP',
    'DOWN',
    'PING',
    'ALL'
]


userinput = str(input('>>> ')).upper()
speed = st.Speedtest()


def check_download_speed():
    msg = f'Checking download speed...'
    print(colored(msg))
    down = speed.download()
    print(f'Your current {colors.GREEN}download{colors.RESET} speed: {colors.RED}{round(down / 1000 / 1000, 1)} Mbit/s\n{colors.RESET}')
    
    
    
def check_upload_speed():
    msg = f'Checking upload speed...'
    print(colored(msg))
    up = speed.upload()
    print(f'Your current {colors.GREEN}upload {colors.RESET}speed: {colors.RED}{round(up / 1000 / 1000, 1)} Mbit/s\n{colors.RESET}')
    
    
def check_ping():
    msg = f'Checking ping...'
    print(colored(msg))
    servers = []
    speed.get_servers(servers)
    server = speed.get_best_server()
    print(f'Your current {colors.YELLOW}ping: {colors.BLUE}{server["latency"]} ms\n')


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
    