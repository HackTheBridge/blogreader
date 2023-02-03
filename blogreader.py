#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import os
import re

def print_progress(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        bar_length  - Optional  : character length of bar (Int)
    """
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    print('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix), end = '\r')

    if iteration == total:
        print()

with open("clients.txt") as f:
    clients = f.read().splitlines()

for client in clients:
    client_dir = f"./{client}"

    if not os.path.exists(client_dir):
        os.makedirs(client_dir)

    with open(f"{client_dir}/element.txt") as f:
        element = f.read().strip()

    with open(f"{client_dir}/class.txt") as f:
        class_name = f.read().strip()

    with open(f"{client_dir}/blogurls.txt") as f:
        blog_urls = f.read().splitlines()

    num_blogs = len(blog_urls)

    print(f"Reading {client.title()}'s blogs.")

    if not os.path.exists(f"{client_dir}/blogs"):
        os.makedirs(f"{client_dir}/blogs")

    for i, url in enumerate(blog_urls):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        content = soup.find(element, class_=class_name)
        if content:
            file_name = re.sub(r"[^a-zA-Z0-9]+", "_", url)
            with open(f"{client_dir}/blogs/{file_name}", "w") as f:
                f.write(content.text)
        else:
            print(f"No element found with element '{element}' and class '{class_name}' in {url}")

        print_progress(i+1, num_blogs, prefix='Progress:', suffix='Complete', bar_length=50)
