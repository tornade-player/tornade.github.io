+++
title       = "Privacy Policy — Tornade"
description = "Tornade privacy policy. No personal data collected."
date        = "2026-03-27"
draft       = false

[params]
  ogTitle       = "Privacy Policy — Tornade"
  ogDescription = "Tornade does not collect any personal data. All processing happens locally on your device."
+++

# Privacy Policy

*Last updated: March 27, 2026*

## Overview

Tornade is a cross-platform local music player. We are committed to protecting your privacy.

## Data Collection

**Tornade does not collect any personal data, on any platform.**

- No analytics or tracking
- No usage data sent to external servers
- No crash reports transmitted without your explicit consent
- No advertising identifiers used

## Local Processing

All operations performed by Tornade happen entirely on your device:

- Music library scanning and indexing
- Audio playback
- Metadata reading (artist, album, track information)
- Artwork loading

No music files, metadata, or listening history ever leave your device.

## Per-Platform Details

### macOS — App Store

- **Purchases**: handled entirely by Apple's StoreKit 2 framework. No payment data is processed by Tornade. Refer to [Apple's Privacy Policy](https://www.apple.com/legal/privacy/) for details.
- **Updates**: delivered through the Mac App Store — no external update service used.
- **Network**: used only for StoreKit purchase verification.

### macOS — Direct Download

- **License verification**: your license key is validated against our server to confirm its validity. No personal information is transmitted — only the key itself.
- **Updates**: checked automatically via [Sparkle](https://sparkle-project.org), an open-source update framework. Only your macOS version and app version are sent to our update feed.
- **Network**: used only for license checks and update checks.

### Windows & Linux

- **License verification**: same as macOS direct download — only the license key is transmitted.
- **Updates**: checked via our update feed. Only your OS version and app version are sent.
- **Network**: used only for license checks and update checks.

### Terminal UI (TUI)

- **No network access**: the TUI version does not connect to any external service.
- **No license system**: the TUI is open-source and free to use.

## Data Retention

Since no personal data is collected, there is nothing to retain or delete.
