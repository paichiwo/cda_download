from datetime import datetime, timedelta
from pycda.main import PyCDA

if __name__ == '__main__':

    download_start_time = datetime.now()
    last_update_time = datetime.now()

    def report_hook(count, block_size, total_size):
        global last_update_time

        # download speed
        elapsed_time = (datetime.now() - download_start_time).total_seconds()
        download_speed = (count * block_size) / (1024 * elapsed_time)

        # progress
        progress = min(1.0, count * block_size / total_size)

        current_time = datetime.now()
        if (current_time - last_update_time) >= timedelta(seconds=1):
            print(f'\rDownloading: {progress:.2f} complete', end='')
            print(f' | Speed: {download_speed:.2f} KB/s', end='')
            last_update_time = current_time

    url1 = 'https://www.cda.pl/video/14967539bc'
    url2 = 'https://www.cda.pl/video/192935076e'
    url3 = 'https://www.cda.pl/video/295066274'
    url4 = 'https://www.cda.pl/video/210880265'
    url5 = 'https://www.cda.pl/video/1252604482'

    cda = PyCDA(url5)
    # cda.download(on_progress_callback=report_hook)
    # cda.title()
    print(cda.thumbnail())
