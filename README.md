# Pneumàtics Guilleries — web

Web estàtica (HTML + CSS, zero JavaScript de tercers) per al taller Pneumàtics Guilleries,
Carrer Torelló 63, 08500 Vic.

Pensada perquè **no necessiti cap manteniment**: no hi ha CMS, ni base de dades, ni plugins,
ni res que caduqui o s'hagi d'actualitzar. Un cop publicada, funciona sola indefinidament.

## Estructura

```
index.html          Pàgina principal (català)
es/index.html       Versió en castellà
avis-legal.html     Avís legal, privacitat i galetes
assets/style.css    Tots els estils
assets/logo.svg     Logotip de la capçalera
assets/favicon.svg  Icona de la pestanya
robots.txt          Indexació
sitemap.xml         Mapa del lloc per a Google
```

## PENDENT de confirmar amb el tiet

Aquestes dades venen de directoris públics i **s'han de verificar abans de publicar**:

| Dada | Valor actual | On es toca |
|---|---|---|
| Horari | Dl–Dj 9–13 i 15–19 · Dv 8–13 · Ds i Dg tancat | `index.html`, `es/index.html` (taula `.hours` i peu) |
| Correu | `guilleries@gmail.com` | Cerca i reemplaça a tots els fitxers |
| Telèfon | 938 890 574 | Cerca i reemplaça `938890574` |
| Nom fiscal i NIF | `[PENDENT]` | `avis-legal.html` |
| Xarxa BestDrive | no mencionada | — |
| Marques de pneumàtics | genèric | secció "El taller" |

També estaria bé substituir el bloc de degradat de la portada per **fotos reals del taller**.

### Logotip

`assets/logo.svg` és una **recreació** feta a partir de la imatge del logo: mateixa
composició (paraula en cursiva, barra groga inclinada, banda de rodadura a la cantonada) i
mateixos colors, però la tipografia no és la original.

Quan tingueu el fitxer original —idealment vectorial (`.svg`, `.ai`, `.eps`)— substituïu
`assets/logo.svg` conservant el nom i tot funcionarà igual. Si només hi ha un PNG, poseu-lo a
`assets/logo.png` i canvieu el `src` a les tres pàgines. Convé que tingui fons transparent i
almenys 600 px d'amplada.

### Paleta de marca

| Ús | Color |
|---|---|
| Blau corporatiu | `#17358F` |
| Blau fosc (fons i peu) | `#0E2160` / `#091641` |
| Groc d'accent | `#FBD200` |
| Negre (banda de rodadura) | `#111318` |

Estan definits com a variables CSS a dalt de `assets/style.css`. Si es canvia el blau allà,
canvia a tot el web.

## Com publicar-la (gratis i per sempre)

### 1. Comprar el domini

`pneumaticsguilleries.cat` — comprovat el 19/07/2026: **lliure** (sense delegació DNS).
`pneumaticsguilleries.com` també ho està, com a alternativa.

Registradors recomanats per a `.cat` (uns 20–40 €/any):
- [CDmon](https://www.cdmon.com) — català, suport en català, el més senzill
- [Nominalia](https://www.nominalia.com)
- [Gandi](https://www.gandi.net)

> El `.cat` demana una breu justificació de vinculació amb la llengua/cultura catalana.
> Una web de negoci escrita en català la compleix; el registrador ho tramita ell mateix.
>
> **Activa la renovació automàtica** i posa la targeta del tiet — és l'única cosa que cal
> vigilar en tot el projecte.

### 2. Publicar (allotjament gratuït)

Recomanat: **Cloudflare Pages** (gratis sense límit de temps, ràpid, HTTPS automàtic).

1. Entra a [dash.cloudflare.com](https://dash.cloudflare.com) → *Workers & Pages* → *Create* → *Pages*
2. *Upload assets* → arrossega la carpeta sencera d'aquest projecte
3. Nom del projecte: `pneumatics-guilleries` → *Deploy*
4. *Custom domains* → afegeix `pneumaticsguilleries.cat` i `www.pneumaticsguilleries.cat`
5. Al registrador, canvia els servidors DNS pels que t'indiqui Cloudflare

Alternatives igual de vàlides: [Netlify](https://www.netlify.com) (arrossegar carpeta a
*Sites* → *Deploy manually*) o GitHub Pages.

El certificat HTTPS es renova sol. No hi ha res més a fer.

### 3. Després de publicar

- Reclama la fitxa de **Google Business Profile** del taller i hi poses la URL nova.
  És el que més visites portarà, molt més que la web en si.
- Envia el `sitemap.xml` a [Google Search Console](https://search.google.com/search-console).
- Posa l'enllaç al Facebook i l'Instagram del negoci.

## Manteniment

Cap, tret de:
- **Renovar el domini un cop l'any** (automàtic si actives la renovació).
- Si canvia l'horari o el telèfon: edita els dos `index.html`, torna a arrossegar la carpeta
  a Cloudflare Pages, i llest.
