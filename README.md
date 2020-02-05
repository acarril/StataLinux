# StataLinux
Sublime Text 3 plugin that adds support for Stata 13-16.

## Dependencies

- `xdotool`
- `xclip`

## Installation

There are two ways to install this plugin:

1. Search for "StataLinux" on Package Control, or
2. Copy/clone the entire plugin folder to `~/.config/sublime-text-3/Packages/`.

Make sure you have installed the [dependencies](#dependencies) listed above before using it.

## Known issues

- Currently, there is an [issue](https://github.com/jordansissel/xdotool/issues/43) with `xdotool`'s `clearmodifiers` option.
This has the consequence that the plugin will fail to operate correctly if any keyboard modifiers (e.g. Caps Lock) are not manually turned off.
