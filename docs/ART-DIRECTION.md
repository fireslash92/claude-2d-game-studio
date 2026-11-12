# Art direction: original classic fantasy JRPG
- Top-down three-quarter perspective; 16x16 environment tiles, 16x24 heroes; scale 3x or 4x with nearest-neighbor. Use one directional light (upper left).
- Palette: forest greens, warm sandstone, slate, muted teal, amber highlights. Avoid arbitrary saturation and inconsistent outlines.
- Starter targets: village, woodland, cave; protagonist, merchant, guard, slime, wolf; idle/walk four directions, attack/hurt/defeat; doors, fences, bridges, foliage, water; HUD, inventory and dialogue.
- Keep logical coordinates and asset pixels separate. Never infer a spritesheet's frame size from file name; inspect dimensions and upstream metadata.
- Use separate ground/decor/collision layers, autotile edges or explicit transition tiles, and bottom-center entity anchors. Sort by feet Y for overlaps.
- Produce original designs rather than copying Legend of Heroes characters or commercial art.
- Check animations at 6–12 fps for walking, no unintended flicker, consistent foot contact, and consistent bounding boxes. Review 1x and integer-scaled contact sheets.
