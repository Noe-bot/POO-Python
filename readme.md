# 1) Utilisation du polymorphisme

Le polymorphisme consiste en la création de classes héritées de parents mais qui conservent une base de fonctions communes, afin d'être adaptées à répondre à de multiples situations. Dans le cas de mon code, la classe **PasswordGuesserAdvanced** hérite de **PasswordGuesser**.

Lors de mes tests, je peux mettre en place un code de type :

```python
password = "password123"
pg_advanced = PasswordGuesserAdvanced(password)
l33ted_password = pg_advanced.l33t()
print(l33ted_password)
```

Ce code démontre l'utilisation du polymorphisme, car je traite l'objet **pg_advanced** comme une instance de la classe de base **PasswordGuesser** et j'appelle la méthode **l33t** spécifique à la classe dérivée, tout en conservant une interface commune.

# 2) Utilisation de l'encapsulation

L'encapsulation permet de cacher les détails de l'implémentation d'une classe en fournissant une interface publique (des méthodes d'accès) pour interagir avec les attributs.

Dans le cas de mon code, par exemple, les méthodes **to_lower(self)** et **to_upper(self)** de ma classe **PasswordGuesser** sont encapsulées, elles manipulent les données privées de password à travers un accès publiques.

# 3) Utilisation de la composition

La composition permet à une classe d'inclure des objets d'autres classes en tant que membres ou attributs pour construire des relations complexes entre objets en créant une structure hiérarchique.

Dans le cas de mon code, c'est dans l'implémentation des classes **PasswordModifier** et **PasswordModifierAdvanced** que nous pouvons observer un cas de composition. Elle se produit dans la fonction **generate_password_variants()**, où un objet **PasswordModifier** est créé et ensuite passé à la classe **PasswordModifierAdvanced** pour créer un objet **PasswordModifierAdvanced** composé de l'objet **PasswordModifier**.

# 4) Utilisation de l'héritage

L'héritage est la création d'une classe enfant à une classe parente qui héritera et aura accès aux méthodes de la classe parente.

Dans le cadre de mon code, l'exemple le plus basique serait la classe **PasswordGuesserAdvanced** qui hérite de la classe **PasswordGuesser**.

# 5) Utilisation d'interface

Une interface définit un ensemble de méthodes communes et garantit un comportement cohérent pour les classes qui l'implémentent, tout en favorisant la modularité, la réutilisabilité et la polymorphie.

En python, il n'y a pas la possibilité d'implémenter d'interfaces, mais pour se rapprocher d'un exemple similaire, j'aurais pu utiliser un code tel que :

```python

from abc import ABC, abstractmethod

class PasswordGuesserInterface(ABC):
    @abstractmethod
    def process_password(self, password):
        pass

class PasswordGuesser(PasswordGuesserInterface):
    def process_password(self, password):
        pass

```

# 6) Utilisation de méthodes et attributs d'objets

Les méthodes sont les fonctions définies dans les classes et les attributs d'objet sont leurs paramètres. Les attributs d'objet sont des variables définies à l'intérieur d'une classe et utilisées pour stocker des valeurs spécifiques pour chaque instance de l'objet.

Dans mon code, la classe **PasswordGuesser** contient les méthodes **to_lower()**, **to_upper()** et **capitalize()** par exemple. Elles prennent **self** en tant que premier paramètre implicite et opèrent sur l'attribut **self.password**.

# 7) Utilisation de méthodes et attributs statiques

Les attributs statiques sont définis en dehors des méthodes de la classe et sont réutilisables par ces dernières.

Par exemple, dans mon code, la classe **PasswordGuesserAdvanced** contient un attribut statique **l33t_dict** qui est réutilisé plus tard dans une méthode en l'appelant avec **self.l33t_dict**.

Les méthodes statiques, quant à elles, sont des méthodes qui n'ont pas accès aux instances de la classe dans laquelle elles sont instanciées.

Par exemple, dans mon code, nous avons dans la classe **PasswordGuesserAdvanced** :

```python

@staticmethod
def get_l33t_dict():
    return PasswordGuesserAdvanced.l33t_dict
```

que nous pouvons appeler si nous voulons voir le dictionnaire **l33t_dict**.

# 8) Utilisation de méthodes et attributs de classe

Les méthodes de classe sont des méthodes associées à la classe elle-même plutôt qu'à une instance spécifique de cette classe. Elles sont typiquement utilisées pour initialiser des variables de classe.

Dans le cadre de mon code, j'ai implémenté une méthode qui vérifie si la date fournie est valide. C'est la méthode **is_valid_date** de la classe **PasswordGuesserDate**.
