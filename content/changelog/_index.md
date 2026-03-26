+++
title       = "Changelog — Tornade Audio Player"
description = "Version history and release notes for Tornade — the native FLAC and lossless audio player for macOS, Windows, Linux and Terminal."
date        = "2026-03-12"
draft       = false

[params]
  ogTitle       = "Tornade Changelog — Release History"
  ogDescription = "Track every release of Tornade, the Rust-powered lossless audio player. New features, bug fixes and improvements."
  ogType        = "website"
+++

## v1.5.0 (2026-03-25)

### Fixed
- App icon not displayed correctly in some contexts
- NAS banner race condition on library load
- Album navigation state reset incorrectly between views
- Pause state not refreshed after track change

---

## v1.4.0 (2026-03-24)

### Changed
- macOS DMG now signed with Developer ID and notarized by Apple — no Gatekeeper bypass needed on install

---

## v1.3.0 (2026-03-23)

### Added
- Drag-and-drop reordering in the playback queue (trackpad and mouse)

---

## v1.2.0 (2026-03-12)

### Added
- Auto-updater via Sparkle 2.x — Tornade now checks for and installs updates automatically
- License system: 30-day free trial, one-time purchase, online activation with device limit
- NAS auto-reconnect on macOS sleep/wake and network loss
- Fuzzy search across tracks, albums, artists and genres
- Featuring artists section in album detail view
- M3U playlist import from the Library modal
- Genres displayed in album info panel
- Animated loading segments on progress bar during NAS track load
- Clean Library button to remove orphaned albums and artists
- Ambient halo effect at the app level with rounded queue panel
- Full app localization (254 strings via xcstrings catalog)

### Fixed
- Duplicate tracks in queue causing infinite loop
- Shuffle ignoring explicit queue track selection
- Artist photos not shown in global search results
- Option+double-click now adds track to queue and plays immediately without clearing it

---

## v1.1.0 (2026-02-25)

### Added
- App Store submission pipeline with sandbox-compatible NAS mount

---

## v1.0.0 (2026-02-25)

### Added
- FLAC, OGG, MP3, WAV and AIFF playback on macOS
- SwiftUI native macOS GUI
- SQLite-backed music library with local and network scanning
- Real-time playback queue
- Terminal UI (TUI) built with ratatui — free and open source, works over SSH
- Core audio engine written in Rust
