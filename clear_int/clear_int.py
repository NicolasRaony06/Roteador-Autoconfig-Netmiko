from netmiko import ConnectHandler
from os import getenv
from dotenv import load_dotenv

load_dotenv()

cisco_r1 = {
    'device_type': 'cisco_ios',
    'host': getenv('HOST'),
    'username': getenv('USER_ROUTER2'),
    'password': getenv('PASSWORD2'),
    'secret': getenv('SECRET')
}

net_connect = ConnectHandler(**cisco_r1)

# net_connect.enable()

interfaces = ['e0/1', 'e0/2']
for interface in interfaces:
    config_commands = [f'int {interface}', 'no ip add', 'shutdown']
    output = net_connect.send_config_set(config_commands)
