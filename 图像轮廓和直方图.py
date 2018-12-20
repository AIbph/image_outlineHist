#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
from PIL import Image
from pylab import *

'''
    figure()    新建一个图像
    contour()   绘制等高线
    hist（）    绘制图像的直方图，函数的第二个参数指定小区间的数目
    
'''


if __name__ == '__main__':
    '''图像的轮廓和直方图'''

    # 读取图像到数组中
    im = array(Image.open("./img/test.jpg").convert("L"))

    # 新建一个图像
    figure()

    # 不使用颜色信息
    gray()

    # 在原点的左上角显示轮廓图像
    contour(im, origin='image')

    # 将横轴纵轴的定标系数设成相同值 ,即单位长度相同
    axis('equal')
    axis('off')

    figure()

    # 绘制图像的直方图
    hist(im.flatten(), 256)

    show()