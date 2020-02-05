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

1. ~~Currently, there is an [issue](https://github.com/jordansissel/xdotool/issues/43) with `xdotool`'s `clearmodifiers` option.
This has the consequence that the plugin will fail to operate correctly if any keyboard modifiers (e.g. Caps Lock) are not manually turned off.~~
Now not an issue, since I'm using `xdotool` with the `--window`, which seems cleaner than focusing and refocusing windows, and has the added bonus of disregarding any active modifiers.

2. There is currently no option for switching focus to the Stata window.
This is because there are good reasons to use `xdotool` with the `--window` option (see issue #1), so I don't plan on implementing this.
Window focus is a task for window managers, anyway.
