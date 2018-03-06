import os

# each crawled website gets a different folder
def createDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Created folder: ",directory)

# creating queue and crawled files (if they don't exist)
def createFiles(projectName, baseURL):
    queue = os.path.join(projectName,'queue.txt') #waiting list
    crawled = os.path.join(projectName,'crawled.txt')
    if not os.path.isfile(queue):
        writeToFile(queue, baseURL)
    if not os.path.isfile(crawled):
        writeToFile(crawled,'')

# creating a new file
def writeToFile(filePath, data):
    f = open(filePath,'w')
    f.write(data)
    f.close()

# appending data to existing file
def appendToFile(filePath, data):
    with open(filePath,'a') as f:
        f.write(data+"\n")

# delete the contents in a file
def deleteContentFromFile(filePath):
    with open(filePath,'w') as f:
        pass

# store each line of file in a set
def fileToSet(filePath):
    res = set()
    with open(filePath,'rt') as f:
        for line in f:
            res.add(line.replace('\n',''))
    return res

# store contents of a set as a new line in a file
def setToFile(urls, filePath):
    with open(filePath,'w') as f:
        for url in sorted(urls):
            f.write(url+'\n')