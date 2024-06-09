
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.children = {}

    def insert(self, word):
        # Insert the node as before
        inserted_node = None
        if word in self.children:
            inserted_node = self.children[word]
        else:
            inserted_node = self.children[word] = RouteTrieNode()
        return inserted_node


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root=RouteTrieNode()
        self.root.handler=root_handler

    def insert(self, split_path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        cur_node = self.root
        for i, word in enumerate(split_path):
            cur_node = cur_node.insert(word)
            if i == len(split_path)-1:
                cur_node.handler = handler

    def find(self, split_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        cur_node = self.root
        for word in split_path:
            if word in cur_node.children:
                cur_node = cur_node.children[word]
            else:
                return None
        return cur_node.handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router_trie = RouteTrie(root_handler)
        self.handler_for_404_page = not_found_handler
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        split_path = self.split_path(path)
        self.router_trie.insert(split_path, handler)
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        split_path = self.split_path(path)
        handler = self.router_trie.find(split_path)
        if not handler:
            return self.handler_for_404_page
        return handler
        
    def split_path(self, path:str):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        split_path = path.split("/")
        split_path = [word for word in split_path if word != ""]
        return split_path


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one