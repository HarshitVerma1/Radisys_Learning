from ast import parse
import configparser
parser = configparser.ConfigParser()
parser.read("config.ini")
print(parser.sections())  # ['SERVER1', 'SERVER2', 'SERVER3']
print(parser.items("SERVER2"))
# [('ip', '2.2.2.2'), ('user', 'Mohit'), ('password', 'Mohi@123')]
print(parser["SERVER3"]["ip"])  # 3.3.3.3
for section in parser.sections():
    for item in parser[section]:
        print("Section = {}   Item = {}   value = {}".format(
            section, item, parser[section][item]))
