# StataLinux

Sublime Text 3 plugin that adds support for Stata (all versions).

![screencast_functions.gif](/screencast_functions.gif "StataLinux in action!")

## Background

I needed a minimal and effective plugin for sending code from Sublime Text into Stata.
Since none of the plugins in the Package Control was specifically tailored for Linux, and none of the maintainers seem to want to add Linux support in the short run, I wrote my own.
This plugin is originally based on [StataEnhanced](https://github.com/andrewheiss/SublimeStataEnhanced), and also on [these notes](https://github.com/cwitt2013/SublimeText_Stata_Linux).

## Dependencies

- `xdotool`
- `xclip`

These packages are likely already in your system.
You can check their presence by typing each name with the `--version` option in your terminal.
For example,
```bash
xdotool --version
```
If the output is something like `xdotool version 3.20160805.1`, then it's installed.
If you get an error, then the package is not installed.
Use your system's package manager to install them.
For example,

### Arch(-based)
```bash
sudo pacman -S xclip xdotool
```

### Ubuntu(-based)
```bash
sudo apt install xclip xdotool
```
etc.



## Installation

There are two ways to install this plugin:

1. Search for "StataLinux" on Package Control, or
2. Copy/clone the entire plugin folder (this repository) to `~/.config/sublime-text-3/Packages/`.

Make sure you have installed the [dependencies](#dependencies) listed above before using it.

## Usage

Make sure you have one instance of Stata open.
Open a `.do` (or `.ado`) file in ST3.
You have two keybindings for executing code:
1. `ctrl+d` executes the current line, or the selected lines if a selection is made, and
2. `crtl+shift+d` executes the entire file.

These actions may also be called using the Command Palette: after invoking it with `ctrl+shit+p`, type "StataLinux" and select an action.
Additionally, these actions are accesible in the main menu under `Tools > Packages > StataLinux`.

## Known issues

1. ~~Currently, there is an [issue](https://github.com/jordansissel/xdotool/issues/43) with `xdotool`'s `clearmodifiers` option.
This has the consequence that the plugin will fail to operate correctly if any keyboard modifiers (e.g. Caps Lock) are not manually turned off.~~
Now not an issue, since I'm using `xdotool` with the `--window`, which seems cleaner than focusing and refocusing windows, and has the added bonus of disregarding any active modifiers.

2. There is currently no option for switching focus to the Stata window.
This is because there are good reasons to use `xdotool` with the `--window` option (see issue #1), so I don't plan on implementing this.
Window focus is a task for window managers, anyway.
