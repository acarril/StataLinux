# StataLinux
Sublime Text 3 plugin that adds support for Stata 13-16.

## Dependencies

- `xdotool`
- `wnctrl`
- `xclip`
- `xprop`

## Known issues

- Currently, there is an [issue](https://github.com/jordansissel/xdotool/issues/43) with `xdotool`'s `clearmodifiers` option.
This has the consequence that the plugin will fail to operate correctly if any keyboard modifiers (e.g. Caps Lock) are not manually turned off.
