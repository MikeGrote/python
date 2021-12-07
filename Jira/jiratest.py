from jira.client import JIRA
import logging

# Defines a function for connecting to Jira
def connect_jira(log, jira_server, jira_user, jira_password):
    '''
    Connect to JIRA. Return None on error
    '''
    try:
        log.info("Connecting to JIRA: %s" % jira_server)
        jira_options = {'server': jira_server}
        jira = JIRA(options=jira_options, basic_auth=(jira_user, jira_password))
                                        # ^--- Note the tuple
        return jira
    except Exception:
        log.error("Failed to connect to JIRA: %s" )
        return None

def create_ticket( ):
    # create logger
    log = logging.getLogger(__name__)

    # NOTE: You put your login details in the function call connect_jira(..) below!

    # create a connection object, jc
    jc = connect_jira(log, "https://incept4-service.atlassian.net", "mike.grote@incept4.de", "HXXT9Mh0fk9I3mKabiCv0F04")
                      
    # print names of all projects
    projects = jc.projects()
    for v in projects:
           print (v)
           
    new_issue = jc.create_issue(project='AUSKUNFT', summary='New issue from jira-python',
                                  description='Look into this one', issuetype={'name': 'Task'})
