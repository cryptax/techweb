# How to create a hardware badge with colours and shape



| Couche | Couleur | Description       |
| ------ | ------- | ----------------- |
| Drill | 
| F. Silk | Blanc | Couche de sérigraphie |
| F. Mask | Vert, | Masque de soudure du haut. Par défaut on indique là où on ne veut pas de masque de soudure |
| F. Cu | Argent | Cuivre |
| B. Silk |
| B. Mask |   | Masque de soudure du bas |
| B. Cu | Argent | Cuivre, couche du bas. Attention, à l'envers |
| Edge Cuts | - | Découpe |


Cuivre + Masque de soudure vert = Bleu Clair
Cuivre sur bakélite = Bleu foncé

On ne peut pas déposer de couche de sérigraphie sur le PCB directement, il faut du masque de soudure dessous.

References:

- https://github.com/badgeek/svg2shenzhen
- https://www.seeedstudio.com/blog/2018/12/25/making-christmassy-pcb-art-with-inkscape-svg2shenzhen-and-kicad/
- https://medium.com/@urish/a-practical-guide-to-designing-pcb-art-b5aa22926a5c
