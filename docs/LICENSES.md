# Licenses and source policy
The original starter code and original art in this repository are MIT licensed (see LICENSE). No upstream asset library is included in this ZIP. The catalog links to nine upstream projects; importer fetches selected ones on demand and records commit SHA. The license of the starter does not override upstream terms.

- Ninja Adventure: original pack is CC0; verify notices for imported files.
- Superpowers: CC0 according to upstream README.
- Tiddybub: catalog claims CC0; check each pack's SOURCE.md and original source, especially fonts/audio.
- LPC: generator code GPL-3.0, artwork has multiple licenses. Export author credits and obey the chosen layers' licenses (including share-alike where applicable). Do not redistribute the entire generator as MIT.
- Jam Ready: each pack has its own license. RUN-only content is restricted outside RUN; select individual CC0 or otherwise compatible packs and keep notices.
- Optional tools: review their code licenses and service terms before installation or publishing generated artwork. Aseprite is separate software; API providers may charge fees or impose output conditions.

Maintain `assets/credits.json` for each shipped third-party file or pack. Retain upstream license and attribution files. Do not commit API keys, purchased assets, or full imported libraries by default. A source marked CC0 by a catalog is not a substitute for verifying the specific pack's provenance.
