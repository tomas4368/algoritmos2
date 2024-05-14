# CLASE
class Trie:
  root =  None  

class TrieNode:
  parent =  None 
  children =  None 
  key =  None 
  isEndOfWord  = False

# insert(T,element) 
#  Descripción:  insert un elemento en T, siendo T un  Trie. 
#  Entrada:  El  Trie  sobre  la  cual  se  quiere  agregar  el  elemento  (Trie)   y 
#  el valor del elemento (palabra) a  agregar. 
#  Salida:   No hay salida definida

def _insertREC(node, element):
  # check existe un key en children
  for i in range(len(node.children)):
    # comparar key
    if node.children[i].key == element[0]:
      # comparar si letra final
      if len(element) == 1:
        # establecer nodo final de la palabra
        node.children[i].isEndOfWord = True
        return
      # eliminar primer carácter y llamar recursividad 
      elementAUX = element[1:]
      _insertREC(node.children[i], elementAUX)
      return
  # no existe el key dentro de children entonce lo agrego
  # creo nodo auxiliar
  nodeAUX = TrieNode()
  nodeAUX.key = element[0]
  nodeAUX.children = []
  nodeAUX.parent = node
  # comparar si letra final
  if len(element) == 1:
    # establezco final de la palabra
    nodeAUX.isEndOfWord = True
    # loa agrego al lista del padre al final
    node.children.append(nodeAUX)
    return
  # como no es final de la palabra
  # loa agrego al lista del padre al final
  node.children.append(nodeAUX)
  # eliminar primer carácter y llamar recursividad
  elementAUX = element[1:]
  _insertREC(node.children[len(node.children)-1], elementAUX)

def insert(T, element):
  # verificar raíz
  if T.root == None:
    # inserto elemento
    T.root = TrieNode()
    T.root.children = []
    T.root.key = ''
  # entrar a recursividad
  _insertREC(T.root, element)

# search(T,element)  Descripción:  Verifica que un elemento se encuentre  dentro del  Trie 
#  Entrada:  El  Trie  sobre  la  cual  se  quiere  buscar  el  elemento  (Trie)   y 
#  el valor del elemento (palabra) 
#  Salida  : Devuelve  False o True   según se encuentre  el elemento.

def _searchREC(node, element):
  # check existe un key en children
  for i in range(len(node.children)):
    # comparar key
    if node.children[i].key == element[0]:
      # comparar si letra final
      if len(element) == 1:
        # comprobar se el nodo i es ta declarado como final de letra
        if node.children[i].isEndOfWord:
          return True
        else: 
          return False
      # eliminar primer carácter y llamar recursividad 
      elementAUX = element[1:]
      return _searchREC(node.children[i], elementAUX)
  # de lo contrario
  return False

def search(T, element):
  # verificar raíz
  if T.root == None:
    return False
  # entrar a recursividad
  return _searchREC(T.root, element)

# delete(T,element)  Descripción:  Elimina un elemento se encuentre dentro  del  Trie 
#  Entrada:  El  Trie  sobre  la  cual  se  quiere  eliminar  el  elemento  (Trie) 
#  y el valor del elemento (palabra) a  eliminar. 
#  Salida  : Devuelve  False o True   según se haya eliminado  el elemento.

def _deleteParent(node):
  # comprobar si tiene hijos de lo contrario llamar al parent
  if len(node.children) == 0:
    # comprobar si es raíz
    if node.parent == None:
      return
    # comprobar si es letra final
    if node.isEndOfWord:
      return
    # eliminar
    node.parent.children.remove(node)
    # llamar recursividad
    _deleteParent(node.parent)

def _deleteREC(node, element):
  # check existe un key en children
  for i in range(len(node.children)):
    # comparar key
    if node.children[i].key == element[0]:
      # si no es final
      if len(element) != 1:
        # eliminar primer carácter y llamar recursividad 
        elementAUX = element[1:]
        return _deleteREC(node.children[i], elementAUX)
      # es final
      # comprobar se el nodo i no esta declarado como final de letra
      if not node.children[i].isEndOfWord:
        return False
      # comprobar si tiene hijos el key
      if len(node.children[i].children) != 0:
        # declaro no ya no es final de una letra
        node.children[i].isEndOfWord = False
        return True
      # no tiene hijos el key eliminar
      del node.children[i]
      # eliminar padres
      _deleteParent(node)
      return True
  # de lo contrario
  return False

