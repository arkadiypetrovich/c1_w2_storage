import os
import tempfile
import argparse
import json

# path to temp file
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

# parse arguments
parser = argparse.ArgumentParser(description="this program read/write from/to file-storage")
parser.add_argument("-k", "--key", help="specify the key")
parser.add_argument("-v", "--value", help="specify the value")
args = parser.parse_args()

# analyze enter and do actions
if args.key is None:
    print("please enter key or key-value pair")

elif args.value is None:
    # obtain data from storage
    try:
        file_storage = open(storage_path, 'r')
    except IOError:
        print("")
        # print("storage is empty")
    else:
        with file_storage:
            storage_data = json.load(file_storage)
            if args.key in storage_data:
                print(*storage_data[args.key], sep=', ')
            else:
                print("no such key found")

else:
    # obtain data from storage
    try:
        file_storage = open(storage_path, 'r')
    except IOError:
        storage_data = {}
    else:
        with file_storage:
            storage_data = json.load(file_storage)

    # write to storage
    with open(storage_path, 'w') as file_storage:
        if args.key in storage_data:
            storage_data[args.key].append(args.value)
            print("value has been updated")
        else:
            storage_data.update({args.key: [args.value]})
            print("key-value pair has been added")
        json.dump(storage_data, file_storage)
