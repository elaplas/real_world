# Problem 5
## Decisions
A nested "map" data structure is used as a "Trie" because it can not only provide the same behavior as a "tree" data structure but also faster insertion and searching. Each node of the "Trie" corresponds to a character of a word. 
## Time efficiency
- insert: O(n) where n is the number of characters in the word
- find: O(n) where n is the number of characters in the word
- suffix: O(n<sup>3</sup>) ~ O(n<sub>r</sub>*(n<sub>c</sub>+n<sub>w</sub>*n<sub>s</sub>)) where n<sub>r</sub> is the number of recursions, n<sub>c</sub> is the number of children in the current recursion, n<sub>w</sub> and n<sub>s</sub> are respectively the number of children with nodes and their corresponding sub-children in the current recursion. 
## Space efficiency
O(n) 