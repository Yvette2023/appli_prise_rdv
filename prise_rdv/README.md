Présentation du projet prise_rdv pour créer l'application mon_appli

Ce projet est une application web de gestion de rendez-vous pour les clients d'un coach en développement personnel.
Fonctionnalités

L'application permet aux utilisateurs de planifier des rendez-vous avec leur coach. Les utilisateurs peuvent :

    Planifier un rendez-vous en choisissant une date, une heure de début, une durée et en ajoutant des notes.
    Voir une liste de leurs rendez-vous passés.
    Les utilisateurs ne peuvent voir que leurs propres rendez-vous.



Le projet utilise deux modèles :

1. Coach
   Le modèle Coach contient les informations sur le coach, telles que son nom et son identifiant.

2. Appointment
   Le modèle Appointment contient les informations sur les rendez-vous, telles que la date, l'heure de début, la durée, les notes et le client qui a réservé le rendez-vous.


Le projet utilise plusieurs vues :

1. Home
   La vue home affiche simplement une page d'accueil.

2. AppointmentCreateView
   La vue AppointmentCreateView permet aux utilisateurs de créer un nouveau rendez-vous. Elle vérifie également que le créneau horaire demandé n'est pas déjà réservé par un autre rendez-vous.

3. AppointmentsHistory
  La vue AppointmentsHistory affiche une liste des rendez-vous passés de l'utilisateur connecté.


Technologies utilisées
Le projet utilise Django, un framework web écrit en Python. Il utilise également une base de données SQLite pour stocker les informations sur les rendez-vous et les utilisateurs.

Installation et utilisation
Pour utiliser l'application, vous devez :

    Cloner le projet depuis Github.
    Installer les dépendances en exécutant la commande pip install -r requirements.txt.
    Exécuter la commande python manage.py migrate pour créer la base de données.
    Exécuter la commande python manage.py runserver pour lancer le serveur.

Une fois le serveur lancé, vous pouvez accéder à l'application en ouvrant votre navigateur et en naviguant vers http://localhost:8000.

Ce projet a été créé par Yvette Ingabire.
