from random import randint

from typing import List
import json

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: GraphInterface = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as input:
                grJson = json.load(input)
                input.close()
                V = grJson['Nodes']
                E = grJson['Edges']
                self.graph = DiGraph()
                for i in V:
                    try:
                        p = (
                            float(i['pos'].split(',')[0]), float(i['pos'].split(',')[1]), float(i['pos'].split(',')[2]))
                        self.graph.add_node(i['id'], p)
                    except KeyError:
                        self.graph.add_node(i['id'])
                    except AttributeError:
                        self.graph.add_node(i['id'])

                for j in E:
                    self.graph.add_edge(j['src'], j['dest'], j['w'])

                return True
        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            V = []
            E = []
            Graph = {"Edges": E, "Nodes": V}
            for i in self.graph.get_all_v():
                d = {'pos': self.graph.get_all_v()[i], 'id': i}
                V.append(d)
                for j in self.graph.all_in_edges_of_node(i).keys():
                    t = {'src': j, 'w': self.graph.all_in_edges_of_node(i).get(j), 'dest': i}
                    E.append(t)

            graphj = json.dumps(Graph)
            with open(file_name, 'w') as out:
                out.write(graphj)
                out.close()
                return True

        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        if id1 not in self.graph.get_all_v() or id2 not in self.graph.get_all_v():
            return -1, path

        distances = {int: float}
        q = []
        distances.update({id1: 0})
        q.append(id1)

        while len(q) != 0:
            curr = q.pop(0)
            for i in self.graph.all_out_edges_of_node(curr).keys():
                if not distances.__contains__(i):
                    distances.update({i: self.graph.all_out_edges_of_node(curr).get(i) + distances.get(curr)})
                    q.append(i)
                elif distances[i] > self.graph.all_out_edges_of_node(curr).get(i) + distances.get(curr):
                    distances.update({i: self.graph.all_out_edges_of_node(curr).get(i) + distances.get(curr)})
                    q.append(i)
        if id1 is id2:
            path.append(id1)
            return 0, path

        if id2 not in distances:
            return -1, None
        tmp = id2
        path.append(tmp)
        while distances[tmp] != 0:
            for i in self.graph.all_in_edges_of_node(tmp).keys():
                if distances[i] + self.graph.all_out_edges_of_node(i)[tmp] == distances[tmp]:
                    path.insert(0, i)
                    tmp = i
                    break
        return distances[id2], path

    def connected_component(self, id1: int) -> list:
        l = self.connected_components()
        for i in range(len(l)):
            if l[i].__contains__(id1):
                return l[i]

    def connected_components(self) -> List[list]:
        x = 0
        q = []
        sccList = []
        preorder = {}
        isFound = {}
        lowlink = {}

        for src in self.graph.get_all_v():
            if src not in isFound:
                queue = [src]
                while queue:
                    v = queue[-1]
                    if v not in preorder:
                        x += 1
                        preorder[v] = x
                    isFinished = True
                    e = self.graph.all_out_edges_of_node(v)
                    for w in e:
                        if w not in preorder:
                            queue.append(w)
                            isFinished = False
                            break
                    if isFinished:
                        lowlink[v] = preorder[v]
                        for w in e:
                            if w not in isFound:
                                if preorder[w] > preorder[v]:
                                    lowlink[v] = min([lowlink[v], lowlink[w]])
                                else:
                                    lowlink[v] = min([lowlink[v], preorder[w]])
                        queue.pop()
                        if lowlink[v] == preorder[v]:
                            isFound[v] = True
                            scc = [v]
                            while q and preorder[q[-1]] > preorder[v]:
                                comp = q.pop()
                                isFound[comp] = True
                                scc.append(comp)
                            sccList.append(scc)
                        else:
                            q.append(v)
        return sccList

    def plot_graph(self) -> None:
        for src in self.graph.get_all_v():
            xs = self.graph.get_all_v()[src][0]
            ys = self.graph.get_all_v()[src][1]
            plt.plot(xs, ys, 'o')
            plt.text(xs, ys, src)
            for dest in self.graph.all_out_edges_of_node(src):
                xd = self.graph.get_all_v()[dest][0]
                yd = self.graph.get_all_v()[dest][1]
                plt.plot([xs, xd], [ys, yd])

        plt.title('My Graph')
        plt.xlabel('X - Axis')
        plt.ylabel('Y - Axis')
        plt.show()
