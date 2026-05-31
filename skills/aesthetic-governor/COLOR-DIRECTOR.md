---
title: Color Director
system: Aesthetic Governor System
layer: Color
version: 1.0.0
status: production
last_updated: 2026-05-31
---

# Color Director

## Core Principle

Color is not decoration. Color is atmosphere, psychology, and brand. Every color decision in a production — from the background tone of a title card to the accent on a call-to-action element — is a deliberate act. The Color Director makes no random decisions.

Randomness in color is not neutrality. It is noise. Noise erodes the coherence that makes premium work feel premium. The Color Director exists to enforce the discipline that separates editorial-grade output from consumer-grade output.

A frame with one unintended color will undermine everything around it. Audit before render. The rules below are not suggestions.

---

## The 70/20/10 Palette Law

Every scene — every frame — obeys the following ratio:

| Zone | Weight | Role | Examples |
|------|--------|------|---------|
| **Dominant** | 70% | Background, ground, sky, primary surface | Wall color, floor, ambient fill |
| **Supporting** | 20% | Secondary surfaces, mid-ground objects, UI elements | Table top, card surfaces, typography body |
| **Accent** | 10% | Single decisive color hit | One highlighted word, one product color pop, one icon tint |

### The Accent Rule

The accent is deployed **once per scene**. Not twice. Not across three elements. Once. The moment a second element receives the same accent treatment, the accent ceases to function. It becomes background noise.

If your accent appears on a headline and an icon and a border — you have no accent. You have three competing elements fighting for attention and losing simultaneously.

### Violation Patterns and Corrections

**Violation 1: Accent Proliferation**
Symptom: The primary brand color appears on headline, icon, button border, and ambient glow.
Correction: Choose one carrier for the accent. Neutralize all others to a supporting tone derived from the dominant zone.

**Violation 2: Inverted Ratios**
Symptom: A bold-color background (40%) with multiple competing surface colors (30%) and multiple accents (30%).
Correction: Desaturate the background toward the dominant intent. Collapse multiple surface colors into one supporting tone. Identify the single highest-value accent and eliminate all others.

**Violation 3: Absent Dominant**
Symptom: No clear ground color — every zone competes at roughly equal visual weight, creating a "billboard" effect.
Correction: Identify the largest surface in the frame. Assign it the dominant role. All other surfaces must read as subordinate through reduced saturation, reduced value contrast, or reduced screen percentage.

**Violation 4: Dominant-Accent Conflict**
Symptom: The dominant color and the accent color are on opposite ends of the complementary spectrum at equal saturation, creating eye vibration.
Correction: Desaturate the dominant by 30–50%. The accent earns contrast from the muted ground, not from a saturated fight.

---

## Palette Mode Taxonomy

### 1. Monochrome

**Character:** Single hue, fully desaturated to grayscale or near-grayscale, elevated grain. The tonal range does all the work. Shadow detail is preserved — crushed blacks are a failure in this mode.

**Production Rules:**
- Desaturate fully or to maximum 8% saturation globally.
- If a hue tint is retained, it must be consistent across all zones (no warm shadows with cool highlights unless using Duotone rules).
- Grain: Medium to Pronounced (0.08–0.18 opacity). Grain is not optional in Monochrome — it is the texture that makes the image read as photographic rather than rendered.
- Tonal curve: Slightly lifted blacks (no pure 0,0,0), with full detail in the shadow range.
- Typography: White or near-white against dark ground, or reversed. No color type in Monochrome mode.

**Reference:** Film noir, Peter Lindbergh portraiture, A24 drama sequences, Bergman-era editorial.

**Forbidden:** Color-graded elements overlaid on a monochrome background (unless a deliberate two-layer editorial decision), desaturated footage with retained neon or screen glow.

---

### 2. Duotone

**Character:** Two tones — one warm, one cool — blended across a luminosity mask. The shadow zone pulls toward one tone, the highlight zone toward the other. Midtones are the contested territory where they meet.

**Production Rules:**
- Warm tone: amber, sepia, gold — placed in shadows or highlights (choose one, be consistent).
- Cool tone: slate blue, desaturated teal, near-black cool — placed in the opposite luminosity zone.
- The two tones must be separated by at least 80° on the color wheel or differentiated through temperature (warm/cool) rather than hue rotation.
- No third color is introduced. Even small elements must be desaturated to one of the two tones.
- Saturation of each tone: 40–65%. Full-saturation duotone reads as poster art, not editorial photography.
- Grain: Medium (0.06–0.10 opacity).

