import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体，防止乱码
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'PingFang SC']
plt.rcParams['axes.unicode_minus'] = False

# 数据准备
categories = ['平均车速\n(km/h)', '加速度标准差\n(m/s²)', '急转弯频率\n(次/km)', '紧急制动频率\n(次/km)']
calm = [45.2, 1.12, 3.2, 1.1]
normal = [52.8, 2.26, 6.8, 2.5]
aggressive = [61.5, 2.7, 12.5, 5.2]

x = np.arange(len(categories))  # 标签位置
width = 0.25  # 条宽度

# 创建图形
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制三组条形图
bars1 = ax.bar(x - width, calm, width, label='冷静型', color='#2E86AB', edgecolor='white')
bars2 = ax.bar(x, normal, width, label='普通型', color='#A23B72', edgecolor='white')
bars3 = ax.bar(x + width, aggressive, width, label='激进型', color='#F18F01', edgecolor='white')

# 添加数值标签
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# 设置图表属性
ax.set_ylabel('数值', fontsize=12)
ax.set_title('不同驾驶风格行为特征对比', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend(loc='upper left', fontsize=10)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# 可选：调整y轴范围使图表更美观
ax.set_ylim(0, 70)

# 显示图表
plt.tight_layout()
plt.show()

# 如果需要保存图片到本地，取消下面一行的注释
# plt.savefig('驾驶风格行为特征对比.png', dpi=300, bbox_inches='tight')