def delete(T, element):
  # verificar raíz
  if T.root == None:
    return False
  # entrar a recursividad
  return _deleteREC(T.root, element)

# Ejercicio 4 
#  Implementar un algoritmo que dado un árbol  Trie  T ,
#  un patrón  p (prefijo)  y un entero  n, escriba todas
#  las palabras del árbol que empiezan por  p  y sean de
#  longitud  n  .

def _prefixPrint(node, string):
  # agregar el string
  string = node.key + string
  # recursividad
  if node.parent == None:
    print(string)
  else:
    _prefixPrint(node.parent, string)

def _prefixREC(node, prefix, n):
  # comprobar longitud
  if n == 0:
    return
  # check existe un key en children
  for i in range(len(node.children)):
    # buscar palabras
    if prefix == '':
      # comprobar se el nodo i es ta declarado como final de letra
      if node.children[i].isEndOfWord:
        # imprimir
        _prefixPrint(node.children[i], '')
      # eliminar primer carácter y llamar recursividad
      nAUX = n - 1
      _prefixREC(node.children[i], prefix, nAUX)
    else:
      # comparar key
      if  node.children[i].key == prefix[0]:
        # comprobar se el nodo i es ta declarado como final de letra
        if node.children[i].isEndOfWord:
          # imprimir
          _prefixPrint(node.children[i], '')
        # eliminar primer carácter y llamar recursividad
        nAUX = n - 1 
        prefixAUX = prefix[1:]
        _prefixREC(node.children[i], prefixAUX, nAUX)
    

def prefix(T, prefix, n):
  # verificar raíz
  if T.root == None:
    return
  # entrar a recursividad
  return _prefixREC(T.root, prefix, n)

# Ejercicio 5 
#  Implementar un algoritmo que dado los  Trie  T1 y T2  devuelva  
#  True  si estos pertenecen al mismo  documento y  False  en caso 
#  contrario. Se considera  que un   Trie  pertenece al mismo documento  
#  cuando:  
#     1.   Ambos Trie sean iguales (esto se debe cumplir)  
#     3.   Si la implementación está basada en LinkedList, considerar el caso donde 
#          las palabras hayan  sido insertadas en un orden diferente.
#  En otras palabras, analizar si todas las palabras de T1 se encuentran en T2.
#  Analizar el costo computacional. 

def _sortChildren(T):
  # declarar nueva lista
  auxChildren = []
  # default
  if len(T.children) == 0:
    return T.children
  # 
  for i in T.children:
    auxChildren.append(i.key)
  # 
  auxChildren.sort()
  for i in range(len(T.children)):
    print()
  
  

def _compareTriREC(T1, T2):
  # comprobar longitud hijos
  if len(T1.children) != len(T2.children):
    return False
  # ordenar las listas
  T1.children.sort()
  T2.children.sort()
  # comparar hijos
  for i in range(len(T1.children)):
    if T1.children[i].key != T2.children[i].key:
      return False
  # recursividad
  for i in range(len(T1.children)):
    estadoAUX = _compareTriREC(T1.children[i], T2.children[i])
    if estadoAUX == False:
      return False
    

def compareTri(T1, T2):
  # verificar raíz
  if T1.root == None or T2.root == None:
    return
  # entrar a recursividad
  estado = _compareTriREC(T1.root, T2.root)
  # verifica
  if estado == None:
    return True
  return False

def print_trie(root, indent=''):
  if root is None:
    return
  if root.isEndOfWord:
    print(indent + root.key + '*')
  else:
    print(indent + root.key)
  for child in root.children:
      print_trie(child, indent + '  ')

# call = Trie()
# insert(call, 'dsad')
# insert(call, 'dsada')
# insert(call, 'flaco')
# insert(call, 'dsad')
# insert(call, 'dsad')
# insert(call, 'dsad')

# print_trie(call.root)

# print()

# prefix(call, 'dsad', 10)

# print(compareTri(call, call))