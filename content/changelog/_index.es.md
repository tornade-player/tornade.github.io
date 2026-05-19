+++
title       = "Changelog - Tornade Audio Player"
description = "Historial de versiones y notas de lanzamiento de Tornade, el reproductor de audio nativo FLAC y lossless para macOS, Windows, Linux y Terminal."
date        = "2026-03-12"
draft       = false

[params]
  ogTitle       = "Tornade Changelog - Historial de versiones"
  ogDescription = "Sigue cada versión de Tornade, el reproductor de audio lossless impulsado por Rust. Nuevas funciones, correcciones y mejoras."
  ogType        = "website"
+++

## v1.8.0 (2026-05-16)

### Añadido
- Barra de menú: menú clic derecho para mostrar/ocultar información de pista y ocultar el reproductor
- Doble clic reproduce inmediatamente por defecto

### Corregido
- Selección de pistas, doble clic, selección por rango (shift) y reordenación por arrastre mejorados
- Gestión de clics rota por el comportamiento de selección de texto en macOS 26
- Asa de arrastre movida a la columna inicial, completamente aislada de los taps de fila
- Reconexión NAS reducida a un solo intento para evitar acumulación de reintentos
- Descripción del comportamiento de doble clic en el modal de bienvenida corregida

---

## v1.7.0 (2026-05-10)

### Añadido
- Reproductor en la barra de menú: controla la reproducción desde la barra de menú de macOS sin abrir la ventana de la app (título, artista, reproducir/pausar, siguiente pista)
- Selección múltiple en listas de reproducción: selecciona varias pistas a la vez para moverlas, eliminarlas o reordenarlas
- Editor de etiquetas: edita los metadatos FLAC (título, artista, álbum, año, géneros, número de disco) directamente en la app, con carga de carátula y scraping de MusicBrainz
- Edición masiva de metadatos para selecciones de múltiples pistas
- "Editar metadatos" al hacer clic derecho en las carátulas de álbum
- Panel de preferencias (barra de menú, actualización automática, calidad de reproducción)
- Modal de bienvenida en el primer inicio

### Corregido
- Invalidación de la caché de carátulas tras editar etiquetas
- Ordenación por fecha de adición, actualización automática de biblioteca tras scraping masivo
- Corrección de firma Developer ID para macOS 26.4.1

---

## v1.6.0 (2026-05-01)

### Añadido
- Apertura automática del modal "Escanear biblioteca" con biblioteca vacía
- Botón de cancelar en el banner de reconexión NAS
- Navegar a la lista "Importada" tras importar un archivo M3U
- Las listas importadas conservan la fecha de adición de las pistas

### Corregido
- Prevención de múltiples instancias de la app al abrir archivos
- Acumulación del volumen con la rueda del ratón
- Actualización del panel de listas tras arrastrar y soltar
- Conformidad sandbox App Store (eliminada API privada NetFS, Sparkle en weak-link)
- Almacenamiento de activación de licencia migrado a UserDefaults
- La búsqueda de géneros usa ahora el motor tornade-core

---

## v1.5.0 (2026-03-25)

### Corregido
- Icono de la aplicación no mostrado correctamente en algunos contextos
- Condición de carrera en el banner NAS al cargar la biblioteca
- Estado de navegación de álbum reiniciado incorrectamente entre vistas
- Estado de pausa no actualizado tras el cambio de pista

---

## v1.4.0 (2026-03-24)

### Cambiado
- El DMG de macOS ahora está firmado con Developer ID y notarizado por Apple, no se necesita eludir Gatekeeper al instalar

---

## v1.3.0 (2026-03-23)

### Añadido
- Reordenación por arrastrar y soltar en la cola de reproducción (trackpad y ratón)

---

## v1.2.0 (2026-03-12)

### Añadido
- Actualizaciones automáticas vía Sparkle 2.x: Tornade comprueba e instala actualizaciones automáticamente
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
- Interfaz Terminal (TUI) construida con ratatui, gratuita y de código abierto, funciona por SSH
- Motor de audio core escrito en Rust
