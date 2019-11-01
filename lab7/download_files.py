from urllib import request

def download_url_file(url0):
    file_open = request.urlopen(url0)
    file_info = file_open.read().decode('utf-8')
    file_info_str = str(file_info)
    file_lines = file_info_str.split("\\n")

    new_file = open("file.txt", "w")
    for info in file_lines:
        new_file.write(info + "\n")
    new_file.close()
    return new_file.name

def words_count(file):
    dict = {}
    count = 0
    with open(file) as f:
        for line in f:
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
    for y in dict.keys():
        print(f"{y} : {dict[y]}")
        count += dict[y]
    return count


def main():
    url = input("Enter the url file: ")
    download_url_file(url)
    print(words_count(download_url_file(url)))

if __name__ == '__main__':
    main()