+++
title       = "Changelog — Tornade Audio Player"
description = "Historial de versiones y notas de lanzamiento de Tornade — el reproductor de audio nativo FLAC y lossless para macOS, Windows, Linux y Terminal."
date        = "2026-03-12"
draft       = false

[params]
  ogTitle       = "Tornade Changelog — Historial de versiones"
  ogDescription = "Sigue cada versión de Tornade, el reproductor de audio lossless impulsado por Rust. Nuevas funciones, correcciones y mejoras."
  ogType        = "website"
+++

## v0.5.0 (2026-03-12)

### Añadido
- Mejoras en la reproducción lossless FLAC y ALAC: transiciones gapless y búsqueda sample-accurate
- Soporte de audio hi-res hasta 32 bits / 384 kHz para archivos FLAC, WAV y AIFF
- macOS: nuevo sistema de fondo ambiental basado en los colores dominantes de la portada
- TUI: superposición de atajos de teclado (pulsar `?` para mostrar)

### Corregido
- Los archivos OGG Vorbis con frecuencias de muestreo no estándar ya no causan tartamudeo
- El escaneo de biblioteca ya no omite archivos FLAC con portadas de alta resolución (> 2 MB)

### Cambiado
- Motor de audio Rust actualizado — uso de memoria reducido ~15% en bibliotecas grandes

---

## v0.4.2 (2026-02-10)

### Añadido
- Búsqueda global entre pistas, álbumes, artistas y géneros
- macOS: binario universal que soporta Intel y Apple Silicon nativamente

### Corregido
- Los archivos WAV codificados con codecs no PCM ahora informan correctamente de formato no soportado
- Los metadatos AIFF (título, artista, álbum) ahora se leen correctamente en macOS

---

## v0.4.0 (2026-01-20)

### Añadido
- Reproducción de FLAC, OGG, MP3, WAV y AIFF en todas las plataformas
- Interfaz Terminal (TUI) construida con ratatui — gratuita y de código abierto, funciona por SSH
- Cola de reproducción en tiempo real con reordenación por arrastrar y soltar (GUI macOS)
- Escaneo de biblioteca local y en red
- macOS: prueba gratuita de 30 días, luego compra única de 9,99 €

### Cambiado
- Motor de audio core reescrito en Rust para menor latencia y seguridad de memoria
