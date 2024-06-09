import hashlib
import time 
import random
import string

def calc_hash():
    sha = hashlib.sha256()
    hash_str = ''.join(random.sample(string.ascii_lowercase, 20)).encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = self.get_timestamp()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = calc_hash()

    def get_timestamp(self):
        return time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())

class Node:
    def __init__(self, block):
        self.block = block
        self.next = None

class BlockChain:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        if not self.top:
            self.top = Node(Block(data, 0))
        else:
            tmp = Node(Block(data, self.get_previous_hash()))
            tmp.next = self.top
            self.top = tmp
        self.size += 1

    def get_previous_hash(self):
        return self.top.block.hash

    def __repr__(self):
        cur_node = self.top
        tmp_str = ""
        count = self.size-1
        while cur_node:
            tmp_str += f"....block {count}....\n"
            tmp_str += f"timestamp: {cur_node.block.timestamp}\ndata: /{cur_node.block.data}\nprevious_hash: {cur_node.block.previous_hash}\nhash: {cur_node.block.hash}\n"
            if cur_node.next:
                tmp_str += "..............\n     |\n     v\n"
            count -= 1
            cur_node = cur_node.next
        return tmp_str

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
# Test Case 1 (simple test)

print("...........test case 1............")
block_chain = BlockChain()
block_chain.push("transaction 0")
block_chain.push("transaction 1")
print(block_chain)

# Test Case 2 (longer case)
print("...........test case 2............")
block_chain = BlockChain()
block_chain.push("transaction 0")
block_chain.push("transaction 1")
block_chain.push("transaction 2")
block_chain.push("transaction 3")
block_chain.push("transaction 4")
block_chain.push("transaction 5")
print(block_chain)

# Test Case 3 (empty case)
print("...........test case 3............")
block_chain = BlockChain()
print(block_chain)
