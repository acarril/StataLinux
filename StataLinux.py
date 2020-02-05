import sublime
import sublime_plugin
import subprocess
from os import remove

class StataLinuxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Collect selected line(s) or current line if none selected:
		region = self.view.line(self.view.sel()[0])
		content = self.view.substr(region)
		# Create temporary file with content to be run:
		filepath = os.path.split(self.view.file_name())[0]
		filename = os.path.join(filepath, "tempfile.do")
		with open(filename, "w") as file:
			file.write(content)
		# Create and execute bash command:
		sublime_stata_sh_path = os.path.join(sublime.packages_path(), "StataLinux", "sublime-stata.sh")
		cmd = "sh " + sublime_stata_sh_path + " " + '"' + filename + '"'
		ret = subprocess.call(cmd, shell = True)
		if ret != 0:
			sublime.error_message("Bash script returned error code %s." % ret)
		# Remove temporary file:
		os.remove(filename)
		# Print status message for debugging:
		# sublime.status_message("Content:%s" % sys.version)

class StataLinuxAllCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Define current file as the one to be run:
		filename = self.view.file_name()
		# Create and execute bash command:
		sublime_stata_sh_path = os.path.join(sublime.packages_path(), "StataLinux", "sublime-stata.sh")
		cmd = "sh " + sublime_stata_sh_path + " " + '"' + filename + '"'
		ret = subprocess.call(cmd, shell = True)
		if ret != 0:
			sublime.error_message("Bash script returned error code %s." % ret)
		
