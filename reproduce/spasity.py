import matplotlib.pyplot as plt

ai = [32, 64, 128, 256, 512, 768, 1024, 1280, 1536, 2048]
# Define the bar colors
bar_colors_default= ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#F9DC5C"]

# Set font size
plt.rcParams.update({'font.size': 12})

# Create a figure and set its size
fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(10, 3), dpi=800)

# llama13b
# int8
l1_flops_13_down = [27.941880872636325,57.159546516092966,113.49732091124291,219.90195471721393,240.37895756312827,312.25007918709565,302.69377673989584,368.64359931690063,361.8579857694101,402.81341632102345]
l20_flops_13_down = [29.49020162018932,58.28202904490611,114.92351661298223,223.61918969368742,239.78965068921886,311.35064496538814,298.63398930920164,362.0174490205772,355.45216633895205,389.044201134592]
l39_flops_13_down = [29.071853713756127,57.55645387988769,110.88667787973625,210.82863954643096,240.0751158576679,304.8339895973291,298.2167013970677,359.09510704932956,349.714222722784,390.76260267670864]

# int4
l1_4_flops_13_down = [49.87248858837347,95.04348045747814,186.40545683735235,360.68686648612083,399.72144959875476,484.1836070493739,476.9400395250404,580.816430150912,579.7089718891923,658.5954505686159]
l20_4_flops_13_down = [48.97154524069176,95.2683545792005,184.74284282108144,355.9718282522583,388.43890827625455,487.66032552075325,473.32230813241966,566.4795827981004,566.0576860067816,641.6312275284]
l39_4_flops_13_down = [48.98849234487298,94.90051511547445,172.96363135792816,316.13702010384765,385.3955955918757,474.4095638454379,472.79524891569343,566.4760395872476,567.1923128560423,641.2486091838211]

with open('reproduce_result/result/spasity', 'r') as f:
    lines = f.readlines()
    data = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        items = line.split(',')
        test_name = items[0]
        values = [float(item) for item in items[1:] if item]
        data.append(values)
    try:
        assert len(data) == 6
        l1_flops_13_down = data[0]
        l20_flops_13_down = data[1]
        l39_flops_13_down = data[2]
        l1_4_flops_13_down = data[3]
        l20_4_flops_13_down = data[4]
        l39_4_flops_13_down = data[5]
    except Exception as e:
        print("continue with prepared data!")

ax3.plot(ai, l1_flops_13_down,  marker='^', label = 'down_proj layer 0', color=bar_colors_default[0], linewidth=2,markersize=4)
ax3.plot(ai, l20_flops_13_down,  marker='v', label = 'down_proj layer 20', color=bar_colors_default[1], linewidth=2,markersize=4)
ax3.plot(ai, l39_flops_13_down,  marker='D', label = 'down_proj layer 39', color=bar_colors_default[2], linewidth=2,markersize=4)

ax4.plot(ai, l1_4_flops_13_down,  marker='^', color=bar_colors_default[0], linewidth=2,markersize=4)
ax4.plot(ai, l20_4_flops_13_down,  marker='v', color=bar_colors_default[1], linewidth=2,markersize=4)
ax4.plot(ai, l39_4_flops_13_down,  marker='D', color=bar_colors_default[2], linewidth=2,markersize=4)

legend_font = {
    'family': 'Times New Roman', # 字体
    'style': 'normal',
    'size': 12, # 字号
    'weight': "normal", # 是否加粗，不加粗
}

# Set the x-axis and y-axis labels for ax1
ax3.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})

# Set the title of ax1
ax3.set_title('Llama-13B, MixQ (W8A8O16)',fontsize=12, fontname='Times New Roman')

# Set the x-axis and y-axis labels for ax2
ax4.set_xlabel('Batch Size',fontsize=12, fontproperties = 'Times New Roman')
# ax4.set_ylabel('TFLOPs',fontsize=12, fontproperties = 'Times New Roman')

# Set the title of ax2
ax4.set_title('Llama-13B, MixQ (W4A4O16)',fontsize=12, fontname='Times New Roman')

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.2)
xxx = [0, 512, 1024, 2048]
ax3.set_xticks(xxx)
ax3.set_xticklabels(xxx)
ax4.set_xticks(xxx)
ax4.set_xticklabels(xxx)

x1_label = ax3.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax3.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
x1_label = ax4.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax4.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
legend_font = {
    'family': 'Times New Roman', # 字体
    'style': 'normal',
    'size': 12, # 字号
    'weight': "normal", # 是否加粗，不加粗
}
# Add a legend to ax1

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.2)

fig2.legend(fontsize='small', bbox_to_anchor=(0.51, -0.05), loc='upper center', ncol=4, prop=legend_font)
fig2.savefig('figure/down_13B.pdf', dpi=800, bbox_inches='tight')

# Show the plot
plt.show()
plt.close()