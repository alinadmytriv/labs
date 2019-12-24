import os, hashlib
from threading import Thread

class Duplicates:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.dict_of_dup = {}

    def hashfile(self, path, blocksize=4500):
        with open(path, 'rb') as f:
            hasher = hashlib.md5()
            file = f.read(blocksize)
            while len(file) > 0:
                hasher.update(file)
                file = f.read(blocksize)
        return hasher.hexdigest()

    def findDuplicates(self, dir_name, file_lst):
        for file_name in file_lst:
            path = os.path.join(dir_name, file_name)
            file_hash = self.hashfile(path)
            if file_hash in self.dict_of_dup:
                self.dict_of_dup[file_hash].append(path)
            else:
                self.dict_of_dup[file_hash] = [path]

    def findDuplicatesInFolder(self, folder_path):
        for folder in folder_path:
            for dir_name, root, file_lst in os.walk(folder):
                self.findDuplicates(dir_name, file_lst)


    def multi_find_duplicates(self):
        lst_of_folders = []
        lst_of_files = []
        for lst in os.listdir(self.folder_path):
            if os.path.isdir(str(self.folder_path) + "\\" + str(lst)):
                lst_of_folders.append(str(self.folder_path) + "\\" + str(lst))
            elif os.path.isfile(str(self.folder_path) + "\\" + str(lst)):
                lst_of_files.append(lst)

        N = 3
        subList = [lst_of_folders[n:n + N] for n in range(0, len(lst_of_folders), N)]

        threads = []

        for lst_of_path in subList:
            thread_for_folders = Thread(target=self.findDuplicatesInFolder, args=[lst_of_path])
            thread_for_folders.start()
            threads.append(thread_for_folders)

        thread_for_files = Thread(target=self.findDuplicates, args=[self.folder_path, lst_of_files])
        thread_for_files.start()
        threads.append(thread_for_files)

        for thread in threads:
            thread.join()

def main(folder0):
    duplicates = Duplicates(folder0)
    duplicates.multi_find_duplicates()
    output_duplicates(duplicates)


def output_duplicates(duplicates0):
    res = list(filter(lambda x: len(x) > 1, duplicates0.dict_of_dup.values()))
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
    else:
        main(folder)
