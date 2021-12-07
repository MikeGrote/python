from jira.client import JIRA
import mysql.connector
import logging


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


def map_issuetype(issuetype):
    if issuetype == b'10103':
        return 'Bug'
    if issuetype == b'10200':
        return 'Anforderung'
    if issuetype == b'10201':
        return 'Unterstützung Tagesgeschäft'
    if issuetype == b'10300':
        return 'MAKO2020'
    if issuetype == b'10104':
        return 'Zugriff'
    else:
        raise SyntaxError("issuetype unknown")
        print(issuetype, not found)
        exit()
        return issuetype
    

# create logger
log = logging.getLogger(__name__)
    
db = mysql.connector.connect(
  host="192.168.101.230",
  user="jiradbuser",
  password="dephor03.",
  database="jiradb"
)

count = 1

cursor = db.cursor(dictionary=True,buffered=True)
cursor.execute("SELECT * FROM jiraissue WHERE project = '10304' ORDER BY issuenum DESC")
#cursor.execute("SELECT * FROM jiraissue WHERE project = '10304' and issuenum = '1833' LIMIT 1")


#jc = connect_jira(log, "https://incept4-service.atlassian.net", "mike.grote@incept4.de", "HXXT9Mh0fk9I3mKabiCv0F04")
jc = connect_jira(log, "https://incept4-service.atlassian.net", "jirabot@i4service.cloud", "48EGvqXhz8p0wBjY3heh471D")


for row in cursor:
    #print(row['ID'])
    #print(row['issuenum'])
    #print(row['DESCRIPTION'])
    #print(row['issuetype'])
              
    #item['title'] = [t.encode('utf-8') for t in row['DESCRIPTION']]
  
      
    temksv = db.cursor(dictionary=True,buffered=True)
    val = ("HAS-" + str(row['issuenum']))
    temksvsql = "SELECT * FROM temksv WHERE oldkey='" + val +"' LIMIT 1"
    temksv.execute(temksvsql)
    #print( temksv.rowcount)
    if temksv.rowcount == 1:
        print(val, "Bereits vorhanden")
        continue

    print(row['issuenum'])
    
# =================== Tickets
    body_issue =  "User: " + row['REPORTER'].decode("utf-8") + "\n"
    body_issue = body_issue + "Datum: " + str(row['UPDATED']) + "\n"
    body_issue = body_issue + row['DESCRIPTION'].decode("utf-8")
    summary = 'STWHAS-' + str(row['issuenum']) + ": " + row['SUMMARY'].decode("utf-8")
    new_issue = jc.create_issue(project='AUSKUNFT',
                                 summary=summary,
                                 description=body_issue,
                                 issuetype={'name': map_issuetype(row['issuetype'])})
   
# ================== Comments
    cursor_action = db.cursor(dictionary=True)
    cursor_action_sql = "SELECT * FROM jiraaction WHERE issueid = " + str(row['ID'])
    cursor_action.execute(cursor_action_sql)
    for row_act in cursor_action:
        body =        "User: " + row_act['AUTHOR'].decode("utf-8") + "\n"
        body = body + "Datum: " + str(row_act['UPDATED']) + "\n"
        body = body + row_act['actionbody'].decode("utf-8")
        body = body[0:32767]
        if row_act['rolelevel'] == None:
            comment = jc.add_comment(new_issue, body)
        else:
           # comment = jc.add_comment(new_issue,body, visibility={'type': 'role', 'value': 'Administrators'})
            comment = jc.add_comment(new_issue,body, visibility={'type': 'group', 'value': 'INCEPT4'})
            
# =================== Attachments
    cursor_att = db.cursor(dictionary=True)
    cursor_att_sql = "SELECT * FROM fileattachment WHERE issueid = " + str(row['ID'])
    cursor_att.execute(cursor_att_sql)

    for row_att in cursor_att:
        path = 'C:\\temp\\JIRA\\Migration\\HAS\\HAS-' + str(row['issuenum']) + '\\' + str(row_att['ID'])
        print(path)
        try:
            jc.add_attachment(issue=new_issue, attachment=path, filename=row_att['FILENAME'].decode("utf-8"))
        except FileNotFoundError as err:
            print("File not found!", row_att['FILENAME'].decode("utf-8"))

    jc.transition_issue(new_issue, "Fertig")

# == OLDKEY NEWKEY
    print(row['issuenum'], new_issue.key)

    sql = "INSERT INTO temksv (oldkey, newkey) VALUES (%s, %s)"
    val = (("HAS-" + str(row['issuenum'])) , new_issue.key)
    temksv.execute(sql,val)

    

    db.commit()

    count = count + 1
    if count >= 2000:
        print("Exit", count)
        break
