from urllib.request import  urlopen
from urlFinder import URLFinder
from general import *
from domain import *

class Spider:

    #Class variables. These variables will be shared among all the instances of this class.
    projectName = ''
    baseURL = ''
    domainName = ''
    queueFile = ''
    crawledFile = ''
    queue = set()
    crawled = set()

    def __init__(self, projectName, baseUrl, domainName):
        Spider.projectName = projectName
        Spider.baseURL = baseUrl
        Spider.domainName = domainName
        Spider.queueFile = Spider.projectName + '/queue.txt'
        Spider.crawledFile = Spider.projectName + '/crawled.txt'
        self.boot()
        self.crawlPage('Crawling Initiated', Spider.baseURL)

    #The first crawler will create the project folder and the queue and crawled text files.
    @staticmethod
    def boot():
        createDir(Spider.projectName)
        createFiles(Spider.projectName, Spider.baseURL)
        Spider.queue = fileToSet(Spider.queueFile)
        Spider.crawled = fileToSet(Spider.crawledFile)

    @staticmethod
    def crawlPage(threadName, URL):
        if URL not in Spider.crawled:
            print(threadName+' >> crawling >> '+URL)
            print('Waiting -> '+ str(len(Spider.queue)))
            print('Done -> ' + str(len(Spider.crawled)))
            Spider.addURLsToQueue(Spider.collectURLs(URL))
            Spider.queue.remove(URL)
            Spider.crawled.add(URL)
            Spider.updateFiles()

    # This method connects to the site. It takes the html. Converts it to a proper HTML format string.
    # Passes it to URLFinder. URLFinder parses through it. Gets a set of all the hyperlinks(urls).
    # Then returns that set of urls.
    @staticmethod
    def collectURLs(url):
        htmlString = ''
        try:
            response = urlopen(url)
            if 'text/html' in response.getheader('Content-Type'): # To make sure it's a HTML file and not some online pdf
                htmlBytes = response.read()
                htmlString = htmlBytes.decode('utf-8')
            urlFinder = URLFinder(Spider.baseURL, url)
            urlFinder.feed(htmlString) # feed() will call handle_starttag()
        except Exception as e:
            print('Exception encountered. Crawling Stopped!!')
            print(str(e))
            return set()
        return urlFinder.pageLinks()

    # This method takes a set of urls and add it to already existing waiting list.
    @staticmethod
    def addURLsToQueue(urls):
        for url in urls:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domainName != getDomainName(url):
                continue
            # if 'prices' not in url:
            #     continue
            Spider.queue.add(url)


    @staticmethod
    def updateFiles():
        setToFile(Spider.queue,Spider.queueFile)
        setToFile(Spider.crawled,Spider.crawledFile)