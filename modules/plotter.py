import os

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style

from modules.db_handler import fetch_user

#data = fetch_user(id=522087338428596245)

#print(data)


# Bar(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
def plot(data: dict):
    sns.set_style("ticks")
    style.use(['seaborn-deep'])
    sns.color_palette("tab10")

    x = ['D4', 'D6', 'D8', 'D10', 'D12', 'D20']
    y = [data['rolls']['d4'], data['rolls']['d6'], data['rolls']['d8'], data['rolls']['d10'], data['rolls']['d12'],
         data['rolls']['d20']]

    sns.barplot(x=x, y=y)
    #plt.show()
    plt.savefig("bar.png")

