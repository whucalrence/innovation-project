import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.distance import cosine


# 创建图和3D轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 设置向量并设置向量颜色
vectors = {
    'Chunk-semantic 1': {'vector': [2, 1, 2], 'color': 'red'},
    'Chunk-semantic 2': {'vector': [3, 3, 0.4], 'color': 'green'},
    'Chunk-semantic 3': {'vector': [0.5, 3, 3], 'color': 'blue'}
}

# 为了将原点置于中心，确定所有向量的最大范围
max_range = max(max(abs(val) for val in vector['vector']) for vector in vectors.values())
# 设置轴界限，使原点在中心
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

# 设置轴界限
ax.set_xlim([0, max_range])
ax.set_ylim([0, max_range])
ax.set_zlim([0, max_range])
ax.invert_yaxis()


    
# Setting the intervals for each axis
ax.set_xticks(range(0, int(max_range)+1, 1))
ax.set_yticks(range(0, int(max_range)+1, 1))
ax.set_zticks(range(0, int(max_range)+1, 1))



# 绘制向量
for name, properties in vectors.items():
    vector = properties['vector']  # 获取向量的数值部分
    color = properties['color']  # 获取颜色

    # 计算向量长度
    length = np.linalg.norm(vector)  # 仅对数值数组使用 np.linalg.norm

    # 绘制向量
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2],
              length=length,  # 设置箭头长度
              normalize=True,
              arrow_length_ratio=0.1,  # 调整箭头头部大小
              color=color,  # 使用指定的颜色
              label=name)
        
# 自定义虚线的间距
dashed_line_style = (0, (5, 10))  # 更大的间距

# 计算并绘制余弦距离连线
for name1, properties1 in vectors.items():
    for name2, properties2 in vectors.items():
        if name1 != name2:
            # 计算余弦距离
            cos_dist = cosine(properties1['vector'], properties2['vector'])
            # 根据余弦距离绘制连线（可根据需要调整阈值）
            if cos_dist < 2:
                ax.plot([properties1['vector'][0], properties2['vector'][0]],
                        [properties1['vector'][1], properties2['vector'][1]],
                        [properties1['vector'][2], properties2['vector'][2]],
                        linestyle=dashed_line_style,color='k',linewidth=1)
                
# 添加轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')



# 添加图例并设置图例的位置
ax.legend(loc=(0.8, 0.8))

# 显示图
plt.show()

                                                                                      