# Final-project-
Bonjour,
Nous avons utilisé l'application visual studio code pour faire notre code. Le code est fonctionnel. En ayant le fichier avec le code et le document data_real.csv dans un même fichier, nous obtenons 6 fichiers en plus : 

-cecal_samples (fichier csv, données extraites) contenant que les valeurs des régions cecal
-cecal_samples (image png, graphique) graphique représentant le log lives bactérias en fonction des traitements

-fecal_samples (fichier csv, données extraites) contenant que les valeurs des régions fecal
-fecal_samples (image png, graphique) graphique représentant le log lives bactérias en fonction des jours de traitement

-ileal_samples (fichier csv, données extraites) contenant que les valeurs des régions ileal
-ileal_samples (image png, graphique) graphique représentant le log lives bactérias en fonction des traitements

Notre code fonctionne pour ce fichier, mais si on veut utiliser un autre fichier :

il faut modifier ligne 248, car 'for mouse_Id in range(17, 33)', bloque le code au 16 souris de l'expérience, donc si on veut plus de souris, il faut modifier avec en premier, le numéro ID de la première souris et en deuxième le numéro ID de la dernière souris +1, ce qui donne:
For mouse_Id in range(fit mouse ID, last mouse ID+1).

Les fichiers créés sont placés dans le même dossier que celui qui contient le code, si on veut créer des dossiers spéciaux pour chaque fichier créé, il faut mettre
Output_ileal = 'file_name\ileal_samples.png' à la place de output_ileal = 'ileal_samples.png' et pareil pour les autres fichiers de sortie.


Nous n'avons pas réussi à créer la légende dans les graphiques, ce qui les rend plus difficiles à lire. Mais pour les graphiques iléal and cecal, à gauche les courbes représentent les courbes du mélange ABX et les courbes de droite représentent les courbes des placebo, et pour le graphique fecal, les courbes jaunes sont les courbes placebo et les courbes bleus sont les courbes du mélange ABX.


Nous pensons néanmoins qu'il est possible de raccourcir notre code puisque nous rappelons à chaque fois les fonctions, mais le code est fonctionnel donc on le garde. Il y a beaucoup de fonctions car c'était le plus simple pour nous pour les écrire et les tester et surtout plus simple pour travailler à deux. Mais cela permet aussi à quelqu'un de récupérer les fonctions qui l'intéressent et dont il a besoin pour son travail.

Nous vous remercions par la même occasion pour le temps que vous nous avez porté pour l'apprentissage de l'informatique et du code.

Pour toute question vous pouvez nous contacter par mail aux adresses suivantes : fr.rastello@gmail.com et alban.aguesse@gmail.com

Bonne journée,

Bien à vous,

François RASTELLO et AGUESSE Alban
préing 2 BTC TD1
Groupe projet n° 30 (Alban AGUESSE et François RASTELLO) 



# Final-project-
Hello,
We used the visual studio code application to make our code. The code is functional. Having the file with the code and the document data_real.csv in one file, we get 6 more files: 

-cecal_samples (csv file, extracted data) containing only the values of the cecal regions
-cecal_samples (png image, graphic) graph representing the bacteria log lives according to treatments

-fecal_samples (csv file, extracted data) containing only the values of the fecal regions
-fecal_samples (png image, graphic) graph representing the bacteria log lives according to the days of treatment

-ileal_samples (csv file, extracted data) containing only the values of the ileal regions
-ileal_samples (png image, graphic) graph representing the bacteria log lives according to treatments

Our code works for this file, but if we want to use another file:

you have to modify line 248, because 'for mouse_Id in range(17, 33)', blocks the code at 16 mouse of the experiment, so if you want more mice, you have to change with first, the ID number of the first mouse and second the ID number of the last mouse +1, which gives:
For mouse_Id in range(fit mouse ID, last mouse ID+1).

The created files are placed in the same folder as the one containing the code, if you want to create special folders for each created file, you must put
Output_ileal = 'file_name ileal_samples.png' instead of output_ileal = 'ileal_samples.png' and the same for other output files.

We were unable to create the legend in the charts, which makes them harder to read. But for the ileal and cecal graphs, on the left the curves represent the curves of the ABX mixture and the curves on the right represent the curves of the placebos, and for the fecal graph, the yellow curves are the placebo curves and the blue curves are the curves of the ABX mixture.

We think it is possible to shorten our code since we recall the functions each time, but the code is functional so we keep it. There are many functions because it was the easiest for us to write and test them and especially easier to work together. But it also allows someone to recover the functions that interest him and he needs for his work.

We also thank you for the time you have given us to learn computer science and code.

If you have any questions, please contact us by email at the following addresses: fr.rastello@gmail.com and alban.aguesse@gmail.com

Have a good day,

Good to you,

François RASTELLO and AGUESSE Alban
preing 2 BTC TD1
Project group 30 (Alban AGUESSE and François RASTELLO) 

