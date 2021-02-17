#! python3
# scheduledWebComicDownloader.py - Once every 24 hours, program checks for new LFG and XKCD comics 
# and downloads them if there are any new ones.
#
# NOTES: Edit the following variables before running the program:
#        1. lfg_comic_num = The latest LFG comic number.  
#        2. xkcd_comic_num = The latest XKCD comic number.
#        The program will check if there are any comics with a number higher than the ones in those two variables.

import requests, os, bs4, time

# Latest comic numbers, to be modififed before the program runs.
lfg_comic_num = 1468
xkcd_comic_num = 2411

abspath = os.path.abspath(os.getcwd())

def download_lfg():
    global lfg_comic_num

    # Create/change appropriate comic folder.
    if os.path.exists(abspath + '/lfg'):
        os.chdir(abspath + '/lfg')
    else:
        os.mkdir(abspath + '/lfg')
        os.chdir(abspath + '/lfg')
    
    # Create the comic URL.
    url = 'https://www.lfg.co/page/' + str(lfg_comic_num) + '/' 

    try:
        # Get the comic page.
        res = requests.get(url)
        res.raise_for_status()

        # Extract the image src.
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        match1 = soup.find('div', id='comic-img')
        match2 = match1.find('img')
        comic_url = match2.get('src')

        # Get the comic image.
        res = requests.get(comic_url)
        res.raise_for_status()

        # Download the comic image.
        print('Downloading LFG comic ' + str(lfg_comic_num) + '...')
        image_file = open('lfg' + str(lfg_comic_num) + '.jpg', 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

        # Increment the latest comic num.
        lfg_comic_num += 1

    except requests.exceptions.HTTPError:
        print('No new LFG comic was found.')

def download_xkcd():
    global xkcd_comic_num

    # Create/change appropriate comic folder.
    if os.path.exists(abspath + '/xkcd'):
        os.chdir(abspath + '/xkcd')
    else:
        os.mkdir(abspath + '/xkcd')
        os.chdir(abspath + '/xkcd')

    # Create the comic URL.
    url = 'https://xkcd.com/' + str(xkcd_comic_num) +'/'

    try:
        # Get the comic page.
        res = requests.get(url)
        res.raise_for_status()
        
        # Extract the image src.
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        match1 = soup.find('div', id='comic')
        match2 = match1.find('img')
        comic_url = 'https:' + match2.get('src')

        # Get the comic image.
        res = requests.get(comic_url)
        res.raise_for_status()

        # Download the comic image.
        print('Downloading XKCD comic ' + str(xkcd_comic_num) + '...')
        image_file = open('xkcd' + str(xkcd_comic_num) + '.jpg', 'wb')
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

        # Increment the latest comic num.
        xkcd_comic_num += 1

    except requests.exceptions.HTTPError:
        print('No new XKCD comic was found.')

# Run this program once a day for 100 days.
for day in range(100):
    print('Checking for new comics...')
    download_xkcd()
    download_lfg()
    print('Check complete. Will check again in 24 hours.')
    for seconds in range(86400): # 86400 seconds = 1 day
        time.sleep(1)
