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

# net_connect.enable() 

for i in range(1,3):
    config_commands = [f'interface ethernet 0/{i}', 'ip add 10.0.0.1 255.255.255.252' if i==1 else 'ip add 10.0.0.5 255.255.255.252', 'no shutdown']
    output = net_connect.send_config_set(config_commands)
    

