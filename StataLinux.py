
import sublime
import sublime_plugin
import os

x = "HALLO"
# allcontent = sublime.Region(0, self.view.size())

class StataLinuxCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		stataname = "Stata/MP 15.1"
		region_all = sublime.Region(0, self.view.size())
		filename = os.path.split(self.view.file_name())[1]
		filepath = os.path.split(self.view.file_name())[0]
		# x = self.view.file_name()
		content = self.view.substr(region_all)
		# self.view.replace(edit, allcontent, 'Hello, World!')
		# self.view.insert(edit, 0, lala)
		# sublime.status_message("Content:%s" % tempfile)
		tempfile = os.path.join(filepath, "tempfile.do")
		with open(tempfile, "w") as file:
			file.write(content)
		cmd = "sh /home/alvaro/.config/sublime-text-3/Packages/StataLinux/sublime-stata.sh" + " " + '"' + tempfile + '"'
		os.system(cmd)
		os.remove(tempfile)
		# sep
		# string = ""
  #       for region in view.sel():
  #       	if not region.empty():
  #           	string += view.substr(region)
  #       if string != "":
  #           sublime.set_clipboard(string)
