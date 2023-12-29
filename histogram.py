import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\project innovation\ACOS.xlsx"  # 使用正确的文件路径
df = pd.read_excel(file_path)
print(df.columns)  # 打印列名

# 指定文件路径
file_path = r"C:\project innovation\ACOS.xlsx"
column_index = 39  # 'AN'列的索引

# 读取Excel文件中特定列的数据
try:    
    # 使用列索引作为标签来读取数据
    data = pd.read_excel(file_path, usecols=[column_index], skiprows=1, nrows=6035)
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

# 绘制直方图
# 使用iloc来引用数据列
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(data.iloc[:, 0].dropna(), bins=100, edgecolor='black',)  # 使用.iloc[:, 0]来引用第一列数据

# 获取直方图中间的索引位置
mid_bin = len(patches) // 2

# 为每个条形应用渐变颜色
for i, patch in enumerate(patches):
    # 计算颜色强度，以中间为最亮黄色，两边逐渐变浅
    color_intensity = 1 - abs(mid_bin - i) / mid_bin
    patch.set_facecolor(plt.cm.Oranges(color_intensity))
    
plt.title('Histogram of Column AN')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
