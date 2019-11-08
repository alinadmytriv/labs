import os, hashlib

# function which change file values into 128 bit hash value
# then for checking the duplicates
def hashfile(path):
    with open(path, 'rb') as f:
        hasher = hashlib.md5()
        file = f.read()
        while len(file) > 0:
            # changing into 128 bit hash value
            hasher.update(file)
            file = f.read()
    return hasher.hexdigest()

# function which create a dictionary with file path and the file entity of hash value
def findDuplicates(folder_path):
    dict_of_dup = {}
    for dir_name, root, file_lst in os.walk(folder_path):
        for file_name in file_lst:
            path = os.path.join(dir_name, file_name)
            file_hash = hashfile(path)
            if file_hash in dict_of_dup:
                dict_of_dup[file_hash].append(path)
            else:
                dict_of_dup[file_hash] = [path]
    return dict_of_dup


def main(dict1):
    # list which has lists of duplicates' paths
    res = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(res) > 0:
        print("Find duplicates: ")
        print("-----------------")
        for r in res:
            for subres in r:
                print(f"{subres}")
            print("-----------------")
    else:
        print("There are no duplicates")

if __name__ == '__main__':
    folder = input("Enter the folder where you want to find duplicates: ")
    if not os.path.exists(folder):
        print(f"{folder} is not a valid path")
    main(findDuplicates(folder))
