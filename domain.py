from urllib.parse import urlparse

# get project name
# It will return something like xyz from abc.xyz.com
def getProjectFolderName(url):
    try:
        results = getSubDomainName(url).split('.')
        return results[-2]
    except:
        return ''

# get domain name
# It will return something like xyz.com
def getDomainName(url):
    try:
        results = getSubDomainName(url).split('.')
        return results[ -2 ] + '.' + results[ -1 ]
    except:
        return ''

# get domain name
# It will return something like xyz.com
def getDomainName(url):
    try:
        results = getSubDomainName(url).split('.')
        return results[ -2 ] + '.' + results[ -1 ]
    except:
        return ''

# get sub domain name.
# It will return something like abc.xyz.com
def getSubDomainName(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


# print(getDomainName('http://budzu.com/prices'))