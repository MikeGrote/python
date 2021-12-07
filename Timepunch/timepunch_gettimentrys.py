import re
from xml.etree import ElementTree
import requests
import hashlib

# url="http://timepunch.incept4.local/TimePunch/API/TpAuth.svc?WSDL"
url = "http://timepunch.incept4.local/timepunch/Api/TpTimeEntries.svc?WSDL"
headers = {'content-type': 'application/soap+xml'}
#headers = {'content-type': 'text/xml'}

# userid = "49dba64d-44b9-40c0-8421-b1dcbafdc159" #Ralf
userid = "a9602120-c498-4c70-a89c-f5a4c0e6a6c2"  # Mike
#userid = ""

url = "http://timepunch.incept4.local/timepunch/Api/TpTimeEntries.svc"
user = "incept4\mike.grote"
password_clear = "1q2w3e"
password = hashlib.md5(password_clear.encode())
print(password.hexdigest().upper())

timeentry_user = "incept4\\mike.grote"
day = "2021-10-25"

body = """
<s:Envelope
	xmlns:s="http://www.w3.org/2003/05/soap-envelope"
	xmlns:a="http://www.w3.org/2005/08/addressing">
	<s:Header>
		<a:Action s:mustUnderstand="1">http://tempuri.org/ITimeEntryService/SearchTimeEntries</a:Action>
		<a:MessageID>urn:uuid:3a48c35d-6d1f-45db-8bae-2a7b9cff71a3</a:MessageID>
		<ActivityId CorrelationId="e3fdf940-b56e-4127-aa0c-deac54f9e40f"
			xmlns="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics">00000000-0000-0000-0000-000000000000
		</ActivityId>
		<a:ReplyTo>
			<a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address>
		</a:ReplyTo>
		<a:To s:mustUnderstand="1">http://timepunch.incept4.local/timepunch/Api/TpTimeEntries.svc</a:To>
	</s:Header>
	<s:Body>
		<SearchTimeEntries
			xmlns="http://tempuri.org/">
			<authentication
				xmlns:b="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.AuthenticationService.Dto"
				xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
				<b:Culture>de</b:Culture>
				<b:CustomerToken>default_timepunch</b:CustomerToken>
				<b:Identity>""" + timeentry_user + """</b:Identity>
				<b:Origin>Management</b:Origin>
				<b:TpHashedPwd>""" + password.hexdigest().upper() + """</b:TpHashedPwd>
				<b:TpUser>""" + user + """</b:TpUser>
			</authentication>
			<search
				xmlns:b="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.TimeEntryService.Dto"
				xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
				<Page
					xmlns="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.Core.Dto">0
				</Page>
				<PageSize
					xmlns="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.Core.Dto">0
				</PageSize>
				<UsePaging
					xmlns="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.Core.Dto">false
				</UsePaging>
				<b:Confidentiality>Undefined</b:Confidentiality>
				<b:Created>0001-01-01T00:00:00</b:Created>
				<b:CreatedBy>00000000-0000-0000-0000-000000000000</b:CreatedBy>
				<b:FilteredProjects
					xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/>
					<b:FilteredTasks
						xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/>
						<b:FilteredUsers
							xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/>
							<b:Id>00000000-0000-0000-0000-000000000000</b:Id>
							<b:IsNew>false</b:IsNew>
							<b:LastUpdate>0001-01-01T00:00:00</b:LastUpdate>
							<b:LastUpdateBy>00000000-0000-0000-0000-000000000000</b:LastUpdateBy>
							<b:LogoffTime>""" + day + """T00:00:00 </b:LogoffTime>
							<b:LogonTime>""" + day + """T00:00:00</b:LogonTime>
							<b:Payment>SearchAllEntries</b:Payment>
							<b:ReportTitle i:nil="true"/>
							<b:ShowBreaks>true</b:ShowBreaks>
							<b:ShowPublicHolidays>false</b:ShowPublicHolidays>
							<b:ShowWeekends>false</b:ShowWeekends>
							<b:ShowWorkingTime>true</b:ShowWorkingTime>
							<b:FilteredCustomers
								xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/>
								<b:ShowMissingdays>false</b:ShowMissingdays>
								<b:ShowWeekdays>false</b:ShowWeekdays>
								<b:FirstModificationTime i:nil="true"/>
								<b:LastModificationTime i:nil="true"/>
								<b:IsImportant i:nil="true"/>
								<b:IsOnSite i:nil="true"/>
								<b:EnhanceWithAuditTrail>false</b:EnhanceWithAuditTrail>
								<b:TimeFrame>UserDefined</b:TimeFrame>
								<b:IsNotInvoiced i:nil="true"/>
								<b:MergeOvernightEntries>false</b:MergeOvernightEntries>
							</search>
						</SearchTimeEntries>
					</s:Body>
				</s:Envelope>
				"""


response = requests.post(url, data=body, headers=headers)
# print(response.content)


# define namespace mappings to use as shorthand below
namespaces = {
    's': 'http://www.w3.org/2003/05/soap-envelope',
    'a': 'http://www.w3.org/2005/08/addressing',
    'b': 'http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.TimeEntryService.Dto',
    'i': 'http://www.w3.org/2001/XMLSchema-instance',
}
root = ElementTree.fromstring(response.content)
body = root.find('s:Body', namespaces)
timeentrys_res = body.find(
    '{http://tempuri.org/}SearchTimeEntriesResponse', namespaces)
if not timeentrys_res:
    print('No Entrys1')
    exit()
timeentrys = timeentrys_res.find(
    '{http://tempuri.org/}SearchTimeEntriesResult', namespaces)
if not timeentrys:
    print('No Entrys2')
    exit()


#timeentrys = body.find('{http://tempuri.org/}SearchTimeEntriesResponse')

# reference the namespace mappings here by `<name>:`
names = root.findall(
    './s:Body'
    '/{http://tempuri.org/}SearchTimeEntriesResponse'
    '/{http://tempuri.org/}SearchTimeEntriesResult'
    '/b:TimeEntryDto'
    '/b:*',
    namespaces
)

for name in names:
    name.tag = re.sub("[{@*&?].*[}@*&?]", "", name.tag)

for name in names:
    print(name.tag, name.text)


def elementtree_to_dict(element):
    node = dict()

    text = getattr(element, 'text', None)
    if text is not None:
        node['text'] = text

    node.update(element.items())  # element's attributes

    child_nodes = {}
    for child in element:  # element's children
        child_nodes.setdefault(child, []).append(elementtree_to_dict(child))

    # convert all single-element lists into non-lists
    for key, value in child_nodes.items():
        if len(value) == 1:
            child_nodes[key] = value[0]

    node.update(child_nodes.items())

    return node


#dict = elementtree_to_dict(timeentrys)
i = 0
for timeentry in timeentrys_res:
	i = i + 1
	zeiten = elementtree_to_dict(timeentry)
	print(zeiten)
	for key in zeiten:
		print("test", zeiten[key] )

	#print(zeiten["{http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.AuthenticationService.Dto}Id"])