**Reference:** Fashion campaign photography, Helmut Newton editorial interpretation, luxury brand films.

**Forbidden:** Three-tone execution (this becomes Restrained Editorial), fully saturated tones, mismatched warmth directions (warm shadows AND warm highlights simultaneously — this collapses the duotone structure).

---

### 3. Restrained Editorial

**Character:** Three neutrals at various luminosity levels plus a single accent color held below 10% of total frame coverage. The neutrals carry the frame. The accent punctuates.

**Production Rules:**
- Neutral 1: The dominant ground (off-white, warm stone, cool grey, warm linen — must be desaturated, no chroma above 12).
- Neutral 2: A mid-tone supporting surface (warm greige, medium slate, natural wood tone — within 30° of Neutral 1 on the color wheel).
- Neutral 3: A dark anchor (near-black, deep charcoal, dark warm brown — the shadow presence that gives the neutrals structure).
- Accent: One saturated or distinct color held to maximum 10% frame coverage. This is often a brand color or a product material.
- The three neutrals must be related. They are variations on a theme, not three unrelated greys.
- Grain: Subtle to Medium (0.04–0.08 opacity).

**Reference:** Aesop product photography, Loewe editorial, museum collection films, Kinfolk magazine.

**Forbidden:** Two accent colors (one accent only), oversaturated neutrals (if a neutral is reading as "color" it has failed its role), neutrals from incompatible temperature families (a cold grey with a warm linen with a warm wood — the cold grey breaks cohesion).

---

### 4. Bold Poster

**Character:** Hard flat colors at maximum or near-maximum saturation. High contrast between zones. No gradients within color fields. Color fills are solid. This is the only mode where color operates at full voltage.

**Production Rules:**
- Colors are selected from a pre-defined poster palette of 3–5 colors maximum.
- Backgrounds are flat single-color fills, not gradients.
- Typography is reversed (dark on light or light on dark) using palette colors only — no neutrals outside the defined palette.
- The 70/20/10 law still applies — even in Bold Poster mode, one color dominates. The mistake is giving all colors equal real estate.
- No texture, no grain (grain would dilute the graphic intensity that defines this mode).
- Contrast ratio between dominant and supporting zones: minimum 4.5:1 for large elements, 7:1 for text.

**Reference:** Bloomberg Businessweek cover design, Pentagram identity work, Saul Bass film titles.

**Forbidden:** Gradients within color fills, more than 5 colors in the palette, photographic textures underneath flat color fields, drop shadows (these imply depth that contradicts flat graphic intent).

---

### 5. Warm Neutral

**Character:** Off-whites and natural earthy tones bathed in golden or warm natural light. The entire palette reads as one family of warmth across different materials. No cool tones permitted.

**Production Rules:**
- Dominant: Off-white, warm white, cream, linen — not pure white (pure white reads clinical, not warm).
- Supporting: Natural wood, sand, warm stone, warm beige, terracotta in small quantities.
- Accent (optional, restrained): A single warm saturated note — burnt orange, warm brass, honey gold. Maximum 8% frame coverage.
- Color temperature of lighting simulation: 4500–5500K (warm natural daylight to golden hour). No cool light sources.
- Saturation across the palette: Low. Maximum 30 saturation for supporting elements. The warmth comes from hue selection, not saturation.
- Grain: Subtle (0.03–0.06 opacity), warm-toned if colored grain is used.

**Reference:** MUJI product photography, Stripe Press publication design, Kinfolk lifestyle, Aesop in warm context.

**Forbidden:** Any cool tone entering the frame (even grey that reads slightly blue breaks this mode), pure white backgrounds, black typography (use very dark warm brown instead — pure black is too cold for this palette).

---

### 6. Dark Ground

**Character:** Deep near-black as the dominant ground, with warm dark surfaces as the supporting zone. Precision accents emerge from depth rather than competing against a light ground. This is not "dark mode" as a UI pattern — it is cinematic depth.

