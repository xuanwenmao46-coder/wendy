# Type Audit

## Immediate Red Flags

- Arial, Inter, Roboto, Poppins, Sora, Trebuchet, Georgia used as final premium typography.
- All text uses the same font, size, and weight.
- Headline below 72px in a 1280x720 launch frame.
- Body below 24px.
- Labels below 16px.
- Numbers are proportional and do not align.
- Text animation is doing the hierarchy work because static type is weak.
- Font files are not embedded.

## Fixes

- Enlarge the display type before adding more decoration.
- Reduce words before shrinking type.
- Use one expressive display font and one quiet support font.
- Use a mono/data font for numbers.
- Add local `@font-face` and rerun lint.

## Checklist

- [ ] Display type has a strong voice.
- [ ] Support type recedes.
- [ ] Data uses tabular numbers.
- [ ] Sizes are video-sized.
- [ ] Fonts are locally embedded.
- [ ] The frame still works with motion disabled.
