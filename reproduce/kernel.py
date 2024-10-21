# llama7b
# int8
fp16_flops =  [33.79959088508295,67.42531167561981,123.38607794659407,190.44819332346125,212.82780435849497,226.02003919101054,225.25800496334165,213.05664082575,210.3696856008408,207.6002775505503]
EETQ_flops =  [52.00409885363701,84.89347934213211,164.28923501405703,191.36054073168773,203.5905173521888,206.24906930080107,199.63765727186143,201.52005028152217,205.17569015401762,143.57089490084593]
torchint8_flops =  [32.84669441873245,62.720129118354514,115.42896972669675,210.94572053006289,279.9624440644904,299.74777716536715,304.5788073471806,307.26751284933295,306.7631232603059,305.8930848886925]
bnb =  [8.534490901156063,17.556245118861728,35.156637198564695,69.78875182922016,115.99024774188051,144.92268471512253,161.7782761608494,179.63527207573102,189.8376194236695,201.10135669522836]
mixq8_flops =  [35.0744066,70.26772431,136.8634123,252.1464379,336.894144,359.5249354,366.7102629,374.5541667,369.652651,373.494615]

# batch size: 2048 
# 7b int8: 1.80X 
# 512: 1.58X
# int4
fp16_flops =  [33.79959088508295,67.42531167561981,123.38607794659407,190.44819332346125,212.82780435849497,226.02003919101054,225.25800496334165,213.05664082575,210.3696856008408,207.6002775505503]
awq_flops = [71.22402954350136,99.49587836426812,126.08128584213148,141.16954513141894,149.3520694540599,160.2351725418114,157.9527622238686,158.40845785620593,159.15425091588241,160.72268549014808]
quikint4_flops = [33.51153635546554,63.015386244025734,116.71377426250659,199.7604675900021,276.1075634189722,297.4918050855583,311.7958712012581,322.02774390959485,326.46849607481704,330.2114014708563]
int4_flops = [78.74162905882547,155.07656215869193,295.7206120689927,477.620500772646,655.6161260150456,698.6625195132398,720.0521834217107,731.6497229395783,734.5183821288424,741.4797895839661]
mixq4_flops =  [34.515996,75.22913175,135.7437936,254.4094554,360.8281626,415.4663195,452.3033424,482.1029778,499.0232276,526.1998309]

# 7b int4: 2.53X
# 1.70X

# llama13b
# int8
fp16_flops_13 = [34.614084095610586,69.64505735375751,125.77880622016492,210.05127768313557,230.40561896764154,224.2357100003851,205.97335166735593,217.51078859326287,216.61063914857291,216.24582065343023]
EETQ_flops_13 = [55.28131415010235,89.96019167047203,172.78523238498494,198.71939551680344,205.78471261293285,207.8812279895072,196.2278128164527,197.47441852800665,201.28579626830188,140.2933655025706]
torchint8_flops_13 = [36.23442671419104,69.39309858071782,130.57147896801823,236.0948718292515,309.32966362698505,330.4336194357541,333.6491933771986,333.77132441481865,332.4473831348948,332.06428397894945]
bnb_13 = [6.854274120500968,22.14927057295131,44.07015936194556,83.93532196147888,132.67795598542259,164.35074249546355,184.75482314970122,198.0463112960303,206.14657333041686,215.3096618751481]
mixq8_flops_13 = [35.79919406,75.83993278,147.7907048,287.5525367,362.9445274,370.8561256,379.7646831,384.5848464,390.0776875,388.1297579]

# 13b int8: 1.79X
# 1.58X
# int4
fp16_flops_13 =  [34.614084095610586,69.64505735375751,125.77880622016492,210.05127768313557,230.40561896764154,224.2357100003851,205.97335166735593,217.51078859326287,216.61063914857291,216.24582065343023]
awq_flops_13 = [59.219276527923085,85.01967364372665,105.53773084417138,118.55758681667999,125.92146005807226,125.37220760198946,126.15290943065031,127.1960550100121,127.99652533929338,128.77594418667948]
quikint4_flops_13 = [26.393877867966744,71.80715810080672,136.74699765274895,237.6645551636315,318.0715909342167,345.5198546215865,358.416042944908,368.96572778041786,372.4885645146752,375.9010539847398]
int4_flops_13 = [83.23793154426251,157.34934373377962,286.0792993642261,528.7826494455269,708.5770843955337,752.8666704349002,773.7140743107078,785.5286527286825,791.1459199764541,797.901834610358]
mixq4_flops_13 =  [41.7538637,82.50419876,157.1566795,298.1841613,421.5590259,475.1344466,512.5750442,540.8160606,559.1300483,572.6332658]
# 13b int4: 2.65X
# 1.83X