**Production Rules:**
- Dominant ground: Near-black at 5–12% luminosity. Pure black (0%) is forbidden — it flattens. The ground must retain some texture and tonality.
- Supporting surfaces: Warm dark tones — deep charcoal with brown undertone, very dark warm grey, muted dark olive. These must be distinguishable from the dominant but remain in the dark register (12–25% luminosity).
- Accent: A precise, saturated or high-luminosity accent that emerges from the dark ground — electric white, specific brand color, warm amber, ice blue. The accent's contrast against the dark ground is its power.
- Typography: Near-white or accent color. No mid-grey type (it disappears or reads as low-contrast on dark ground).
- Grain: Medium to Subtle (0.05–0.10 opacity) — visible enough to prevent the dark areas from looking like solid fills.

**Reference:** Linear product films, Vercel brand assets, Figma dark editorial, Pitch deck dark mode.

**Forbidden:** Blue-black dominants (too literal for "dark mode" UI reading), competing warm and cool accents in the same scene, ground areas that are pure black fills with no texture or tonality.

---

## LUT Reference Library

LUTs are applied as the final color science layer, after exposure and white balance are correct. A LUT cannot fix a poorly exposed or incorrectly white-balanced source. Apply LUT at 60–85% opacity unless a full-strength application is intentional and specified.

---

### 1. Kodak TRI-X 400 Emulation

**Visual Character:** Deep, slightly warm blacks with a slight silver-grey lift in the shadows. Mids are punchy with strong contrast. Highlights roll off smoothly, never clipping to pure white. The grain structure (when applied separately) is medium and slightly chunky — not fine digital noise. The overall tonal character reads as heavy, authoritative, documentary.

**When to Use:** Documentary segments, journalistic brand storytelling, archive-style sequences, behind-the-scenes footage intended to feel like reportage, fashion work that references 1960s–1990s print photography.

**Pairs With:** Monochrome palette mode. Occasionally Duotone when the warm tone is positioned in the highlights.

**Forbidden Uses:** Product beauty shots (the shadow depth conceals surface detail), SaaS product UI demonstrations (makes interfaces read as aged/broken), any sequence where color communication is load-bearing.

---

### 2. Fuji Superia 400

**Visual Character:** A slight warm-green shift in the shadows and mids, with neutral-to-slightly-cool highlights. The overall impression is nostalgic without being aggressively retro. Skin tones take on a slightly golden-green cast that reads as "film" rather than "digital." Grain is fine and even. Blacks are lifted slightly, creating a characteristic "faded" quality.

**When to Use:** Lifestyle sequences, personal storytelling, brand films with a human/organic tone, travel content, fashion editorial with a 1990s–2000s Kodachrome-adjacent reference.

**Pairs With:** Warm Neutral palette mode (with careful attention to the green cast in the neutrals — it can enrich or contaminate depending on the source material). Restrained Editorial when the accent color is warm.

**Forbidden Uses:** Clinical product photography (the green lift contaminates product color accuracy), tech brand films where cool precision is required, Monochrome (the hue cast is invisible but the tone structure conflicts with TRI-X emulation expectations).

---

### 3. Cinematic Teal-Orange (Detuned)

**Visual Character:** The detuned version specifically reduces the teal saturation in shadows to 40–60% of the standard cinematic teal-orange grade. Skin tones remain warm-orange but are not pushed to caricature. Shadow areas shift toward a muted, desaturated teal-grey rather than a vivid cyan. The result reads as a contemporary film grade, not as a YouTube color preset. It is recognizable as influenced by the teal-orange convention but is not a literal execution of it.

**When to Use:** Contemporary editorial sequences, brand films with cinematic ambition, interview-style segments with professional lighting, fashion film contexts where the full teal-orange grade would read as derivative.

**Pairs With:** Restrained Editorial palette mode. Dark Ground palette mode when the shadow desaturation is increased further.

**Forbidden Uses:** The standard (non-detuned) teal-orange is forbidden for all premium work — it is a marker of amateur post-production. The detuned version is forbidden in: SaaS product UI context, Monochrome sequences, Bold Poster palette mode.

---

### 4. Bleach Bypass

**Visual Character:** Lifted blacks (no blacks below 15% luminosity), significantly desaturated colors across all zones, high contrast in the mids that gives the image a harsh, gritty quality. Colors that remain visible are muted and slightly sickly. Skin tones grey. The overall effect is forensic, unflinching, high-stakes.

**When to Use:** High-tension brand narratives, sequences requiring urgency or severity, documentary-style investigations, editorial sequences where comfort is the enemy of the message.

