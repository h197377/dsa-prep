# 208. Implement Trie

**Link**: [LeetCode - Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

---

## Problem
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

---

## Example
### Normal
- Input ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
- Output [null, null, true, false, true, null, true]

---

## Approach
1. **Brute Force**:
    - (describe)

2. **Optimal Solution**:
    - make a **Node** class that has isWord boolean and children dict (or array of 26 if lowercase chars)
    - for __init__, make a root object of a node
    - for insert, for thru chars of the input word, for each char make it children of last, then at end .isWord = True
    - for search, just walk down each character, verify if at the end .isWord == True
    - for startsWith, samething but no need for .isWord == True 

---

## Complexity
- **Time**: O(n)
- **Space**: O(n)

---

## Pitfalls
- class Node def __init__
- to make a node, = self.Node() 

---
