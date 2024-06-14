# CDA_download

![PyPI - Downloads](https://img.shields.io/pypi/dm/cda_download)


### A library that helps download videos from CDA website



### Installation:
`pip install cda_download`

### How to use:
```python
from cda_download import CdaDownload

url = "CDA url"

cda = CdaDownload(url=url)
cda.download()
```


### Additional features:


#### Progress callback
If you need to get progress like percentage or download speed, you can create a function 
and pass as a parameter in the download method.

```python
from datetime import datetime, timedelta
from cda_download import CdaDownload

download_start_time = datetime.now()
last_update_time = datetime.now()

def show_progress(count, block_size, total_size):
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


url = "CDA url"

cda = CdaDownload(url=url)
cda.download(on_progress_callback=show_progress)
```


#### Filename
You can pass filename as a parameter in the form of a string to specify download location.
Using download method without the `filename` parameter will save the file to where your script is located.

```python
from cda_download import CdaDownload

url = "cda url"

cda = CdaDownload(url=url)
output_path = "D:/Downloads/title.mp4"

cda.download(filename=output_path)
```


#### Other data
Apart from downloading, you can access other data about CDA video:

```python
from cda_download import CdaDownload

url = "CDA url"
cda = CdaDownload(url=url)

# video title
print(cda.title())

# channel name
print(cda.channel())

# video description
print(cda.description())

# video publish date
print(cda.publish_date())

# video duration
print(cda.duration())

# file size in bytes
print(cda.filesize())

# thumbnail image
print(cda.thumbnail())
```
