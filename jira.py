import sys

sys.path.append('./modules/jira')
import Jira

j = Jira.Jira("test-project")

j.display_project()