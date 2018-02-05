from urllib import request
import re
import os

# url = 'https://tieba.baidu.com/p/5366093412'
url = input('输入贴吧链接：')
url = str(url)


with request.urlopen(url) as f:
    data = f.read()

    title = re.compile('<title>(.*?)_百度贴吧</title>').findall(data.decode('utf-8'))

    try:
        title = re.compile('<title>(.*?)_百度贴吧</title>').findall(data.decode('utf-8'))
        os.mkdir(str(title[0]))
        print("成功创建文件夹")
        os.chdir(os.path.join(os.getcwd(), str(title[0])))
    except:
        print("出现错误")


def page(url):
    start = input("开始页码：")
    end = input("结束页码：")
    p = int(start)
    while p < int(end):
        url2 = url + '?pn=' + str(p)
        image_content(url2)
        p = int(p) + 1


def image_content(url):
    html_content = request.urlopen(url).read()
    print(html_content)
    image_list = re.compile('(?:[a-zA_Z0-9="^>]+ )*src="(.*?)" ').findall(html_content.decode('UTF-8'))

    if len(image_list) == 0:
        print("没有发现图片")
    else:
        print("有图片")
        print("正在下载")
        print(len(image_list))
        for i in range(len(image_list)):
            image_name = str(i + 1) + '.jpg'
            try:
                #存储图片
                request.urlretrieve(image_list[i], image_name)
                #存储成功打印
                print("成功下载：" + image_list[i])
            except Exception as Error:
                print("下载失败" + image_list[i])

# create_file(url)
page(url)
image_content(url)
