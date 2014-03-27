Galax
=====

Galax - Jeu de domination spatiale par tour de jeu - Gestion de projet hiver 2014

Galax
Jeu de domination spatiale, par tour de jeu (turn-based)

Un humain au commande d'un flotte doit conquérir l'ensemble des étoiles appartenant aux civilisations Czin et Gubru, (ou Indépendant qui sont essentiellement des NPC) avant que ces derniers ne deviennent invincibles et conquièrent l'univers.
Chaque étoile dispose d'un certains nombres de manufactures qui génèrent de 0 à 6 vaisseaux par tour.

Situation de départ
Chaque civilisation dispose d'une étoile à l'origine qui compte 10 manufactures et 100 vaisseaux.

Comment jouer
On joue à ce jeu en formant des flottes qu'on dirige vers des étoiles afin de les conquérir.

Préparation des flottes
Chaque protagoniste peut créer autant de flottes qu'il le désire, à partir des vaisseaux qui sont au port.
Chaque flotte prendra un certain temps pour se rendre à destination, calculé en dixième d'année. Une flotte aura typiquement une quantité de vaisseaux, une destination et une année d'arrivée calculée dès le départ, suivant la fonction suivante :
Si distance <= 2
    durée = distance / 2
sinon
    durée = 1 + ((distance- 2) / 3)

Lorsque le joueur humain a terminé de préparer ses flottes, il entame "la guerre", à savoir passer la main afin que les autres puissent préparer leurs flottes, puis que l’ordinateur procède à faire avancer le jeu d’un an .
Alors, le système fait l'analyse de la situation en faisant se dérouler l'année en dixième et évalue la situation de chaque flotte pour chaque dixième.


Combat
Si une flotte arrive à une étoile qui disposent d'une flotte ennemi (Indépendant, Gubru ou Czin), le combat est automatiquement entamé jusqu'à l'annihilation d'une des flottes protagonistes.
Lorsqu'on s'empare d'une étoile, ses manufactures nous appartiennent et produisent pour nous.
Typiquement, le combat se déroule ainsi:
Le défenseur attaque la force d'invasion avec 70% de chance d'éliminer un vaisseau.
L'envahisseur attaque à son tour
On poursuit ainsi à tour de rôle jusqu'à l'anéantissement d'une des deux forces en présence
Si l'envahisseur est vainqueur, il prend possession de l'étoile et de ses manufactures

Attaque surprise
Lorsque les effectifs de la flotte d'attaques sont moindres que celles des défenseurs, ils peuvent parvenir à faire une attaque surprise, c'est à dire qu'ils ont alors la capacité d'attaquer les premiers.
La probabilité P de l'effet de "surprise" se calcule ainsi:
r= nombre de défenseurs / nombre d'envahisseurs
si r<5
P= r/10
sinon
si r<20
P= (3*r + 35) /100
sinon
P=0.95

Intelligence
Si on sélectionne une étoile n'appartenant pas à notre civilisation, on peut obtenir de l'information sur celle-ci dans certains cas:
Niveau 0: Les informations concernant une étoile sont inconnues avant qu'on y ait envoyé un vaisseau. 
Niveau 1:  Lorsqu'on envoie des vaisseaux, on obtient le nombre de vaisseaux résidant sur l’étoile au moment de l'arrivée. 
Niveau 2: On découvre la capacité manufacturière de l'étoile lors d'un envoi subséquent.
Niveau 3: On obtient l'information en temps réel sur cette étoile après trois visites.
Naturellement, si une étoile nous appartient ou nous déjà appartenue, on reste au niveau 3.

Stratégie des Gubru
Les  Gubru adoptent une stratégie d'envahissement au plus près. Ils essaiment progressivement vers l'extérieur, relativement à leur étoile principale.
Les Gubrus se choisissent une étoile-mère, à savoir la première de la liste des étoiles leur appartenant. Ceci fait une différence seulement si leur étoile-mère a été conquise.

Puissance d'attaque
La force_attaque = max de 
temps_courant * nbr_vaisseaux_par_attaque + force_attaque_basique)
OU
force_attaque_basique * 2
Valeurs
nbr_vaisseaux_par_attaque = 5
force_attaque_basique =10

Formation de flotte
Si le nombre de vaisseaux sur l'étoile-mère est plus grande que
 force_attaque +force_attaque_basique, alors les Gubru créent des flottes.
