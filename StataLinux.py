import sublime
import sublime_plugin
import subprocess
from os import remove
from os import path

settingsfile = "StataLinux.sublime-settings"

class StataLinuxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings(settingsfile)
		# Collect selected line(s) or current line if none selected:
		region = self.view.line(self.view.sel()[0])
		content = self.view.substr(region)
		# Create temporary file with content to be run:
		filepath = path.split(self.view.file_name())[0]
		filename = path.join(filepath, "tempfile.do")
		with open(filename, "w") as file:
			file.write(content + "\n")
		# Create and execute bash command:
		sublime_stata_sh_path = path.join(sublime.packages_path(), "StataLinux", "sublime-stata.sh")
		cmd = "sh " + sublime_stata_sh_path + " " + '"' + filename + '"'
		ret = subprocess.call(cmd, shell = True)
		if ret != 0:
			if ret == 1:
				sublime.error_message("Bash script returned error code %s.\nIt seems Stata is not running." % ret)
			else:
				sublime.error_message("Bash script returned error code %s." % ret)
		# Remove temporary file:
		remove(filename)
		# Print status message for debugging:
		# sublime.status_message("Content:%s" % content)

class StataLinuxAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings(settingsfile)
		# Switch focus to Stata or not after sending a command depending on a setting
		if settings.get('save_before_run_all'):
			self.view.run_command("save")
		# Define current file as the one to be run, saving it first
		filename = self.view.file_name()
		# Create and execute bash command:
		sublime_stata_sh_path = path.join(sublime.packages_path(), "StataLinux", "sublime-stata.sh")
		cmd = "sh " + sublime_stata_sh_path + " " + '"' + filename + '"'
		ret = subprocess.call(cmd, shell = True)
		if ret != 0:
			if ret == 1:
				sublime.error_message("Bash script returned error code %s.\nIt seems Stata is not running." % ret)
			else:
				sublime.error_message("Bash script returned error code %s." % ret)
		
