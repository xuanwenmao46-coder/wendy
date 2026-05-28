# Font Embedding For HyperFrames

## Folder Convention

Put clip-specific fonts here:

```text
clip-folder/
  assets/
    fonts/
      display.woff2
      text.woff2
      mono.woff2
```

## CSS Pattern

```css
@font-face {
  font-family: "Clip Display";
  src: url("assets/fonts/display.woff2") format("woff2");
  font-weight: 300 900;
}

@font-face {
  font-family: "Clip Text";
  src: url("assets/fonts/text.woff2") format("woff2");
  font-weight: 300 700;
}

@font-face {
  font-family: "Clip Mono";
  src: url("assets/fonts/mono.woff2") format("woff2");
  font-weight: 400 700;
}
```

## Validation

After adding fonts:

```bash
npx hyperframes lint
```

The result should not contain `font_family_without_font_face`.

## Practical Notes

- Prefer `.woff2` for final projects.
- `.ttf` is acceptable for local tests if lint accepts it and render works.
- Do not rely on browser/system fonts for final video.
- If a font cannot be embedded, choose a different font before rendering.
