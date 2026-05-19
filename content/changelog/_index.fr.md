+++
title       = "Changelog - Tornade Audio Player"
description = "Historique des versions et notes de mise à jour de Tornade, le lecteur audio natif FLAC et lossless pour macOS, Windows, Linux et Terminal."
date        = "2026-03-12"
draft       = false

[params]
  ogTitle       = "Tornade Changelog - Historique des versions"
  ogDescription = "Suivez chaque version de Tornade, le lecteur audio lossless propulsé par Rust. Nouvelles fonctionnalités, corrections et améliorations."
  ogType        = "website"
+++

## v1.8.0 (2026-05-16)

### Ajouté
- Barre de menu : menu clic droit pour afficher/masquer les infos de piste et cacher le lecteur
- Double-clic joue immédiatement par défaut

### Corrigé
- Sélection de piste, double-clic, sélection par plage (shift) et réordonnancement par glisser fiabilisés
- Gestion des clics cassée par le comportement de sélection de texte sous macOS 26
- Poignée de drag déplacée en colonne de tête, isolée des taps de ligne
- Reconnexion NAS réduite à une seule tentative pour éviter les empilements
- Description du comportement double-clic dans la modal de bienvenue corrigée

---

## v1.7.0 (2026-05-10)

### Ajouté
- Lecteur dans la barre de menu : contrôlez la lecture depuis la barre de menu macOS sans ouvrir la fenêtre de l'app (titre, artiste, lecture/pause, piste suivante)
- Sélection multiple dans les playlists : sélectionnez plusieurs pistes à la fois pour les déplacer, supprimer ou réordonner
- Éditeur de tags : modifiez les métadonnées FLAC (titre, artiste, album, année, genres, numéro de disque) directement dans l'app, avec upload de pochette et scraping MusicBrainz
- Édition de métadonnées en lot pour les sélections multi-pistes
- "Modifier les métadonnées" au clic droit sur les pochettes d'album
- Panneau de préférences (barre de menu, mise à jour auto, qualité de lecture)
- Modal de bienvenue au premier lancement

### Corrigé
- Invalidation du cache de pochettes après modification des tags
- Tri par date d'ajout, rafraîchissement auto de la bibliothèque après scraping en lot
- Correction de la signature Developer ID pour macOS 26.4.1

---

## v1.6.0 (2026-05-01)

### Ajouté
- Ouverture automatique de la modale "Scanner la bibliothèque" sur bibliothèque vide
- Bouton d'annulation sur la bannière de reconnexion NAS
- Navigation vers la playlist "Importée" après import de fichier M3U
- Les playlists importées conservent la date d'ajout des pistes

### Corrigé
- Prévention de l'ouverture de plusieurs instances de l'app
- Accumulation du volume à la molette
- Mise à jour du panneau de playlists après glisser-déposer
- Conformité sandbox App Store (suppression API privée NetFS, Sparkle en weak-link)
- Stockage de l'activation de licence migré vers UserDefaults
- La recherche de genres utilise désormais le moteur tornade-core

---

## v1.5.0 (2026-03-25)

### Corrigé
- Icône de l'application non affichée correctement dans certains contextes
- Race condition sur la bannière NAS au chargement de la bibliothèque
- État de navigation album réinitialisé incorrectement entre les vues
- État de pause non rafraîchi après un changement de piste

---

## v1.4.0 (2026-03-24)

### Modifié
- Le DMG macOS est désormais signé avec un Developer ID et notarisé par Apple, plus besoin de contourner Gatekeeper à l'installation

---

## v1.3.0 (2026-03-23)

### Ajouté
- Réorganisation par glisser-déposer dans la file de lecture (trackpad et souris)

---

## v1.2.0 (2026-03-12)

### Ajouté
- Mise à jour automatique via Sparkle 2.x: Tornade vérifie et installe les mises à jour automatiquement
- Système de licence : essai gratuit 30 jours, achat unique, activation en ligne avec limite d'appareils
- Reconnexion automatique au NAS après veille macOS ou perte réseau
- Recherche floue sur les pistes, albums, artistes et genres
- Section artistes en featuring dans la vue détail album
- Import de playlists M3U depuis la modale Bibliothèque
- Genres affichés dans le panneau d'informations de l'album
- Segments de chargement animés sur la barre de progression lors du chargement d'une piste NAS
- Bouton "Nettoyer la bibliothèque" pour supprimer les albums et artistes orphelins
- Effet de halo ambiant au niveau de l'application avec panneau de file arrondi
- Localisation complète de l'application (254 chaînes via le catalogue xcstrings)

### Corrigé
- Pistes dupliquées dans la file causant une boucle infinie
- Le shuffle ignorait la sélection explicite d'une piste dans la file
- Photos d'artistes absentes des résultats de recherche globale
- Option+double-clic ajoute désormais la piste à la file et la joue immédiatement sans vider la file

---

## v1.1.0 (2026-02-25)

### Ajouté
- Pipeline de soumission App Store avec montage NAS compatible sandbox

---

## v1.0.0 (2026-02-25)

### Ajouté
- Lecture FLAC, OGG, MP3, WAV et AIFF sur macOS
- Interface native macOS en SwiftUI
- Bibliothèque musicale SQLite avec scan local et réseau
- File de lecture en temps réel
- Interface Terminal (TUI) construite avec ratatui, gratuite et open source, fonctionne via SSH
- Moteur audio core écrit en Rust
