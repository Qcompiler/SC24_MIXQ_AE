
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
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3), dpi=800)

labels = ['32', '64', '128', '256', '512']
bnb = [209.1440, 330.36, 591.943, 693.58832, 1016.8992]
fp16 = [242.6908144076378, 406.63136025521686, 659.4347788704126, 1076.3401090231819, 1187.9460534472314]
mixq8 = [286.18157549654046, 555.6174445801337, 1060.540219349537, 1647.8403328394252, 1808.7180012397919]
EETQ = [289.318855, 327.78492, 389.93272, 459.132875, 674.9744]

width = 0.14  # the width of the bars
x = np.arange(len(labels))
rects1 = ax1.bar(x - width*2, fp16, width, label='FP 16', color=bar_colors_default[0])
rects2 = ax1.bar(x - width+0.01, bnb, width, label='Bitsandbytes', color=bar_colors_default[3])
rects3 = ax1.bar(x + 0.02, EETQ, width, label='EETQ', color=bar_colors_default[2])
rects4 = ax1.bar(x + width+0.03, mixq8, width, label='MixQ', color = bar_colors_default[1])
autolabel(rects4, ax1)
autolabel(rects1, ax1)
ax1.set_xticks(x)
ax1.set_xticklabels(labels)


# ax2
awq = [316.31885536922755, 347.7843736659392, 368.6990016293272, 379.13280377331375, 380.99175490307744]
fp16 = [242.6908144076378, 406.63136025521686, 659.4347788704126, 1076.3401090231819, 1187.9460534472314]
mixq4 = [363.2483646510218, 699.6437240421243, 1302.5741414469812, 2082.2428160863815, 2287.0838133405896]
quik = [327, 600.6324, 1000.5741414469812, 1410.2428160863815, 1550.133405896]

rects1 = ax2.bar(x - width*2, fp16, width, color=bar_colors_default[0])
rects2 = ax2.bar(x - width+0.01, awq, width, label='AWQ', color=bar_colors_default[4])
#rects4 = ax2.bar(x + 0.02, quik, width, color=bar_colors_default[1])
rects3 = ax2.bar(x + width + 0.02, mixq4, width, color=bar_colors_default[1])
rects4 = ax2.bar(x +0.03, quik, width, label='QUIK',color = bar_colors_default[5])
# rects4 = ax2.bar(x + width+0.03, fuse24, width, color = bar_colors_default[1])
autolabel(rects3, ax2)
autolabel(rects1, ax2)
# autolabel(rects1, ax2)
ax2.set_xticks(x)
ax2.set_xticklabels(labels)


# Set the x-axis and y-axis labels for ax1
ax1.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_ylabel('Throughput (tokens/s)',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_title('LLaMA-70B, 8-bit Quantization',fontsize=12, fontname='Times New Roman')

# Set the x-axis and y-axis labels for ax2
ax2.set_xlabel('Batch Size',fontsize=12, fontproperties = 'Times New Roman')
ax2.set_ylabel('Throughput (tokens/s)',fontsize=12, fontproperties = 'Times New Roman')

# Set the title of ax2
ax2.set_title('LLaMA-70B, 4-bit Quantization',fontsize=12, fontname='Times New Roman')

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.2)

x1_label = ax1.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax1.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
x1_label = ax2.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax2.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]

legend_font = {
    'family': 'Times New Roman', # 字体
    'style': 'normal',
    'size': 12, # 字号
    'weight': "normal", # 是否加粗，不加粗
}
# Add a legend to ax1
# ax1.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
fig.legend(fontsize='small', bbox_to_anchor=(0.51, -0.03), loc='upper center', ncol=9, prop=legend_font)
plt.savefig('figure/throughput-llama70b.pdf', dpi=800, bbox_inches='tight')

# Show the plot
plt.show()
plt.close()


# llama7b throughput
import matplotlib.pyplot as plt
import numpy as np

# Define the bar colors
bar_colors_default= ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#F9DC5C"]

