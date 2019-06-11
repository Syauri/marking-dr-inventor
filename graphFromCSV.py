import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize


powell = pd.read_csv("A Powell.csv")

relations = powell[powell['tag'].str.startswith("R")]
relations['component'] = relations['component'].str.replace("Arg1:", "")
relations['component'] = relations['component'].str.replace("Arg2:", "")
relations = relations['component'].iloc[:5]

fg = nx.DiGraph()


for relation in relations:
    tokens = nltk.word_tokenize(relation)
    if not fg.has_edge(tokens[1], tokens[2]):
        fg.add_edges_from([(tokens[1], tokens[2])], labels=tokens[0])


nx.draw(fg, pos=nx.spring_layout(fg), with_labels=True)
# edge_labels=nx.draw_networkx_edge_labels(fg,pos=nx.spring_layout(fg))
plt.show()

# pos = nx.draw_spring(fg)
# nx.draw(fg, pos, with_labels=True)
# nx.draw_networkx_edge_labels(fg, pos)
# plt.show()

# fg.add_edges_from([("T4", "T5")], label = 'supports')
# pos = nx.spring_layout(fg)
# nx.draw(fg, pos, with_labels=True)
## edge_label ="supports"
# nx.draw_networkx_edge_labels(fg, pos)
# plt.show()





