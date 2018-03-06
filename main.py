import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

HOMEPAGE= 'https://www.youtube.com/'
# 'http://www.netscrap.com/netscrap.cfm' #input("Enter the base URL > ")
PROJECT = getProjectFolderName(HOMEPAGE)
# print(PROJECT)
DOMAIN_NAME =getDomainName(HOMEPAGE)
# print(DOMAIN_NAME)
QUEUE_FILE=PROJECT+'/queue.txt'
CRAWLED_FILE=PROJECT+'/crawled.txt'
NUMBER_OF_THREADS=8
queue = Queue()
Spider(PROJECT,HOMEPAGE,DOMAIN_NAME)

# creating worker threads
def createWorkers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# execute the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawlPage(threading.current_thread().name, url)
        queue.task_done()

# Each url in the queue is a job
def createJobs():
    for url in fileToSet(QUEUE_FILE):
        queue.put(url)
    queue.join()
    crawl()

# Crawl if there are pending items left in the queue
def crawl():
    waitingURLs = fileToSet(QUEUE_FILE)
    if len(waitingURLs) > 0:
        print(str(len(waitingURLs)), 'urls left in the queue')
        createJobs()

createWorkers()
crawl()