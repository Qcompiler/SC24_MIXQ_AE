# batch size == 1024
import matplotlib.pyplot as plt
plt.rcParams['pdf.fonttype'] = 42

import numpy as np

# Define the bar colors
bar_colors_default= ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#F9DC5C"]

# Set font size
plt.rcParams.update({'font.size': 12})

def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate("%.2f"%(height), ha='center', va='bottom', fontsize=10, color="k",fontname='SimHei',
                    xy=(rect.get_x() + rect.get_width() / 2, height - 4),
                    xytext=(0, 1),  # 1 points vertical offset
                    textcoords="offset points")

# Create a figure and set its size
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3), dpi=800)


# Plot the second graph on ax2
labels = ['unscheduled', 'unfused', 'fuse1', 'fuse2']


labels = ['LLaMA-7B', 'LLaMA-13B', 'LLaMA-70B']
bnb = [162.82762765832004, 183.2560764360725, 207.09288710112858]
unschedule = [186.6653794, 167.2737553, 192.921466]
unfuse = [262.0566106, 244.3806752, 277.1870944]
fuse1 = [348.3529008, 348.3529008, 348.3529008]
fuse2 = [366.7102629, 366.7102629, 448.6939782]



bnb = np.array(bnb)
unschedule = np.array(unschedule)/ bnb
unfuse = np.array(unfuse) / bnb
fuse1 = np.array(fuse1) / bnb
fuse2 = np.array(fuse2) / bnb
bnb = bnb /bnb 


width = 0.14  # the width of the bars
x = np.arange(len(labels))
rects0 = ax1.bar(x - width*2, bnb, width, label='Bitsandbytes', color=bar_colors_default[4])
rects1 = ax1.bar(x - width+0.01, unschedule, width, label='w/o. QAD', color=bar_colors_default[0])
rects2 = ax1.bar(x + 0.02, unfuse, width, label='QAD', color=bar_colors_default[3])
rects3 = ax1.bar(x + width + 0.03, fuse1, width, label='fuse quantization', color=bar_colors_default[2])
rects4 = ax1.bar(x + width*2 + 0.04, fuse2, width, label='fuse dequantization', color = bar_colors_default[1])
autolabel(rects0, ax1)
autolabel(rects1, ax1)
autolabel(rects2, ax1)
autolabel(rects3, ax1)
autolabel(rects4, ax1)
ax1.set_xticks(x)
ax1.set_xticklabels(labels)


# ax2
unschedule4 = [195.440493, 166.1059161, 225.8313132]
unfuse4 = [371.5115662, 323.9310135, 428.3879121]
fuse14 = [379.7646831, 470.0601602, 479.0544778]
fuse24 = [452.3033424, 512.5750442, 663.6802144]



unschedule4 = np.array(unschedule4) 
unfuse4 = np.array(unfuse4) / unschedule4
fuse14 = np.array(fuse14) / unschedule4
fuse24 = np.array(fuse24) / unschedule4
unschedule4 = unschedule4 /unschedule4 

rects1 = ax2.bar(x - width*2, unschedule4, width, color=bar_colors_default[0])
rects2 = ax2.bar(x - width+0.01, unfuse4, width, color=bar_colors_default[3])
rects3 = ax2.bar(x + 0.02, fuse14, width, color=bar_colors_default[2])
rects4 = ax2.bar(x + width+0.03, fuse24, width, color = bar_colors_default[1])
autolabel(rects1, ax2)
autolabel(rects2, ax2)
autolabel(rects3, ax2)
autolabel(rects4, ax2)
ax2.set_xticks(x)
ax2.set_xticklabels(labels)


# Set the x-axis and y-axis labels for ax1
# ax1.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'SimHei', 'size' : 16})
ax1.set_ylabel('加速倍数',fontsize=12,fontdict={'size' : 16})
ax1.set_title('8-bit Quantization, Batch Size = 1024',fontsize=12, fontname='SimHei')

# Set the x-axis and y-axis labels for ax2
# ax2.set_xlabel('Batch Size',fontsize=12, fontproperties = 'SimHei')
ax2.set_ylabel('加速倍数',fontsize=12)

# Set the title of ax2
ax2.set_title('4-bit Quantization, Batch Size = 1024',fontsize=12, fontname='SimHei')


x1_label = ax1.get_xticklabels() 
[x1_label_temp.set_fontname('SimHei') for x1_label_temp in x1_label]
y1_label = ax1.get_yticklabels() 
[y1_label_temp.set_fontname('SimHei') for y1_label_temp in y1_label]
 
x1_label = ax2.get_xticklabels() 
[x1_label_temp.set_fontname('SimHei') for x1_label_temp in x1_label]
y1_label = ax2.get_yticklabels() 
[y1_label_temp.set_fontname('SimHei') for y1_label_temp in y1_label]

legend_font = {
    'family': 'SimHei', # 字体
    'style': 'normal',
    'size': 12, # 字号
    'weight': "normal", # 是否加粗，不加粗
}
# Add a legend to ax1


fig.legend(fontsize='small', bbox_to_anchor=(0.51, -0.11), loc='upper center', ncol=9, prop=legend_font)
plt.savefig('figure/break_down.pdf', dpi=800, bbox_inches='tight')