**Pairs With:** Monochrome palette mode (full desaturation extension). Duotone with a cool-dominant application.

**Forbidden Uses:** Lifestyle content, warm brand narratives, product beauty shots, any context where the audience needs to feel comfortable or aspirational. Bleach Bypass creates anxiety — it is a specific editorial tool, not a general grade.

---

### 5. Day-for-Night

**Visual Character:** A blue-cold shift across the entire image, simulating night scenes shot in daylight. Shadows are pushed toward deep blue-indigo. Highlights are desaturated toward blue-white. The overall effect is deliberate unreality — the audience knows this is a color convention, not literal night. Exposure is typically reduced in the grade.

**When to Use:** Dream sequence contexts, narrative brand films with a surreal or contemplative register, editorial sequences exploring uncertainty or introspection, music-adjacent brand content.

**Pairs With:** Duotone palette mode with the cool tone dominating. Dark Ground palette mode when combined with a warm accent for contrast.

**Forbidden Uses:** Literal product demonstrations, SaaS explainer content, lifestyle content intended to feel warm and present-tense, any context where the audience needs to trust the reality being presented.

---

### 6. Warm Print

**Visual Character:** Amber-to-sepia lift in the shadow zones, transitioning through neutral mids to a paper-white (slightly warm, not clinical white) in the highlights. The overall impression is of a quality photographic print — warm, inviting, with depth in the shadows that reads as dimensionality rather than darkness. Colors are slightly shifted toward warmth across the full range.

**When to Use:** Archival-tone brand storytelling, editorial sequences referencing print culture, craft and artisan brand content, publishing and media brand films, any context where a sense of quality, permanence, and craft is required.

**Pairs With:** Warm Neutral palette mode (natural pairing). Restrained Editorial with a warm accent.

**Forbidden Uses:** Tech and SaaS contexts (the warmth reads as analog/outdated in this context), Dark Ground palette mode (the highlight lift conflicts with dark ground intent), Bold Poster mode.

---

### 7. Magazine Matte

**Visual Character:** Slightly lifted blacks (10–15% luminosity minimum), slightly reduced contrast in the mids, desaturated highlights. The result is a "flat" quality that is not underexposed — it is deliberately restrained. Colors are present but not vivid. The image reads as editorial in the truest sense: sophisticated, controlled, slightly aloof.

**When to Use:** High-fashion editorial sequences, luxury brand films, any context where the aesthetic register is "magazine feature" rather than "commercial advertisement," museum and gallery brand content.

**Pairs With:** Restrained Editorial palette mode (primary pairing). Duotone. Monochrome when pushed further toward full desaturation.

**Forbidden Uses:** Product e-commerce content (the flattening hides product detail and color accuracy), SaaS product UI demos, Bold Poster mode (directly contradicts the high-contrast intent of that mode), any context where the audience needs vivid color communication.

---

### 8. Studio Neutral

**Visual Character:** Near-accurate color reproduction with a subtle warmth bias in the mid tones — approximately +200K color temperature relative to true neutral. Blacks are clean, contrast is natural, no aggressive curve shaping. This is not "no LUT" — it is a precision LUT that removes the slight green or magenta bias common in digital capture while adding just enough warmth to prevent clinical sterility.

**When to Use:** Product beauty shots requiring color accuracy, SaaS UI demonstrations where interface colors must read correctly, corporate communications requiring trust and transparency, any context where distorting color accuracy would be a communication failure.

**Pairs With:** All palette modes as a foundation grade before the palette-specific LUT is applied. Most effective as a standalone grade for Warm Neutral and Dark Ground modes where a heavy character LUT would interfere with the palette intent.

**Forbidden Uses:** Should not be used as the only grade in editorial or fashion contexts — it will read as "ungraded" to a trained eye. It is a foundation, not a finish.

---

## Film Grain Implementation

### Why Grain Matters

AI-generated imagery and video shares a common failure mode: hyper-smooth surfaces. The mathematical perfection of diffusion model outputs creates a specific kind of synthetic sheen that reads immediately as generated to trained observers. Film grain is the primary technical remedy.

Grain destroys synthetic smoothness by introducing an organic, non-repeating texture pattern that the eye reads as evidence of physical capture. It is not merely aesthetic — it is a signal of authenticity. Calibrated grain is the difference between an image that reads as "photographed" and one that reads as "generated."

