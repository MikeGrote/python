import requests
import hashlib

#url="http://timepunch.incept4.local/TimePunch/API/TpAuth.svc?WSDL"
url="http://timepunch.incept4.local/timepunch/Api/TpTimeEntries.svc?WSDL"
headers = {'content-type': 'application/soap+xml'}
#headers = {'content-type': 'text/xml'}

#userid = "49dba64d-44b9-40c0-8421-b1dcbafdc159" #Ralf
userid = "a9602120-c498-4c70-a89c-f5a4c0e6a6c2" #Mike 
#userid = ""

url = "http://timepunch.incept4.local/timepunch/Api/TpTimeEntries.svc"
user = "incept4\mike.grote"
password_clear = "1q2w3e"
password      = hashlib.md5(password_clear.encode())
print(password.hexdigest().upper())

timeentry_user = "incept4\\mike.grote"


body = """
<s:Envelope
	xmlns:s="http://www.w3.org/2003/05/soap-envelope"
	xmlns:a="http://www.w3.org/2005/08/addressing">
	<s:Header>
		<a:Action s:mustUnderstand="1">http://tempuri.org/ITimeEntryService/ValidateAndSaveTimeEntry</a:Action>
		<a:MessageID>urn:uuid:9ad36c3d-2dca-484f-82b7-ef7a2b302785</a:MessageID>
		<ActivityId CorrelationId="6e76d5e6-570c-4861-80ad-bfd0cc229081"
			xmlns="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics">00000000-0000-0000-0000-000000000000
		</ActivityId>
		<a:ReplyTo>
			<a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address>
		</a:ReplyTo>
		<a:To s:mustUnderstand="1">""" + url + """</a:To>
	</s:Header>
	<s:Body>
		<ValidateAndSaveTimeEntry
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
			<timeEntry i:type="b:TimeEntryDto"
				xmlns:b="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.TimeEntryService.Dto"
				xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
				<Id
					xmlns="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.Core.Dto">a8c42988-c4ae-4c52-a35c-870a5f22df88
				</Id>
				<LastUpdate
					xmlns="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.Core.Dto">0001-01-01T00:00:00
				</LastUpdate>
				<Created
					xmlns="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.Core.Dto">0001-01-01T00:00:00
				</Created>
				<b:BreakTime>0</b:BreakTime>
				<b:Description>testr2 &#xD;test
</b:Description>
				<b:HasBeenPaid>false</b:HasBeenPaid>
				<b:LogoffTime>2021-10-26T11:00:00</b:LogoffTime>
				<b:LogonName>incept4\mike.grote</b:LogonName>
				<b:LogonTime>2021-10-26T09:00:00</b:LogonTime>
				<b:ProjectId>bd0d4523-aea6-4a42-b840-ef61b54b1ed3</b:ProjectId>
				<b:TaskId>5875c45d-1767-4a1e-b2f3-bb2ce0bb852d</b:TaskId>
				<b:Usage>WorkTime</b:Usage>
				<b:CustomerId>e16b5b28-d8f5-4114-9a7c-94ecd2f67615</b:CustomerId>
				<b:IsImportant>false</b:IsImportant>
				<b:IsOnSite>false</b:IsOnSite>
				<b:IsNotInvoiced>false</b:IsNotInvoiced>
				<b:Duration>4</b:Duration>
				<b:CutTime>0</b:CutTime>
				<b:LogoffLocation i:nil="true"/>
				<b:LogonLocation i:nil="true"/>
				<b:SiblingId>00000000-0000-0000-0000-000000000000</b:SiblingId>
				<b:BackgroundColor>0</b:BackgroundColor>
				<b:DrivingTime>0</b:DrivingTime>
				<b:Leave>0</b:Leave>
				<b:ProjectName/>
				<b:Sick>0</b:Sick>
				<b:TakenOvertime>0</b:TakenOvertime>
				<b:TaskName i:nil="true"/>
				<b:TextColor>0</b:TextColor>
				<b:WorkTime>8</b:WorkTime>
				<b:UserId> """ + userid + """</b:UserId>
				<b:CustomerName i:nil="true"/>
				<b:CustomerRefNr i:nil="true"/>
				<b:IsVirtual>false</b:IsVirtual>
				<b:CreatedBy
					xmlns:c="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.AuthenticationService.Dto">
					<c:Email i:nil="true"/>
					<c:Id>00000000-0000-0000-0000-000000000000</c:Id>
					<c:LogonName i:nil="true"/>
					<c:SaveAsName i:nil="true"/>
					<c:UserName i:nil="true"/>
				</b:CreatedBy>
				<b:DurationAsDay>0</b:DurationAsDay>
				<b:LastUpdatedBy
					xmlns:c="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.AuthenticationService.Dto">
					<c:Email i:nil="true"/>
					<c:Id>00000000-0000-0000-0000-000000000000</c:Id>
					<c:LogonName i:nil="true"/>
					<c:SaveAsName i:nil="true"/>
					<c:UserName i:nil="true"/>
				</b:LastUpdatedBy>
				<b:ProjectDescription i:nil="true"/>
				<b:TaskDescription i:nil="true"/>
				<b:TaskNameId i:nil="true"/>
				<b:OnCallServiceTime>0</b:OnCallServiceTime>
				<b:LogoffOrigin i:nil="true"/>
				<b:LogonOrigin i:nil="true"/>
			</timeEntry>
		</ValidateAndSaveTimeEntry>
	</s:Body>
</s:Envelope>"""



response = requests.post(url,data=body,headers=headers)
print(response.content)
