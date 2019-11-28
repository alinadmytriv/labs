import os
from urllib import request
from threading import Thread

class download_url_files1(Thread):
    def __init__(self, url, number):
        """ the thread's initialization """
        Thread.__init__(self)
        self.number = number
        self.url = url

    def run(self):
        """ start the thread """
        file_open = request.urlopen(self.url)
        file_name = os.path.basename(self.url)
        chunk_size = 1024 * 2
        with open(file_name, "wb") as handler:
            while True:
                file_info = file_open.read(chunk_size)
                if not file_info:
                    break
                handler.write(file_info)
        print(f"Thread {self.number} finished to download {self.url}")

class download_url_files2(Thread):
    def __init__(self, url, number):
        """ the thread's initialization """
        Thread.__init__(self)
        self.number = number
        self.url = url

    def run(self):
        """ start the thread """
        file_open = request.urlopen(self.url)
        file_name = os.path.basename(self.url)
        chunk_size = 1024 * 2
        with open(file_name, "wb") as handler:
            while True:
                file_info = file_open.read(chunk_size)
                if not file_info:
                    break
                handler.write(file_info)
        print(f"Thread {self.number} finished to download {self.url}")

class download_url_files3(Thread):
    def __init__(self, url, number):
        """ the thread's initialization """
        Thread.__init__(self)
        self.number = number
        self.url = url

    def run(self):
        """ start the thread """
        file_open = request.urlopen(self.url)
        file_name = os.path.basename(self.url)
        chunk_size = 1024 * 2
        with open(file_name, "wb") as handler:
            while True:
                file_info = file_open.read(chunk_size)
                if not file_info:
                    break
                handler.write(file_info)
        print(f"Thread {self.number} finished to download {self.url}")

def main():
    """ run the program """
    urls = "http://www.mathros.net.ua/rozvjazuvannja-zvychajnyh-dyferencialnyh-rivnjan-metodom-adamsa.html"
    thread1 = download_url_files1(urls, 1)
    thread1.start()
    thread2 = download_url_files2(urls, 2)
    thread2.start()
    thread3 = download_url_files3(urls, 3)
    thread3.start()

if __name__ == "__main__":
    main()