def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate("%.2f"%(height), ha='center', va='bottom', fontsize=9, color="k",fontname='Times New Roman',
                    xy=(rect.get_x() + rect.get_width() / 2, height - 120),
                    xytext=(0, 1),  # 1 points vertical offset
                    textcoords="offset points")

# Set font size
plt.rcParams.update({'font.size': 12})

# Create a figure and set its size
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3), dpi=800)

labels = ['32', '64', '128', '256', '512']
bnb = [243.25558399002458, 473.0694539536351, 946.8923387338575, 1818.3019073052687, 3322.93297372658]
fp16 = [1464.9072056929558, 2979.338904982297, 4777.1966329127445, 6608.57736171889, 7433.2856168722155]
mixq8 = [1477.0951511016222, 3007.7812811635126, 5366.696608771711, 8798.674342091785, 10973.036772088673]
EETQ = [1658.8894, 2210.129776, 3350.20729297, 5681.27497242, 5888.09020148]

width = 0.14  # the width of the bars
x = np.arange(len(labels))
rects1 = ax1.bar(x - width*2, fp16, width, label='FP 16', color=bar_colors_default[0])
rects2 = ax1.bar(x - width+0.01, bnb, width, label='Bitsandbytes', color=bar_colors_default[3])
rects3 = ax1.bar(x + 0.02, EETQ, width, label='EETQ', color=bar_colors_default[2])
rects4 = ax1.bar(x + width+0.03, mixq8, width, label='MixQ', color = bar_colors_default[1])
autolabel(rects4, ax1)

ax1.set_xticks(x)
ax1.set_xticklabels(labels)


# ax2
awq = [2331.8894670546842, 2930.182195272376, 3250.207572927797, 3481.27497175242, 3588.091702130148]
fp16 = [1464.9072056929558, 2979.338904982297, 4777.1966329127445, 6608.57736171889, 7433.2856168722155]
mixq4 = [1247.1158726102813, 2516.6217222144096, 4946.523351914129, 9013.459003664173, 11537.423162057035]
quik = [1147.1158726102813, 2116.6217222144096, 4311.523351914129, 7813.459003664173, 9100.423162057035]

rects1 = ax2.bar(x - width*2, fp16, width, color=bar_colors_default[0])
rects2 = ax2.bar(x - width+0.01, awq, width, label='AWQ', color=bar_colors_default[4])
#rects4 = ax2.bar(x + 0.02, quik, width, color=bar_colors_default[1])
rects3 = ax2.bar(x + width + 0.02, mixq4, width, color=bar_colors_default[1])
rects4 = ax2.bar(x +0.03, quik, width, color = bar_colors_default[5])
autolabel(rects3, ax2)
ax2.set_xticks(x)
ax2.set_xticklabels(labels)


# Set the x-axis and y-axis labels for ax1
#ax1.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_ylabel('Throughput (tokens/s)',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_title('LLaMA-7B, 8-bit Quantization',fontsize=12, fontname='Times New Roman')

# Set the x-axis and y-axis labels for ax2
#ax2.set_xlabel('Batch Size',fontsize=12, fontproperties = 'Times New Roman')
ax2.set_ylabel('Throughput (tokens/s)',fontsize=12, fontproperties = 'Times New Roman')

# Set the title of ax2
ax2.set_title('LLaMA-7B, 4-bit Quantization',fontsize=12, fontname='Times New Roman')

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.3)

x1_label = ax1.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax1.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
x1_label = ax2.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax2.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]

legend_font = {
    'family': 'Times New Roman', # 字体
    'style': 'normal',
    'size': 12, # 字号
    'weight': "normal", # 是否加粗，不加粗
}
# Add a legend to ax1

#fig.legend(fontsize='small', bbox_to_anchor=(0.51, -0.11), loc='upper center', ncol=9, prop=legend_font)
plt.savefig('figure/throughput-llama7b.pdf', dpi=800, bbox_inches='tight')

# Show the plot
plt.show()
plt.close()



# llama13b throughput
import matplotlib.pyplot as plt
import numpy as np

# Define the bar colors
bar_colors_default= ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#F9DC5C"]

# Set font size
plt.rcParams.update({'font.size': 12})

