import matplotlib.pyplot as plt
import numpy as np

I = np.eye(2)
Z = np.array([[1,0],
              [0,-1]])

def get_Z_list(num):
    z_list = []
    # Z[i]を作成
    for i in range(num):
        # テンソル積を計算
        z_i = 1
        for j in range(num):
            if i==j: z_i=np.kron(z_i,Z)
            else: z_i=np.kron(z_i,I)
        z_list.append(z_i)
    return z_list


# //ーーーーーーーーーーーーーーーーーーーーー
def get_color_lerp(start,end,rate):
    if rate<0: rate=0
    elif rate>1: rate=1

    r = start[0] + (end[0] - start[0]) * rate
    g = start[1] + (end[1] - start[1]) * rate
    b = start[2] + (end[2] - start[2]) * rate
    return (r, g, b)

def my_plot_histogram(data, figsize=(10,6), title="Histogram", xlabel="x Label", ylabel="y Label",gradation=False):
    keys = list(data.keys())
    values = list(data.values())

    colors = []
    if gradation:
        val_max = max(values)
        val_min = min(values)
        blue = (0,0,0.4)
        red = (0.8,0.2,0.2)
        for i in range(len(values)):
            rate = (values[i]-val_min)/(val_max-val_min)
            colors.append(get_color_lerp(blue,red,rate))
    else:
        colors = [(0.2,0.5,1) for i in range(len(values))]

    plt.figure(figsize=figsize)
    plt.bar(keys, values, color=colors)
    plt.xticks(rotation=-90)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.show()