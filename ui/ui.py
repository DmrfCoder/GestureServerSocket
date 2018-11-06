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
    bsRecord = [0] * 4400

    def updateI(self, newI):
        print("update on ui date" + str(newI[0]))
        self.I = newI

    def updateQ(self, newQ):
        self.Q = newQ

    def updateBsRecord(self, newBs):
        self.bsRecord = newBs

    def __init__(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        self.fig = plt.figure(figsize=(16, 10))
        # IQ幅度
        ax1 = self.fig.add_subplot(2, 2, 1)
        # IQ复平面
        ax2 = self.fig.add_subplot(2, 2, 2)
        # 原始数据
        ax3 = self.fig.add_subplot(2, 2, 3)

        x = np.arange(0, 2200, 1)

        ax1.set_ylim(-1, 1)
        self.line1, = ax1.plot(x, self.I, label='I')
        self.line2, = ax1.plot(x, self.Q, label='Q', color='red', linewidth=1.0, linestyle='--')
        ax1.legend(loc='upper right')
        ax1.set_ylabel('I/Q')
        ax1.set_xlabel('Time(s)')

        ax2.set_ylim(-1, 1)
        ax2.set_xlim(-1, 1)
        ax2.set_xlabel('I')
        ax2.set_ylabel('Q')

        self.line2, = ax2.plot(self.I, self.Q)

        self.line3 = ax3.plot(self.bsRecord)
        ax3.set_title('Raw Signal')

    def initAnimation(self):
        self.line1.set_ydata(self.I)
        self.line2.set_ydata(self.Q)
        self.line3.set_ydata(self.bsRecord)
        return self.line1, self.line2, self.line3

    def animate(self, i):
        # 接着，构造自定义动画函数animate，用来更新每一帧上各个x对应的y坐标值，参数表示第i帧
        # plt.cla() 这个函数很有用，先记着它
        self.line1.set_ydata(self.I)
        self.line2.set_ydata(self.Q)
        self.line3.set_ydata(self.bsRecord)

        return self.line1, self.line2, self.line3

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