# Show the plot
plt.show()
plt.close()

# ------------------------------------
# batch size == 1024
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
        ax.annotate("%.2f"%(height), ha='center', va='bottom', fontsize=10, color="k",fontname='SimHei',
                    xy=(rect.get_x() + rect.get_width() / 2, height - 4),
                    xytext=(0, 1),  # 1 points vertical offset
                    textcoords="offset points")

# Create a figure and set its size
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3), dpi=800)


# Plot the second graph on ax2
labels = ['unscheduled', 'unfused', 'fuse1', 'fuse2']


labels = ['LLaMA-7B', 'LLaMA-13B', 'LLaMA-70B']
bnb = [162.82762765832004, 183.2560764360725, 207.09288710112858]
unschedule = [186.6653794, 167.2737553, 192.921466]
unfuse = [262.0566106, 244.3806752, 277.1870944]
fuse1 = [348.3529008, 348.3529008, 348.3529008]
fuse2 = [366.7102629, 366.7102629, 448.6939782]



bnb = np.array(bnb)
unschedule = np.array(unschedule)/ bnb
unfuse = np.array(unfuse) / bnb
fuse1 = np.array(fuse1) / bnb
fuse2 = np.array(fuse2) / bnb
bnb = bnb /bnb 


width = 0.14  # the width of the bars
x = np.arange(len(labels))
rects0 = ax1.bar(x - width*2, bnb, width, label='Bitsandbytes', color=bar_colors_default[4])
rects1 = ax1.bar(x - width+0.01, unschedule, width, label='w/o. QAD', color=bar_colors_default[0])
rects2 = ax1.bar(x + 0.02, unfuse, width, label='QAD', color=bar_colors_default[3])
rects3 = ax1.bar(x + width + 0.03, fuse1, width, label='fuse quantization', color=bar_colors_default[2])
rects4 = ax1.bar(x + width*2 + 0.04, fuse2, width, label='fuse dequantization', color = bar_colors_default[1])
autolabel(rects0, ax1)
autolabel(rects1, ax1)
autolabel(rects2, ax1)
autolabel(rects3, ax1)
autolabel(rects4, ax1)
ax1.set_xticks(x)
ax1.set_xticklabels(labels)


# ax2
unschedule4 = [195.440493, 166.1059161, 225.8313132]
unfuse4 = [371.5115662, 323.9310135, 428.3879121]
fuse14 = [379.7646831, 470.0601602, 479.0544778]
fuse24 = [452.3033424, 512.5750442, 663.6802144]



unschedule4 = np.array(unschedule4) 
unfuse4 = np.array(unfuse4) / unschedule4
fuse14 = np.array(fuse14) / unschedule4
fuse24 = np.array(fuse24) / unschedule4
unschedule4 = unschedule4 /unschedule4 

rects1 = ax2.bar(x - width*2, unschedule4, width, color=bar_colors_default[0])
rects2 = ax2.bar(x - width+0.01, unfuse4, width, color=bar_colors_default[3])
rects3 = ax2.bar(x + 0.02, fuse14, width, color=bar_colors_default[2])
rects4 = ax2.bar(x + width+0.03, fuse24, width, color = bar_colors_default[1])
autolabel(rects1, ax2)
autolabel(rects2, ax2)
autolabel(rects3, ax2)
autolabel(rects4, ax2)
ax2.set_xticks(x)
ax2.set_xticklabels(labels)


# Set the x-axis and y-axis labels for ax1
# ax1.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'SimHei', 'size' : 16})
ax1.set_ylabel('加速倍数',fontsize=12,fontdict={ 'size' : 16})
ax1.set_title('8-bit Quantization, Batch Size = 1024',fontsize=12, fontname='SimHei')

# Set the x-axis and y-axis labels for ax2
# ax2.set_xlabel('Batch Size',fontsize=12, fontproperties = 'SimHei')
ax2.set_ylabel('加速倍数',fontsize=12)

# Set the title of ax2
ax2.set_title('4-bit Quantization, Batch Size = 1024',fontsize=12, fontname='SimHei')


x1_label = ax1.get_xticklabels() 
[x1_label_temp.set_fontname('SimHei') for x1_label_temp in x1_label]
y1_label = ax1.get_yticklabels() 
[y1_label_temp.set_fontname('SimHei') for y1_label_temp in y1_label]
 
x1_label = ax2.get_xticklabels() 
[x1_label_temp.set_fontname('SimHei') for x1_label_temp in x1_label]
y1_label = ax2.get_yticklabels() 
[y1_label_temp.set_fontname('SimHei') for y1_label_temp in y1_label]

legend_font = {
    'family': 'SimHei', # 字体
    'style': 'normal',
    'size': 12, # 字号
    'weight': "normal", # 是否加粗，不加粗
}
# Add a legend to ax1


fig.legend(fontsize='small', bbox_to_anchor=(0.51, -0.11), loc='upper center', ncol=9, prop=legend_font)
plt.savefig('figure/break_down.pdf', dpi=800, bbox_inches='tight')

# Show the plot
plt.show()
plt.close()
