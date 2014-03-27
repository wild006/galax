Galax
=====

Galax - Jeu de domination spatiale par tour de jeu - Gestion de projet hiver 2014

Galax
Jeu de domination spatiale, par tour de jeu (turn-based)

Un humain au commande d'un flotte doit conqu�rir l'ensemble des �toiles appartenant aux civilisations Czin et Gubru, (ou Ind�pendant qui sont essentiellement des NPC) avant que ces derniers ne deviennent invincibles et conqui�rent l'univers.
Chaque �toile dispose d'un certains nombres de manufactures qui g�n�rent de 0 � 6 vaisseaux par tour.

Situation de d�part
Chaque civilisation dispose d'une �toile � l'origine qui compte 10 manufactures et 100 vaisseaux.

Comment jouer
On joue � ce jeu en formant des flottes qu'on dirige vers des �toiles afin de les conqu�rir.

Pr�paration des flottes
Chaque protagoniste peut cr�er autant de flottes qu'il le d�sire, � partir des vaisseaux qui sont au port.
Chaque flotte prendra un certain temps pour se rendre � destination, calcul� en dixi�me d'ann�e. Une flotte aura typiquement une quantit� de vaisseaux, une destination et une ann�e d'arriv�e calcul�e d�s le d�part, suivant la fonction suivante :
Si distance <= 2
    dur�e = distance / 2
sinon
    dur�e = 1 + ((distance- 2) / 3)

Lorsque le joueur humain a termin� de pr�parer ses flottes, il entame "la guerre", � savoir passer la main afin que les autres puissent pr�parer leurs flottes, puis que l�ordinateur proc�de � faire avancer le jeu d�un an .
Alors, le syst�me fait l'analyse de la situation en faisant se d�rouler l'ann�e en dixi�me et �value la situation de chaque flotte pour chaque dixi�me.


Combat
Si une flotte arrive � une �toile qui disposent d'une flotte ennemi (Ind�pendant, Gubru ou Czin), le combat est automatiquement entam� jusqu'� l'annihilation d'une des flottes protagonistes.
Lorsqu'on s'empare d'une �toile, ses manufactures nous appartiennent et produisent pour nous.
Typiquement, le combat se d�roule ainsi:
Le d�fenseur attaque la force d'invasion avec 70% de chance d'�liminer un vaisseau.
L'envahisseur attaque � son tour
On poursuit ainsi � tour de r�le jusqu'� l'an�antissement d'une des deux forces en pr�sence
Si l'envahisseur est vainqueur, il prend possession de l'�toile et de ses manufactures

Attaque surprise
Lorsque les effectifs de la flotte d'attaques sont moindres que celles des d�fenseurs, ils peuvent parvenir � faire une attaque surprise, c'est � dire qu'ils ont alors la capacit� d'attaquer les premiers.
La probabilit� P de l'effet de "surprise" se calcule ainsi:
r= nombre de d�fenseurs / nombre d'envahisseurs
si r<5
P= r/10
sinon
si r<20
P= (3*r + 35) /100
sinon
P=0.95

Intelligence
Si on s�lectionne une �toile n'appartenant pas � notre civilisation, on peut obtenir de l'information sur celle-ci dans certains cas:
Niveau 0: Les informations concernant une �toile sont inconnues avant qu'on y ait envoy� un vaisseau. 
Niveau 1:  Lorsqu'on envoie des vaisseaux, on obtient le nombre de vaisseaux r�sidant sur l��toile au moment de l'arriv�e. 
Niveau 2: On d�couvre la capacit� manufacturi�re de l'�toile lors d'un envoi subs�quent.
Niveau 3: On obtient l'information en temps r�el sur cette �toile apr�s trois visites.
Naturellement, si une �toile nous appartient ou nous d�j� appartenue, on reste au niveau 3.

Strat�gie des Gubru
Les  Gubru adoptent une strat�gie d'envahissement au plus pr�s. Ils essaiment progressivement vers l'ext�rieur, relativement � leur �toile principale.
Les Gubrus se choisissent une �toile-m�re, � savoir la premi�re de la liste des �toiles leur appartenant. Ceci fait une diff�rence seulement si leur �toile-m�re a �t� conquise.

Puissance d'attaque
La force_attaque = max de 
temps_courant * nbr_vaisseaux_par_attaque + force_attaque_basique)
OU
force_attaque_basique * 2
Valeurs
nbr_vaisseaux_par_attaque = 5
force_attaque_basique =10

Formation de flotte
Si le nombre de vaisseaux sur l'�toile-m�re est plus grande que
 force_attaque +force_attaque_basique, alors les Gubru cr�ent des flottes.
