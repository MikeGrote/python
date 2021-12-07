Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
Traceback (most recent call last):
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connection.py", line 169, in _new_conn
    conn = connection.create_connection(
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\socket.py", line 954, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connectionpool.py", line 394, in _make_request
    conn.request(method, url, **httplib_request_kw)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connection.py", line 234, in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1279, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1325, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1274, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 1034, in _send_output
    self.send(msg)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\http\client.py", line 974, in send
    self.connect()
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connection.py", line 200, in connect
    conn = self._new_conn()
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connection.py", line 181, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x000001CF70ADB5B0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\adapters.py", line 439, in send
    resp = conn.urlopen(
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\connectionpool.py", line 755, in urlopen
    retries = retries.increment(
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\urllib3\util\retry.py", line 574, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='wsf.cdyne.com', port=80): Max retries exceeded with url: /WeatherWS/Weather.asmx?WSDL (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CF70ADB5B0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py", line 12, in <module>
    response = requests.post(url,data=body,headers=headers)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\api.py", line 117, in post
    return request('post', url, data=data, json=json, **kwargs)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\sessions.py", line 542, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\sessions.py", line 655, in send
    r = adapter.send(request, **kwargs)
  File "C:\Users\mike.grote\AppData\Local\Programs\Python\Python39\lib\site-packages\requests\adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='wsf.cdyne.com', port=80): Max retries exceeded with url: /WeatherWS/Weather.asmx?WSDL (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x000001CF70ADB5B0>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
>>> 
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b'<!DOCTYPE html>\r\n<html>\r\n    <head>\r\n        <title>The resource cannot be found.</title>\r\n        <meta name="viewport" content="width=device-width" />\r\n        <style>\r\n         body {font-family:"Verdana";font-weight:normal;font-size: .7em;color:black;} \r\n         p {font-family:"Verdana";font-weight:normal;color:black;margin-top: -5px}\r\n         b {font-family:"Verdana";font-weight:bold;color:black;margin-top: -5px}\r\n         H1 { font-family:"Verdana";font-weight:normal;font-size:18pt;color:red }\r\n         H2 { font-family:"Verdana";font-weight:normal;font-size:14pt;color:maroon }\r\n         pre {font-family:"Consolas","Lucida Console",Monospace;font-size:11pt;margin:0;padding:0.5em;line-height:14pt}\r\n         .marker {font-weight: bold; color: black;text-decoration: none;}\r\n         .version {color: gray;}\r\n         .error {margin-bottom: 10px;}\r\n         .expandable { text-decoration:underline; font-weight:bold; color:navy; cursor:pointer; }\r\n         @media screen and (max-width: 639px) {\r\n          pre { width: 440px; overflow: auto; white-space: pre-wrap; word-wrap: break-word; }\r\n         }\r\n         @media screen and (max-width: 479px) {\r\n          pre { width: 280px; }\r\n         }\r\n        </style>\r\n    </head>\r\n\r\n    <body bgcolor="white">\r\n\r\n            <span><H1>Server Error in \'/TimePunch\' Application.<hr width=100% size=1 color=silver></H1>\r\n\r\n            <h2> <i>The resource cannot be found.</i> </h2></span>\r\n\r\n            <font face="Arial, Helvetica, Geneva, SunSans-Regular, sans-serif ">\r\n\r\n            <b> Description: </b>HTTP 404. The resource you are looking for (or one of its dependencies) could have been removed, had its name changed, or is temporarily unavailable. &nbsp;Please review the following URL and make sure that it is spelled correctly.\r\n            <br><br>\r\n\r\n            <b> Requested URL: </b>/timepunch/api/projectTimes.asmx<br><br>\r\n\r\n            </font>\r\n\r\n    </body>\r\n</html>\r\n'
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b''
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b''
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b''
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b''
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b''
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b'<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://www.w3.org/2005/08/addressing/fault</a:Action><a:RelatesTo>urn:uuid:60f4a386-ced9-41ac-a7c4-f0b4a952f055</a:RelatesTo><ActivityId CorrelationId="43b0d010-23b9-4143-9888-059cd315ef0d" xmlns="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics">00000000-0000-0000-0000-000000000000</ActivityId></s:Header><s:Body><s:Fault><s:Code><s:Value>s:Sender</s:Value><s:Subcode><s:Value>a:ActionNotSupported</s:Value></s:Subcode></s:Code><s:Reason><s:Text xml:lang="en-US">The message with Action \'http://tempuri.org/ITimeEntryService/CheckTimeEntryOverlapping\' cannot be processed at the receiver, due to a ContractFilter mismatch at the EndpointDispatcher. This may be because of either a contract mismatch (mismatched Actions between sender and receiver) or a binding/security mismatch between the sender and the receiver.  Check that sender and receiver have the same contract and the same binding (including security requirements, e.g. Message, Transport, None).</s:Text></s:Reason></s:Fault></s:Body></s:Envelope>'
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b'<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://www.w3.org/2005/08/addressing/fault</a:Action><a:RelatesTo>urn:uuid:60f4a386-ced9-41ac-a7c4-f0b4a952f055</a:RelatesTo><ActivityId CorrelationId="e966fca0-42f7-4523-8d4c-c8dea67a0f62" xmlns="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics">00000000-0000-0000-0000-000000000000</ActivityId></s:Header><s:Body><s:Fault><s:Code><s:Value>s:Sender</s:Value><s:Subcode><s:Value>a:ActionNotSupported</s:Value></s:Subcode></s:Code><s:Reason><s:Text xml:lang="en-US">The message with Action \'http://tempuri.org/ITimeEntryService/CheckTimeEntryOverlapping\' cannot be processed at the receiver, due to a ContractFilter mismatch at the EndpointDispatcher. This may be because of either a contract mismatch (mismatched Actions between sender and receiver) or a binding/security mismatch between the sender and the receiver.  Check that sender and receiver have the same contract and the same binding (including security requirements, e.g. Message, Transport, None).</s:Text></s:Reason></s:Fault></s:Body></s:Envelope>'
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b''
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b''
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b'<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://www.w3.org/2005/08/addressing/fault</a:Action><a:RelatesTo>urn:uuid:60f4a386-ced9-41ac-a7c4-f0b4a952f055</a:RelatesTo><ActivityId CorrelationId="f06b8a7e-6d24-4365-9e2d-7b6d5957af3a" xmlns="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics">00000000-0000-0000-0000-000000000000</ActivityId></s:Header><s:Body><s:Fault><s:Code><s:Value>s:Sender</s:Value><s:Subcode><s:Value>a:ActionNotSupported</s:Value></s:Subcode></s:Code><s:Reason><s:Text xml:lang="en-US">The message with Action \'http://tempuri.org/ITimeEntryService/CheckTimeEntryOverlapping\' cannot be processed at the receiver, due to a ContractFilter mismatch at the EndpointDispatcher. This may be because of either a contract mismatch (mismatched Actions between sender and receiver) or a binding/security mismatch between the sender and the receiver.  Check that sender and receiver have the same contract and the same binding (including security requirements, e.g. Message, Transport, None).</s:Text></s:Reason></s:Fault></s:Body></s:Envelope>'
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b'<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://schemas.microsoft.com/net/2005/12/windowscommunicationfoundation/dispatcher/fault</a:Action><a:RelatesTo>urn:uuid:60f4a386-ced9-41ac-a7c4-f0b4a952f055</a:RelatesTo><ActivityId CorrelationId="417b0e2a-c5a1-42eb-ae22-16331086cb05" xmlns="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics">00000000-0000-0000-0000-000000000000</ActivityId></s:Header><s:Body><s:Fault><s:Code><s:Value>s:Sender</s:Value><s:Subcode><s:Value xmlns:a="http://schemas.microsoft.com/net/2005/12/windowscommunicationfoundation/dispatcher">a:DeserializationFailed</s:Value></s:Subcode></s:Code><s:Reason><s:Text xml:lang="en-US">The formatter threw an exception while trying to deserialize the message: There was an error while trying to deserialize parameter http://tempuri.org/:entryToCheckOverlapping. The InnerException message was \'There was an error deserializing the object of type TimePunch.Core.Services.TimeEntryService.Dto.TimeEntryDto. \'\xef\xbf\xbdtzung Liefprojekt\' contains invalid UTF8 bytes.\'.  Please see InnerException for more details.</s:Text></s:Reason></s:Fault></s:Body></s:Envelope>'
>>> 
= RESTART: C:/Users/mike.grote/AppData/Local/Programs/Python/Python39/timepunch.py
b'<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing"><s:Header><a:Action s:mustUnderstand="1">http://tempuri.org/ITimeEntryService/CheckTimeEntryOverlappingResponse</a:Action><a:RelatesTo>urn:uuid:60f4a386-ced9-41ac-a7c4-f0b4a952f055</a:RelatesTo><ActivityId CorrelationId="ed49c33c-9a47-44bb-9d9e-d8671b4ff70f" xmlns="http://schemas.microsoft.com/2004/09/ServiceModel/Diagnostics">00000000-0000-0000-0000-000000000000</ActivityId></s:Header><s:Body><CheckTimeEntryOverlappingResponse xmlns="http://tempuri.org/"><CheckTimeEntryOverlappingResult>false</CheckTimeEntryOverlappingResult><fault i:nil="true" xmlns:b="http://schemas.datacontract.org/2004/07/TimePunch.Core.Services.AuthenticationService.Dto" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"/></CheckTimeEntryOverlappingResponse></s:Body></s:Envelope>'
>>> 