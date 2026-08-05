# Your work gallery

The Work section on the site shows up to 6 image tiles. Each tile is filled by
an image file in THIS folder, named by number.

## To add or change a piece
1. Prepare a web-sized image (JPG or PNG, ideally ~1600px wide, under ~1 MB).
2. Name it by the tile you want to fill:
   - Tile 1 → `1.jpg`   (or `1.png`)
   - Tile 2 → `2.jpg`
   - Tile 3 → `3.jpg`
   - Tile 4 → `4.jpg`
   - Tile 5 → `5.jpg`
   - Tile 6 → `6.jpg`
3. Upload it into this `work/` folder on the
   `claude/quam-art-portfolio-54sfnl` branch (GitHub → Add file → Upload files).
4. Commit. Vercel redeploys automatically in ~1 minute and the image appears.

Uploading a new `1.jpg` replaces whatever was in tile 1. An empty tile just
shows a brand-coloured gradient — nothing breaks.

## To change the label under a tile
Open `index.html`, find the `<figure class="tile tile-1 ...">` line for that
tile, and edit the `t-tag` (category) and `t-title` (piece name) text.

Want more than 6 tiles, or different labels? Ask Claude and it'll extend the grid.
