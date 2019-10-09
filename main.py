"""
Lorsqu'on appelle `import fibo`, l'interpreteur cherche d'abord ce nom dans les built-in modules.
S'il n'est pas trouvé, alors il cherche pour un fichier nommé fibo.py dans la liste des dossiers 
donnés par sys.path.
La variable sys.path est initialisée à partir:
* du dossier contenant le script ou le dossier courant
* PYTHONPATH
"""
import fibo

#import awesome
from awesome import utils
from awesome import *

print(fibo.fib(100))

print(fibo.fib2(100))

#print(awesome.utils.verlan)
print(utils.verlan("hello"))

utils.submodule_print()