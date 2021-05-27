#!/usr/bin/python3

import yaml
import json
import sys
import hashlib
import getopt


def help():
    print("                            MYCHEATSHEET                             ")
    print(" --------------------------------------------------------------------")
    print("| AADD     mycheatsheet.py -c <command> -a <alias> -d <description>  |")
    print("| REMOVE   mycheatsheet.py -r <id or alias>                          |")
    print("| LIST     mycheatsheet.py -l                                        |")
    print("| FIND     mycheatsheet.py -f <id or alias>                          |")
    print(" --------------------------------------------------------------------")

# def options(argv):
#     alias = ''
#     description = ''
#     command = ''

#     try:
#         opts, args = getopt.getopt(argv, "a:d:c:")
#     except getopt.GetoptError:
#         print('test.py -i <alias> -o <description>')
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print('test.py -a <alias> -d <description> -c <command>')
#             sys.exit()
#         elif opt in ("-a", "--alias"):
#             alias = arg
#         elif opt in ("-d", "--description"):
#             description = arg
#         elif opt in ("-c", "--command"):
#             command = arg
#     if(not alias or not description or not command):
#         help()
#     else:
#         validated = [alias, description, command]
#         return validated


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


def show_all_commands():
    with open(r'data.yml') as file:
        yml = yaml.load(file, Loader=yaml.FullLoader)
        try:
            for x in yml:
                print('')
                print(x)
                for y in yml[x]:
                    print(y, ':', yml[x][y])
        except:
            print("vazio")


def show_by_category(category):
    with open(r'.mycheatsheet.yml') as file:
        yml = yaml.load(file, Loader=yaml.FullLoader)
        try:
            for x in yml:
                if(yml.get(x).get("category") == "linux"):
                    print(x)
                    for y in yml[x]:
                        print(y, ':', yml[x][y])
        except:
            print("vazio")


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
            file = open("data.yml","r+")
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


def md5_create(alias):
    m = hashlib.md5()
    m.update(alias.encode())
    # print(m.hexdigest())
    return m.hexdigest()


def call_manager():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hao:v", ["add=", "rm=","list", "find="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
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
                json_insertion = {str(id(a)): {'alias': alias_cmd, 'command': a,'description': ''}}
            elif(len(sys.argv[2:]) == 3):
                alias_cmd = sys.argv[3]
                description_cmd = sys.argv[4]
                json_insertion = {str(id(a)): {'alias': alias_cmd, 'command': a,'description': description_cmd}}
            else:
                json_insertion = {str(id(a)): {'alias': '', 'command': a,'description': ''}}
            
            print(json_insertion)
            add_command(json_insertion)
            sys.exit()
        elif o in ("-r", "--rm"):
            print("rm ON")
            rm_command(a)
            sys.exit()
        elif o in ("-l", "--list"):
            print("list ON")
            show_all_commands()
            # output = a
        elif o in ("-f", "--find"):
            print("find ON")
            find_command(a)
            # output = a
        else:
            assert False, "unhandled option"


if __name__ == "__main__":

    ready_file = True if test_open_file() == 0 else create_file()
    
    # sys.exit(22)
    if(ready_file == True):
        pass
    else:
        sys.exit(2)

    # sys.exit(22)
    # call_manager(sys.argv)
    # print(" ".join(sys.argv))

    # sys.exit(22)
    if(len(sys.argv)) == 1:
        help()
        sys.exit(0)
    else:
        # list_elements = sys.argv[1:]
        # print(list_elements)
        # call_manager(" ".join(sys.argv[1:]))
        call_manager()
        


