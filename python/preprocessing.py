# -*- coding: utf-8 -*-

import pickle
import osmnx as ox
import numpy as np
import networkx as nx

if __name__ == '__main__':
    np.random.seed(20191224)

    # tokyo station
    lat, lot = 35.681236, 139.767125
    p = (lat, lot)
    basename = "tokyo_station"
    lD = list(range(500, 3001, 250))

    for d in lD:
        fn = "{}_d{}.pickle".format(basename, d)
        G = pickle.load(open(fn, "rb"))

        # simplify IDs
        node2id = {}
        for n in G.nodes:
            node2id[n] = len(node2id)

        with open("{}_d{}_nodes.csv".format(basename, d), "w") as f:
            for n, data in G.nodes(data=True):
                f.write("{},{},{}\n".format(node2id[n], data['x'], data['y']))

        with open("{}_d{}_edges.csv".format(basename, d), "w") as f:
            for (u, v, data) in G.edges(data=True):
                n1, n2, d12 = node2id[u], node2id[v], data['length']
                f.write("{},{},{}\n".format(n1, n2, round(d12, 3)))
