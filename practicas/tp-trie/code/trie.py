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


def print_trie(root, indent=''):
  if root is None:
    return
  if root.isEndOfWord:
    print(indent + root.key + '*')
  else:
    print(indent + root.key)
  for child in root.children:
      print_trie(child, indent + '  ')

call = Trie()
insert(call, 'dsad')
insert(call, 'dsada')
insert(call, 'flaco')
insert(call, 'dsad')
insert(call, 'dsad')
insert(call, 'dsad')

print_trie(call.root)

