import sys
import networkx as nx
from collections import defaultdict, Counter

sys.setrecursionlimit(10000)


file = "in.txt"
try:
    file = sys.argv[1]
except IndexError:
    pass

inp = open(file).read().strip()
LINES = inp.split("\n")


def dfs(G, vis, u, comp):
    comp.append(u)
    vis.add(u)
    for v in G[u]:
        if v not in vis:
            dfs(G, vis, v, comp)


def solve(G, edges, tot):
    vis = set()
    for ed in edges:
        u, v = ed[0], ed[1]
        if u not in vis:
            comp = []
            dfs(G, vis, u, comp)
            tot.append(comp)
        if v not in vis:
            comp = []
            dfs(G, vis, v, comp)
            tot.append(comp)
        if len(tot) > 2:
            return tot
    return tot


def try_all_combs():
    N = len(edges)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                G = defaultdict(list)
                for en, ed in enumerate(edges):
                    u, v = ed
                    if en not in [i, j, k]:
                        G[u].append(v)
                        G[v].append(u)
                tot = []
                solve(G, edges, tot)
                if len(tot) == 2:
                    print("bad_brute_force:", len(tot[0] * len(tot[1])))
                    return


def min_cut(edges, vertices):
    G = nx.Graph()
    G.add_edges_from(edges, capacity=1.0)
    G.remove_edges_from(nx.minimum_edge_cut(G))
    print("Total connected components after cut:", len([*nx.connected_components(G)]))
    a, b = nx.connected_components(G)
    print(len(a) * len(b))

    # Below would be faster as we know that cut_value is 3, so we can return early
    # for u in vertices:
    #     for v in vertices:
    #         if u != v:
    #             cut_value, partition = nx.minimum_cut(G, u, v)
    #             if cut_value == 3:
    #                 print("ans:", len(partition[0]) * len(partition[1]))
    #                 return

    # Some useful functions
    # nx.connected_components(G)
    # Note: If you wanna use min_cut instead of minimum_edge_cut, you need to assign capacity to edges -> G.add_edges_from(edges, capacity=1.0)


edges = []
vertices = set()
for ln, line in enumerate(LINES):
    u, r = line.split(":")
    r = r.split()
    for v in r:
        edges.append((u, v))
        vertices.add(u)
        vertices.add(v)


print("Total Edges:", len(edges))
print("Total Vertices:", len(vertices))
min_cut(edges, vertices)
# try_all_combs()
