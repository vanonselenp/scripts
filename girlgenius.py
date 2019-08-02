import BeautifulSoup
import requests
import urllib2

# start_url = 'http://www.girlgeniusonline.com/comic.php?date=20021104'
start_url = 'http://www.girlgeniusonline.com/comic.php?date=20180108'
start_counter = 2395


def download_webpage(url):
    response = urllib2.urlopen(url)
    content = response.read()
    soup = BeautifulSoup.BeautifulSoup(content)
    return soup


def get_next_page(page):
    return page.find(id='bottomnext').get('href')


def get_image_url(page):
    return page.find(alt='Comic').get('src')


def download_image(url, counter):
    content = requests.get(url).content
    with open('images/gg-%s.jpg' % counter, 'w') as f:
        f.write(content)
    

if __name__ == '__main__':
    counter = start_counter
    url = start_url
    previous = start_url
    while True:
        page = download_webpage(url)
        print("%s %s" % (url, counter))
        download_image(get_image_url(page), counter)
        url = get_next_page(page)
        if previous == url:
            break
        previous = url
        counter += 1
