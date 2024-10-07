# Vocabulaire sur la pagination.

- L'espace d'adressage d'un processus est découpé en pages
- La mémoire physique est découpée en cadres
- Les pages et les cadres font la même taille
- Le contenu d'une page est stocké dans le cadre associé => le cadre "contient" la page
- Les processus utilisent des adresses logiques/virtuelles
- La mémoire physique utilise des adresses physiques
- Chaque page dans une table des pages possède des flags : ils donnent des informations sur la page
	- Dirty : si la page a été accédée en écriture, la MMU met ce bit à 1
	- Accessed : si la page a subi une lecture/écriture/exécution, mettre ce bit à 1
	- User/Supervisor : si = 1, la page est accessible par tout le monde, sinon elle n'est accessible uniquement par le noyau
	- Read/Write : si = 1, la page est en lecture/écriture, sinon elle est en lecture seule
	- Present : si = 1, alors la page est présente dans un cadre en mémoire physique, sinon elle n'est pas stockée en mémoire physique => y accéder provoque un défaut de page
- Chaque processus possède sa table des pages
- Quand un processus est créé, dans son espace d'adressage se trouveront les segments text, data et heap dont les pages seront associées à des cadres par la table des pages. Il y a également les pages associées au noyau. Toutes les autres adresses logiques de l'espace d'adressage du processus qui sont inutilisées n'auront pas de cadre associé par la table des pages.
- La table des pages associe chaque page avec un cadre
- La table des pages est stockée en mémoire physique dans un ou plusieurs cadres
- Soit un processus qui veut accéder à une adresse logique : 
	- la MMU possède un registre contenant l'adresse physique de début de la table des pages du processus courant : elle consulte cette adresse.
	- la MMU décompose l'adresse logique pour trouver la bonne entrée dans la table des pages : elle obtient l'adresse du cadre associé à la page
	- la MMU ajoute l'offset à l'adresse du cadre : l'adresse physique associée à l'adresse logique est maintenant formée
