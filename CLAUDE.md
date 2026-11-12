# Claude 2D Game Studio

Read `catalog/sources.json`, `docs/ART-DIRECTION.md` and `docs/LICENSES.md` before choosing artwork. Use existing sprites, tiles and animation sheets instead of placeholder geometry. Start with the bundled original art and playable demo; use `python3 scripts/import_assets.py --list` to discover sources, and `--starter` to import Ninja Adventure with user approval and network access. Never claim an import worked without inspecting files. Do not run third-party code without reviewing it and obtaining permission when necessary.

## Production loop
1. Define the gameplay, art direction, tile size, perspective, palette, target viewport and animation state table.
2. Inspect available asset files and source notices. Select one coherent pack or adapt assets deliberately. Keep unmodified upstream assets in vendor folders; copy chosen art to a project-specific folder with credits.
3. Build a vertical slice: exploration, NPC interaction, battle transition, inventory, save state, touch controls. The included demo is intentionally small, not a complete JRPG.
4. Create missing art with the game-art-director skill; use Pixel Art Studio (Python/Pillow), optional Sprite Forge/PixelLab, or Aseprite only if installed and authorized. Verify transparent alpha, exact frame sizes, nearest-neighbor scale and animation timing.
5. Test keyboard, touch, narrow viewport, orientation, missing asset paths and visual consistency. Never require hover. Ship a playable build and an asset/license manifest.

## Rules
- No secrets, API keys or paid asset redistribution in commits. Never silently install external MCP services or tools.
- Use relative URLs for GitHub Pages. Preserve upstream licenses and author notices.
- Use original visual direction, not ripped commercial game sprites; classic JRPG inspiration is welcome.
- For cloud sessions, check internet/dependency availability. If imports fail, continue using bundled originals and explain the limitation.
