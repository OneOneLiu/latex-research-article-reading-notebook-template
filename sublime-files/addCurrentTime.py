import sublime
import datetime
import sublime_plugin
class AddCurrentTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents": "\\textcolor{blue}{%s}" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        )
