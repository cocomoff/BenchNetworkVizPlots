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
        Gd = ox.graph_from_point(p, network_type="drive", distance=d)
        Gd = Gd.to_undirected()
        print(d, Gd.number_of_nodes(), Gd.number_of_edges())
        fn = "{}_d{}.pickle".format(basename, d)
        with open(fn, "wb") as f:
            pickle.dump(Gd, f)