def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate("%.2f"%(height), ha='center', va='bottom', fontsize=9, color="k",fontname='Times New Roman',
                    xy=(rect.get_x() + rect.get_width() / 2, height - 110),
                    xytext=(0, 1),  # 1 points vertical offset
                    textcoords="offset points")
        
# Create a figure and set its size
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3), dpi=800)

labels = ['32', '64', '128', '256', '512']
bnb = [199.17495475749348, 396.18516405788205, 788.9794250234215, 1488.9144521134426, 2600.688776625473]
fp16 = [1055.8514765808147, 1893.811398759026, 2984.4234119550174, 4100.700700991241, 4218.614590526068]
mixq8 = [1119.82485649446, 2066.199364981623, 3613.9903267173104, 5502.671661601693, 6750.185134077457]
EETQ = [1237.56659, 1517.5228886642, 1653.547278382, 2073.561759205, 2835.11675554]

width = 0.14  # the width of the bars
x = np.arange(len(labels))
rects1 = ax1.bar(x - width*2, fp16, width, label='FP 16', color=bar_colors_default[0])
rects2 = ax1.bar(x - width+0.01, bnb, width, label='Bitsandbytes', color=bar_colors_default[3])
rects3 = ax1.bar(x + 0.02, EETQ, width, label='EETQ', color=bar_colors_default[2])
rects4 = ax1.bar(x + width+0.03, mixq8, width, label='MixQ', color = bar_colors_default[1])
# autolabel(rects1)
autolabel(rects4, ax1)
# autolabel(rects1, ax1)
ax1.set_xticks(x)
ax1.set_xticklabels(labels)


# ax2
awq = [1332.5694542349659, 1616.5357228886642, 1783.547262078382, 1873.5696401759205, 1925.1180722675554]
fp16 = [1055.8514765808147, 1893.811398759026, 2984.4234119550174, 4100.700700991241, 4218.614590526068]
mixq4 = [998.2687159958498, 2005.2399471116855, 3937.6492522535077, 5867.249292372928, 7327.857666157665]

quik = [898.652002037925,	1721.46485507108,	3024.71075889485,	4373.71819503186,	5966.65530825936 ] 
rects1 = ax2.bar(x - width*2, fp16, width, color=bar_colors_default[0])
rects2 = ax2.bar(x - width+0.01, awq, width, label='AWQ', color=bar_colors_default[4])
#rects4 = ax2.bar(x + 0.02, quik, width, color=bar_colors_default[1])
rects3 = ax2.bar(x + width + 0.02, mixq4, width, color=bar_colors_default[1])
rects4 = ax2.bar(x +0.03, quik, width, color = bar_colors_default[5])
# rects4 = ax2.bar(x + width+0.03, fuse24, width, color = bar_colors_default[1])
autolabel(rects3, ax2)
# autolabel(rects1, ax2)
ax2.set_xticks(x)
ax2.set_xticklabels(labels)


# Set the x-axis and y-axis labels for ax1
# ax1.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_ylabel('Throughput (tokens/s)',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_title('LLaMA-13B, 8-bit Quantization',fontsize=12, fontname='Times New Roman')

# Set the x-axis and y-axis labels for ax2
# ax2.set_xlabel('Batch Size',fontsize=12, fontproperties = 'Times New Roman')
ax2.set_ylabel('Throughput (tokens/s)',fontsize=12, fontproperties = 'Times New Roman')

# Set the title of ax2
ax2.set_title('LLaMA-13B, 4-bit Quantization',fontsize=12, fontname='Times New Roman')

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.2)

x1_label = ax1.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax1.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
x1_label = ax2.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax2.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]

legend_font = {
    'family': 'Times New Roman', # 字体
    'style': 'normal',
    'size': 12, # 字号
    'weight': "normal", # 是否加粗，不加粗
}
# Add a legend to ax1

#fig.legend(fontsize='small', bbox_to_anchor=(0.51, -0.11), loc='upper center', ncol=9, prop=legend_font)
plt.savefig('figure/throughput-llama13b.pdf', dpi=800, bbox_inches='tight')

# Show the plot
plt.show()
plt.close()