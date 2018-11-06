# -*-coding:utf-8-*-

from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import tkinter
from tkinter import *
import tkinter.font as tkFont

import _thread


class Ui:
    I = [0] * 2200
    Q = [0] * 2200

    def updateI(self, newI):
        print("update on ui date" + str(newI[0]))
        self.I = newI

    def updateQ(self, newQ):
        self.Q = newQ

    def __init__(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        self.fig = plt.figure(figsize=(15, 10))
        ax1 = self.fig.add_subplot(2, 1, 1)
        ax2 = self.fig.add_subplot(2, 1, 2)

        x = np.arange(0, 2200, 1)

        ax1.set_ylim(-1, 1)
        self.line1, = ax1.plot(x, self.I)

        ax2.set_ylim(-1, 1)
        self.line2, = ax2.plot(x, self.Q)

    def initAnimation(self):
        self.line1.set_ydata(self.I)
        self.line2.set_ydata(self.Q)
        return self.line1, self.line2

    def animate(self, i):
        # 接着，构造自定义动画函数animate，用来更新每一帧上各个x对应的y坐标值，参数表示第i帧
        # plt.cla() 这个函数很有用，先记着它
        self.line1.set_ydata(self.I)
        self.line2.set_ydata(self.Q)

        return self.line1, self.line2

    # 接下来，我们调用FuncAnimation函数生成动画。参数说明：
    # fig 进行动画绘制的figure
    # func 自定义动画函数，即传入刚定义的函数animate
    # frames 动画长度，一次循环包含的帧数
    # init_func 自定义开始帧，即传入刚定义的函数init
    # interval 更新频率，以ms计
    # blit 选择更新所有点，还是仅更新产生变化的点。应选择True，但mac用户请选择False，否则无法显示动画

    def drawView(self):
        ani = animation.FuncAnimation(fig=self.fig,
                                      func=self.animate,
                                      frames=100,
                                      init_func=self.initAnimation,
                                      interval=100,
                                      blit=False)
        plt.show()

    def start(self):
        self.drawView()
