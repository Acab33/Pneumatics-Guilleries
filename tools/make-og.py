"""Genera assets/og.jpg (1200x630) — imatge de previsualitzacio per a WhatsApp/Facebook.

Reprodueix el logotip amb els colors de marca sobre fons blanc, amb una franja
blava inferior amb les dades de contacte.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
SS = 2  # supersampling per a vores suaus

BLUE = (23, 53, 143)
BLUE_DEEP = (9, 22, 65)
YELLOW = (251, 210, 0)
BLACK = (17, 19, 24)
GREY = (65, 71, 85)
STRIPE = (243, 246, 252)

F = "C:/Windows/Fonts/"
f_logo_top = ImageFont.truetype(F + "segoeuiz.ttf", 96 * SS)   # bold italic
f_logo_bot = ImageFont.truetype(F + "segoeuiz.ttf", 116 * SS)
f_tag = ImageFont.truetype(F + "segoeui.ttf", 34 * SS)
f_band = ImageFont.truetype(F + "segoeuib.ttf", 30 * SS)

img = Image.new("RGB", (W * SS, H * SS), "white")
d = ImageDraw.Draw(img)

K = 0.25  # tangent de la inclinacio de 14 graus del logo


def skew_rect(x, y, w, h, k=K):
    """Parallelogram inclinat cap a la dreta a la part superior."""
    off = h * k
    return [(x + off, y), (x + w + off, y), (x + w, y + h), (x, y + h)]


# --- fons: franges diagonals molt suaus -------------------------------------
for i in range(-H, W + H, 62 * SS):
    d.polygon(skew_rect(i, 0, 26 * SS, H * SS, k=0.30), fill=STRIPE)

# --- amidem el logotip per centrar-lo --------------------------------------
top_w = d.textlength("pneumàtics", font=f_logo_top)
bot_w = d.textlength("GUILLERIES", font=f_logo_bot)
logo_w = max(top_w, bot_w)
x0 = (W * SS - logo_w) / 2
y0 = 96 * SS

# paraula superior
d.text((x0, y0), "pneumàtics", font=f_logo_top, fill=BLUE)

# banda de rodadura a la cantonada superior dreta
bx = x0 + top_w + 16 * SS
by = y0 + 12 * SS
bw, bh, gap = 22 * SS, 15 * SS, 5 * SS
for row in range(3):
    for col in range(4):
        d.polygon(
            skew_rect(bx + col * (bw + gap) + row * 7 * SS,
                      by + row * (bh + gap), bw, bh),
            fill=BLACK,
        )

# barra groga
bar_y = y0 + 128 * SS
d.polygon(skew_rect(x0 + 6 * SS, bar_y, logo_w - 6 * SS, 22 * SS), fill=YELLOW)

# paraula inferior
d.text((x0, bar_y + 34 * SS), "GUILLERIES", font=f_logo_bot, fill=BLUE)

# --- descriptiu -------------------------------------------------------------
tag = "Taller de pneumàtics i mecànica ràpida a Vic"
tw = d.textlength(tag, font=f_tag)
d.text(((W * SS - tw) / 2, 434 * SS), tag, font=f_tag, fill=GREY)

# --- franja inferior amb el contacte ---------------------------------------
band_y = 522 * SS
d.rectangle([0, band_y - 7 * SS, W * SS, band_y], fill=YELLOW)
d.rectangle([0, band_y, W * SS, H * SS], fill=BLUE)

left = "Carrer Torelló, 63 — 08500 Vic"
right = "938 890 574"
cy = band_y + (H * SS - band_y) / 2
d.text((64 * SS, cy), left, font=f_band, fill="white", anchor="lm")
d.text((W * SS - 64 * SS, cy), right, font=f_band, fill=YELLOW, anchor="rm")

# --- exporta ----------------------------------------------------------------
out = ("C:/Users/Adri/Documents/Projectes/WEB_PNEUMATICS_GUILLERIES/assets/og.jpg")
img.resize((W, H), Image.LANCZOS).save(out, "JPEG", quality=90, optimize=True)
print("escrit:", out)
