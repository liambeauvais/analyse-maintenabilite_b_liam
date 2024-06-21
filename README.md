# analyse-maintenabilite_b_liam

## Sommaire

- [Exercice 1](#Exercice-1)
    - [Question 1](#Question-1)
    - [Question 2](#Question-2)
    - [Question 3](#Question-3)
    - [Question 4](#Question-4)
- [Exercice 2](#Exercice-2)
    - [Installer et lancer le projet](#Installer-et-lancer-le-projet)
    - [Executer les tests](#Executer-les-tests)
    - [Commentaires](#Commentaires)

## Exercice 1

### Question 1
> Les principales sources de comp^lexité dans un système de logiciel sont:
> - Taille du code : Plus le code est volumineux, plus il devient difficile de le comprendre et de le maintenir.
> - Interdépendances : Les dépendances entre différents modules ou composants peuvent compliquer les modifications et les tests.
> - Évolution des exigences : Les changements fréquents des spécifications peuvent compliquer le développement et la maintenance.
### Question 2
> le fait de programmer vers une interface et non vers une implémentation procure plusieurs avantages:
> - Flexibilité : Permet de changer l'implémentation sans affecter le code qui utilise l'interface.
> - Testabilité : Facilite le remplacement des implémentations concrètes par des versions de test ou des mocks.
> - Réutilisabilité : Encourage la réutilisation de code en fournissant une couche d'abstraction.
### Question 3
> - "First make it run" : L'objectif initial est de produire un prototype fonctionnel, même s'il est imparfait.
> - "Next make it correct" : Une fois que le système fonctionne, l'étape suivante est d'assurer qu'il fait ce qu'il doit faire correctement, en éliminant les bugs et en respectant les spécifications.
> - "Only after that worry about making it fast" : L'optimisation des performances ne doit être envisagée qu'après avoir un système stable et correct, afin de ne pas introduire de complexités prématurées. 

> D'une manière plus globale, je pense que cette heuristique recommande de se concentrer sur la fonctionnalité de base avant de se soucier de la perfection et des performances, en évitant ainsi les pièges de l'optimisation prématurée.
### Question 4
> - Tests unitaires : Avant de commencer le refactoring, assurez-vous d'avoir une couverture de tests suffisante pour détecter toute régression.
> - Refactorings petits et itératifs : Effectuez des changements en petites étapes, en testant à chaque étape pour s'assurer que le comportement du code reste correct.
> - Code Review : Faites réviser votre code par des pairs pour identifier d'éventuels problèmes et obtenir des suggestions d'amélioration.
> - Documentation : Documentez les modifications apportées pour faciliter la compréhension et la maintenance future du code.
> - Automatisation : Utilisez des outils de refactoring et d'analyse statique pour automatiser certaines tâches et garantir la qualité du code.
## Exercice 2

### Installer et lancer le projet
Pour lancer le projet, il vous faudra python, et créer un environnement virtuel python. \
Ensuite, vous pourrez accéder à votre environnement virtuel, puis lancer la commande `pip install -r requirements.txt`. \
Ensuite lancez la commande `python ./invoice.py`.

### Executer les tests
Lancez la commande `python -m pytest`

### Commentaires
    