Grain must be calibrated to content type. Under-graining is invisible and useless. Over-graining is distracting and reads as a filter, which is worse than no grain.

---

### Grain Scale by Application

**Subtle: 0.02–0.05 opacity**
Applications: Product photography, SaaS interface sequences, data visualization, corporate communication, any content where the primary register is precision and the audience's attention must be on content rather than texture.
Grain size: Fine (1–2px particle scale at 1080p). Monochromatic grain preferred — luminance grain only, no color grain.
Effect: Invisible on casual viewing. Visible on direct comparison with an ungraded frame. Destroys AI sheen without drawing attention to the grain itself.

**Medium: 0.06–0.12 opacity**
Applications: Editorial sequences, lifestyle content, documentary-style brand films, interview segments, any content where a handmade or human-scale quality is intentional.
Grain size: Medium (2–4px particle scale at 1080p). Slight color variation in grain is acceptable — warm grain bias is appropriate for Warm Neutral and Warm Print contexts.
Effect: Perceptible on direct viewing. Contributes to the overall texture and feel of the image. Pairs with matte LUT applications.

**Pronounced: 0.13–0.20 opacity**
Applications: Black and white sequences, film emulation work, fashion editorial with an explicit photographic reference (Lindbergh, Newton, Avedon), archive-style storytelling.
Grain size: Coarse (4–8px particle scale at 1080p). Color grain is acceptable in film emulation contexts. Grain should be animated (frame-to-frame variation) — static grain reads as a texture overlay, not as film grain.
Effect: Immediately perceptible. The grain is a visible part of the aesthetic. In this range, grain is not hiding anything — it is the texture itself.

**Applying Grain to Video:** Grain must be animated — each frame must have a different random seed. Static grain applied uniformly across a video sequence reads immediately as a post-production filter. In AI video generation, specify "film grain" or "photographic grain" in prompts. In post-production compositing, use a dedicated grain layer with random seed variation per frame.

---

## Color Constraint System for AI Generators

### Universal Negative Prompts (inject into all AI image/video generation)

These terms are injected as negative prompts or exclusion instructions regardless of palette mode:

```
oversaturated, neon lights, HDR effect, Instagram filter, plastic texture,
rainbow gradients, digital art glow, chromatic neon, LED glow,
unrealistic color, artificial color enhancement, color pop effect,
selective color, lens flare rainbow, iridescent sheen
```

### Standard Positive Color Anchors (inject into all AI image/video generation)

These terms are injected as positive directional prompts, then overridden by palette-specific instructions:

```
muted colors, film photography, cinematic color grade, controlled lighting,
intentional shadow, natural light, photographic color, desaturated,
editorial photography, analog grain, restrained palette
```

### Palette-Mode-Specific Positive Injections

| Palette Mode | Positive Injection |
|---|---|
| Monochrome | `black and white photography, silver gelatin print, grayscale, tonal contrast, film grain` |
| Duotone | `duotone photograph, two-color palette, warm and cool tones, split-tone photography` |
| Restrained Editorial | `neutral tones, editorial photography, minimal color, one accent color, Scandinavian palette` |
| Bold Poster | `flat graphic colors, poster design, high contrast, solid color fills, no gradients` |
| Warm Neutral | `warm natural light, golden hour, earth tones, off-white, natural materials, warm daylight` |
| Dark Ground | `dark background, cinematic deep shadows, dramatic lighting, dark atmospheric, precision lighting` |

### Palette-Mode-Specific Negative Injections

| Palette Mode | Negative Injection |
|---|---|
| Monochrome | `color cast, colored light, colored shadows, color tint` |
| Duotone | `full color, multicolor, more than two colors, rainbow` |
| Restrained Editorial | `bright colors, multiple accent colors, colorful, vibrant, saturated` |
| Bold Poster | `gradients, textures, photographic, soft colors, muted` |
| Warm Neutral | `cool tones, blue light, grey, silver, cold atmosphere` |
| Dark Ground | `bright background, white background, light atmosphere, high key lighting` |

---

## Forbidden Color Moves by School