Chaque flotte aura force_attaque nombre de vaisseaux. Ainsi ils formeront autant de flottes que le nombre de vaisseaux le permet. Ces flottes sont envoyées vers les étoiles les plus proches qui ne sont pas dans l'empire Gubru. Tous les vaisseaux retournent à l'étoile-mère après une conquête, à moins que le nombre de vaisseaux soit plus grand que 25, auquel cas, ils laissent une force de 15 vaisseaux et envoient le reste . Subséquemment quand le nombre de 25 est dépassé, ils envoient le surplus (plus grand que 15) vers l'étoile-mère.

Stratégie des Czin
La stratégie de base des Czin est d'assimilé les étoiles par grappes, à savoir un nombre d'étoiles assez rapprochées les unes des autres, d'y établir une base, d'augmenter les effectifs sur cette base jusqu'à être prêt à aller conquérir une autre grappe.
Si une base devient trop isolée, les effectifs sont transférés vers l'étoile-mère.
Les Czin font une Armada qu'ils envoient vers l'étoile centrale de la grappe choisit. Après cette conquête, ils tentent de conquérir le reste de la grappe en éventail, séparant l'armada en flottes diverses.

Déterminer une grappe
Initialiser la valeur_grappe de chaque étoile à 0. 
Pour chaque étoile i
    Pour chaque étoile j
        si la distance entre i et j <= distance_grappe
            alors s= distance_grappe - distance +1
            ajouter s*s à la valeur_grappe (de i? )

La valeur de distance_grappe est de 4.
Les Czin choisissent en vertu d'une équilibre entre la valeur_grappe et la distance de la base courante (au début l'étoile-mère)
La nouvelle base est choisi avec la fonction suivante
    pour chaque étoile
        si la valeur_grappe = 0 alors la valeur_base = 0
        sinon valeur_base = valeur_grappe -3 * distance

Choix des attaques
force_attaque = temps_courant * nbr_vaisseaux_par_attaque * force_attaque_basique
où nbr_vaisseaux_par_attaque=4 et force_attaque_basique=20

Les Czin utilisent divers modes
Le mode rassemblement_forces : retourner les vaisseaux vers la base depuis les étoiles qui sont à distance_rassemblement (6 ans). S'il n'y a plus d'étoiles à cette distance de la base, changer la base pour l'étoile-mère (aussi, si la base a été conquise).

Les Czin laissent une garnison de 3 vaisseaux sur les étoiles avant d'envoyer le reste se rassembler sur la base.

Si le mode est rassemblement_forces et que la base est rendu à une force de création d'Armada (3* force_attaque), on envoie l'ensemble de cette en armada vers une nouvelle base prospective, on change le mode pour etablir_base.
Si on est à etablir_base jusqu'à ce que l'armada arrive à sa destination. Si elle gagne cette étoile, elle essaime vers les étoiles de la grappe, avec des flottes de force_attaque vers les étoiles les plus proches. Le temps maximal d'atteinte est noté et on passe en mode conquerir_grappe.

Si la base n'est pas conquise on fait de l'étoile-mère notre base et on passe en mode rassemblement_force.
si on est en mode conquerir_grappe, et que la dernière flotte est rendue, on passe en mode rassemblement_force.

Déroulement
Le temps est initialement à 0, à chaque tour, on offre au Gubru de jouer (faire des flottes), puis au Czin.
On incrémente le temps courant de 0.1, on vérifie si des flottes pour chaque civilisation (Humain, Gubru, Czin) sont arrivées à destination (le cas échéant on procède aux attaques).  après 10 incréments, si la partie n'est pas terminée, on mets à jour les étoiles (on ajoute les vaisseaux par manufacture), et on recommence.

Fin de partie
La partie se termine s'il ne reste aucune ressource au Gubru et au Czin - Humain a remporté la victoire.
Si les Humains perdent toutes leurs ressources, le joueur perd. Point!!!

 
Interface classique sur Macintosh plus (circa 1986)
 

NOTES d'interface
Il manque un widget d'interface pour que le joueur demande de démarrer le "prochain tour" (qui fait faire le travail de passage d'une année) Dans l'original sur Mac cette fonction se trouvait sous un menu en item version "ordinaire" et un en version rapide.
Dans la version "ordinaire" un dialogue venait montrer la situation à l'arrivée de chaque flotte humaine vers une destination où se trouvait décrite la situation (combat coup-par-coup, renforcement) ainsi que toute flotte ennemie arrivant sur une étoile humaine.
Dans le coin inférieur droit, on trouvait des informations sur ce que l'ordinateur faisait pendant l'exécution du "prochain tour", à savoir, choix des Gubru, choix des Czin, combat année n.1, n.2,  etc.


