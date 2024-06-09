# Problem 7
## Decisions
A nested "map" data structure is used as a "Trie" because it can not only provide the same behavior as a "tree" data structure but also faster insertion and searching. Each node corresponds to a word instead of a character to avoid lengthy iterations. 
## Time efficiency
- add_handler: O(n) where n is the number of words in the path
- lookup: O(n) where n is the number of words in the path
## Space efficiency
O(n) 