# 🧠 Quote Generator

Ce projet est une application graphique développée avec Pygame et Pygame GUI, permettant d’afficher aléatoirement des citations philosophiques célèbres, accompagnées de leur auteur.
## 🎯 Objectif

Permettre à l’utilisateur de générer des citations inspirantes et profondes issues des plus grands penseurs de l’histoire, dans une interface simple, visuelle et interactive.

## Démo

[Demo](https://youtu.be/juR5DtQ52aw)

## 📁 Structure du projet

.
├── quote_generator.py       # Script principal de l'application Pygame
├── quotes.json              # Base de données de citations (format JSON)

## ⚙️ Installation et dépendances

Avant de lancer le projet, assure-toi d’avoir installé les modules suivants :

pip install pygame pygame_gui

## ▶️ Lancer l'application

Lance simplement le fichier quote_generator.py :

python quote_generator.py

Une fenêtre s’ouvre avec un bouton Play. En cliquant dessus, une citation aléatoire s’affiche au centre de l’écran.
📚 Contenu

    quotes.json contient plus de 100 citations de philosophes (Socrate, Nietzsche, Kant, Camus, etc.), structurées sous la forme :

{
  "Socrate": "\"Tout ce que je sais, c’est que je ne sais rien\"",
  "Albert Einstein": "\"Dieu ne joue pas au dé\"",
  ...
}

## 🎨 Interface

    Fond pastel (bleu clair)

    Texte centré et clair

    Police : Comic Sans MS (citation) et Times New Roman (titre)

    Couleurs vives pour une meilleure lisibilité

## 🛠 Fonctionnalités

    Génération aléatoire de citations à chaque clic sur le bouton Play

    Chargement dynamique depuis le fichier JSON

    Affichage optimisé et stylisé avec Pygame

## 🧩 À venir (idées d’amélioration)

    Ajouter un bouton “Copier” pour copier la citation dans le presse-papiers

    Ajouter une option de filtre par auteur

    Ajouter un mode “citation du jour”

## 👤 Auteur

Projet réalisé par Lesno(Charles Noah) — pour apprendre Pygame et partager un peu de sagesse.