# llama70b
# int8
fp16_flops_70 = [30.97896444491913,66.41180624968473,120.90815928786483,183.14938116073694,233.26311430678055,212.93044927995172,206.73052839156844,220.54390829890173,217.9632928038952,231.87042197030587]
EETQ_flops_70 = [54.78453345273015,84.28389942368466,140.334044832964,199.73827214091784,205.46716594791005,201.86597748693922,214.44093944902622,184.4217583403688,178.4607691457658,202.11078239527987]
torchint8_flops_70 = [37.68060966714834,73.18880384966862,142.53734626244287,264.04180188020104,311.9833326320168,320.1432953933689,401.18644490345275,383.0484591166593,371.33618085521624,395.255580185042]
bnb_70 = [8.183177532187878,29.26040855519975,57.1773811673724,99.42878805058972,159.88046106464537,191.241291573594,207.09288710112858,218.14202671314635,225.8705957731409,233.75712148840256]
mixq8_flops_70 = [36.15972373,77.94997015,153.3430102,303.1271474,343.9333531,347.9471736,448.6939782,429.6174515,413.8229176,443.0965984]

# 70b int8: 1.91X
# 1.47X
# int4
fp16_flops_70 =  [30.97896444491913,66.41180624968473,120.90815928786483,183.14938116073694,233.26311430678055,212.93044927995172,206.73052839156844,220.54390829890173,217.9632928038952,231.87042197030587]
awq_flops_70 = [50.123136219567044,61.596396345687246,71.68933381594215,75.46426897986902,74.85595724338427,75.5020020843029,76.21734517815756,77.40948896908525,76.80703177741067,77.11121805561984]
quikint4_flops_70 = [26.573137667893345,85.57010000877175,162.8097232068248,292.4898170251239,367.47012298660206,387.2499331099759,458.39387149570115,452.01137811428396,449.0689582457772,470.3386837842806]
int4_flops_70 = [78.56855897021117,155.06891208251795,301.7484818261625,574.877170928665,685.7359584042521,711.8642330979947,945.0887880393484,905.2324304980647,880.601322399482,978.0637098060688]
mixq4_flops_70 =  [47.18519199,94.15722892,181.6553862,352.7150406,470.4446198,522.9709596,663.6802144,655.9960328,655.7068586,724.9304643]
# 70b int4: 3.13X
# 2.02X

import matplotlib.pyplot as plt
plt.rcParams['pdf.fonttype'] = 42
ai = [32, 64, 128, 256, 512, 768, 1024, 1280, 1536, 2048]

# Define the bar colors
bar_colors_default= ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#F9DC5C"]

# Set font size
plt.rcParams.update({'font.size': 12})

# Create a figure and set its size
fig1, (ax1, ax3, ax5) = plt.subplots(1, 3, figsize=(10, 3), dpi=800)
fig2, (ax2, ax4, ax6) = plt.subplots(1, 3, figsize=(10, 3), dpi=800)

with open('reproduce_result/result/kernel_8', 'r') as f:
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
        assert len(data) == 15
        fp16_flops = data[0]
        EETQ_flops = data[1]
        torchint8_flops = data[2]
        bnb = data[3]
        mixq8_flops = data[4]
        fp16_flops_13 = data[5]
        EETQ_flops_13 = data[6]
        torchint8_flops_13 = data[7]
        bnb_13 = data[8]
        mixq8_flops_13 = data[9]
        fp16_flops_70 = data[10]
        EETQ_flops_70 = data[11]
        torchint8_flops_70 = data[12]
        bnb_70 = data[13]
        mixq8_flops_70 = data[14]
    except Exception as e:
        print("continue with prepared data!")