- Une entrée dans une table des pages est vide quand elle est composée uniquement de 0
- Si une page d'un processus est swappée, dans son entrée dans la table des pages, son bit Present passera à 0.
- Si une page d'un processus ne fait pas partie de son working set, le noyau pourra la swapper => la page est utilisée dans l'espace d'adressage du processus mais comme elle a été swappée, elle n'est pas stockée dans un cadre en mémoire donc son entrée dans la table des pages possède le bit Present à 0.
- Si un processus demande à accéder à une adresse logique d'une page qui avait été évincée (swap-out) : comme la page est non présente en mémoire physique, son bit Present est à 0 => la MMU lève une exception de type défaut de page et stocke l'adresse logique ayant provoquée le défaut de page dans un registre.  (raison = lecture d'une page évincée)
	- c'est le noyau qui traite le défaut de page : si l'accès à l'adresse logique est valide et qu'il reste assez de cadres libres en mémoire, le noyau rapatrie (swap-in) la page dans un cadre libre (page refault) et actualise la table des pages (dans l'entrée de la page : adresse du cadre et bit Present à 1). Si aucun cadre n'est libre, évincer (swap-out) une ou plusieurs pages de la mémoire physique pour libérer un ou des cadres selon une politique de remplacement (LRU, FIFO, ...). Si l'adresse logique demandée est invalide : exemple pointeur NULL, accès out-of-bound d'une entrée dans un tableau, ... => SEGFAULT.
- Le thrashing est le phénomène que peut subir un système d’exploitation s’il passe son temps à réaliser des opérations de swap de pages : les ressources de l’ordinateur sont monopolisées par l’activité de swap => ralentissement des applications utilisateurs

# Termes du papier

- reclaim pages : le noyau a besoin de cadres vides mais il n'y en a plus assez de libres en mémoire physique
=> il va devoir libérer des cadres non vides pour pouvoir stocker ce dont il a besoin (procédé appelé "reclaim"). 
Le choix des pages (appelée "reclaimable pages") à libérer dépend de plusieurs facteurs (faire le moins de dégâts possible) : 
	- page qui n'a pas été utilisée récemment par un processus (principe de localité temporelle, ne faisant partie d'aucun working-set) => algorithme LRU
	- évincer sur l'espace de swap des pages (ex : anonymous pages)
	- le contenu de la page est déjà présent autre part : page dans le page cache non-modifiée (si la page avait été modifiée, le noyau devra écrire les modifications sur le disque)
Les pages qu'il ne faut pas libérer sont appelées "unreclaimable pages". Exemple : page contenant des données du noyau.
- CPU contention : phénomène quand plusieurs processus sont en compétition pour accéder au CPU (tous en l'état prêt à tourner), le scheduler en choisira un seul pour s'exécuter donc certain processus ne seront mis sur le processeur que possiblement beaucoup plus tard 
- daemon : dans le sens strict, c'est un processus dont le père est le processus init. Plus généralement, un daemon est un processus s'exécutant en arrière plan. Les noms des processus daemon terminent par 'd'.
- kswapd : thread noyau qui est lancé au démarrage de l'ordinateur par kswapd_init(). Il est réveillé lorsque le nombre de cadres libres est en dessous de 'pages_low' (= threshold low-watermark) et il va continuer à libérer des cadres tant qu'il n'y a pas 'page_high' cadres de libres. Quand ça sera les cas, kswapd pourra retourner dormir.
- fonctionnement de mmap : 
	- (MAP_PRIVATE et MAP_SHARED => memory mapped files) crée une projection en mémoire physique d'un fichier sur le disque, un mapping entre les cadres contenant les données du fichier projeté et l'espace d'adressage du processus appelant est réalisé. Il y a la création d'un nouveau segment dans l'espace d'adressage du processus : celui-ci contient les données du fichier projeté. Avec MAP_SHARED, les changements sur les données du fichier sont répercutées sur le fichier sur le disque alors qu'avec MAP_PRIVATE, aucune modification n'est apportée sur le fichier sur le disque.
	- (MAP_ANONYMOUS => anonymous mappings) partage un bloc de mémoire rempli de zéros provenant de la mémoire physique qui n'est associé à aucun fichier à l'espace d'adressage du processus appelant.
- anonymous pages : page qui n'est associée à aucun fichier sur le disque. Contient les segments data, stack etc... des processus. Par exemple, pour étendre le stack ou le heap, des anonymous pages sont utilisées.
- file-backed pages : pages dans le page cache, pages contenant des données d'un fichier sur le disque. Si une file-backed page ne contient pas de données nouvellement écrites, le noyau pourra la reclaim.
- page cache : il contient des cadres de la mémoire physique dont ceux-ci contiennent des blocs de données d'un disque (fichiers). 
	Une page dans le page cache peut être partagée (shared page) si elle est utilisée par plusieurs processus, sinon si elle est possédée par un seul processus et qu'elle n'est pas partagée, on dit qu'elle est une page privée (private page).
	- Quand un processus lit des données d'un fichier, le noyau va regarder si elles sont dans le page cache. Si oui => cache hit, le noyaux n'a pas besoin d'accéder au disque. Si non => cache miss, le noyau va devoir accéder au disque : les données sont mises dans le page cache pour éviter des accès lents sur le disque pour les lectures futures. 
	- Quand un processus écrit dans un fichier, Linux utilise la stratégie de write-back. Le processus écrit les données directement dans le page cache et celles-ci seront mises sur le disque ultérieurement (= write-back). Les pages contenant les données à écrire sont dirty (appartiennent à la dirty list) dès que le contenu d'une page a été copié sur le disque, la page n'est plus dirty. Si le noyau veut reclaim une page dirty, il va d'abord devoir synchroniser son contenu sur le disque.
- Attention, le TLB (cache stockant les dernières traduction d'adresses virtuelles à physiques) et le page cache (cache stockant les dernières pages accédées) sont différents.
- Types de défauts de page : 
	- Minor page fault : le défaut de page sera réglé sans avoir à accéder au disque. Exemple : un processus veut accéder à une adresse logique d'une page inutilisée pour la première fois. Cette page n'a donc aucun cadre associé dans la table des pages donc l'entrée correspondante à cette page possède le bit Present à 0 => y accéder provoque un défaut de page. Le noyau va chercher un cadre libre en mémoire pour stocker cette page : s'il en trouve un, le défaut de page sera réglé sans avoir eu besoin d'accéder au disque : c'est donc une minor page fault.
	- Major page fault : le défaut de page sera réglé en accédant au disque. Exemple : un processus veut accéder à une page qui n'est pas présente en mémoire comme une page swapée sur le disque. 
- espace de swap Linux : partition sur le disque dur
- ZRAM : sur Linux, l'espace de swap peut être placé soit dans un fichier ou soit sur une partition du disque. Sur Android, ça n'est pas le cas. En effet, sur un système Android, l'espace de swap se trouve dans une partie de la RAM nommée zRAM. Chaque élément (page) placé dans la zRAM est compressé et chaque élément qui la quitte est décompressé.
Du fait que les pages soient compressées dans la zRAM, y évincer des pages permet de gagner de l'espace libre dans la RAM (une page compressée prend environ 25% de la place d'une page non compressée).
Il y a deux principaux avantages d'utiliser la zRAM pour y placer l'espace de swap : 
	- la vitesse des entrées-sorties par rapport à l'utilisation d'un disque 
	- des opérations d'écritures répétées sur le disque dues au swap raccourcirait sa durée de vie. 
	
	L'inconvénient est que la compression/décompression des pages peut être coûteuse pour le CPU.
La zRAM grandit ou rétrécit selon les pages qu'elle contient mais elle possède une taille maximale fixée par le constructeur : celle-ci est accessible avec la commande : ./adb shell cat /proc/meminfo dans le champ SwapTotal (2 Go sur mon mobile).
- refault distance : représente le temps entre le moment où la page a été évincée et le moment où la page a été rapatriée. On veut que ce temps soit le plus long possible : il est coûteux d'effectuer des opérations de swap trop souvent.
- garbage collector : gestion automatique de la mémoire, reclaim la mémoire qui a été allouée par un programme mais qui est maintenant inutilisée.
- cold start/launching : création du processus de l'application, se passe si l'application démarre pour la première fois depuis le démarrage du système ou si le système avait tué l'application.
- warm start/launching : les données de l'application ont été évincées et l'utilisateur lance l'application
- hot start/launching : toutes les données de l'application sont déjà en mémoire
- Out Of Memory (OOM) : état d'un système quand toute sa mémoire est pleine, même en comptant l'espace de swap. Sur Linux, il y a un mécanisme pour aider à combattre ce gros problème nommé OOM_Killer. Ce mécanisme consiste à tuer (SIG-KILL) un processus pour récupérer la mémoire voulue : le processus à tuer est choisi avec la fonction select_bad_process() qui utilise la fonction badness(). => chaque processus possède un "OOM-score" qui varie selon la mémoire utilisée par le processus et depuis quand il vit. La fonction badness() retourne cette valeur pour un processus donné. Le processus avec le plus haut "OOM-Score" sera tué. Il est possible d'ajusté le OOM_score avec OOM_score_adj : c'est une valeur sur l'intervalle [-1000, 1000] -> une valeur proche de -1000 réduit les chances que le processus soit tué par le OOM_Killer alors qu'une valeur proche de 1000 augmente les chances que le processus soit tué par le OOM_Killer. Sur Android, le daemon lmkd (version noyau >= 4.12) ou le pilote lmk (version noyau < 4.12) s'occupe de OOM_Killer.
