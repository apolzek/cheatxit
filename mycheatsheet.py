#!/usr/bin/python3

import yaml
import json
import sys
import hashlib
import getopt


def help():
    print("MYCHEATSHEET\n")
    print("mycheatsheet.py --add <alias> <command> <description>")
    print("mycheatsheet.py --list")
    print("mycheatsheet.py --find <hash>\n")


def test_open_file():
    try:
        with open('data.yml') as f:
            return 0
    except IOError:
        return 1


def create_file():
    try:
        f = open("data.yml", "w+")
    except:
        return 1


def list_all_commands():
    with open(r'data.yml') as file:
        yml = yaml.load(file, Loader=yaml.FullLoader)
        try:
            for x in yml:
                print('')
                print(x)
                for y in yml[x]:
                    print(y, ':', yml[x][y])
        except:
            print("Empty")


def add_command(json_insertion):
    json_obj = json.dumps(json_insertion)
    ff = open("data.yml", "a")
    yaml.dump(json_insertion, ff, default_flow_style=False)


def rm_command(id_or_alias):
    with open(r'data.yml') as file:
        yml = yaml.load(file, Loader=yaml.FullLoader)
        print(id_or_alias)
        print(yml)

        try:
            yml.pop(id_or_alias)
        except:
            print("not found")

        json_obj = json.dumps(yml)
        ff = open("data.yml", "w")
        yaml.dump(yml, ff, default_flow_style=False)

        if(len(yml) == 0):
            file = open("data.yml", "r+")
            file.truncate(0)
            file.close()


def find_command(alias):
    with open(r'data.yml') as file:
        yml = yaml.load(file, Loader=yaml.FullLoader)

        try:
            if(yml.get(alias) is not None):
                print(yml.get(alias))
            else:
                print("not found")
        except:
            print("not found")


def call_manager():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hao:v", [
                                   "add=", "rm=", "list", "find="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-a", "--add"):
            print("add ON")
            if(len(sys.argv[2:]) == 2):
                alias_cmd = sys.argv[3]
                json_insertion = {
                    str(id(a)): {'alias': alias_cmd, 'command': a, 'description': ''}}
            elif(len(sys.argv[2:]) == 3):
                alias_cmd = sys.argv[3]
                description_cmd = sys.argv[4]
                json_insertion = {
                    str(id(a)): {'alias': alias_cmd, 'command': a, 'description': description_cmd}}
            else:
                json_insertion = {
                    str(id(a)): {'alias': '', 'command': a, 'description': ''}}

            print(json_insertion)
            add_command(json_insertion)
            sys.exit()
        elif o in ("-r", "--rm"):
            # print("rm ON")
            rm_command(a)
            sys.exit()
        elif o in ("-l", "--list"):
            # print("list ON")
            list_all_commands()
            # output = a
        elif o in ("-f", "--find"):
            # print("find ON")
            find_command(a)
            # output = a
        else:
            assert False, "unhandled option"
            help


if __name__ == "__main__":

    ready_file = True if test_open_file() == 0 else create_file()

    # help()
    # sys.exit(1)

    if(ready_file == True):
        pass
    else:
        sys.exit(2)

    if(len(sys.argv)) == 1:
        help()
        sys.exit(0)
    else:
        call_manager()
