class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_end = False
        self.children = {}
    
    def insert(self, char, is_end = False):
        ## Add a child node in this Trie
        inserted_node = None
        if char in self.children:
            inserted_node = self.children[char]
        else:
            self.children[char] = TrieNode()
            inserted_node = self.children[char]

        if is_end:
            inserted_node.is_end = True

        return inserted_node

    def __suffixes_recursive(self, node, current_visited_suffix, all_suffixes):
        ## Helper function to recurse on the children with nodes 

        if node.is_end:
            all_suffixes.append( current_visited_suffix)
        
        if not len(node.children):
            return

        for char in node.children:
            new_visited_suffix =  current_visited_suffix + char
            self.__suffixes_recursive(node.children[char], new_visited_suffix, all_suffixes)

        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        current_visited_suffix = ""
        all_suffixes = []
        self.__suffixes_recursive(self, current_visited_suffix, all_suffixes)
        return all_suffixes


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        cur_node = self.root
        is_end = False
        for i, char in enumerate(word):
            if i == len(word)-1:
                is_end = True
            cur_node = cur_node.insert(char, is_end)

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        cur_node = self.root
        for char in prefix:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                cur_node = None
                break
        return cur_node



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

######### test 1 ###########
f_prefixes = MyTrie.find("f")
suffixes = f_prefixes.suffixes()
print("............test 1.............")
print("expected: ", "['un', 'unction', 'actory']")
print("result: ", suffixes)

######### test 2 ###########
f_prefixes = MyTrie.find("fu")
suffixes = f_prefixes.suffixes()
print("............test 2.............")
print("expected: ", "['n', 'nction']")
print("result: ", suffixes)

######### test 3 ###########
f_prefixes = MyTrie.find("an")
suffixes = f_prefixes.suffixes()
print("............test 3.............")
print("expected: ", "['t', 'thology', 'tagonist', 'tonym']")
print("result: ", suffixes)