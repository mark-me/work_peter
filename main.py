import numpy as np
import pandas as pd
import igraph as ig
import networkx as nx
from pyvis.network import Network

FILE_INFRA = 'PP environments flow.csv'


def main():
    df_flow = pd.read_csv(FILE_INFRA, sep=';')
    network = nx.from_pandas_edgelist(df_flow, source = 'Source', target = 'Target', create_using=nx.DiGraph())
    visnet = Network(height = "1080", width = "100%", bgcolor='#222222', font_color='white')
    visnet.from_nx(network, directed=True)
    visnet.show('graph_community.html')


if __name__ == "__main__":
    main()