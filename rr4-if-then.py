import requests

useme = "http://paper.people.com.cn/rmrb/html/2016-05/06/nw.D110000renmrb_20160506_2-01.htm"

usemetoo = "http://paper.people.com.cn/rmrb/html/2016-07/04/nw.D110000renmrb_20160704_2-01.htm"

def runner(link):

    request = requests.get(link)
    if request.status_code == 200:
        print('Web site exists')
    else:
        print('Web site does not exist')

runner(useme)
print ""
runner(usemetoo)
