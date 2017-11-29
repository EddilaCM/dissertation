# -*- coding:utf-8 -*-
# __author__ = 'cm'
from numpy import *
import numpy as np


if __name__ == '__main__':
    # creat array
    a = array([2,3,4])
    a.dtype # the number's type in the array

    #attention please: when use function array() to creat a new array, we must keep the all numbers in [], not only have numbers.

    # show the numbers'type in the array
    c = array([[1,2],[3,4]],dtype=complex)

    # use function zeros() creat a array that it's all numbers are 0
    d = zeros((3,4))  #3-row,4-column

    # set the number's type manually
    e = ones((2,3,4),dtype=int16)  # 2个 3-row 4-column 的二维数组，即一个3维数组

    #empty, unlike zeros, does not set the array values to zero, and may therefore be marginally faster. On the other hand, it requires the user to manually set all the values in the array, and should be used with caution.
    # return an array which shape is set.       e.g. a array include 2 rows and 3 columns
    f = empty((2,3))

    # function arange(start,end,step); return a arithmetic progression(等差数列) array; this functioin's arg accept int and float
    # but because of the precision's limit of float, we can't forecast the total number of the array, so need linspace()
    g = arange(0,2,0.5)

    # linespace(start,end,averageNumber)
    h = linspace(-1, 0, 5)
    # means array([-1.  , -0.75, -0.5 , -0.25,  0.  ])



    # Python中自带的整型、浮点型和复数类型远远不够，因此NumPy中添加了许多数据类型。如下:
    # NumPy中的基本数据类型
    # 名称	描述
    # bool	用一个字节存储的布尔类型（True或False）
    # inti	由所在平台决定其大小的整数（一般为int32或int64）
    # int8	一个字节大小，-128 至 127
    # int16	整数，-32768 至 32767
    # int32	整数，-2 ** 31 至 2 ** 32 -1
    # int64	整数，-2 ** 63 至 2 ** 63 - 1
    # uint8	无符号整数，0 至 255
    # uint16	无符号整数，0 至 65535
    # uint32	无符号整数，0 至 2 ** 32 - 1
    # uint64	无符号整数，0 至 2 ** 64 - 1
    # float16	半精度浮点数：16位，正负号1位，指数5位，精度10位
    # float32	单精度浮点数：32位，正负号1位，指数8位，精度23位
    # float64或float	双精度浮点数：64位，正负号1位，指数11位，精度52位
    # complex64	复数，分别用两个32位浮点数表示实部和虚部
    # complex128或complex	复数，分别用两个64位浮点数表示实部和虚部


    # numpy computation
    #1 plus 、 subtract——according to element operation one by one
    a= array([20,30,40,50])
    b= arange(4)
    c= a-b
    # 2、 multiplication
    A = array([[1,1],[0,1]])
    B = array([[2,0],[3,4]])
    print A*B  #对应位子的元素相乘，类似加减法
    print dot(A,B)  # matrix multiplication

    # 有些操作符如+=和*=用来更改已存在数组而不创建一个新的数组。
    # 当数组中存储的是不同类型的元素时，数组将使用占用更多位（bit）的数据类型作为其本身的数据类型，也就是偏向更精确的数据类型(这种行为叫做upcast)。

    # 非数组运算，用ndarray类的方法实现
    a1 = np.random.random((2,3))
    print a1.sum()
    print a1.min()
    print a1.max()
    print "a1:",a1
    #可以指定相应的轴进行操作
    b1 = np.arange(12).reshape(3,4)
    print "b1:",b1
    print u'计算每一列的和:',b1.sum(axis=0)
    print u"获取每一行的最小值:",b1.min(axis=1)
    print u"计算每一行的累积和 :",b1.cumsum(axis=1)
    #  axis: 维度的意思，二维就是1-row,0-column

    # 索引、切片、迭代
    # arange函数用于创建等差数组，使用频率非常高，arange非常类似range函数，会python的人肯定经常用range函数，比如在for循环中，几乎都用到了range，
    # 下面我们通过range来学习一下arange，两者的区别仅仅是arange返回的是一个数据，而range返回的是list。
    a2= np.arange(10)**3 #记住，操作符是对数组中逐元素处理的！0-9每个数的3次方
    print 'a2:',a2
    print u'下标2-5所对应的元素:',a2[2:5]
    # a2[:6:2] =-1000
    print u'从0到第6个位置，每隔一个元素将其赋值为-1000:', a2
    print u'反转:', a2[::-1]
    for i in a2:
        print i**(1/3.)

    # 多维数据以轴为索引

