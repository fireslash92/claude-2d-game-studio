# Claude 3D Game Studio — browser-first

No desktop game-development app required. Use Claude Code web, GitHub and Safari. The included demo runs directly in the browser; cloud asset imports need Git and Python 3, not phone installations.

## Quick start
1. Upload the `3d/` directory to your GitHub repo (keep your existing 2D files).
2. Enable GitHub Pages from Settings → Pages → Deploy from a branch → main / root, if not already enabled.
3. Open `https://<username>.github.io/<repo>/3d/` on your phone. The demo loads Babylon.js and a licensed animated fox over HTTPS.
4. Open the repository in Claude Code web and ask it to read `3d/CLAUDE.md` and `3d/.claude/skills/3d-game-director/SKILL.md` (the nested skill must be read explicitly, or copied into root `.claude/skills/` for auto-discovery).
5. In the cloud session run `python3 3d/import_assets.py`. This downloads KayKit packs and indexes their GLB/glTF models in `3d/models.json`. Review licenses and select only the models required for your project. Commit selected models, textures and original license notices.

## Stack
- Babylon.js: https://github.com/BabylonJS/Babylon.js — primary browser engine.
- Three.js: https://github.com/mrdoob/three.js — alternative for custom rendering.
- PlayCanvas: https://github.com/playcanvas/engine — browser engine and optional online editor (https://playcanvas.com/).
- Godogen: https://github.com/htdt/godogen — optional AI development workflows; full generator may require extra cloud dependencies, GPU and API keys.
- KayKit Adventurers: https://github.com/KayKit-Game-Assets/KayKit-Character-Pack-Adventures-1.0
- KayKit Dungeon: https://github.com/KayKit-Game-Assets/KayKit-Dungeon-Remastered-1.0
- KayKit Medieval Hexagon: https://github.com/KayKit-Game-Assets/KayKit-Medieval-Hexagon-Pack-1.0
- KayKit Skeletons: https://github.com/KayKit-Game-Assets/KayKit-Character-Pack-Skeletons-1.0
- Other asset sources: https://kenney.nl/assets/category:3D, https://quaternius.com/, https://polyhaven.com/ (download GLB/glTF where available; check per-asset licenses).

## Demo
Wildwood is a tiny real 3D exploration game: animated fox, forest, follow camera, keyboard/touch navigation, and five collectible crystals. Trees and terrain are procedural low-poly geometry; the fox is a remotely loaded glTF model. It is not a finished RPG or AAA-quality game. No local build or editor needed. Requires Internet and WebGL. For production, vendor pinned Babylon.js dependencies and selected GLB files locally, test on device, and optimize assets.

## Credits
Fox model: PixelMannen, tomkranis, AsoboStudio, scurest. CC BY 4.0. Full credits and source: https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/Fox . License https://creativecommons.org/licenses/by/4.0/ . Scaled in this demo. KayKit packs advertise CC0; retain each original license and verify the current source before redistribution. No paid assets are bundled. Demo code and procedural scene are original starter code.

## Verification
Source syntax can be checked locally; live browser rendering and upstream asset downloads need verification in your cloud workspace. GitHub Pages must be enabled by the repository owner. No third-party asset archives are bundled.
