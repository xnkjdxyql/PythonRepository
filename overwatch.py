class Overwatch(object):
	def __init__(self,name,size,height):
		self.__name=name
		self.__size=size
		self.height=height
	def printDva(self):
		print('overwatch的身高是%s,大小是%s,名字为%s'%(self.__height,self.__size,self.__name))
	def getsize(self):
		print('悄悄告诉你%s的size是%s'%(self.__name,self.__size))