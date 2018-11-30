import sys, os

import tqdm
import fire
import numpy as np
import pandas

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# import seaborn as sns
import pymongo
import networkx as nx
import imageio

COMPUTED = os.environ.get('COMPUTED')
OUTPUT = os.environ.get('MEMO_DIR')
os.environ['CUDA_VISIBLE_DEVICES'] = '1'


def run():
    conn = pymongo.MongoClient(port=27017)
    coll = conn['grass']['scores']
    recs = coll.find({'exp_key': 'test2'})
    # nodes = []
    # edges = []
    graphs = []
    for rec in recs:
        H = nx.DiGraph(score=rec['scores_dict']['perf'])
        # tmp_nodes = []
        # tmp_edges = []
        for key, value in rec['pars'].items():
            n = int(key.split('_')[0][1:])
            prop = key.split('_')[-1]
            try:
                e2 = int(prop)
            except:
                if n not in H:
                    H.add_node(n, {prop: value})
                else:
                    H[n][prop] = value
                # tmp_nodes.append((n, {prop: value}))
            else:
                if value == 1:
                    # tmp_edges.append((n, e2))
                    H.add_edge(n, e2)
        graphs.append(H)


def get_data(exp='test3'):
    data = np.load('{}.pkl.npy'.format(exp))
    graphs = []
    fig = plt.figure(dpi=150)
    ax = fig.add_subplot(111)
    for recno, rec in enumerate(tqdm.tqdm(data)):
        # import ipdb; ipdb.set_trace()
        if rec['scores_dict'] is not None:
            H = nx.DiGraph(score=rec['scores_dict']['perf'])
            # tmp_nodes = []
            # tmp_edges = []
            top = rec['pars']['num_layers'] - 1
            for key, value in rec['pars'].items():
                if key != 'num_layers':
                    n = key.split('_')[0][1:]
                    if int(n) <= top:
                        prop = key.split('_')[1]
                        if prop in ['inputs', 'state'] or prop.isdigit():
                            if value:
                                H.add_edge(prop,n)
                        else:
                            if n not in H:
                                H.add_node(n, {prop: value})
                            else:
                                H.node[n][prop] = value


            # graphs.append(H)

            # top = max([int(n) for n in H if n not in ['inputs', 'state']])
            H = nx.relabel_nodes(H, {str(top): 'output',
                             'inputs': 'input',
                             str(top-1): 'new state'})

            pos = {}  #nx.spring_layout(H)
            pos['input'] = np.array([0,0])
            pos['state'] = np.array([1,0])
            y = np.linspace(0, 1, top + 1)[1:-1]
            # import ipdb; ipdb.set_trace()
            for n in range(top - 1):
                pos[str(n)] = (np.random.rand(), y[n])
            pos['output'] = np.array([0,1])
            pos['new state'] = np.array([1,1])

            colors = []
            for n, attr in H.nodes(data=True):
                if 'convolution' in attr:
                    if attr['convolution'] == 'identity':
                        colors.append('#B72467')
                    else:
                        colors.append('#524FA1')  # blue
                else:
                    colors.append('#F68B1F')  # orange

            # import ipdb; ipdb.set_trace()
            ax.clear()
            ax.set_axis_off()
            nx.draw_networkx(H, pos=pos,
                             with_labels=True,
                             node_color=colors,
                             node_shape='s',
                             edge_color='#777777')

            ax.bar(1.3, rec['scores_dict']['perf'], .1, color='#CC0000')
            ax.text(1.3, -.05, 'performance', ha='center')
            # import ipdb; ipdb.set_trace()
            plt.tight_layout()
            fig.canvas.draw()
            data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
            data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
            # plt.imshow(data)
            # plt.show()
            # import ipdb; ipdb.set_trace()
            graphs.append(data)
        if recno > 75: break

    # import ipdb; ipdb.set_trace()
    imageio.mimwrite('../img/search.gif', graphs, fps=15)


if __name__ == '__main__':
    fire.Fire()