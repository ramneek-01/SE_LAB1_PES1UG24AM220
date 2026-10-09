# Lab 04 — Implementation Notes

## Task 1 — Fix pyramid projection
Changed the row offset in the cube projection to use true division so rows are horizontally centered.

## Task 2 — Add level colour palettes
The palette helper selects a palette using `palettes[(level - 1) % len(palettes)]`, cycling through the configured palettes.

## Task 3 — Add cube completion flash
When a cube is completed, its cell is stored in `COMPLETION_FLASHES` with an expiry timestamp. The drawing code uses this timestamp for brief visual feedback.

## Task 4 — Add bonus life threshold
The bonus-life threshold helper returns `1000`, and the existing score bookkeeping uses the threshold to award extra lives.

## Verification note
The source was reconstructed from the provided completed game source and README. The game was not run in this environment, and no gameplay video was recorded. These notes are implementation documentation, not proof of runtime behavior.
