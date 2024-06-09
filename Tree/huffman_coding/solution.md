# Problem 3
## Decisions
A "map" data structure is used to create a frequency table where the keys and values of "map" are respectively the characters and their frequencies. A tree node is defined and used for each row in the frequency table and a "min heap" is implemented and used to keep track of the tree nodes with minimum frequencies for merging them and creating a new tree node. 
## Time efficiency
- Encoding: O(n) ~ O(n<sub>1</sub>) + O(n<sub>2</sub>) + O(n<sub>3</sub>) + O(n<sub>4</sub>) where O(n<sub>1</sub>), O(n<sub>2</sub>), O(n<sub>3</sub>) and O(n<sub>4</sub>) are respectively the time complexities for creating the frequency table, min heap, Huffman tree and binary message. 
- Decoding: O(n)
## Space efficiency
O(n)