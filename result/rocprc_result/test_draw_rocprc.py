import pandas as pd
import matplotlib.pyplot as plt

df_sweet = pd.read_csv('sweet.csv')
df_bitter = pd.read_csv('bitter.csv')
df_umami = pd.read_csv('umami.csv')


plt.figure(figsize=(4,2),dpi=300)

name = df_sweet.loc[:,'File Name']

# 'AUROC' 'AUPRC'
val = 'AUPRC'

sweet_roc = df_sweet.loc[:,val]
bitter_roc = df_bitter.loc[:,val]
umami_roc = df_umami.loc[:,val]

width = 0.3

plt.bar([i for i in range(len(name))],sweet_roc,width=width,label='sweet',color='#EBC655')
plt.bar([i + width for i in range(len(name))],bitter_roc,width=width,label='bitter',color='#5D509F')
plt.bar([i + 2*width  for i in range(len(name))],umami_roc,width=width,label='umami',color='#71C7EA')

plt.xticks([x + width for x in range(len(name))],name,rotation=45, fontsize=4)

plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0],fontsize=5)

for a,b in zip([i for i in range(len(name))],sweet_roc):   #柱子上的数字显示
    plt.text(a,b,'%.3f'%b,ha='center',va='bottom',fontsize=2.5);

for a,b in zip([i+width for i in range(len(name))],bitter_roc):   #柱子上的数字显示
    plt.text(a,b,'%.3f'%b,ha='center',va='bottom',fontsize=2.5);

for a,b in zip([i+ 2*width for i in range(len(name))],umami_roc):   #柱子上的数字显示
    plt.text(a,b,'%.3f'%b,ha='center',va='bottom',fontsize=2.5);

plt.legend(bbox_to_anchor=(0.98,1),loc='upper left',borderaxespad=0,fontsize=3,)
plt.grid(True,axis='y',linestyle='-',color='grey',alpha=0.6)
plt.tick_params(pad=0.0,bottom=False, top=False,left=False)

plt.gca().spines['bottom'].set_color('grey')
plt.gca().spines['left'].set_color('grey')
plt.gca().spines['top'].set_color('white')
plt.gca().spines['right'].set_color('white')

plt.show()