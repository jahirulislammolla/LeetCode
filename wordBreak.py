class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        TrieDataSet = Trie()
        check = [True for i in range(len(wordDict))]
        wordDict = sorted(wordDict)
        for i in range(len(wordDict)):
            for j in range(i+1,len(wordDict)):
                sp_join = "".join(wordDict[j].split(wordDict[i]))
                if sp_join == "" or sp_join in wordDict[:i]:
                    check[j]=False
        for i in range(len(wordDict)):
            if check[i]:
                TrieDataSet.insetString(wordDict[i])
        set_list ={}
        for i in range(len(s)):
            set_list[i] = TrieDataSet.searchString(i+1,s[i:])
        print(len(s))
        check = [False for i in s]+[False]
        list_check = set_list[0]
        j=0
        while len(list_check):
            j+=1
            new_list = []
            for i in list_check:
                if i==len(s):
                    return True
                for k in set_list[i]:
                    if check[k] == False:
                        new_list+=[k]
                        check[k]=True
            list_check = new_list
        return TrieDataSet.status
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
class Trie:
    def __init__(self):
        self.status = False
        self.root = TrieNode()
    def insetString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
    def searchString(self,parent,word):
        current = self.root
        re_list = []
        for i in range(len(word)):
            node = current.children.get(word[i])
            if node == None:
                return re_list
            if node.endOfString == True:
                re_list+=[parent+i]
            current = node
        if current != None and current.endOfString == True:
            re_list+=[parent+i]
        return re_list
