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

## v0.5.0 (2026-03-12)

### Added
- FLAC and ALAC lossless playback improvements: gapless transitions and exact sample-accurate seeking
- Hi-res audio support up to 32-bit / 384 kHz for FLAC, WAV and AIFF files
- macOS: new ambient background system using album artwork dominant colours
- TUI: keyboard shortcut overlay (press `?` to display)

### Fixed
- OGG Vorbis files with non-standard sample rates no longer cause playback stutter
- Library scan no longer skips FLAC files embedded with high-resolution artwork (>2 MB)

### Changed
- Rust audio engine updated — reduced memory usage by ~15% on large libraries

---

## v0.4.2 (2026-02-10)

### Added
- Global search across tracks, albums, artists and genres
- macOS: universal binary supporting Intel and Apple Silicon natively

### Fixed
- WAV files encoded with non-PCM codecs now correctly report unsupported format instead of crashing
- AIFF metadata (title, artist, album) now read correctly on macOS

---

## v0.4.0 (2026-01-20)

### Added
- FLAC, OGG, MP3, WAV and AIFF playback on all platforms
- Terminal UI (TUI) built with ratatui — free and open source, works over SSH
- Real-time playback queue with drag-and-drop reordering (macOS GUI)
- Network and local library scanning
- macOS: 30-day free trial, then €9.99 one-time purchase

### Changed
- Core audio engine rewritten in Rust for lower latency and memory safety
