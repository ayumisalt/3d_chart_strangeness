import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

# データパスの設定
path = os.getcwd()
datapath = "modified_data.txt"

# フォント
plt.rcParams["font.family"] = "Times New Roman"
# plt.rcParams["font.size"] = 14

# データの読み込み
data = pd.read_csv(datapath, sep="\t", header=None)
data.columns = ["Z", "N", "MS", "RD", "LP", "FI", "FU", "SP", "PF", "UN", "ST"]

# 色の設定
decay_modes = ["MS", "RD", "LP", "FI", "FU", "SP", "PF", "UN"]
colors = ["cyan", "black", "orange", "yellow", "brown", "blue", "green", "purple"]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")


# 各崩壊形式ごとにプロット
for mode, color in zip(decay_modes, colors):
    mask = data[mode] == 1
    xs = data[mask]["N"].astype(float)
    ys = data[mask]["Z"].astype(float)
    zs = np.zeros_like(xs)
    dx = dy = 1.0  # 立方体のサイズ
    dz = data[mask]["ST"].astype(float) + 0.02  # 少し高さを増加させる
    ax.bar3d(xs, ys, zs, dx, dy, dz, color=color, alpha=0.6)

# ストレンジネス-1
mask_st = data["ST"] == 1
xs = data[mask_st]["N"].astype(float)
ys = data[mask_st]["Z"].astype(float)
zs = np.ones_like(xs)  # Z軸の値を1に設定
dx = dy = 1.0  # 立方体のサイズ
dz = data[mask_st]["ST"].astype(float) + 0.02 - 1  # 少し高さを増加させる
ax.bar3d(xs, ys, zs, dx, dy, dz, color="magenta", alpha=0.6, label="Strangeness")

# ストレンジネス-2
mask_st = data["ST"] == 2
xs = data[mask_st]["N"].astype(float)
ys = data[mask_st]["Z"].astype(float)
zs = np.ones_like(xs) + 1  # Z軸の値を2に設定
dx = dy = 1.0  # 立方体のサイズ
dz = data[mask_st]["ST"].astype(float) + 0.02 - 2  # 少し高さを増加させる
ax.bar3d(xs, ys, zs, dx, dy, dz, color="red", alpha=0.6, label="Strangeness")

# 観察の角度を設定
ax.view_init(elev=25, azim=-115)

# 描写範囲を設定
ax.set_xlim(0, 200)
ax.set_ylim(0, 135)
ax.set_zlim(0, 3)

# XYのアスペクト比を保つ
ax.set_box_aspect([200, 135, 90])  # アスペクト比を調整

# グリッド表示をオフにする
ax.grid(False)

# Z軸の目盛を0, -1, -2に設定
ax.set_zticks([0, 1, 2])
ax.set_zticklabels(["0", "-1", "-2"])

# 軸の設定
ax.set_xlabel("Neutron number")
ax.set_ylabel("Proton number")
ax.set_zlabel("Strangeness")
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.xaxis._axinfo["grid"].update({"color": "w", "linewidth": 0.0})
ax.yaxis._axinfo["grid"].update({"color": "w", "linewidth": 0.0})
ax.zaxis._axinfo["grid"].update({"color": "w", "linewidth": 0.0})
# ax.xaxis.set_ticks_position("none")
# ax.yaxis.set_ticks_position("none")
# ax.zaxis.set_ticks_position("none")

# プロットの表示
plt.show()

# 画像の保存
fig.savefig("3d_chart.png")
