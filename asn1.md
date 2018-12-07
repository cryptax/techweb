# ASN.1

## ASN.1 tags

Les valeurs entre crochets [] sont appelees des tags, et leur but ultime est d'
viter toute ambiguite d'encodage.

**Taggage implicite**: la valeur du tag remplace la valeur du "T" dans l'encodage BE
R (type TLV)

```
Exemple : Toto ::= CHOICE {
			gauche [0] IMPLICIT NULL,
			droite [1] IMPLICIT NULL
		   }
```

Si on ne met pas les tags [0] ou [1], on ne peut pas differencier un NULL "gauch
e" d'un "droite".

Le fait de mettre des tags, la valeur du tag remplace la valeur du Type (ici un 
Null). L'encodage d'un NULL gauche sera donc `00-01-00`, et pour un droite `01-01-00`.

**Taggage explicite**: on encapsule la donnee dans un nouveau TLV, avec pour T la va
leur du tag.

Exemple : `Tata ::= [2] EXPLICIT INTEGER` avec valeur 7, sera encode `02-03-01-01-07è. 

Pour eviter de se fatiguer a mettre tantot `IMPLICIT`, tantot  `EXPLICIT`, on peut specifier le mode general de l'environnement.

- a) IMPLICIT TAGS : tout est tagge de par defaut sous forme IMPLICIT sauf les Choice* et les elements marques `EXPLICIT`
- b) EXPLICIT TAGS: tout est tagge par defaut `EXPLICIT`, sauf les elements marques IMPLICIT.
- c) AUTOMATIC TAGS: le taggage est effectue automatiquement, en commencant par 0,  de maniere implicite - sauf pour les sequences ou sets qui comportent des tags (alors pas de taggage automatique), et sauf pour les Choices.

* Un choice ne peut pas etre tagge implicitement. 

En effet, si on mettait 

```
TotoPrime ::= CHOICE [2] {
			gauche [0] IMPLICIT NULL,
			droite [1] IMPLICIT NULL
		   }
```
alors quelque soit le null (gauche ou droite), son type serait remplace par le t
ag 2. En consequence, l'ASN.1 interdit le taggage implicite du choice.

NB. Ne pas confondre le cas Toto (on tagge des NULLs) et TotoPrime (on tagge un 
choice).
