# Jira modules to deploy jira instance
class Jira:
  def __init__(self, project):
    self.project = project
  
  def display_project(self):
    print(self.project)