import matplotlib.pyplot as plt

def my_plot_histogram(data, figsize=(10,6), title="Histogram", xlabel="x Label", ylabel="y Label"):
    keys = list(data.keys())
    values = list(data.values())
    plt.figure(figsize=figsize)
    plt.bar(keys, values)
    plt.xticks(rotation=-90)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.show()