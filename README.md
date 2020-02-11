# StataLinux

Sublime Text 3 plugin that adds basic support for Stata (all versions) in Linux.

- Language definitions for `do` and `ado` files
- Commands for sending a selection of lines or the whole file to Stata.
See [usage](#usage) for more details. 

![screencast_functions.gif](https://raw.githubusercontent.com/acarril/StataLinux/master/img/screencast_functions.gif "StataLinux in action!")

## Background

I needed a minimal yet robust plugin for sending code from Sublime Text into Stata.
Since none of the plugins in the Package Control was specifically tailored for Linux, and none of the maintainers seem to want to add Linux support to theirs, I wrote my own.
This plugin is originally based on [StataEnhanced](https://github.com/andrewheiss/SublimeStataEnhanced), and also on [these notes](https://github.com/cwitt2013/SublimeText_Stata_Linux).

This plugin aims for robustness over bells and whistles, and almost all the decisions were taken with that philosophy in mind.
It basically creates a temporary file which is to be executed in Stata.
The file is sent for execution by copying `do <filepath>` to the clipboard with `xclip`, and then pasting this string directly (and in the background) to Stata's command pane using `xdotool`.


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
1. `ctrl+alt+d` executes the current line, or the selected lines if a selection is made, and
2. `crtl+alt+shift+d` executes the entire file.

These actions may also be called using the Command Palette: after invoking it with `ctrl+shit+p`, type "StataLinux" and select an action.
Additionally, these actions are accessible in the main menu under `Tools > Packages > StataLinux`.

Note that if a line is only partially selected, the program will automatically select the whole line for execution.

## Other features

### Comments

Comment toggling for entire lines works with the default ST3 keybinding, `ctrl+\`.

![comments_basic.gif](/img/comments_basic.gif "Comments in action!")

### Locals

Typing a backtick `` ` `` anywhere in the code will immediately put a closing tick after it, with the cursor inside.
Typing a backtick with a `word` selected will yield `` `word' ``.

![locals.gif](/img/locals.gif "Locals in action!")

## Stata versions, flavors and instances

Make sure you have an instance of Stata *with GUI* open (`xstata`, or its various flavors); this plugin doesn't work with Stata's CLI.
No additional configuration needs to be added to indicate version or flavor, since the program will detect any running instance automatically.
If you have more than one instance of Stata open, the plugin will default to choosing the most recently opened one (internally, it looks for the last entry of `xdotool search --classname "stata"`).


## Known issues

1. ~~Currently, there is an [issue](https://github.com/jordansissel/xdotool/issues/43) with `xdotool`'s `clearmodifiers` option.
This has the consequence that the plugin will fail to operate correctly if any keyboard modifiers (e.g. Caps Lock) are not manually turned off.~~
Now not an issue, since I'm using `xdotool` with the `--window`, which seems cleaner than focusing and refocusing windows, and has the added bonus of disregarding any active modifiers.

2. There is currently no option for switching focus to the Stata window.
This is because there are good reasons to use `xdotool` with the `--window` option (see issue #1), so I don't plan on implementing this.
Window focus is a task for window managers, anyway.
