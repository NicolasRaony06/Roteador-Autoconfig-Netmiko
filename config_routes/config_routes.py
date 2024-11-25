from netmiko import ConnectHandler
from dotenv import load_dotenv
from os import getenv

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

routes = {
    'route_1': ['10.0.0.8', '255.255.255.252', '10.0.0.2', '1'],
    'route_2': ['10.0.0.8', '255.255.255.252', '10.0.0.6', '2'] 
}

net_connect.config_mode()

for route in routes.values():
    route_config = f'ip route {route[0]} {route[1]} {route[2]} {route[3]}'
    net_connect.send_command(route_config)
