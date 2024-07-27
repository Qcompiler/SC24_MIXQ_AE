# llama70b throughput
import matplotlib.pyplot as plt
import numpy as np

# Define the bar colors
bar_colors_default= ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#F9DC5C"]
def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate("%.2f"%(height), ha='center', va='bottom', fontsize=9, color="k",fontname='Times New Roman',
                    xy=(rect.get_x() + rect.get_width() / 2, height - 20),
                    xytext=(0, 1),  # 1 points vertical offset
                    textcoords="offset points")
# Set font size
plt.rcParams.update({'font.size': 12})

# Create a figure and set its size
fig, ax1 = plt.subplots(1, 1, figsize=(6, 3), dpi=800)

import numpy as np
labels = ['32', '64', '128', "256", "512"]
fp8 = [454.5084377,923.3477591,1719.662241,2880.001614,3657.796975]
fp16 = [324.7421773966231, 600.0817201560811, 1019.1094069141465, 1508.5728672586265,2158.689404699797]
mixq8 = [522.7656492518856, 1033.4854969238233, 1649.8317105063006, 2896.415630378135, 3157.999170605311]

width = 0.2  # the width of the bars
x = np.arange(len(labels))
rects3 = ax1.bar(x - width, fp16, width, label='FP16', color = bar_colors_default[3])
rects4 = ax1.bar(x, fp8, width, label='FP8', color = bar_colors_default[0])
rects1 = ax1.bar(x + width, mixq8, width, label='MixQ', color=bar_colors_default[1])
autolabel([rects4[4]], ax1)
autolabel(rects1, ax1)
autolabel(rects3, ax1)
ax1.set_xticks(x)
ax1.set_xticklabels(labels)

# Set the x-axis and y-axis labels for ax1
ax1.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_ylabel('Throughput (tokens/s)',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_title('LLaMA-70B, H100',fontsize=12, fontname='Times New Roman')


plt.subplots_adjust(wspace=0.2)

x1_label = ax1.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax1.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 

legend_font = {
    'family': 'Times New Roman', # 字体
    'style': 'normal',
    'size': 12, # 字号
    'weight': "normal", # 是否加粗，不加粗
}
# Add a legend to ax1

fig.legend(fontsize='small', bbox_to_anchor=(0.50, -0.03), loc='upper center', ncol=4, prop=legend_font)
plt.savefig('figure/throughput-fp8.pdf', dpi=800, bbox_inches='tight')

# Show the plot
plt.show()
plt.close()
