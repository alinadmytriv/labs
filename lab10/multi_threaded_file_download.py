import os
from urllib import request
from threading import Thread

class download_url_files(Thread):
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
    urls = ["http://www.mathros.net.ua/rozvjazuvannja-zvychajnyh-dyferencialnyh-rivnjan-metodom-adamsa.html",
            "http://thefuture.news/camera360",
            "http://thefuture.news/blog/futurio-app-ar-lesson"]
    for i, url in enumerate(urls):
        thread = download_url_files(url, i+1)
        thread.start()


if __name__ == "__main__":
    main()
