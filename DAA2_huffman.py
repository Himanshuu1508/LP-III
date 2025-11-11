# Huffman Coding Implementation in Python
class Node:
    def __init__(self,left=None,right=None,value=None,frequency=None): #initializing node
        self.left = left
        self.right = right 
        self.value = value 
        self.frequency = frequency
# Return children of the node    
    def children(self):
        return (self.left,self.right)


# Huffman Encoding Class
class Huffman_Encoding:
    def __init__(self,string):
        self.q = [] #priority queue
        self.string = string 
        self.encoding = {} #dictionary to store encoding

    def char_frequency(self): #calculate frequency of each character
        count = {}
        for char in self.string: #count frequency
            if char not in count:
                count[char] = 0
            count[char] += 1 

        for char,value in count.items(): #create node for each character
            node = Node(value=char,frequency=value)
            self.q.append(node) #add node to priority queue
        self.q.sort(key=lambda x: x.frequency)    #sort queue based on frequency

    def build_tree(self): #build huffman tree
        while len(self.q) > 1: #until only one node remains
            n1 = self.q.pop(0) #pop two nodes with smallest frequency
            n2 = self.q.pop(0)
            node = Node(left=n1,right=n2,frequency=n1.frequency + n2.frequency)
            self.q.append(node) #add new node to queue
            self.q.sort(key = lambda x:x.frequency) #sort queue again

    
    def helper(self,node:Node,binary_str="",): #recursive helper to generate encoding
        if type(node.value) is str: #leaf node
            self.encoding[node.value] = binary_str
            return
        l,r = node.children()
        self.helper(node.left,binary_str + "0") #traverse left
        self.helper(node.right,binary_str + "1") #traverse right
        #print(node.frequency) 
        return
        

    def huffman_encoding(self): #generate huffman encoding
        root = self.q[0] #root of the tree
        self.helper(root,"") #start recursive encoding generation


    def print_encoding(self): #print the encoding
        print(' Char | Huffman code ')  #header
        print('----------------------')
        for char,binary in self.encoding.items(): 
            print(" %-4r |%12s" % (char,binary))   #print each character and its code
    
    def encode(self):
        self.char_frequency()
        self.build_tree()
        self.huffman_encoding()
        self.print_encoding()

string = input("Enter string to be encoded: ")
# string = 'AAAAAAABBCCCCCCDDDEEEEEEEEE'
encode = Huffman_Encoding(string)
encode.encode()


# The time complexity for encoding each unique character based on its frequency is O(nlog n).

# Extracting minimum frequency from the priority queue takes place 2*(n-1) times and its complexity is O(log n). Thus the overall complexity is O(nlog n).

