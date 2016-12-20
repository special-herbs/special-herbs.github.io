#!/usr/bin/env python
from jinja2 import Template
from collections import OrderedDict
from bs4 import BeautifulSoup
from PIL import Image
from StringIO import StringIO
import json
import datetime
import requests
import sys

# load the JSON data
data = json.loads(open('herbs.json').read(), object_pairs_hook=OrderedDict)

# fetch image URLs from discogs
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
images = {}
for albumName, album in data.iteritems():
    if 'releases' in album:
        for release in album['releases']:
            releaseFile = 'img' + release[release.rfind('/'):] + '.jpg'
            images[release] = releaseFile
            #request = requests.get(release, headers=headers)
            #soup = BeautifulSoup(request.content, 'lxml')
            #coverImg = soup.find(property='og:image')['content']
            #request = requests.get(coverImg)
            #image = Image.open(StringIO(request.content))
            #image.save(releaseFile)

# generate the HTML from template
template = Template(open('index.template.html').read())
print template.render(data=data,
        images=images,
        generationDate=datetime.datetime.now().strftime("%Y-%m-%d")).encode('utf-8')
