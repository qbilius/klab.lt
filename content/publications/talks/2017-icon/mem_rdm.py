import os
import pandas
import matplotlib.pyplot as plt
import streams.utils


def plot_mem(model_time=19):
    path = os.path.join('/braintree/home/qbilius/dropbox/memo', 'store', '0148_2017-06-26_10-20-53', 'val.csv')
    val = pandas.read_csv(path, index_col=0)
    sel = (val.model_time == model_time) & (val.kind == 'corr')
    val = val[sel]
    val = val.rename(columns={'value': 'Pearson r'})
    streams.utils.timeplot(data=val, x='memory_decay',
                           y='Pearson r', hue='time')
    plt.savefig('memory_decay_rdm_{}.png'.format(model_time), format='png')
    plt.show()


plot_mem()