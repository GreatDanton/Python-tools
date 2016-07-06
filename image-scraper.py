import urllib.request

# scrap images from links:

links = ['https://scrot.moe/image/OE4y',
'https://scrot.moe/image/OtxU',
'https://scrot.moe/image/Ovmm',
'https://scrot.moe/image/OOk6',
'https://scrot.moe/image/OZrC',
'https://scrot.moe/image/OnLj',
'https://scrot.moe/image/Ooph',
'https://scrot.moe/image/OpFl',
'https://scrot.moe/image/Olez',
'https://scrot.moe/image/O7vQ',
'https://scrot.moe/image/OA4n',
'https://scrot.moe/image/OCye',
'https://scrot.moe/image/Okmu',
'https://scrot.moe/image/ONkv',
'https://scrot.moe/image/OU0Y',
'https://scrot.moe/image/ORLd',
'https://scrot.moe/image/OdHD',
'https://scrot.moe/image/O4Qa',
'https://scrot.moe/image/O5eN',
'https://scrot.moe/image/OuOX'
]

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

headers = {'User-Agent':user_agent,}

def parse_html(url):
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    data = str(response.read())
    response.close()
    return(data)


def parse_image_url(html_string):
    container = html_string.find('rel="image_src"')
    start = html_string.find('href="', container + 1)
    end = html_string.find('"', start + 6)
    link = html_string[start+6:end]
    return(link)

# save images in the same folder as this script
for link in links:
    html_string = parse_html(link)
    image_url = parse_image_url(html_string)
    image_path = image_url.split('/')
    name_of_image = image_path[-1]
    print(name_of_image)

    urllib.request.urlretrieve(image_url, name_of_image) 
