import numpy as np
import pandas as pd
import igraph as ig
import networkx as nx
from pyvis.network import Network

FILE_INFRA = 'PP environments flow.csv'


def main():
    print("hello")
    df_flow = pd.read_csv(FILE_INFRA, sep=';')
    network = nx.from_pandas_edgelist(df_flow, source = 'Source', target = 'Target')
    visnet = Network(height = "100%", width = "100%", bgcolor='#222222', font_color='white')
    visnet.from_nx(network)
    visnet.show('graph_community.html')


if __name__ == "__main__":
    main()