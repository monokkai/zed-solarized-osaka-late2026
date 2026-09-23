# Solarized Osaka Late 2026

A Zed port of [craftzdog/solarized-osaka.nvim](https://github.com/craftzdog/solarized-osaka.nvim)
at `style = "vivid"` — the variant used in his
[feat/late-2026](https://github.com/craftzdog/dotfiles/tree/feat/late-2026/dot_config/nvim)
Neovim config.

Colours were read out of the running Neovim theme rather than sampled from
screenshots, so the same token lands on the same hex in both editors.

## Variants

| Theme | Surfaces |
| --- | --- |
| **Solarized Osaka Late 2026** | opaque |
| **Solarized Osaka Late 2026 (Blurred)** | translucent, for window blur |

The blurred variant lowers the alpha on panels, tab bar, title bar and terminal
so the OS blur shows through. Colours are otherwise identical.

## Palette

| Role | Colour |
| --- | --- |
| Background | `#001419` |
| Cursor line | `#002c38` |
| Selection, borders | `#063540` |
| Foreground | `#b6c5c6` |
| Comments | `#7b99a2` |
| Strings, numbers, constants | `#34c5b9` |
| Keywords, operators, native tags | `#a2bb00` |
| Functions, properties, attributes | `#5aaefa` |
| Types, enums | `#dba500` |
| JSX components | `#ff6c6a` |
| Parameters, cursor, active line | `#fb724a` |
| Namespaces | `#9498ea` |
| Enum variants | `#fe67a8` |
| Brackets, delimiters | `#e0e2ea` |

### JSX / TSX

Native HTML elements (`div`, `h1`, `p`) take the keyword green; imported
components (`<Box>`, `<BasePage>`) take the red of the `import` keyword they
arrived on. Attributes are blue, brackets near-white — matching the Neovim
config.

## Install

### From Zed's extension list

`cmd-shift-p` → **zed: extensions** → search "Solarized Osaka Late 2026" →
**Install**. Then `cmd-k cmd-t` to select it.

### From source

```bash
git clone https://github.com/monokkai/zed-solarized-osaka-late2026
```

`cmd-shift-p` → **zed: install dev extension** → select the cloned folder.

### Window blur

```json
{
  "window_background": "blurred",
  "theme": "Solarized Osaka Late 2026 (Blurred)"
}
```

## Development

Both variants are generated from one palette:

```bash
python3 build.py
```

Edit `PALETTE` in `build.py` and re-run. Do not hand-edit
`themes/solarized-osaka-late2026.json` — it is overwritten on every build.

## Publishing to the Zed extension registry

**1. Push this repo to GitHub**

```bash
git remote add origin https://github.com/monokkai/zed-solarized-osaka-late2026
git push -u origin main
git tag v0.1.0 && git push --tags
```

**2. Fork [zed-industries/extensions](https://github.com/zed-industries/extensions)**

**3. Add this repo as a submodule**

```bash
git submodule add https://github.com/monokkai/zed-solarized-osaka-late2026 \
  extensions/solarized-osaka-late2026
```

**4. Register it in `extensions.toml`**

```toml
[solarized-osaka-late2026]
submodule = "extensions/solarized-osaka-late2026"
version = "0.1.0"
```

**5. Normalise and open a PR**

```bash
pnpm install && pnpm sort-extensions
```

Commit, push, and open a pull request against `zed-industries/extensions`. Once
merged it appears in Zed's extension list for everyone.

**Updating later:** bump `version` in `extension.toml`, tag a release here, then
raise the matching `version` in `extensions.toml` with a new PR.

## Credits

- [solarized-osaka.nvim](https://github.com/craftzdog/solarized-osaka.nvim) by
  Takuya Matsuyama — Apache 2.0

## License

Apache License 2.0, inherited from the upstream theme.
