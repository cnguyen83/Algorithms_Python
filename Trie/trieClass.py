#LastName: Nguyen
#FirstName: Christina


from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
        assert(len(w) > 0)
        
        if w[0] in self.next:
            next_node = self.next[w[0]]
            if len(w) == 1:
                next_node.count = next_node.count + 1
                next_node.isWordEnd = True
            else:
                word = w[1:]
                next_node.addWord(word)
        else:
            new_node = MyTrieNode(False)
            if len(w) == 1:
                new_node.count = new_node.count + 1
                new_node.isWordEnd = True
                self.next[w[0]] = new_node
            else:
            	self.next[w[0]] = new_node
            	new_node.addWord(w[1:])
        
        '''
        if self.next[w[0]]:
        	word = w[1:]
        	self.next[w[0]].addWord(word)
        
        else:
        	new_node = MyTrieNode(False)
        	if len(w) == 1:
        		new_node.count = new_node.count + 1
        	self.next[new_node]
        	remaining_word = w[1:]
        	new_node.next.addWord(remaining_word)
        '''

        # YOUR CODE HERE
        # If you want to create helper/auxiliary functions, please do so.
        
        return

    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.

        # YOUR CODE HERE
        letter = w[0]
        count = 0
        if len(w) == 1 and letter in self.next:
        	count = self.next[letter].count
        	return count
        
        elif letter in self.next:
        	next_node = self.next[letter]
        	remaining_word = w[1:]
        	count = next_node.lookupWord(remaining_word)
        	
        else:
        	count = 0
        
        return count # TODO: change this line, please
    

    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        #YOUR CODE HERE
        autoList = []
        
        if (self.searchPrefix(w) == None):
        	return autoList
        else:
        	start_node = self.searchPrefix(w)
        	start_node.autoCompleteHelper(w, autoList)
        	return autoList
    
    def autoCompleteHelper(self, w, autoList):
        if self.isWordEnd:
        	autoList.append((w, self.count))
        for key in self.next:
        	next_node = self.next[key]
        	growingWord = w + key
        	next_node.autoCompleteHelper(growingWord, autoList)  	
        
    def searchPrefix(self, w):
    	letter = w[0]
    	if len(w) == 1 and letter in self.next:
    		return self.next[letter]
    	elif letter in self.next:
    		next_node = self.next[letter]
    		remaining_word = w[1:]
    		return next_node.searchPrefix(remaining_word)
    	else:
    		return None

if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
 
    
    
     
