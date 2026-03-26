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

## v1.5.0 (2026-03-25)

### Corregido
- Icono de la aplicación no mostrado correctamente en algunos contextos
- Condición de carrera en el banner NAS al cargar la biblioteca
- Estado de navegación de álbum reiniciado incorrectamente entre vistas
- Estado de pausa no actualizado tras el cambio de pista

---

## v1.4.0 (2026-03-24)

### Cambiado
- El DMG de macOS ahora está firmado con Developer ID y notarizado por Apple — no se necesita eludir Gatekeeper al instalar

---

## v1.3.0 (2026-03-23)

### Añadido
- Reordenación por arrastrar y soltar en la cola de reproducción (trackpad y ratón)

---

## v1.2.0 (2026-03-12)

### Añadido
- Actualizaciones automáticas vía Sparkle 2.x — Tornade comprueba e instala actualizaciones automáticamente
- Sistema de licencia: prueba gratuita de 30 días, compra única, activación en línea con límite de dispositivos
- Reconexión automática al NAS tras suspensión de macOS o pérdida de red
- Búsqueda difusa en pistas, álbumes, artistas y géneros
- Sección de artistas colaboradores en la vista de detalle de álbum
- Importación de listas de reproducción M3U desde el modal Biblioteca
- Géneros mostrados en el panel de información del álbum
- Segmentos de carga animados en la barra de progreso durante la carga de pistas NAS
- Botón "Limpiar biblioteca" para eliminar álbumes y artistas huérfanos
- Efecto de halo ambiental a nivel de aplicación con panel de cola redondeado
- Localización completa de la aplicación (254 cadenas vía catálogo xcstrings)

### Corregido
- Pistas duplicadas en la cola provocaban un bucle infinito
- El modo aleatorio ignoraba la selección explícita de pista en la cola
- Fotos de artistas no mostradas en los resultados de búsqueda global
- Option+doble clic ahora añade la pista a la cola y la reproduce de inmediato sin vaciarla

---

## v1.1.0 (2026-02-25)

### Añadido
- Pipeline de envío a App Store con montaje NAS compatible con sandbox

---

## v1.0.0 (2026-02-25)

### Añadido
- Reproducción de FLAC, OGG, MP3, WAV y AIFF en macOS
- Interfaz nativa macOS en SwiftUI
- Biblioteca musical SQLite con escaneo local y en red
- Cola de reproducción en tiempo real
- Interfaz Terminal (TUI) construida con ratatui — gratuita y de código abierto, funciona por SSH
- Motor de audio core escrito en Rust
