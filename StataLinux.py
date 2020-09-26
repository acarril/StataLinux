import sublime
import sublime_plugin
import subprocess
from os import remove
from os import path
from tempfile import mkstemp

settingsfile = "StataLinux (Linux).sublime-settings"

class StataLinuxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Load settings
		settings = sublime.load_settings(settingsfile)
		always_extract_full_line = settings.get('always_extract_full_line')
		remove_temp_file = settings.get('remove_temp_file')
		

		# Collect selected range or full current line if no selection in a list 
		contents = []
		for region in self.view.sel():
			# select full line if region starts and ends at the same point
			if always_extract_full_line or region.a == region.b:
				region = self.view.full_line(region)
			contents.append(self.view.substr(region))

		# write contents into a temporary file
		fd, filename = mkstemp(prefix="StataLinux_", suffix=".do")
		with open(filename, "w") as file:
			for content in contents:
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
		if remove_temp_file: remove(filename)
		# Print status message for debugging:
		# sublime.status_message("Content:%s" % content)
		sublime.status_message('StataLinuxCommand ran successfully')


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
		