with open('reproduce_result/result/kernel_4', 'r') as f:
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
        assert len(data) == 15
        fp16_flops = data[0]
        awq_flops = data[1]
        quikint4_flops = data[2]
        int4_flops = data[3]
        mixq4_flops = data[4]
        fp16_flops_13 = data[5]
        awq_flops_13 = data[6]
        quikint4_flops_13 = data[7]
        int4_flops_13 = data[8]
        mixq4_flops_13 = data[9]
        fp16_flops_70 = data[10]
        awq_flops_70 = data[11]
        quikint4_flops_70 = data[12]
        int4_flops_70 = data[13]
        mixq4_flops_70 = data[14]
    except Exception as e:
        print("continue with prepared data!")

ax1.plot(ai, fp16_flops, label='FP 16', marker='s', color=bar_colors_default[4], linewidth=2,markersize=4)
ax1.plot(ai, EETQ_flops, label='EETQ', marker='^', color=bar_colors_default[1], linewidth=2,markersize=4)
ax1.plot(ai, torchint8_flops, label='SmoothQuant', marker='o', color=bar_colors_default[5], linewidth=2,markersize=4)
ax1.plot(ai, bnb, label='Bitsandbytes', marker='h', color=bar_colors_default[3], linewidth=2,markersize=4)
ax1.plot(ai, mixq8_flops, label='MixQ W8A8O16', marker='D', color=bar_colors_default[2], linewidth=2,markersize=4)

# Plot the second graph on ax2
ax2.plot(ai, fp16_flops, label='FP 16', marker='s', color=bar_colors_default[4], linewidth=2,markersize=4)
ax2.plot(ai, awq_flops, label='AWQ', marker='<', color=bar_colors_default[1], linewidth=2,markersize=4)
ax2.plot(ai, quikint4_flops, label='QUIK', marker='p', color=bar_colors_default[5], linewidth=2,markersize=4)
ax2.plot(ai, int4_flops, label='CUTLASS', marker='>', color=bar_colors_default[0], linewidth=2,markersize=4)
ax2.plot(ai, mixq4_flops, label='MixQ W4A4O16', marker='D', color=bar_colors_default[2], linewidth=2,markersize=4)
# Customize the second graph as needed

# Set the x-axis and y-axis labels for ax1
ax1.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
ax1.set_ylabel('TFLOPs',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})

# Set the title of ax1
ax1.set_title('Llama-7B, 8-bit Quantization',fontsize=12, fontname='Times New Roman')

# Set the x-axis and y-axis labels for ax2
ax2.set_xlabel('Batch Size',fontsize=12, fontproperties = 'Times New Roman')
# ax2.set_ylabel('TFLOPs',fontsize=12, fontproperties = 'Times New Roman')

# Set the title of ax2
ax2.set_title('Llama-7B, 4-bit Quantization',fontsize=12, fontname='Times New Roman')

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.2)
ax1.set_xticks([0, 512, 1024, 2048])
ax1.set_xticklabels([0, 512, 1024, 2048])
ax2.set_xticks([0, 512, 1024, 2048])
ax2.set_xticklabels([0, 512, 1024, 2048])
x1_label = ax1.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax1.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
x1_label = ax2.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax2.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
        
