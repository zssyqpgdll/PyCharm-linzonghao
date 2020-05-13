import requests
import bs4

def get_url(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    res=requests.get(url,headers=headers)

    return res

def wtext(soup,flag):
    with open(str(flag)+'.text','a',encoding='utf-8') as file:
        titles=soup.find_all('li',class_="video-item matrix")
        for i in titles:
            file.write(i.a['title']+'\n')
        file.close()

def main():
    flag=['totalrank','click','dm','stow']
    keyword=input("请输入关键词:")
    url="https://search.bilibili.com/all?keyword="+keyword
    page=eval(input("请输入爬取页数:"))
    for i in range(len(flag)):
        url_1=url+"&order="+flag[i]
        for j in range(page):
            url_2=url_1+'&page='+str(j+1)
            res=get_url(url_2)
            soup=bs4.BeautifulSoup(res.txt,'html.parser')
            wtext(soup,flag[i])
        
main()
