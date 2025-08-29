# 133. Clone Graph

**Link**: [LeetCode - Clone Graph](https://leetcode.com/problems/clone-graph/)

---

## Problem
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

---

## Example
### Normal
- Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
- Output: [[2,4],[1,3],[2,4],[1,3]]

### Edge
- Input: [[1]]
- Output: [[1]]

### Invalid
- Input: []
- Output: []

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - make a hm of {node -> new deep copy of node}
    - make a queue, add root in
    - perform bfs, for each nodes neighbor, create nodes
    - copy nodes neighbor.append(copied nodes)

---

## Complexity
- **Time**: O(n)
- **Space**: O(n)

---

## Pitfalls
- if neighbor not in hashmap, we need to create it in hashmap, then add it to the queue too 

---
