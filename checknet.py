import urllib2
def CheckNet(url):
    try:
        req = urllib2.Request(url, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        response = urllib2.urlopen(req).read()
        return 0;
    except IOError:
        return 1;
websites = ["https://www.google.com/", "https://github.com/", "https://twitter.com/explore", "http://espn.com/", "https://en.wikipedia.org/wiki/Main_Page"]
a = 0;
y = 0;
while(a < len(websites)):
    #print websites[a];
    #print a;
    #print CheckNet(websites[a]);
    y = y + CheckNet(websites[a]);
    a = a + 1;
s = len(websites) - y
rate = float(float(s) / float((len(websites))) * float(100))
print str(s) + " out of " + str(len(websites)) + " tests were successful. That makes for a success rate of " + str(rate) + "%."
