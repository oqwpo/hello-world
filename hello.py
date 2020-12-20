# import requests
# import re
# url='http://topit.pro'
# response=requests.get(url)
# results=re.findall("<img[\\s\\s]+?src=\"(.+?)\"", response.text)
# name=0
# for result in results:
#     img_url=url+result
#     f=open(str(name)+'.jpg','wb')
#     f.write(requests.get(img_url).content)
#     f.close()
#     name+=1

# from bs4 import BeautifulSoup

# # 读取html文件
# f = open('test.html', 'r')
# str = f.read()
# f.close()

# # 创建BeautifulSoup对象，第一个参数为解析的字符串，第二个参数为解析器
# soup = BeautifulSoup(str, 'html.parser')

# # 匹配内容，第一个为标签名称，第二个为限定属性，下面表示匹配class为test的img标签
# img_list = soup.find_all('img', {'class':'test'})

# # 遍历标签 
# for img in img_list:
#     # 获取img标签的src值
#     src = img['src']
#     print(src)
# import requests
# from bs4 import BeautifulSoup

# def get_movies():
#     headers={
#         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.4",
#         "Host":"movie.douban.com"
#     }
#     movie_list=[]
#     for i in range(0,10):
#         link="https://movie.douban.com/top250?start="+str(i*25)
#         r=requests.get(link,headers=headers,timeout=10)
#         print(str(i+1),"页响应状态码：",r.status_code)
        
#         soup=BeautifulSoup(r.text,"lxml")
#         div_list=soup.find_all('div',class_='hd')
#         for each in div_list:
#             movie=each.a.span.text.strip()
#             movie_list.append(movie)
#     return movie_list

# movies=get_movies()
# print(movies)
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.implicitly_wait(20) # 隐性等待，最长等20秒
#把上述地址改成你电脑中geckodriver.exe程序的地址
driver.get("http://www.santostang.com/2018/07/04/hello-world/")
time.sleep(5)
for i in range(0,3):
    # 下滑到页面底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 转换iframe，再找到查看更多，点击
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
    load_more = driver.find_element_by_css_selector('button.more-btn')
    load_more.click()
    # 把iframe又转回去
    driver.switch_to.default_content()
    time.sleep(2)
    driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))
    comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print (content.text)