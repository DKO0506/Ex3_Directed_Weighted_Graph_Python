from random import randint

from GraphInterface import GraphInterface


# noinspection PyArgumentList,PyTypeChecker
class DiGraph(GraphInterface):
    def __init__(self):
        self.nodes = {}
        self.edgesOut = {int: dict}
        self.edgesIn = {int: dict}
        self.mc = 0
        self.eSize = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.eSize

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes and id2 in self.nodes:
            if id2 not in self.edgesOut[id1] and id1 not in self.edgesIn[id2] and weight > 0:
                self.edgesOut[id1].update({id2: weight})
                self.edgesIn[id2].update({id1: weight})
                self.eSize += 1
                self.mc += 1
                return True

            return False

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if pos is None:
            pos = (randint(1, 100), randint(1, 100))
        if node_id not in self.nodes:
            self.nodes.update({node_id: pos})
            self.edgesOut.update({node_id: {}})
            self.edgesIn.update({node_id: {}})
            self.mc += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            for i in (self.edgesIn.get(node_id).keys()):
                self.edgesOut.get(i).pop(node_id)
                self.eSize -= 1

            for i in (self.edgesOut.get(node_id).keys()):
                self.edgesIn.get(i).pop(node_id)
                self.eSize -= 1

            self.edgesOut.pop(node_id)
            self.edgesIn.pop(node_id)
            self.nodes.pop(node_id)
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id2 in self.edgesOut[node_id1] and node_id1 in self.edgesIn[node_id2]:
            self.edgesOut.get(node_id1).pop(node_id2)
            self.edgesIn.get(node_id2).pop(node_id1)
            self.eSize -= 1
            return True
        else:
            return False

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.edgesIn[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edgesOut[id1]

    def get_all_v(self) -> dict:
        return self.nodes

    def __repr__(self):
        answer = "|V| = {} , |E| = {} , ModeCounter = {}\n\n".format(self.v_size(), self.eSize, self.mc)

        for v in self.nodes:
            answer += str(v) + ": " + "\t"
            for u in self.edgesOut.get(v).keys():
                answer += "[" + str(u) + "]" + ", "
            answer += "\n\n"
        return answer
