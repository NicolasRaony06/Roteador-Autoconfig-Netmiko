from netmiko import ConnectHandler
from os import getenv
from dotenv import load_dotenv

load_dotenv()

cisco_r1 = {
    'device_type': 'cisco_ios',
    'host': getenv('HOST'),
    'username': getenv('USER_ROUTER'),
    'password': getenv('PASSWORD'),
    'secret': getenv('SECRET')
}

net_connect = ConnectHandler(**cisco_r1)

output = net_connect.send_command('show ip int brief')

print(output)