##############
# QUESTION 2 #
##############
class Node:
    def __init__(self,value,end_indicator, alphabet):
        """
            Function description: Initialises an trie node with a given arguments and default values
            Input: 
                value: char value, a letter
                end_indicator: boolean value, indicates an leaf node
                alphabet: integer value, indicates alphabet size
            Output: 
                None
            Time complexity: 
                O(A), A for size of alphabet
            Time complexity analysis : 
                Performs a fixed number of 6 operations, but initilising the alphabet array takes O(A) time
            Space complexity: 
                O(A), A for size of alphabet
            Space complexity analysis:
                The amount of space needed grows linearly in time based on alphabet value.
        """
        self.value = value
        self.next = [None]*alphabet
        self.end = end_indicator
        self.freq = 0        
        self.max_child_len = 0
        self.found = None
        self.search_length = 0
        
    def update_search_length(self):
        """
            Function description: Resets search frequency of node to original frequency value in node.
            Input: 
                None
            Output: 
                None
            Time complexity: 
                O(1)
            Time complexity analysis : 
                One operation is done only.
            Space complexity: 
                O(1)
            Space complexity analysis:
                No auxillary space is initialised, only reassignment of pre-existing attributes.
        """
        self.search_length = self.freq


    #def __repr__(self):
       #return f'{self.value}-{self.search_length}-{self.freq}'   
   
class Found:
    def __init__(self):
        """
            Function description: Initialises an Found indicator instance. This is to ensure that an already searched leaf will not be searched again or updates frequency of node.
            Input: 
                None
            Output: 
                None
            Time complexity: 
                O(1)
            Time complexity analysis : 
                One operation only.
            Space complexity: 
                O(1)
            Space complexity analysis:
                assigning a boolean value to a variable takes a constant amount of space, regardless of input
        """
        self.value = True
        
    #def __repr__(self):
    #  return 'found'   
       

