from urllib import request

def download_url_file(url0):
    file_open = request.urlopen(url0)
    chunk_size = 1024 * 10
    while 1:
        file_info = str(file_open.read(chunk_size).decode('utf-8')).split("\n")
        if not file_info:
            break
        return file_info

def words_stats(file):
    dict = {}
    for line in file:
        # remove the leading spaces and newlines characters
        # convert the characters in line to lowercase to avoid case mismatch
        # split the line into words
        line = line.strip().lower().split(" ")
        for word in line:
            if word in dict:
                # increment count of word by 1
                dict[word] += 1
            else:
                # add the word to dictionary with count 1
                dict[word] = 1
    return dict

def words_count(dict):
    count = 0
    for y in dict.keys():
        count += dict[y]
    return count

def main():
    url = input("Enter the url file: ")
    print("Статистика слів:")
    dict = words_stats(download_url_file(url))
    for y in dict.keys():
        print(f"{y} : {dict[y]}")
    count = words_count(dict)
    print(f"Кількість слів - {count}")

if __name__ == '__main__':
    main()
