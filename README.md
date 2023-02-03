# blogreader
Python script to read blogs from a list of blog urls gained from using blurlscraper and stored the contents of the blog in a file.

# Requirements

Create a clients.txt file with names of clients/company names:

```
client1
client2
client3
client4
```
Create directories for each client including a list of blog urls and an element (such as "div", "article" etc) and class ("post", "post-body", "content" etc).

It should look something like this:

```
.
├── blogreader.py
├── clients.txt
├── client1
│   ├── blogurls.txt
├── client2
│   ├── blogurls.txt
├── client3
│   ├── blogurls.txt
└── client4
    └── blogurls.txt

```
When you run `./blogreader` it will create a new directory called `blogs` where it will stored the contents of each blog within their own file named after the blog url.
