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
