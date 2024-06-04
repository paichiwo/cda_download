import time
from pycda.main import PyCDA

if __name__ == '__main__':

    start_time = time.time()

    def report_hook(count, block_size, total_size):
        pass
        # # progress percentage
        # progress = min(1.0, float(count * block_size) / total_size)
        # print(f'progress: {progress:.2f}')
        #
        # # download speed
        # elapsed_time = time.time() - start_time
        # if elapsed_time > 0:
        #     speed = (count * block_size) / (1024 * elapsed_time)  # speed in KB/s
        #     print(f'Download speed: {speed:.2f} KB/s')

        # new
        # downloaded = count * block_size
        # percent = min(100, downloaded * 100 / total_size)
        # print(f"\rDownloading: {percent:.2f}% complete", end='')

    url1 = 'https://www.cda.pl/video/14967539bc'
    url2 = 'https://www.cda.pl/video/192935076e'
    url3 = 'https://www.cda.pl/video/295066274/'

    cda = PyCDA(url1)
    cda.download(on_progress_callback=report_hook)
