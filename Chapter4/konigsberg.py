# @file: Chapter4/konigsberg.py
# @brif: This file contains the implementation of the Konigsberg bridge problem.
# @date: 2021-08-21
# Copyright 2023 Kyungwon Chun
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
sys.path.insert(0, '.') # so we can access the Chapter2 package in the parent directory

from typing import TypeVar, List, Optional
from dataclasses import dataclass

from Chapter2.generic_search import Stack
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge

V = TypeVar('V') # type of the vertices in the graph

@dataclass
class KonigsbergNode:
    """
    Represents a node in the Konigsberg bridge problem.

    Attributes:
        we (WeightedEdge): The weighted edge associated with the node.
        crossed (int): The number of crossed bridges.
        parent (Optional[KonigsbergNode]): The parent node.
    """
    we: WeightedEdge
    crossed: int
    parent: Optional['KonigsbergNode']

def goal_test(node: KonigsbergNode, num_bridge: int) -> bool:
    """
    Check if the given node has crossed the specified number of bridges.

    Args:
        node (KonigsbergNode): The node to be checked.
        num_bridge (int): The number of bridges to be crossed.

    Returns:
        bool: True if the node has crossed the specified number of bridges, False otherwise.
    """
    return node.crossed == num_bridge

def traverse(wg: WeightedGraph[V], root: V) -> Optional[KonigsbergNode]:
    """
    Traverses a weighted graph starting from a given root node.

    Args:
        wg (WeightedGraph[V]): The weighted graph to traverse.
        root (V): The root node to start the traversal from.

    Returns:
        Optional[KonigsbergNode]: The final node reached during the traversal, or None if no such node is found.
    """
    first: int = wg.index_of(root) # find starting index
    crossed: List[int] = [] # crossed bridges
    frontier: Stack[int] = Stack()
    for we in wg.edges_for_index(first):
        frontier.push(KonigsbergNode(we, 1, None))
        crossed.append(we.weight)

    num_bridge: int = len(set(we.weight for v in range(wg.vertex_count) for we in wg.edges_for_index(v)))
    while not frontier.empty:
        current_node: KonigsbergNode = frontier.pop()
        if goal_test(current_node, num_bridge):
            return current_node
        for we in wg.edges_for_index(current_node.we.v):
            if we.weight in crossed:
                continue
            crossed.append(we.weight)
            frontier.push(KonigsbergNode(we, current_node.crossed + 1, current_node))
    
    return None

def node_to_path(node: KonigsbergNode) -> List[WeightedEdge]:
    """
    Converts a node to a path by traversing the parent pointers.

    Args:
        node (KonigsbergNode): The node to convert to a path.

    Returns:
        List[WeightedEdge]: The path represented as a list of weighted edges.
    """
    path: List[WeightedEdge] = []
    while node is not None:
        path.append(node.we)
        node = node.parent
    path.reverse()
    return path

if __name__ == '__main__':
    konigsberg: WeightedGraph[str] = WeightedGraph(["A", "B", "C", "D"])
    konigsberg.add_edge_by_vertices("A", "B", 1)
    konigsberg.add_edge_by_vertices("A", "B", 2)
    konigsberg.add_edge_by_vertices("B", "C", 3)
    konigsberg.add_edge_by_vertices("A", "C", 4)
    konigsberg.add_edge_by_vertices("B", "D", 5)
    konigsberg.add_edge_by_vertices("B", "D", 6)
    konigsberg.add_edge_by_vertices("C", "D", 7)
    konigsberg.add_edge_by_vertices("A", "D", 8)

    print(konigsberg)

    for start in ["A", "B", "C", "D"]:
        path: List[WeightedEdge] = traverse(konigsberg, start)
        if path is None:
            print(f"Start from {start}:", path)
        else:
            print(node_to_path(path))
