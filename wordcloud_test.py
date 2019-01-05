# coding: utf-8

from os import path  #用来获取文档的路径

#词云
from PIL import Image
import numpy as  np
import matplotlib.pyplot as plt
#词云生成工具
from wordcloud import WordCloud,ImageColorGenerator
#需要对中文进行处理
import matplotlib.font_manager as fm
import io

#背景图
bg=np.array(Image.open("images.jpeg"))

#获取当前的项目文件加的路径
d=path.dirname(__file__)


#读取要分析的文本
text_path="remove_stop_words_without_flag.txt"
#读取要分析的文本，读取格式
text= io.open(path.join(d,text_path), encoding = 'gbk').read()


#生成
wc=WordCloud(
    background_color="white",
    scale = 1.5,
    max_words=100,
    mask=bg,            #设置图片的背景
    max_font_size=200,
    random_state=80,
    font_path='simfang.ttf'   #中文处理，用系统自带的字体
    #font_path='黑体.ttf'   #中文处理，用系统自带的字体
    ).generate(text)
#为图片设置字体
my_font=fm.FontProperties(fname='simfang.ttf')
#产生背景图片，基于彩色图像的颜色生成器
image_colors=ImageColorGenerator(bg)
#开始画图
plt.imshow(wc.recolor(color_func=image_colors))
#为云图去掉坐标轴
plt.axis("off")
#画云图，显示
#plt.figure()
plt.show()
#为背景图去掉坐标轴
plt.axis("off")
plt.imshow(bg,cmap=plt.cm.gray)

#保存云图
wc.to_file("ciyun_02.png")
