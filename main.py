import json

# Definimos la clase Nodo para construir árboles binarios
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"<Nodo{self.valor}>"

    def preorden(self, result_list):
        result_list.append(self.valor)
        if self.left is not None:
            self.left.preorden(result_list)
        if self.right is not None:
            self.right.preorden(result_list)

    def inorden(self, result_list):
        if self.left is not None:
            self.left.inorden(result_list)
        result_list.append(self.valor)
        if self.right is not None:
            self.right.inorden(result_list)

    def postorden(self, result_list):
        if self.left is not None:
            self.left.postorden(result_list)
        if self.right is not None:
            self.right.postorden(result_list)
        result_list.append(self.valor)

# Creamos una instancia de la clase Nodo llamada 'arbol' (tiempo constante, O(1))
arbol = Nodo(1)

# Configuramos los nodos hijos del árbol (tiempo constante, O(1))
arbol.left = Nodo(2)
arbol.right = Nodo(3)
arbol.left.left = Nodo(4)
arbol.left.right = Nodo(5)

# Creamos una segunda instancia de la clase Nodo llamada 'arbol2' (tiempo constante, O(1))
arbol2 = Nodo(1)

# Configuramos los nodos hijos del segundo árbol (tiempo constante, O(1))
arbol2.left = Nodo(2)
arbol2.right = Nodo(3)
arbol2.left.left = Nodo(4)
arbol2.left.right = Nodo(5)
arbol2.right.left = Nodo(6)
arbol2.right.right = Nodo(7)

# Creamos listas vacías para almacenar los resultados (tiempo constante, O(1))
resultado_preorden = []
resultado_inorden = []
resultado_postorden = []

# Realizamos recorridos en el primer árbol 'arbol' (complejidad O(n), donde 'n' es el número de nodos)
arbol.preorden(resultado_preorden)
arbol.inorden(resultado_inorden)
arbol.postorden(resultado_postorden)

# Creamos listas vacías para almacenar los resultados del segundo árbol (tiempo constante, O(1))
resultado2_preorden = []
resultado2_inorden = []
resultado2_postorden = []

# Realizamos recorridos en el segundo árbol 'arbol2' (complejidad O(m), donde 'm' es el número de nodos)
arbol2.preorden(resultado2_preorden)
arbol2.inorden(resultado2_inorden)
arbol2.postorden(resultado2_postorden)

# Imprimimos los resultados de los recorridos en formato JSON (tiempo constante, O(1))
print("El recorrido en preorden es:\n", json.dumps(resultado_preorden))
print("El recorrido en inorden es:\n", json.dumps(resultado_inorden))
print("El recorrido en postorden es:\n", json.dumps(resultado_postorden))

print("El recorrido del segundo árbol en preorden es:\n", json.dumps(resultado2_preorden))
print("El recorrido del segundo árbol en inorden es:\n", json.dumps(resultado2_inorden))
print("El recorrido del segundo árbol en postorden es:\n", json.dumps(resultado2_postorden))

# Complejidad total del algoritmo:
# La complejidad de los recorridos en los árboles 'arbol' y 'arbol2' es O(n + m),
# donde 'n' es el número de nodos en el primer árbol 'arbol' y 'm' es el número de nodos