import copy
class Vector (object):
	def __init__(self, vector):
		self.vector = vector

	def Index(self,lista1,num):
		try:
			return lista[num]
		except:
			return -1
		pass

	def ListToString(self):
		return "{}".format(self.vector)
	#==
	def IsEqual(self,a,res,lista1,lista2):
		res = 0
		for num in lista1:
			for num2 in lista2:
				if (num == num2):
					res = res+1
		if (res == a):
			return True
		return False
	#!=
	def IsNotEqual(self,res):
		return not(res)
	#Leer
	def Read(self,lista1):
		res =[]
		for i in lista1:
			res.append(i)
		return res
	#Imprimir
	def Print(self,lista1):
		for i in lista1:
			print(i)

	def main():	
		res = False
		Right =[]
		#num = 10
		lista1 = [1,2,3,4,5,6,7,8,9]
		copyVectorcito = copy.deepcopy(lista1)
		#lista2 = [1,2,3,4,5,6,7,8,9]
		vectorcito = Vector(lista1)
		#vectorcito2 = Vector(lista2)
		a = len(lista1)
		res = vectorcito.IsEqual(a,res,lista1,copyVectorcito)
		res = vectorcito.IsNotEqual(res)
		print(res)
		print()
		Left = vectorcito.Read(lista1)
		vectorcito.Print(Left)
		print(vectorcito.Index(lista1,10))

#Inicio
if __name__ == '__main__':
    Vector.main()
    pass