class SpellChecker:
    def __init__(self, message_file):
        """
            Function description: 
                This function creates an prefix trie iterating through an input text file's strings.
            Approach Description:
                The input file is opened and read character by character.It calls on the self.index_c() method to convert characters into an index for the trie node children array. 

                if character exists, it is added in the trie as an node. if it doesnt exist, the function increments the node frequency by 1 if it does. The current node in focus is reassigned to the character's node regardless.
                If it returns -1, then this character does not exist in the defined alphabet and designated as an seperator, indicating the end of an word. If the full word does not exist in the trie, a new leaf node is added to the last character's children to indicate end. If it does, then the leaf node increments by 1. The current node in focus is assigned back to the root for a new word to be inputed. 

            Input: 
                message_file: string, name of an txt file
            Output: 
                None
            Time complexity: 
                O(T), where T is the number of characters in the message_file text file
            Time complexity analysis : 
                The function reads the entire text file character by character, taking O(T) time. At worst, each character initialises an Node instance, which takes O(A) time for its alphabet. It is already defined that the alphabet size is 63 (a-z,A-Z,0-10, end_indicator), thus taking  O(63) to initialise an node, effectively O(1) time.  
                All self.index_c() calls take O(1) since it is all simple comparison operations. A update_search_length() calls are O(1) time as it is an single reassignment operation.
            Space complexity: 
                O(T)
            Space complexity analysis:
                The trie can hold up to T number of nodes, each holding an k amount of unique children characters, which is the alphabet. The alphabet is defined as a constant size of 63 (a-z,A-Z,0-10, end_indicator). Thus, k is fixed to a constant 63. It initialises O(63) space per node regardless of input and can be ignored.
                All other method calls do not make auxillary space. 
        """
        alphabet = 26+26+10+1
        self.root = Node('?', False, alphabet)
        with open(message_file,"r") as f:
            current = self.root
            for c in f.read():
                index = self.index_c(c)
                # letter 
                if index != -1:
                    if current.next[index] is None:
                        new =Node(c,False,alphabet)
                        current.next[index] = new
                    current.next[index].freq+=1
                    current = current.next[index]
                #seperator
                else:
                    if current.next[0] is None:
                        new = Node('$', True, alphabet)
                        current.next[0] = new
                    current.next[0].freq +=1
                    current.next[0].update_search_length()
                    current = self.root
            if current.next[0] is None:
                current.next[0] = Node('$', True, alphabet)
                current.next[0].freq +=1

        
    def index_c(self, c):
        """
            Function description: Converts an given char value into an integer value. This is index of letter in an given trie node's children array.
            Input: 
                c: char value, a letter of the alphabet
            Output: 
                integer value
            Time complexity: 
                O(1)
            Time complexity analysis : 
                Each operation is constant time
            Space complexity: 
                O(1)
            Space complexity analysis:
                No dynamic data structures are initialised, only fixed sized values. 
        """
        index = -1
        char = ord(c)
        if '0'<=c<='9':
            index = char - ord('0')
        elif 'A' <= c <= 'Z':
            index = 11+char-ord('A')
        elif 'a' <= c <= 'z':
            index = 11+26+char-ord('a')
        elif char == ord('$'):
            index = 0
        return index
        
    def check(self, input): #recursive 
        """
            Function description: 
                This function returns a list of up to 3 strings using DFS as trie transversal. 
            Approach description:
                This function first searches for exact word match in trie against input, returning if leaf node is reached. It will also maintain a temp array to note the letters that do match a substring of the prefix. 

                if input does not exist, it maintains the deepest possible node to find similar words. Depth first search is performed to find the word with the highest frequency from the node. The frequency of the word is subtracted from nodes searched as it recurses back to ensure it will not be searched in the exact same logic. The word formed is appended to result array. If the array has less than 3 elements, the temp array is used to backtrack against the prefix substring to further apply DFS onto. 
            Input: 
                input: string value
            Output: 
                Depending on input, an empty array or an array containing up to 3 strings.
            Time complexity: 
                O(M+U), where M is the size of input and U is the total number of characters in output array if input does not exist in trie.
                O(M), where M is the size of input if input does exist as a word in the trie
            Time complexity analysis : 
                searching for exact match with input takes up to O(M) time to transverse the nodes. Extracting the input substring based on length of temp array takes up to O(M) time. This can be simplified to just O(M) time.

                if input does not exist:
                    At each loop iteration, DFS takes O(U*A) time, where A is the size of the possible children an given node can have. Based on problem scenario and Spellchecker initialisation, it assigns a constant O(63) sized array, making A = 63. This constant number of operations based on A can be disregarded, leaving the total dynamic time as O(U). The prefix may be updated to remove one character, taking O(M) time. This loop runs for at most 3 iterations, resulting O(3*(M+U)) time to find similar words.

                    Hence, the total time is O(5*M+3*U), simplified to O(M+U).

            Space complexity: 
                O(M+U), where M is the size of input and U is the total number of characters in output array if input does not exist in trie.
                O(M), where M is the size of input if input does exist as a word in the trie
            Space complexity analysis:
                the temp array maintains up to O(M) nodes to transverse from. 
                DFS maintains no auxillary space making it O(1).
                if input does not exist as word in trie:
                    the returned result array will hold up to O(U) characters. U contains at least 3*M characters.
            
        """
        current = self.root
        word = input +'$'
        result = []
        temp = [current]
        #O(M) done
        for c in word:
            index = self.index_c(c)
            if current.next[index] is not None:
                current = current.next[index]
                if not current.end:
                    temp.append(current)
                if current.end and c=='$':
                    return result  
            else:
                break
        #O(M+U)
        index = 1
        prefix = input[:len(temp)-2] #O(M)
        found = Found()
        while len(result) <3:
            current = temp[0-index]
            if current == self.root:
                return result
            #########
            freq,suffix =self.dfs(current, found) #O(O-M)
            #########
            if suffix =='#' or suffix == '':
                index+=1
                prefix = prefix[:0-index] #O(M)
                found = Found()
            else:
                result.append(prefix+suffix)
        return result
        
    def dfs(self, current, found):
        """
            Function description: 
                This function is an implementation of Depth first search to find the most frequent occuring nodes and return the combined string formed adding each node value.
            Input: 
                current: Node instance, a given letter in the trie
                found: Found instance
            Output: 
                A tuple containing an integer and 
            Time complexity: 
                O(S*A), where S is number of nodes transversed and A is the size of the trie node's children
            Time complexity analysis : 
                Each letter node is visted exactly once contributing to O(S) time until reaching leaf node. 
                update_search_length() is of O(1).
                Per node, finding the most frequent child node is done through the self.find_next_freq() call. This takes O(A) time to transverse all of the nodes alphabet array. 
            Space complexity: 
                O(S), where S is number of nodes transversed
            Space complexity analysis:
                Each recursive call adds to the memory stack, which at most is O(S) depth. All update_search_length() and self.find_next_freq() calls are O(1) space.
        """
        if current.end and current.found != found:
            current.found = found
            current.search_length -= current.freq
            return (current.freq,'' ) 
        if current.found != found:
            current.update_search_length()
            current.found = found
        freq, value = self.find_next_freq(current, found)
        if value == '#' or freq == '#':
            return (0,'#')
        freq,suffix  = self.dfs(current.next[self.index_c(value)], found)
        if suffix == '#':
            return (0,'#')
        current.search_length -= freq
        return ( freq,current.value+suffix)


    def find_next_freq(self, current, found):
        """
            Function description: This function returns an tuple. This tuple contains the letter child of current that is the most frequent, as of the search.
            Input: 
                current: Node instance
                found: Found instance
            Output: 
                A tuple containing an integer and char value.
            Time complexity: 
                O(A), where A is the size of the alphabet
            Time complexity analysis : 
                It must iterate over the entire size of the alphabet to determine the most frequent child node of current. This takes O(A) time. 
            Space complexity: 
                O(1)
            Space complexity analysis:
                No dynamic data structures are initialised.  
        """
        num = (0,'#')
        for i in current.next:
            if i is not None:
                if i.value != '$' and i.found != found:
                        i.update_search_length()
                        i.found = found                 
                if  num[0] == i.search_length:
                    num = (num[0], min(num[1], i.value))
                else:
                    num = max(num, (i.search_length, i.value))
        return num
                