ax1.text(ai[-1]-150, fp16_flops[-1] + 10, "%.2f"%(fp16_flops[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax1.text(ai[-1]-150, EETQ_flops[-1] - 40, "%.2f"%(EETQ_flops[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax1.text(ai[-1]-150, torchint8_flops[-1] - 30, "%.2f"%(torchint8_flops[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax1.text(ai[-1]-150, bnb[-1] - 20, "%.2f"%(bnb[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax1.text(ai[-1]-150, mixq8_flops[-1] -25, "%.2f"%(mixq8_flops[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')


ax2.text(ai[-1]-150, fp16_flops[-1] + 10, "%.2f"%(fp16_flops[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax2.text(ai[-1]-150, awq_flops[-1] - 60, "%.2f"%(awq_flops[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax2.text(ai[-1]-150, quikint4_flops[-1] - 0, "%.2f"%(quikint4_flops[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax2.text(ai[-1]-150, int4_flops[-1] - 60, "%.2f"%(int4_flops[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax2.text(ai[-1]-150, mixq4_flops[-1] + 10, "%.2f"%(mixq4_flops[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')

ax3.plot(ai, fp16_flops_13, marker='s', color=bar_colors_default[4], linewidth=2,markersize=4)
ax3.plot(ai, EETQ_flops_13,  marker='^', color=bar_colors_default[1], linewidth=2,markersize=4)
ax3.plot(ai, torchint8_flops_13, marker='o', color=bar_colors_default[5], linewidth=2,markersize=4)
ax3.plot(ai, bnb_13,  marker='h', color=bar_colors_default[3], linewidth=2,markersize=4)
ax3.plot(ai, mixq8_flops_13,  marker='D', color=bar_colors_default[2], linewidth=2,markersize=4)

# Plot the second graph on ax4
ax4.plot(ai, fp16_flops_13, marker='s', color=bar_colors_default[4], linewidth=2,markersize=4)
ax4.plot(ai, awq_flops_13, marker='<', color=bar_colors_default[1], linewidth=2,markersize=4)
ax4.plot(ai, quikint4_flops_13,  marker='p', color=bar_colors_default[5], linewidth=2,markersize=4)
ax4.plot(ai, int4_flops_13,  marker='>', color=bar_colors_default[0], linewidth=2,markersize=4)
ax4.plot(ai, mixq4_flops_13, marker='D', color=bar_colors_default[2], linewidth=2,markersize=4)
# Customize the second graph as needed

legend_font = {
    'family': 'Times New Roman', # 字体
    'style': 'normal',
    'size': 12, # 字号
    'weight': "normal", # 是否加粗，不加粗
}
# Add a legend to ax1

# Set the x-axis and y-axis labels for ax1
ax3.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})

# Set the title of ax1
ax3.set_title('Llama-13B, 8-bit Quantization',fontsize=12, fontname='Times New Roman')

# Set the x-axis and y-axis labels for ax2
ax4.set_xlabel('Batch Size',fontsize=12, fontproperties = 'Times New Roman')

# Set the title of ax2
ax4.set_title('Llama-13B, 4-bit Quantization',fontsize=12, fontname='Times New Roman')

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.2)

ax3.set_xticks([0, 512, 1024, 2048])
ax3.set_xticklabels([0, 512, 1024, 2048])
ax4.set_xticks([0, 512, 1024, 2048])
ax4.set_xticklabels([0, 512, 1024, 2048])
x1_label = ax3.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax3.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
x1_label = ax4.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax4.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
        
ax3.text(ai[-1]-150, fp16_flops_13[-1] + 10, "%.2f"%(fp16_flops_13[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax3.text(ai[-1]-150, EETQ_flops_13[-1] - 40, "%.2f"%(EETQ_flops_13[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax3.text(ai[-1]-150, torchint8_flops_13[-1] - 40, "%.2f"%(torchint8_flops_13[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax3.text(ai[-1]-150, bnb_13[-1] - 25, "%.2f"%(bnb_13[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax3.text(ai[-1]-150, mixq8_flops_13[-1] + 5, "%.2f"%(mixq8_flops_13[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')

ax4.text(ai[-1]-150, fp16_flops_13[-1] - 10, "%.2f"%(fp16_flops_13[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax4.text(ai[-1]-150, awq_flops_13[-1] + 10, "%.2f"%(awq_flops_13[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax4.text(ai[-1]-150, quikint4_flops_13[-1] - 0, "%.2f"%(quikint4_flops_13[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax4.text(ai[-1]-150, int4_flops_13[-1] -10, "%.2f"%(int4_flops_13[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax4.text(ai[-1]-150, mixq4_flops_13[-1] + 10, "%.2f"%(mixq4_flops_13[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')

ax5.plot(ai, fp16_flops_70,  marker='s', color=bar_colors_default[4], linewidth=2,markersize=4)
ax5.plot(ai, EETQ_flops_70, marker='^', color=bar_colors_default[1], linewidth=2,markersize=4)
ax5.plot(ai, torchint8_flops_70,  marker='o', color=bar_colors_default[5], linewidth=2,markersize=4)
ax5.plot(ai, bnb_70,  marker='h', color=bar_colors_default[3], linewidth=2,markersize=4)
ax5.plot(ai, mixq8_flops_70, marker='D', color=bar_colors_default[2], linewidth=2,markersize=4)

# Plot the second graph on ax4
ax6.plot(ai, fp16_flops_70, marker='s', color=bar_colors_default[4], linewidth=2,markersize=4)
ax6.plot(ai, awq_flops_70,  marker='<', color=bar_colors_default[1], linewidth=2,markersize=4)
ax6.plot(ai, quikint4_flops_70,  marker='p', color=bar_colors_default[5], linewidth=2,markersize=4)
ax6.plot(ai, int4_flops_70, marker='>', color=bar_colors_default[0], linewidth=2,markersize=4)
ax6.plot(ai, mixq4_flops_70, marker='D', color=bar_colors_default[2], linewidth=2,markersize=4)
# Customize the second graph as needed

legend_font = {
    'family': 'Times New Roman', # 字体
    'style': 'normal',
    'size': 12, # 字号
    'weight': "normal", # 是否加粗，不加粗
}
# Add a legend to ax1

# Set the x-axis and y-axis labels for ax1
ax5.set_xlabel('Batch Size',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})
# ax5.set_ylabel('TFLOPs',fontsize=12,fontdict={'family' : 'Times New Roman', 'size' : 16})

# Set the title of ax1
ax5.set_title('Llama-70B, 8-bit Quantization',fontsize=12, fontname='Times New Roman')

# Set the x-axis and y-axis labels for ax2
ax6.set_xlabel('Batch Size',fontsize=12, fontproperties = 'Times New Roman')
# ax6.set_ylabel('TFLOPs',fontsize=12, fontproperties = 'Times New Roman')

# Set the title of ax2
ax6.set_title('Llama-70B, 4-bit Quantization',fontsize=12, fontname='Times New Roman')

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.2)

ax5.set_xticks([0, 512, 1024, 2048])
ax5.set_xticklabels([0, 512, 1024, 2048])
ax6.set_xticks([0, 512, 1024, 2048])
ax6.set_xticklabels([0, 512, 1024, 2048])
x1_label = ax5.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax5.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
x1_label = ax6.get_xticklabels() 
[x1_label_temp.set_fontname('Times New Roman') for x1_label_temp in x1_label]
y1_label = ax6.get_yticklabels() 
[y1_label_temp.set_fontname('Times New Roman') for y1_label_temp in y1_label]
 
        
ax5.text(ai[-1]-150, fp16_flops_70[-1] - 35, "%.2f"%(fp16_flops_70[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax5.text(ai[-1]-150, EETQ_flops_70[-1] - 40, "%.2f"%(EETQ_flops_70[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax5.text(ai[-1]-150, torchint8_flops_70[-1] - 0, "%.2f"%(torchint8_flops_70[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax5.text(ai[-1]-150, bnb_70[-1] + 0, "%.2f"%(bnb_70[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax5.text(ai[-1]-150, mixq8_flops_70[-1] + 8, "%.2f"%(mixq8_flops_70[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')


ax6.text(ai[-1]-150, fp16_flops_70[-1] - 0, "%.2f"%(fp16_flops_70[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax6.text(ai[-1]-150, awq_flops_70[-1] + 10, "%.2f"%(awq_flops_70[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax6.text(ai[-1]-150, quikint4_flops_70[-1] - 0, "%.2f"%(quikint4_flops_70[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax6.text(ai[-1]-150, int4_flops_70[-1] - 0, "%.2f"%(int4_flops_70[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
ax6.text(ai[-1]-150, mixq4_flops_70[-1] + 10, "%.2f"%(mixq4_flops_70[-1]), ha='center', va='bottom', fontsize=10, color="k",fontname='Times New Roman')
fig1.legend(fontsize='small', bbox_to_anchor=(0.51, -0.05), loc='upper center', ncol=3, prop=legend_font)
fig2.legend(fontsize='small', bbox_to_anchor=(0.51, -0.05), loc='upper center', ncol=3, prop=legend_font)
fig1.savefig('figure/tflops_int8_overall.pdf', dpi=800, bbox_inches='tight')
fig2.savefig('figure/tflops_int4_overall.pdf', dpi=800, bbox_inches='tight')

# Show the plot
plt.show()
plt.close()