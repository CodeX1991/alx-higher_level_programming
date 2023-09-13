#!/usr/bin/python3

"""A JSON Module"""


from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    arg_count = len(argv)
    p_list = []

    if arg_count >= 2:
        for i in range(1, arg_count):
            p_list.append(argv[i])

    save_to_json_file(p_list, "add_item.json")
    load_from_json_file("add_item.json")


main()
