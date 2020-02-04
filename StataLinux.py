import sublime
import sublime_plugin
import os

class StataLinuxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Current file info:
		filename = os.path.split(self.view.file_name())[1]
		filepath = os.path.split(self.view.file_name())[0]
		# Determine if content is selection and select region accordingly:
		is_selection = len(self.view.sel()[0]) > 0
		if is_selection:
			region = self.view.sel()[0]
		else:
			region = sublime.Region(0, self.view.size())
		content = self.view.substr(region)
		# Create temporary file with content to be run
		tempfile = os.path.join(filepath, "tempfile.do")
		with open(tempfile, "w") as file:
			file.write(content)
		# Create and execute bash command:
		cmd = "sh /home/alvaro/.config/sublime-text-3/Packages/StataLinux/sublime-stata.sh" + " " + '"' + tempfile + '"'
		os.system(cmd)
		# Remove temporary file:
		os.remove(tempfile)
		# Print status message for debugging:
		# sublime.status_message("Content:%s" % lala)