Chaque flotte aura force_attaque nombre de vaisseaux. Ainsi ils formeront autant de flottes que le nombre de vaisseaux le permet. Ces flottes sont envoy�es vers les �toiles les plus proches qui ne sont pas dans l'empire Gubru. Tous les vaisseaux retournent � l'�toile-m�re apr�s une conqu�te, � moins que le nombre de vaisseaux soit plus grand que 25, auquel cas, ils laissent une force de 15 vaisseaux et envoient le reste . Subs�quemment quand le nombre de 25 est d�pass�, ils envoient le surplus (plus grand que 15) vers l'�toile-m�re.

Strat�gie des Czin
La strat�gie de base des Czin est d'assimil� les �toiles par grappes, � savoir un nombre d'�toiles assez rapproch�es les unes des autres, d'y �tablir une base, d'augmenter les effectifs sur cette base jusqu'� �tre pr�t � aller conqu�rir une autre grappe.
Si une base devient trop isol�e, les effectifs sont transf�r�s vers l'�toile-m�re.
Les Czin font une Armada qu'ils envoient vers l'�toile centrale de la grappe choisit. Apr�s cette conqu�te, ils tentent de conqu�rir le reste de la grappe en �ventail, s�parant l'armada en flottes diverses.

D�terminer une grappe
Initialiser la valeur_grappe de chaque �toile � 0. 
Pour chaque �toile i
    Pour chaque �toile j
        si la distance entre i et j <= distance_grappe
            alors s= distance_grappe - distance +1
            ajouter s*s � la valeur_grappe (de i? )

La valeur de distance_grappe est de 4.
Les Czin choisissent en vertu d'une �quilibre entre la valeur_grappe et la distance de la base courante (au d�but l'�toile-m�re)
La nouvelle base est choisi avec la fonction suivante
    pour chaque �toile
        si la valeur_grappe = 0 alors la valeur_base = 0
        sinon valeur_base = valeur_grappe -3 * distance

Choix des attaques
force_attaque = temps_courant * nbr_vaisseaux_par_attaque * force_attaque_basique
o� nbr_vaisseaux_par_attaque=4 et force_attaque_basique=20

Les Czin utilisent divers modes
Le mode rassemblement_forces : retourner les vaisseaux vers la base depuis les �toiles qui sont � distance_rassemblement (6 ans). S'il n'y a plus d'�toiles � cette distance de la base, changer la base pour l'�toile-m�re (aussi, si la base a �t� conquise).

Les Czin laissent une garnison de 3 vaisseaux sur les �toiles avant d'envoyer le reste se rassembler sur la base.

Si le mode est rassemblement_forces et que la base est rendu � une force de cr�ation d'Armada (3* force_attaque), on envoie l'ensemble de cette en armada vers une nouvelle base prospective, on change le mode pour etablir_base.
Si on est � etablir_base jusqu'� ce que l'armada arrive � sa destination. Si elle gagne cette �toile, elle essaime vers les �toiles de la grappe, avec des flottes de force_attaque vers les �toiles les plus proches. Le temps maximal d'atteinte est not� et on passe en mode conquerir_grappe.

Si la base n'est pas conquise on fait de l'�toile-m�re notre base et on passe en mode rassemblement_force.
si on est en mode conquerir_grappe, et que la derni�re flotte est rendue, on passe en mode rassemblement_force.

D�roulement
Le temps est initialement � 0, � chaque tour, on offre au Gubru de jouer (faire des flottes), puis au Czin.
On incr�mente le temps courant de 0.1, on v�rifie si des flottes pour chaque civilisation (Humain, Gubru, Czin) sont arriv�es � destination (le cas �ch�ant on proc�de aux attaques).  apr�s 10 incr�ments, si la partie n'est pas termin�e, on mets � jour les �toiles (on ajoute les vaisseaux par manufacture), et on recommence.

Fin de partie
La partie se termine s'il ne reste aucune ressource au Gubru et au Czin - Humain a remport� la victoire.
Si les Humains perdent toutes leurs ressources, le joueur perd. Point!!!

 
Interface classique sur Macintosh plus (circa 1986)
 

NOTES d'interface
Il manque un widget d'interface pour que le joueur demande de d�marrer le "prochain tour" (qui fait faire le travail de passage d'une ann�e) Dans l'original sur Mac cette fonction se trouvait sous un menu en item version "ordinaire" et un en version rapide.
Dans la version "ordinaire" un dialogue venait montrer la situation � l'arriv�e de chaque flotte humaine vers une destination o� se trouvait d�crite la situation (combat coup-par-coup, renforcement) ainsi que toute flotte ennemie arrivant sur une �toile humaine.
Dans le coin inf�rieur droit, on trouvait des informations sur ce que l'ordinateur faisait pendant l'ex�cution du "prochain tour", � savoir, choix des Gubru, choix des Czin, combat ann�e n.1, n.2,  etc.


