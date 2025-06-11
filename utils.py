from PIL import Image, ImageDraw

def load_and_split(img: Image.Image, size: int = 300):
    img = img.convert("RGB")
    img = img.resize((size, size))
    tile_w, tile_h = size // 3, size // 3
    tiles = []
    for row in range(3):
        for col in range(3):
            left = col * tile_w
            upper = row * tile_h
            right = left + tile_w
            lower = upper + tile_h
            tile = img.crop((left, upper, right, lower))
            tiles.append(tile)
    return tiles

def assemble(board_nums, tiles, size: int = 300):
    board_img = Image.new("RGB", (size, size), color="white")
    tile_w, tile_h = size // 3, size // 3
    draw = ImageDraw.Draw(board_img)
    for idx, num in enumerate(board_nums):
        row, col = divmod(idx, 3)
        left = col * tile_w
        upper = row * tile_h
        if num == 0:
            draw.rectangle([left, upper, left + tile_w, upper + tile_h], fill="white")
        else:
            tile = tiles[num - 1].resize((tile_w, tile_h))
            board_img.paste(tile, (left, upper))
    return board_img