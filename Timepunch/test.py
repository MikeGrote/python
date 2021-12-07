#Anayse
#python -m zeep http://timepunch.incept4.local/timepunch/Api/TpTimeEntries.svc?WSDL
#TimeEntrySearchDto(Page: xsd:int, PageSize: xsd:int, UsePaging: xsd:boolean, Confidentiality: ns10:Confidentiality, Created: xsd:dateTime, CreatedBy: ns4:guid, FilteredProjects: ns3:ArrayOfguid, FilteredTasks: ns3:ArrayOfguid, FilteredUsers: ns3:ArrayOfguid, Id: ns4:guid, IsNew: xsd:boolean, LastUpdate: xsd:dateTime, LastUpdateBy: ns4:guid, LogoffTime: xsd:dateTime, LogonTime: xsd:dateTime, Payment: ns8:TimeEntrySearchPayment, ReportTitle: xsd:string, ShowBreaks: xsd:boolean, ShowPublicHolidays: xsd:boolean, ShowWeekends: xsd:boolean, ShowWorkingTime: xsd:boolean, FilteredCustomers: ns3:ArrayOfguid, ShowMissingdays: xsd:boolean, ShowWeekdays: xsd:boolean, FirstModificationTime: xsd:dateTime, LastModificationTime: xsd:dateTime, IsImportant: xsd:boolean, IsOnSite: xsd:boolean, EnhanceWithAuditTrail: xsd:boolean, TimeFrame: ns8:TimeEntrySearchTimeFrame, IsNotInvoiced: xsd:boolean, MergeOvernightEntries: xsd:boolean)

import xlsxwriter
import hashlib
from zeep import Client
password_clear = "1q2w3e"
password      = hashlib.md5(password_clear.encode())
#print(password.hexdigest().upper())

client = Client('http://timepunch.incept4.local/timepunch/Api/TpTimeEntries.svc?WSDL')

factory = client.type_factory('ns2')

auth_type = client.get_type('ns2:TpAuthentication')
auth = auth_type(Origin = 'Management', Culture = 'de', Identity = 'incept4\\mike.grote', TpUser = 'incept4\mike.grote',  TpHashedPwd = password.hexdigest().upper())

search_type = client.get_type('ns7:TimeEntrySearchDto')
#print(search_type)

SearchPayment_type = client.get_type('ns8:TimeEntrySearchPayment')
#print(SearchPayment_type)
SearchPayment = SearchPayment_type(value = 'SearchAllEntries')

search = search_type(UsePaging = False,  
                    Page = '0',
                    PageSize = '0',
                    Payment = 'SearchAllEntries',
                    ShowBreaks  = False,
                    IsImportant = False,
                    ShowPublicHolidays = False,
                    ShowWeekends = False,
                    ShowWorkingTime = True,
                    ShowMissingdays = False,
                    ShowWeekdays = True,
                    LogonTime = '2021-10-01T00:00:00',
                    LogoffTime = '2021-10-31T00:00:00',
                    ReportTitle = 'Test',
                    Confidentiality = 'Undefined',
                    Created = '0001-01-01T00:00:00',
                    CreatedBy = '00000000-0000-0000-0000-000000000000',
                    TimeFrame = 'UserDefined')


#response_type = client.get_type('ns8:TimeEntrySearchPayment')

response = client.service.SearchTimeEntries(auth,search)
#print(response)

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('c:\Temp\Expenses01.xlsx')
worksheet = workbook.add_worksheet()
# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

TimeEntrys = response['SearchTimeEntriesResult']['TimeEntryDto']
for TimeEntry in TimeEntrys:
    print(TimeEntry)
    print(TimeEntry['LogonName'])
    print(TimeEntry['ProjectName'])
    print(TimeEntry['TaskName'])
    print(TimeEntry['Description'])
    print(TimeEntry['Duration'])
    print(TimeEntry['LogonTime'])
    print(TimeEntry['LogoffTime'])
    worksheet.write(row, col,     TimeEntry['LogonName'])
    worksheet.write(row, col + 1, TimeEntry['ProjectName'])
    worksheet.write(row, col + 2, TimeEntry['TaskName'])
    worksheet.write(row, col + 3, TimeEntry['Description'])
    worksheet.write(row, col + 4, TimeEntry['Duration'])
    worksheet.write(row, col + 5, TimeEntry['WorkTime'])
    worksheet.write(row, col + 6, TimeEntry['DrivingTime'])
    worksheet.write(row, col + 7, TimeEntry['Leave'])
    
    
    
    
    format_date = workbook.add_format({'num_format': 'dd/mm/yyyy'})
    format_time= workbook.add_format({'num_format': 'hh:mm'})

    worksheet.write(row, col + 8, TimeEntry['LogonTime'].date(),format_date)
    worksheet.write(row, col + 9, TimeEntry['LogonTime'].time(),format_time)
    worksheet.write(row, col + 10, TimeEntry['LogoffTime'].date(),format_date)
    worksheet.write(row, col + 11, TimeEntry['LogoffTime'].time(),format_time)
    row += 1


worksheet.set_column('A:A',30)
worksheet.set_column('I:I',12)
worksheet.set_column('K:K',12)
workbook.close()