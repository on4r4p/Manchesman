#Huffman String Encoder

from node import Node

class HuffmanCoding():

	def __init__(self, message):

		self.message = message
		self.weightedDict = {}
		self.codedlist = []
		self.codedDict = {}

	def stringToWeightedDict(self, string):
		rDict = {}

		for c in string:
			if(c in rDict):
				rDict[c] += 1
			else:
				rDict[c] = 1

		return rDict

	def insertNode(self, node):
		#This makes it O(N) best case, I could use a built in heap library, but this was more about showing
		#knowedge of Huffman Coding, rather than the perfect program.

		i = 0
		for n in self.codedlist:
			if n.weight > node.weight:
				i += 1

		self.codedlist.insert(i, node  )

	def dictToNodes(self):
		for k, v in self.weightedDict.items():
			newNode = Node(elem=k, weight=v)
			self.insertNode(newNode)

	def reduce(self):

		while len(self.codedlist) > 1:
			n1 = self.codedlist.pop()
			n2 = self.codedlist.pop()
			n3 = Node(elem = None, weight = n1.weight + n2.weight, lChild = n1, rChild = n2)
			self.insertNode(n3)

	def treeToCodes(self, node, code = ''):

		if(node.elem != None):
			self.codedDict[node.elem] = code

		if(node.lChild != None):
			self.treeToCodes(node.lChild, code + "0")

		if(node.rChild != None):
			self.treeToCodes(node.rChild, code + "1")

	def stringToBin(self):
		r = ''
		for c in self.message:
			r += self.codedDict[c]
#			print(r)

		self.message = r

	def binToString(self, dict):
		cString = ''
		mes = ''
		for c in self.message:
			cString += c
			if cString in dict:
				mes += dict[cString]
				cString = ''
		self.message = mes

	def encode(self):
		self.weightedDict = self.stringToWeightedDict(self.message)
		self.dictToNodes()
		self.reduce()

		self.treeToCodes(self.codedlist[0])
		self.stringToBin()



	def printWeightedList(self):

		x = [x.weight for x in self.codedlist]
		print(x)

#test = HuffmanCoding("this is an example for huffman encoding")
#test.encode()
#print(test.codedDict)
#print(test.message)
#test.binToString(dict([[v,k] for k,v in test.codedDict.items()]))
#print(test.message)
