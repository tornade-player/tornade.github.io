+++
title       = "Politique de confidentialité — Tornade"
description = "Politique de confidentialité de Tornade. Aucune donnée personnelle collectée."
date        = "2026-03-27"
draft       = false

[params]
  ogTitle       = "Politique de confidentialité — Tornade"
  ogDescription = "Tornade ne collecte aucune donnée personnelle. Tout le traitement s'effectue localement sur votre appareil."
+++

# Politique de confidentialité

*Dernière mise à jour : 27 mars 2026*

## Vue d'ensemble

Tornade est un lecteur de musique local multi-plateforme. Nous nous engageons à protéger votre vie privée.

## Collecte de données

**Tornade ne collecte aucune donnée personnelle, sur aucune plateforme.**

- Pas d'analyse ni de suivi
- Aucune donnée d'utilisation envoyée à des serveurs externes
- Aucun rapport de crash transmis sans votre consentement explicite
- Aucun identifiant publicitaire utilisé

## Traitement local

Toutes les opérations effectuées par Tornade se déroulent entièrement sur votre appareil :

- Scan et indexation de la bibliothèque musicale
- Lecture audio
- Lecture des métadonnées (artiste, album, titre)
- Chargement des pochettes

Aucun fichier musical, métadonnée ou historique d'écoute ne quitte jamais votre appareil.

## Détails par plateforme

### macOS — App Store

- **Achats** : entièrement gérés par le framework StoreKit 2 d'Apple. Aucune donnée de paiement n'est traitée par Tornade. Consultez la [politique de confidentialité d'Apple](https://www.apple.com/fr/legal/privacy/) pour plus de détails.
- **Mises à jour** : distribuées via le Mac App Store — aucun service de mise à jour externe n'est utilisé.
- **Réseau** : utilisé uniquement pour la vérification des achats StoreKit.

### macOS — Téléchargement direct

- **Vérification de licence** : votre clé de licence est validée auprès de notre serveur. Aucune information personnelle n'est transmise — uniquement la clé elle-même.
- **Mises à jour** : vérifiées automatiquement via [Sparkle](https://sparkle-project.org), un framework open-source. Seules votre version macOS et la version de l'app sont envoyées à notre flux de mise à jour.
- **Réseau** : utilisé uniquement pour les vérifications de licence et de mise à jour.

### Windows & Linux

- **Vérification de licence** : identique à macOS téléchargement direct — seule la clé de licence est transmise.
- **Mises à jour** : vérifiées via notre flux de mise à jour. Seules votre version d'OS et la version de l'app sont envoyées.
- **Réseau** : utilisé uniquement pour les vérifications de licence et de mise à jour.

### Interface Terminal (TUI)

- **Aucun accès réseau** : la version TUI ne se connecte à aucun service externe.
- **Aucun système de licence** : la TUI est open-source et gratuite.

## Conservation des données

Aucune donnée personnelle n'étant collectée, il n'y a rien à conserver ni à supprimer.
