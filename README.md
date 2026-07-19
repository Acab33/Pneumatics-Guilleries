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
assets/og.jpg       Imatge de previsualització en compartir (1200×630)
tools/make-og.py    Script que genera assets/og.jpg
robots.txt          Indexació
sitemap.xml         Mapa del lloc per a Google
.nojekyll           Desactiva el processat Jekyll a GitHub Pages
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

### Imatge per compartir (WhatsApp, Facebook)

`assets/og.jpg` (1200 × 630 px) és el que surt quan algú envia l'enllaç per WhatsApp. Està
generada a partir del logotip amb `tools/make-og.py`:

```
python tools/make-og.py
```

Necessita Pillow (`pip install pillow`) i tipografies Segoe UI, o sigui que s'ha d'executar a
Windows. **No cal tornar-la a generar mai** tret que canviïn el telèfon, l'adreça o el logo.

Quan hi hagi fotos del taller, una foto real de la façana o de la nau funcionarà encara
millor que el logo: només cal desar-la com a `assets/og.jpg` a 1200 × 630 px.

> Després de canviar aquesta imatge, WhatsApp i Facebook en guarden una còpia en memòria
> cau durant dies. Per forçar-ne l'actualització, passa la URL pel
> [Sharing Debugger de Facebook](https://developers.facebook.com/tools/debug/).

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

## Estat actual

Publicada provisionalment a GitHub Pages:
**https://acab33.github.io/pneumatics-guilleries/**

Tots els enllaços interns són **relatius**, de manera que el web funciona igual des d'un
subdirectori (GitHub Pages) que des de l'arrel d'un domini propi. Quan es canviï de domini
només cal tocar les URL absolutes, que són poques i estan totes en aquests llocs:

- `index.html` i `es/index.html` → `canonical`, `hreflang`, `og:url`, `og:image` i el bloc
  `application/ld+json`
- `robots.txt` → línia `Sitemap:`
- `sitemap.xml` → totes les `<loc>`

Cerca i reemplaça `https://acab33.github.io/pneumatics-guilleries` pel domini nou i llest.

El fitxer `.nojekyll` evita que GitHub Pages processi el web amb Jekyll: no cal per res i
així el desplegament és més ràpid i previsible.

## Com publicar-la amb domini propi

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

### 2. Apuntar-hi el web

Si es continua amb GitHub Pages: *Settings → Pages → Custom domain*, s'hi posa el domini, i
al registrador es creen els registres DNS que GitHub indiqui. Es genera un fitxer `CNAME` al
repositori. Marca **Enforce HTTPS**.

Alternativa igual de vàlida: **Cloudflare Pages** ([dash.cloudflare.com](https://dash.cloudflare.com)
→ *Workers & Pages* → *Create* → *Pages* → *Upload assets*, arrossegant la carpeta sencera).

En qualsevol dels dos casos el certificat HTTPS es renova sol. No hi ha res més a fer.

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
