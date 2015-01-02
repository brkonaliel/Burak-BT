__author__ = 'burakonal'
import re
import sys
import time


def read_file(file):
    f = open(file, 'r')
    tuples = re.findall(r'\|\s*(\d+)\s*\|([\w\s]+)+\|\s*(\d*)\s*\|', f.read())
    f.close()
    return tuples

def create_traversal(employees):
    traversal = {}
    for key in employees:
        managerID = employees[key][0]
        managerPath = []
        while managerID != '':
            managerPath.append(managerID)
            managerID = employees[managerID][0]
        traversal[key] = managerPath
    return traversal

def find_keys(name, employees):
    keys = []
    for key in employees:
        name = name.lower().strip()
        name = re.sub(r'\s\s+', ' ', name)
        chart_name = employees[key][1].lower()
        chart_name = re.sub(r'\s\s+', ' ', chart_name)
        if name == chart_name:
            keys.append(key)
    return keys

def find_mutual_manager(paths, employees):
    for key in 


def main():


    # employee dictionary: keys are employeeIDs, values are managerIDs and names in this given order. Names are stripped.
    # names are taken from user. They are stripped and
    employees = {}
    paths = {}

    name1 = sys.argv[2]
    name2 = sys.argv[3]
    for a in read_file(sys.argv[1]):
        employees[a[0].strip()] = [a[2].strip(), a[1].strip()]

    traversal = create_traversal(employees)

    key1 = find_keys(name1, employees)
    key2 = find_keys(name2, employees)

    if len(key1) is 0:
        raise RuntimeError('No name as %s is found in input file!' % name1)
    elif len(key2) is 0:
        raise RuntimeError('No name as %s is found in input file!' % name2)

    for key in key1:
        paths[key] = traversal[key]
    for key in key2:
        paths[key] = traversal[key]

    find_mutual_manager(paths, employees)

if __name__ == "__main__":
    main()




# class Node(object):
#     def __init__(self, employeeID, name, managerID):
#         self.name = name
#         self.emloyeeID = employeeID
#         self.managerID = managerID
#         self.children = []
#
#     def add_children(self, obj):
#         self.children.append(obj)