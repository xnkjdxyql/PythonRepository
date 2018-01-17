from GetUrlSet import GetPostUrlSet
from GetPicWithinPost import GetPics

url_set = set()
counter = 1
for n in range(1, 10):
    page = 'http://91.t9p.today/forumdisplay.php?fid=19&page={}'.format(n)
    urlsgetter = GetPostUrlSet(page)
    url_set.clear()
    url_set = urlsgetter.get_urls_set()
    for post_url in url_set:
        picgetter = GetPics(post_url, counter)
        counter +=1
        picgetter.getpic()
