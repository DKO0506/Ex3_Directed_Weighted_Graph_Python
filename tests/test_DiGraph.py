from src.DiGraph import DiGraph
from unittest import TestCase


class TestDiGraph(TestCase):
    def setUp(self) -> None:
        self.g = DiGraph()
        for i in range(5):
            self.g.add_node(i)
        self.g.add_edge(1, 2, 1)
        self.g.add_edge(1, 3, 1)
        self.g.add_edge(1, 4, 1)
        self.g.add_edge(2, 1, 1)
        self.g.add_edge(2, 0, 1.5)
        self.g.add_edge(3, 1, 1)
        self.g.add_edge(4, 0, 4.8)
        self.g.add_edge(4, 2, 1)

    def test_v_size(self):
        self.assertEqual(5, self.g.v_size())


    def test_e_size(self):
        self.assertEqual(8, self.g.e_size())

    def test_get_mc(self):
        self.assertEqual(13, self.g.get_mc())

    def test_add_edge(self):
        self.assertFalse(self.g.add_edge(9, 5, 0.35))
        self.assertTrue(self.g.add_edge(0, 2, 0.93))


    def test_add_node(self):
        self.assertFalse(self.g.add_node(0))
        self.assertTrue(self.g.add_node(5))
        self.assertFalse(self.g.add_node(5))



    def test_remove_node(self):
        self.assertFalse(self.g.remove_node(6))
        self.assertTrue(self.g.remove_node(4))
        self.assertEqual(5, self.g.e_size())


    def test_remove_edge(self):
        self.assertFalse(self.g.remove_edge(0,7))
        self.assertTrue(self.g.remove_edge(1,2))
        self.assertEqual(7, self.g.e_size())


    def test_all_in_edges_of_node(self):
        self.assertEqual({2: 1.5, 4: 4.8},self.g.all_in_edges_of_node(0))

    def test_all_out_edges_of_node(self):
        self.assertEqual({2: 1, 3: 1, 4:1},self.g.all_out_edges_of_node(1))

    def test_get_all_v(self):
        self.assertEqual(5, len(self.g.get_all_v()))
        d = {0: self.g.get_all_v()[0], 1: self.g.get_all_v()[1], 2: self.g.get_all_v()[2], 3: self.g.get_all_v()[3], 4: self.g.get_all_v()[4]}
        self.assertEqual(d, self.g.get_all_v())
