
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import os

# 1. 加载数据 / Load the dataset
df = pd.read_csv("D:\RM\Data\Results_21MAR2022_nokcaladjust.csv")

# 2. 数据清洗 - 删除缺失值 / Drop rows with missing values
clean_df = df.dropna(subset=[
    "diet_group", "sex", "age_group",
    "mean_ghgs", "mean_land", "mean_watscar", "mean_eut",
    "mean_ghgs_ch4", "mean_ghgs_n2o", "mean_bio", "mean_watuse", "mean_acid"
])

# 3. 定义需归一化的环境指标 / Environmental indicators for normalization
impact_columns = [
    "mean_ghgs", "mean_land", "mean_watscar", "mean_eut",
    "mean_ghgs_ch4", "mean_ghgs_n2o", "mean_bio", "mean_watuse", "mean_acid"
]

# 4. Min-Max 归一化 / Normalize using MinMaxScaler
scaler = MinMaxScaler()
normalized_impacts = scaler.fit_transform(clean_df[impact_columns])
normalized_df = clean_df.copy()
normalized_df[impact_columns] = normalized_impacts

# 5. 构造综合环境影响评分 / Create composite score
normalized_df["total_impact_score"] = normalized_df[impact_columns].sum(axis=1)

# 6. 按饮食类型分组计算平均值 / Group by diet type and compute means
grouped = normalized_df.groupby("diet_group")[impact_columns].mean().reset_index()
grouped["total_impact_score"] = grouped[impact_columns].sum(axis=1)

# 7. 创建雷达图并保存至 images 文件夹 / Create radar chart and save to images/
labels = impact_columns
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

for i, row in grouped.iterrows():
    values = row[labels].tolist()
    values += values[:1]
    ax.plot(angles, values, label=row["diet_group"])
    ax.fill(angles, values, alpha=0.1)

# 设置雷达图样式 / Configure radar chart
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=10)
plt.title("Normalized Environmental Impact by Diet Type", size=14)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()

# 自动保存图像 / Automatically save image to 'images' folder
os.makedirs("images", exist_ok=True)
plt.savefig("images/diet_radar_chart.png")
plt.show()

