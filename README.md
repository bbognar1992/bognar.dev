# bognar.dev

Három testvér, három technológia, egy közös név: Bognár.

## Testvérek

- **Bognár Bence** – Software Engineer / Python / backend
- **Bognár Levente** – Software Engineer / JS / frontend  
- **Bognár Lehet** – Software Engineer / C++

## Helyi fejlesztés

```bash
npm install
npm run dev
```

A helyi szerver a `http://localhost:3000` címen lesz elérhető.

## Vercel deployment

A projekt Vercel-re készült. Telepítéshez:

### Framework kiválasztása Vercel-en

**Fontos:** Amikor a Vercel kérdezi a framework-et, válaszd ki az **"Other"** vagy **"Static Site"** opciót.

Ez egy tiszta statikus HTML oldal, nincs szükség framework-re (React, Next.js, stb.). A `vercel.json` fájlban explicit módon `"framework": null` van beállítva.

### Telepítési lépések:

1. **GitHub-on keresztül:**
   - Csatlakoztasd a GitHub repository-t a Vercel dashboardon
   - Framework: **"Other"** vagy **"Static Site"** választása
   - Build Command: üresen hagyható (vagy `echo "No build needed"`)
   - Output Directory: `.` (vagy üresen hagyható)

2. **Vercel CLI-vel:**
   ```bash
   npm i -g vercel
   vercel
   ```
   - Amikor kérdezi a framework-et, válaszd: **"Other"**

A Vercel automatikusan felismeri a statikus HTML oldalt és telepíti.

## Projekt struktúra

```
.
├── index.html          # Főoldal
├── vercel.json         # Vercel konfiguráció
├── package.json        # NPM konfiguráció
└── README.md          # Dokumentáció
```

