import matplotlib.pyplot as plt
import os


# 设置字体为黑体，以支持汉字
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def plot_elements(elements):
    # 创建x轴的索引
    x = range(len(elements))

    # 指定保存图表的文件夹
    folder = "result"
    if not os.path.exists(folder):  # 如果文件夹不存在，则创建它
        os.makedirs(folder)

    # 完整的文件路径
    file_path = os.path.join(folder, "plot.png")

    # 绘制线图
    plt.figure(figsize=(10, 5))
    plt.plot(x, elements, marker='o', linestyle='-', color='b')

    # 添加标题和标签
    plt.title('基于机械恶化下最优工作时间')
    plt.xlabel('搜索次数')
    plt.ylabel('最优总用时')

    # 显示网格
    plt.grid(True)

    # 保存图表到指定的文件夹和文件名
    plt.savefig(file_path)

    folder = "result"
    if not os.path.exists(folder):  # 如果文件夹不存在，则创建它
        os.makedirs(folder)

    file_path = os.path.join(folder, "plot.png")
    plt.savefig(file_path)

