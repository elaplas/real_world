import sys

class HeapNode:
    def __init__(self, treeNode):
        self.tree_node = treeNode
        self.next = None

class TreeNode:
    def __init__(self, freq = None, char = None):
        self.frequency = freq
        self.character = char
        self.left = None
        self.right = None

class MinHeap:
    def __init__(self):
        self.top = None
        self.__size = 0

    def push(self, tree_node):
        if self.top is None:
            self.top = HeapNode(tree_node)
        else:
            if (tree_node.frequency < self.top.tree_node.frequency) or (tree_node.frequency == self.top.tree_node.frequency \
                and tree_node.character and self.top.tree_node.character and tree_node.character < self.top.tree_node.character):
                new_node = HeapNode(tree_node)
                new_node.next = self.top
                self.top = new_node
            else:
                cur_node = self.top
                while  cur_node.next and ( (cur_node.next.tree_node.frequency < tree_node.frequency) or  \
                    (cur_node.next.tree_node.frequency == tree_node.frequency and cur_node.next.tree_node.character \
                    and tree_node.character and cur_node.next.tree_node.character < tree_node.character) ):
                    cur_node = cur_node.next
                tmp = cur_node.next
                new_node = HeapNode(tree_node)
                cur_node.next = new_node
                new_node.next = tmp
        self.__size +=1


    def pop(self):
        if self.top is None:
            return None
        tmp = self.top.tree_node
        self.top = self.top.next
        self.__size -= 1
        return tmp 

    def size(self):
        return self.__size

def get_frequency_table(message):
    table = {}
    for s in message:
        if s in table:
            table[s] += 1
        else:
            table[s] = 1
    return table


def get_huffman_tree(data):
    frequency_table = get_frequency_table(data)
    min_heap = MinHeap()
    for key in frequency_table:
        tree_node = TreeNode(frequency_table[key], key)
        min_heap.push(tree_node)
    
    while min_heap.size() > 1:
        left_tree_node = min_heap.pop()
        right_tree_node = min_heap.pop()
        new_tree_node = TreeNode(left_tree_node.frequency + right_tree_node.frequency)
        new_tree_node.left = left_tree_node
        new_tree_node.right = right_tree_node
        min_heap.push(new_tree_node)
    
    return min_heap.pop()


def get_encoding_table_from_huffman_tree(huffman_tree):
    encoding_table = {}
    traverse_tree_recursive(huffman_tree, "" ,encoding_table)
    return encoding_table

def traverse_tree_recursive(root, huffman_code, encoding_table):
    if not root.left and not root.right:
        encoding_table[root.character] = huffman_code
        return

    if root.left:
        traverse_tree_recursive(root.left,  huffman_code + "0", encoding_table)
    if root.right:
        traverse_tree_recursive(root.right, huffman_code + "1", encoding_table) 


def huffman_encoding(data):
    if data == "":
        return "", None
    huffman_tree = get_huffman_tree(data)
    huffman_encoding_table = get_encoding_table_from_huffman_tree(huffman_tree)
    encoded_data = ""
    for s in data:
        encoded_data += huffman_encoding_table[s]
    return encoded_data, huffman_tree

def huffman_decoding(data, tree):

    if data == "" or tree is None:
        return ""
    
    cur_node = tree
    message = ""
    for bit in data:
        if cur_node.character:
            message += cur_node.character
            cur_node = tree
        if bit == '0':
            cur_node = cur_node.left
        else:
            cur_node = cur_node.right
    message += cur_node.character
    return message



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1 (simple message)
    input_message = "AAAAAAABBBCCCCCCCDDEEEEEE"
    encoded_message, huffman_tree = huffman_encoding(input_message)
    decoded_message = huffman_decoding(encoded_message, huffman_tree)
    print(".............................test case 1.................................")
    print(" encoded messaged:\n{}\n decoded message:\n{}\n input message: \n{}".format(
    encoded_message,
    decoded_message, 
    input_message))
    print(" are decoded message and input message the same? {} ".format(decoded_message == input_message))

    # Test Case 2 (long messages)
    input_message = "The first use of the slogan 'Woman, Life, Freedom' goes back to series of protests following the Death of\
Mahsa Amini in September 2022. The slogan was first chanted in Amini's funeral in Saqqez and then was heard in the initial\
protests in Sanandaj after the funeral. On 21 September, the slogan was chanted by students at University of Tehran, and by\
protesters around the country 'Iran' in the following days."
    encoded_message, huffman_tree = huffman_encoding(input_message)
    decoded_message = huffman_decoding(encoded_message, huffman_tree)
    print(".............................test case 2.................................")
    print(" encoded messaged:\n{}\n decoded message:\n{}\n input message: \n{}".format(
    encoded_message,
    decoded_message, 
    input_message))
    print(" are decoded message and input message the same? {} ".format(decoded_message == input_message))

    # Test Case 3 (empty message)
    input_message = ""
    encoded_message, huffman_tree = huffman_encoding(input_message)
    decoded_message = huffman_decoding(encoded_message, huffman_tree)
    print(".............................test case 3.................................")
    print(" encoded messaged:\n{}\n decoded message:\n{}\n input message: \n{}".format(
    encoded_message,
    decoded_message, 
    input_message))
    print(" are decoded message and input message the same? {} ".format(decoded_message == input_message))
    