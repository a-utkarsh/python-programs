class Trie:
    class Node:
        def __init__(self,c):
            self.char=c
            self.children=[]
            self.cnt=0
    def __init__(self):
        self.root=self.Node("*")

    def addWord(self,word):
        T=self.root
        for c in word:
            for child in T.children:
                if child.char==c:
                    break
            else:
                child=self.Node(c)
                T.children.append(child)
            T=child
            T.cnt+=1
    def searchWord(self,word):
        T=self.root
        for i,c in enumerate(word):
            for child in T.children:
                if child.char==c:
                    T=child
                    break
            if T.cnt==1:
                return word[:i+1]
        return word

    def prefix(self,arr):
        T=Trie()
        for w in arr:
            T.addWord(w)
        ans=[]
        for w in arr:
            pref=T.searchWord(w)
            ans.append(pref)
        return ans



arr1=['zebra', 'dog', 'duck', 'dove']
arr=Trie()
print(arr.prefix(arr1))



