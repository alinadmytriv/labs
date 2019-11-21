from urllib import request

def download_url_file(url0):
    file_open = request.urlopen(url0)
    chunk_size = 1024 * 10
    while True:
        file_info = str(file_open.read(chunk_size).decode('utf-8')).split("\n")
        if not file_info:
            break
        return file_info

def words_stats(file):
    dictionary = {}
    count = 0
    for line in file:
        # line = line.strip().lower().split(" ")
        for word in line.strip().lower().split(" "):
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1
            count += 1
    return dictionary, count

def main():
    url = input("Enter the url file: ")
    print("Word statistics:")
    dictionary = words_stats(download_url_file(url))[0]
    for y in dictionary.keys():
        print(f"{y} : {dictionary[y]}")
    count = words_stats(download_url_file(url))[1]
    print(f"The number of words - {count}")

if __name__ == '__main__':
    main()
