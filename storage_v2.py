import os
import tempfile
import argparse
import json

# path to temp file
storage_path = os.path.join(tempfile.gettempdir(), 'storage2.data')


def clear():
    os.remove(storage_path)
    print("file has been deleted")


def get_data():
    # obtain data from storage
    try:
        file_storage = open(storage_path, 'r')
    except IOError:
        return {}
    else:
        with file_storage:
            return json.load(file_storage)


def put(key, value):
    # write to storage
    storage_data = get_data()
    if key == "all":
        raise ValueError("incorrect key")
    if key in storage_data:
        storage_data[key].append(value)
        print("value has been updated")
    else:
        storage_data[key] = [value]
        print("key-value pair has been added")

    with open(storage_path, 'w') as file_storage:
        json.dump(storage_data, file_storage)


def get(key):
    storage_data = get_data()
    if key == "all":
        return storage_data
    if key in storage_data:
        return storage_data.get(key)
    else:
        return "no such key found"


if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(description="this program read/write from/to file-storage")
    parser.add_argument("-k", "--key", help="specify the key")
    parser.add_argument("-v", "--value", help="specify the value")
    parser.add_argument("-c", "--clear", action="store_true", help="Clear")

    args = parser.parse_args()

    if args.clear:
        clear()
    elif args.key and args.value:
        put(args.key, args.value)
    elif args.key:
        printout = get(args.key)
        if type(printout) == list:
            print(*printout, sep=', ')
        else:
            print(printout)
    else:
        print('Wrong command')
