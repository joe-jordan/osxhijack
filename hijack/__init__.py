import os

def open_terminal_app():
  """activates the terminal application."""
  os.system("""osascript -e 'tell application "Terminal" to activate """)

def terminal(command):
  """uses the applescript command to run a script in an existing terminal window,
so that the process will live on after this session has logged out."""
  l = """osascript -e 'tell application "Terminal" to do script """ + '"' + command + '"\''
  os.system(l)
