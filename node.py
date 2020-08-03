class Node():
	
	def __init__(self, elem = None, weight = None, lChild = None, rChild = None):
		self.elem = elem
		self.weight = weight
		self.lChild = lChild
		self.rChild = rChild

	def printPreOrder(self):
		print("Elem: " + str(self.elem))
		print("Weight: " + str(self.weight))
		if(self.lChild != None):
			print("Left Child: ")
			print()
			self.lChild.printPreOrder()

		if(self.rChild != None):
			print("Right Child: ")
			print()
			self.rChild.printPreOrder()