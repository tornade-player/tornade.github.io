+++
title       = "Changelog — Tornade Audio Player"
description = "Historique des versions et notes de mise à jour de Tornade — le lecteur audio natif FLAC et lossless pour macOS, Windows, Linux et Terminal."
date        = "2026-03-12"
draft       = false

[params]
  ogTitle       = "Tornade Changelog — Historique des versions"
  ogDescription = "Suivez chaque version de Tornade, le lecteur audio lossless propulsé par Rust. Nouvelles fonctionnalités, corrections et améliorations."
  ogType        = "website"
+++

## v0.5.0 (2026-03-12)

### Ajouté
- Améliorations de la lecture FLAC et ALAC lossless : transitions gapless et seek sample-accurate
- Support audio hi-res jusqu'à 32 bits / 384 kHz pour les fichiers FLAC, WAV et AIFF
- macOS : nouveau système de fond ambiant basé sur les couleurs dominantes de la pochette
- TUI : overlay des raccourcis clavier (appuyer sur `?` pour afficher)

### Corrigé
- Les fichiers OGG Vorbis avec des fréquences d'échantillonnage non standard ne causent plus de saccades
- Le scan de bibliothèque ne saute plus les fichiers FLAC avec une pochette haute résolution (> 2 Mo)

### Modifié
- Moteur audio Rust mis à jour — usage mémoire réduit d'environ 15% sur les grandes bibliothèques

---

## v0.4.2 (2026-02-10)

### Ajouté
- Recherche globale parmi les pistes, albums, artistes et genres
- macOS : binaire universel supportant Intel et Apple Silicon nativement

### Corrigé
- Les fichiers WAV encodés avec des codecs non-PCM signalent maintenant correctement le format non supporté
- Les métadonnées AIFF (titre, artiste, album) sont maintenant lues correctement sur macOS

---

## v0.4.0 (2026-01-20)

### Ajouté
- Lecture FLAC, OGG, MP3, WAV et AIFF sur toutes les plateformes
- Interface Terminal (TUI) construite avec ratatui — gratuite et open source, fonctionne via SSH
- File de lecture en temps réel avec réorganisation par glisser-déposer (GUI macOS)
- Scan de bibliothèque locale et réseau
- macOS : essai gratuit 30 jours, puis achat unique 9,99 €

### Modifié
- Moteur audio core réécrit en Rust pour une latence réduite et la sécurité mémoire
