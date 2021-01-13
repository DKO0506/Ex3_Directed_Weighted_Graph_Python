from unittest import TestCase
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def setUp(self) -> None:
        self.g = DiGraph()
        for i in range(6):
            self.g.add_node(i)
        self.g.add_edge(1, 2, 1)
        self.g.add_edge(1, 3, 2.9)
        self.g.add_edge(1, 4, 3.6)
        self.g.add_edge(2, 1, 1)
        self.g.add_edge(2, 0, 1.5)
        self.g.add_edge(3, 1, 1)
        self.g.add_edge(4, 0, 4.8)
        self.g.add_edge(4, 2, 1)
        self.g.add_edge(2, 4, 0.2)
        self.g.add_edge(0, 5, 2.5)
        self.g_algo = GraphAlgo(self.g)

    def test_get_graph(self):
        self.assertEqual(self.g_algo.graph, self.g_algo.get_graph())

    def test_save_load_from_json(self):
        g_algo2 = GraphAlgo(self.g_algo.get_graph())
        g_algo2.save_to_json("C:/users/omer2/Desktop/test")
        g_algo2.load_from_json("C:/users/omer2/Desktop/test")
        self.assertEqual(self.g_algo.graph.get_all_v().keys(), g_algo2.get_graph().get_all_v().keys())
        for v in self.g_algo.graph.get_all_v():
            self.assertEqual(self.g_algo.graph.all_out_edges_of_node(v), g_algo2.get_graph().all_out_edges_of_node(v))
            self.assertEqual(self.g_algo.graph.all_in_edges_of_node(v), g_algo2.get_graph().all_in_edges_of_node(v))

        g_algo2.graph.remove_node(1)
        g_algo2.save_to_json("C:/users/omer2/Desktop/test1")
        g_algo2.load_from_json("C:/users/omer2/Desktop/test1")
        self.assertNotEqual(self.g_algo.graph.get_all_v(), g_algo2.get_graph().get_all_v())
        g_algo2.load_from_json("C:/users/omer2/Desktop/test")
        self.assertEqual(self.g_algo.graph.get_all_v().keys(), g_algo2.get_graph().get_all_v().keys())


    def test_shortest_path(self):
        self.assertEqual((1, [1, 2]), self.g_algo.shortest_path(1, 2))
        self.assertEqual((1.2, [1, 2, 4]), self.g_algo.shortest_path(1, 4))
        self.g.remove_edge(1, 4)
        self.g.add_edge(1, 4, 0.8)
        self.assertEqual((0.8, [1, 4]), self.g_algo.shortest_path(1, 4))
        self.g.remove_edge(1, 4)
        self.assertEqual((1.2, [1, 2, 4]), self.g_algo.shortest_path(1, 4))
        self.assertEqual((5, [1, 2, 0, 5]), self.g_algo.shortest_path(1, 5))




    def test_connected_component(self):
        self.assertEqual([5], self.g_algo.connected_component(5))
        self.assertEqual([0], self.g_algo.connected_component(0))
        self.assertEqual([1, 3, 2, 4], self.g_algo.connected_component(1))
        self.assertEqual([1, 3, 2, 4], self.g_algo.connected_component(2))
        self.assertEqual([1, 3, 2, 4], self.g_algo.connected_component(3))
        self.assertEqual([1, 3, 2, 4], self.g_algo.connected_component(4))
        self.g.add_edge(5, 0, 4)
        self.g.add_edge(0, 4, 3)
        self.assertEqual([0, 4, 2, 1, 3, 5], self.g_algo.connected_component(4))
        self.g.remove_node(4)
        self.assertEqual([1, 3, 2], self.g_algo.connected_component(1))
        self.assertEqual([0, 5], self.g_algo.connected_component(0))



    def test_connected_components(self):
        self.assertEqual([[5], [0], [1, 3, 2, 4]], self.g_algo.connected_components())
        self.g.add_edge(5, 0, 4)
        self.g.add_edge(0, 2, 8)
        self.assertEqual([[0, 2, 1, 4, 3, 5]], self.g_algo.connected_components())
        self.g.remove_node(1)
        self.assertEqual([[0, 2, 4, 5], [3]], self.g_algo.connected_components())
        self.g.add_edge(3, 0, 2.6)
        self.g.add_edge(5, 3, 3.3)
        self.assertEqual([[0, 2, 4, 5, 3]], self.g_algo.connected_components())
        self.g.remove_node(0)
        self.g.remove_node(2)
        self.assertEqual([[3], [4], [5]], self.g_algo.connected_components())




