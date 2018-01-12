from GetAllMainPageUrlDics import GetActressMainPageDics
from GetNameAndPageNum import GetTotalPageNumAndName
from GetBigPicPageUrlList import GetBigPigPages
from GetPicfromBigimgPage import GetBigImage

info_item_dics = {}
info_item_dics = GetActressMainPageDics.get_pages()
name_list = list(info_item_dics.keys())
base_page = list(info_item_dics.values())

for i in range(1, len(name_list)):
    main_page = base_page[i]
    actress_name = name_list[i]
    counter = GetTotalPageNumAndName(actress_name)
    total_page = counter.get_total_pages_from_url(main_page)
    # print('total num of {} is {}----->{}/{}'.format(actress_name,total_page-1, i, len(name_list)))
    for j in range(1, total_page):
        movie_list_page = (main_page + '/{}'.format(j))
        UrlGetter = GetBigPigPages()
        BigPicUrlsWithinPage = UrlGetter.get_big_pic_urls_within_page(movie_list_page)
        for k in range(0, len(BigPicUrlsWithinPage)):
                GetBigImage.get_pic(BigPicUrlsWithinPage[k], actress_name)





