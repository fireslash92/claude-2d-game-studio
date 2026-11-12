# Claude 2D Game Studio — Pixel Realm

A single Claude-ready workspace for classic 2D RPG production, with nine upstream asset/tool sources, an opt-in importer, an original starter sprite pack, a mobile-friendly asset browser and a small playable village. This is a hub, not a redistribution of entire third-party libraries.

## Quick start (iPhone / Claude Code)
1. Create a new repository on GitHub, upload the contents of this folder (including hidden `.claude` directory and `.gitignore`), or push it from a terminal. Keep it private until you decide to publish.
2. Open Claude Code on the web/mobile with your GitHub repo connected. Ask it to read `CLAUDE.md`, `catalog/sources.json`, and `docs/ART-DIRECTION.md`.
3. Ask Claude to run `python3 scripts/import_assets.py --list` and, if the environment permits network access, `python3 scripts/import_assets.py --starter`. This downloads Ninja Adventure into `assets/vendor/`. No third-party execution occurs automatically.
4. Ask Claude to create a vertical slice using the imported art and the art-direction skill. Copy selected files and their notices into your game's committed assets folder, then update `assets/credits.json`.
5. To preview: run `python3 -m http.server 8000` in the project folder and open the preview URL; or enable GitHub Pages from the root of your default branch where available. Open `index.html` for an offline-capable starter using bundled images and plain JavaScript.

## Asset sources
| Source | Use | Import |
|---|---|---|
| Ninja Adventure | coherent RPG characters/world/audio | `--starter` |
| Superpowers | RPG battle, fantasy and platformer art | `superpowers` |
| Tiddybub | large genre-organized asset library | `tiddybub` (selected folders) |
| Universal LPC | customizable character sheets | manual, export credits |
| Jam Ready | varied 2D and audio packs | manual, per-pack licensing + Git LFS |
| Agent Sprite Forge | generation and animation pipeline | manual plugin setup |
| PixelLab MCP | AI sprites and tiles | manual API configuration |
| Aseprite Pixel Plugin | editable pixel art and animations | manual host setup |
| Pixel Art Studio | Python/Pillow custom art skill | `--install-skill` |

All exact links and license caveats are in `catalog/sources.json`. The catalog page lists every source; `docs/LICENSES.md` describes the license safeguards. The three opt-in library imports may be large. Imported vendor trees are gitignored. Do not install optional tools or send data to external APIs without review and approval.

## Commands
```sh
python3 scripts/import_assets.py --list
python3 scripts/import_assets.py --starter
python3 scripts/import_assets.py superpowers
python3 scripts/import_assets.py --all-free # potentially large
python3 scripts/import_assets.py --install-skill # copies skill source; review before using
python3 -m pip install pillow # only needed for art generation
python3 scripts/make_starter_art.py # recreate original sprite sheets
python3 -m http.server 8000
```

## Example Claude task
> Read CLAUDE.md. Build an original classic fantasy JRPG vertical slice: a village, forest, one NPC quest, turn-based combat, inventory and local saves. Use the bundled starter art for initial testing, then select a consistent licensed asset pack. Target iPhone Safari with large touch controls and a responsive canvas. If using Phaser, install Phaser 3 in a web build with relative asset paths and a production export. Show a playable preview and test it before claiming it is finished. Keep all original/third-party assets properly credited.

## Layout
- `index.html`, `demo/` — mobile asset browser and dependency-free Canvas starter
- `assets/starter/` — real original PNG sheets + frame manifest
- `catalog/` — upstream sources and licensing metadata
- `scripts/` — import and deterministic art generation
- `.claude/skills/game-art-director/` — project-local Claude skill
- `docs/` — art direction and licensing

The starter is a small movement/interaction demo, not a full RPG. Phaser is an optional next step, not installed in this dependency-free version. External imports need Git, a network-enabled host and appropriate permission; no paid services are configured. See LICENSE for original work; upstream assets/tools retain their own licenses.
