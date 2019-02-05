import numpy as np
from pathlib import Path
import random, yaml, os
import SelfMethods

shoplist = []

class shop:

    def __init__(self, name, typeArg, location, services, timetable):
        self.name = name
        self.typeArg = typeArg
        self.location = location
        self.services = services
        self.timetable = timetable
        shoplist.append(self)
        filedata = {self.typeArg: [self.name, self.location, self.services, self.timetable]}
        yaml_config.yaml_dump_check('shopref.yml', self.typeArg, filedata)

class yaml_config:

    #Check if file exists
    def check_file_inst(filepath):
        if not os.path.exists(filepath):
            with open(filepath, 'w'):
                print("File does not exist -- Generating " + filepath)
        else:
            print("File exists -- Skipping generation")

    #Loading from file
    def yaml_loader(filepath):
        with open(filepath, "r") as file_descriptor:
            data = yaml.safe_load(file_descriptor)
        return data

    #Writing to file
    def yaml_dump(filepath, data):
        with open(filepath, 'a') as file_descriptor:
            yaml.safe_dump(data, stream=file_descriptor, default_flow_style=False)

    #Check for instance before write
    def yaml_dump_check(filepath, key, data):
        with open(filepath, 'a') as file_descriptor:
            store_data = yaml_config.yaml_loader(filepath)
            if os.stat(filepath).st_size == 0 or key not in store_data:
                yaml.safe_dump(data, stream=file_descriptor, default_flow_style=False)

    #Search for an item within a file
    def search_key_replace(filepath, key, criteria):
        foundflag = False
        with open(filepath, 'r') as file_descriptor:
            store_data = yaml_config.yaml_loader(filepath)
            for inst, v in store_data.items():
                if inst == key and criteria[0] in v[2] and criteria[1] in v[3]:
                    print("Found a shop that matches your criteria")
                    foundflag = True
                    shopitem = [currentuser.id, criteria[0], criteria[1]]
                    replace = str(input("Would you like to book your selection? (y/n): "))
                    if replace == 'y':
                        v[3][v[3].index(shopitem[2])] = shopitem
                        with open(filepath, 'w') as f:
                            yaml.dump(store_data, f)
        if foundflag == False:
            print("No availble shops match your criteria")

    #Remove item from a file
    def remove_booking(filepath, key, criteria):
        criteria.insert(0, currentuser.id)
        with open(filepath, 'r') as file_descriptor:
            store_data = yaml_config.yaml_loader(filepath)
            for inst, v in store_data.items():
                if inst == key and criteria in v[3]:
                    print("Removing booking")
                    v[3][v[3].index(criteria)] = criteria[2]
                    with open(filepath, 'w') as f:
                        yaml.dump(store_data, f)
                        break

if __name__ == "__main__":
    currentuser = SelfMethods.user()
    yaml_config.check_file_inst('shopref.yml')

coffeeshop = shop('Coffee Co', 'coffee', 'pymble', ['latte', 'mocha', 'espresso'], [7,9,11,13,15,17])
hairdresser = shop('Hair Co','hairdresser', 'kincumber', ['cuts', 'colours'], [9,11,13,15,17])
#selfmethods.methods.search('hairdresser', 'kincumber', 50, 'colours', 15)
#selfmethods.methods.search('coffee', 'pymble', 50, 'latte', 9)
yaml_config.search_key_replace('shopref.yml', 'coffee', ['latte', 9])
#print(coffeeshop.timetable)
#selfmethods.methods.rembooking(currentuser, coffeeshop, 9)
yaml_config.remove_booking('shopref.yml', 'coffee', ['latte', 9])
#print(coffeeshop.timetable)

#print(shoplist)
#selfmethods.methods.search('coffee', 'pymble', 50, 'latte', 9)