### Minimalist Precision
1. Using pure white (#FFFFFF) as the dominant — it reads clinical and undesigned. Use off-white with minimal warm undertone.
2. Adding a second accent color "for clarity" — one accent, always. Two accents collapse the visual hierarchy.
3. Using grey as a neutral without committing to a temperature — grey must be warm grey or cool grey, never the ambiguous middle.
4. Drop shadows on type or elements — they introduce the third dimension that minimalism refuses.
5. Tinting the entire palette toward one hue without intentional commitment — accidental warmth or coolness reads as an exposure error, not a palette decision.

### Editorial Luxury
1. Using brand primary colors at full saturation in editorial context — luxury does not shout its brand.
2. Any metallic gradient effect (gold gradients, silver sheen) — luxury materials are implied through photography, not simulated through digital effects.
3. Using black as the dominant without tonal variation in the dark zone — editorial luxury requires depth, not flat black fills.
4. Placing the accent color in more than one element per scene — the accent is a punctuation mark, not a repeated motif.

### Bold Statement
1. Using more than 5 colors in the palette — the power of Bold Poster comes from discipline within flatness.
2. Introducing photographic textures or gradients within color fills — these dilute the graphic voltage.
3. Using desaturated or neutral tones as the dominant — Bold Poster requires color commitment in the dominant zone.
4. Mixing full-saturation colors with muted neutrals — the contrast between a vivid color and a muted neutral reads as unresolved, not sophisticated.

### Warm Human
1. Introducing any cool or blue-adjacent tone into the palette — a single cool element breaks the warmth that is the entire basis of this mode.
2. Using pure white highlights — warm human palette requires cream, linen, or paper white. Pure white is too clinical.
3. Using black for shadow anchor — the darkest tone must be a warm dark brown, not black.
4. Oversaturating earth tones — the warmth in this palette comes from hue selection, not saturation push.
5. Adding a non-warm accent — if an accent is used, it must come from the warm family (amber, gold, terracotta). A blue or green accent betrays the palette.

### Dark Premium
1. Using pure black (#000000) as the dominant ground — true dark premium requires tonal variation in the dark zone.
2. Adding warm and cool accents simultaneously — one accent direction per scene.
3. Allowing any element to read as "dark mode UI" — the distinction between cinematic dark ground and interface dark mode is tonal sophistication. Flat dark fills read as UI.
4. Using mid-grey typography on dark ground — mid-grey disappears or reads as inaccessible contrast. Type is near-white or accent color only.

### Monochrome Film
1. Allowing any color element in the frame — zero color tolerance in true Monochrome mode.
2. Crushing blacks to pure 0,0,0 — shadow detail is a requirement. Black clip is a failure.
3. Applying digital noise instead of film grain — digital noise is regular and mathematical; film grain is organic and irregular. They read differently.
4. Using linear tonal mapping — monochrome film requires an S-curve with slightly lifted shadows and controlled highlights.
5. Mixing a warm-toned element into a cool-toned monochrome execution — if a tint is used, it is applied globally and consistently.

---

## Color Audit Checklist

Run this checklist before finalizing the color treatment of any clip or sequence.

- [ ] **1. 70/20/10 Ratio Verified.** Confirm that the dominant zone occupies approximately 70% of the frame, supporting zone approximately 20%, and accent zone is at or below 10%. If the ratio is violated, identify which zone is out of balance and correct before proceeding.

- [ ] **2. Accent Count = 1.** Count the number of distinctly colored accent elements in the frame. If the count is greater than one, identify the highest-value accent and neutralize all others to supporting tones.

- [ ] **3. Palette Mode Purity.** Identify the active palette mode. Check for any color element that violates the mode's rules. Specifically: any cool tone in Warm Neutral, any color element in Monochrome, any gradient in Bold Poster, any pure black in Dark Ground.

- [ ] **4. LUT Applied at Correct Opacity.** Confirm the LUT is applied at 60–85% opacity unless full-strength is intentionally specified. Confirm the LUT character matches the palette mode and content type.

- [ ] **5. Grain Present and Animated.** Confirm film grain is applied at the correct opacity range for the content type. Confirm the grain is animated (frame-to-frame variation) and not static. Confirm grain particle size is appropriate for the resolution.

- [ ] **6. Negative Prompt Injection Verified.** Confirm that universal negative color prompts have been injected into any AI-generated source material in this sequence. Confirm palette-mode-specific negative prompts are active. Flag any source frame that reads as oversaturated, neon-adjacent, or HDR-processed.
