# latency
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator, LogFormatter

# Define the bar colors
bar_colors_default= ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#F9DC5C"]

# Set font size
plt.rcParams.update({'font.size': 12})

# Create a figure and set its size
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3), dpi=800)

# llama-7b
ai = ['32', '64', '128', '256', '512']
bnb = [142.65122264623642, 141.70000702142715, 141.91774278879166, 147.552952170372, 161.74716502428055]
fp16 = [21.390482783317566, 21.109476685523987, 26.986397802829742, 39.13969546556473, 69.53547894954681]
mixq8 = [21.204158663749695, 21.685630083084106, 26.923902332782745, 29.14535254240036, 47.19104617834091]
mixq4 = [25.466181337833405, 25.455959141254425, 25.772616267204285, 28.453469276428223, 44.490471482276917]
awq = [13.806268572807312, 22.203445434570312, 39.96925801038742, 75.26524364948273, 145.86584270000458]
quik = [34.13808345794678, 37.72461414337158, 35.460710525512695, 36.52536869049072, 57.08885192871094]
tolerate = [100, 100, 100, 100, 100]
# bi = ['0','32', '64', '128', '256', '512','1024']

ax1.plot(ai, fp16, label='FP 16', marker='s', color=bar_colors_default[4], linewidth=2.5,markersize=4)
ax1.plot(ai, bnb, label='Bitsandbytes', marker='^', color=bar_colors_default[1], linewidth=2.5,markersize=4)
ax1.plot(ai, awq, label='AWQ', marker='x', color=bar_colors_default[3], linewidth=2.5,markersize=4)
ax1.plot(ai, quik, label='QUIK', marker='<', color=bar_colors_default[2], linewidth=2.5,markersize=4)
ax1.plot(ai, tolerate, label='Tolerance', color='red', linewidth=2.5,markersize=4, linestyle='dashed')
ax1.plot(ai, mixq8, label='MixQ (W8A8O16)', marker='o', color=bar_colors_default[5], linewidth=2.5,markersize=4)
ax1.plot(ai, mixq4, label='MixQ (W4A4O16)', marker='v', color=bar_colors_default[0], linewidth=2.5,markersize=4)
ax1.set_yscale('log')

# ax2: llama13b
bnb_13 = [176.095150411129, 167.4976497888565, 172.25614190101624, 181.8150132894516, 201.14820450544357]
fp16_13 = [30.41689097881317, 34.61074084043503, 43.0297926068306, 62.418319284915924, 121.56081944704056]
mixq4_13 = [32.52644091844559, 32.091282308101654, 32.49236196279526, 43.626464903354645, 69.97773796319962]
mixq8_13 = [28.723537921905518, 31.038537621498108, 35.39577126502991, 46.916693449020386, 76.8558606505394]
awq_13 = [24.39606934785843, 40.25109112262726, 73.28598946332932, 139.71683382987976, 271.97592705488205]
quik_13 = [43.000221252441406, 42.47903823852539, 42.62816905975342, 53.888797760009766, 86.6461992263794]

ax2.plot(ai, fp16_13, marker='s', color=bar_colors_default[4], linewidth=2.5,markersize=4)
ax2.plot(ai, bnb_13, marker='^', color=bar_colors_default[1], linewidth=2.5,markersize=4)
ax2.plot(ai, tolerate, color='red', linewidth=2.5,markersize=4, linestyle='dashed')
ax2.plot(ai, awq_13, marker='x', color=bar_colors_default[3], linewidth=2.5,markersize=4)
ax2.plot(ai, quik_13, marker='<', color=bar_colors_default[2], linewidth=2.5,markersize=4)
ax2.plot(ai, mixq8_13, marker='o', color=bar_colors_default[5], linewidth=2.5,markersize=4)
ax2.plot(ai, mixq4_13, marker='v', color=bar_colors_default[0], linewidth=2.5,markersize=4)
ax2.set_yscale('log')


# Set the x-axis and y-axis labels for ax1
ax1.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_ylabel('time/ms (log scale)',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_title('Latency of Inference LLaMA-7B',fontsize=12, fontname='Times New Roman')

# Set the x-axis and y-axis labels for ax2
ax2.set_xlabel('Batch Size',fontsize=12, fontproperties = 'Times New Roman')
ax2.set_ylabel('time/ms (log scale)',fontsize=12, fontproperties = 'Times New Roman')

# Set the title of ax2
ax2.set_title('Latency of Inference LLaMA-13B',fontsize=12, fontname='Times New Roman')

# Adjust the spacing between subplots
# plt.subplots_adjust(wspace=0.2)

x1_label = ax1.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]

ax1.set_yticks([5, 20, 30, 50, 100, 150])
ax1.set_yticklabels(['5','20', '30', '50', '100', '150'])
y1_label = ax1.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]

ax2.set_yticks([25, 40, 50, 80, 100, 160, 200])
ax2.set_yticklabels(['25', '40', '50', '80', '100', '160', '200'])
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

fig.legend(fontsize='small', bbox_to_anchor=(0.51, -0.05), loc='upper center', ncol=4, prop=legend_font)
plt.savefig('figure/latency.pdf', dpi=800, bbox_inches='tight')

# Show the plot
plt.show()
plt.close()
