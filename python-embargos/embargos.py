
#Consumo API SECURITY con su ambiente respectivo Deposit-account:read:user
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "grant_type=client_credentials&scope=Deposit-account:read:user"

headers = {
    'authorization': "Basic ZjI5ODllNmYtNWQzZC00NjAzLWFjODAtNjNlYTk3NWM2OGQ1Oko4bFc3dkQzaEk3d0kybEcyYU8zd1gwdUU2dVgybUo2aVQzc0M1d0MwYlcwY1g0YkMx",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json"
    }

conn.request("POST", "/v1/security/oauth-otp-pymes/oauth2/token", payload, headers)

res = conn.getresponse()
#Convierto la variable data_Security_bytes en String ya que estaba en Bytes.
data_Security_bytes = res.read()
data_Security_cadena=data_Security_bytes.decode()
#Luego, obtengo el token de acceso del array de datos que contiene la variable array_data_security
array_data_security=data_Security_cadena.split(",")
array_accessTokenSecurity=array_data_security[1].split(":")
token_security_Deposit=array_accessTokenSecurity[1].replace('"','')

#print("respuesta consumo API Security: "+"\n"+token_security_Deposit)


#Consumo API ATTACHMENT IDENTITY ACCOUNT ambiente Deposit-account:read:user
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"customerDocumentType\":\"CC\",\"customerDocumentNumber\":\"15290489\"}]}"

headers = {
    'content-type': "application/vnd.bancolombia.v1+json",
    #FALTABA AUTHORIZATION!!
    'authorization':"Bearer "+token_security_Deposit,
    'accept': "application/vnd.bancolombia.v1+json"
    }

conn.request("POST", "/v1/operations/product-specific/accounts-partners/attachment-accounts", payload, headers)

res = conn.getresponse()
data_attachment_identity_account = res.read()


#print("respuesta consumo API ATTACHMENT IDENTITY ACCOUNT: "+"\n"+data_attachment_identity_account.decode("utf-8"))

#Consumo API SECURITY con su ambiente respectivo Attachment:write:app
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "grant_type=client_credentials&scope=Attachment:write:app"

headers = {
    'authorization': "Basic ZjI5ODllNmYtNWQzZC00NjAzLWFjODAtNjNlYTk3NWM2OGQ1Oko4bFc3dkQzaEk3d0kybEcyYU8zd1gwdUU2dVgybUo2aVQzc0M1d0MwYlcwY1g0YkMx",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json"
    }

conn.request("POST", "/v1/security/oauth-otp-pymes/oauth2/token", payload, headers)

res = conn.getresponse()
#Convierto la variable data_Security_bytes en String ya que estaba en Bytes.
data_Security_bytes_Attachment = res.read()
data_Security_cadena_Attachment=data_Security_bytes_Attachment.decode()
#Luego, obtengo el token de acceso del array de datos que contiene la variable array_data_security
array_data_security_Attachment=data_Security_cadena_Attachment.split(",")
array_accessTokenSecurity_Attachment=array_data_security_Attachment[1].split(":")
token_security_Attachment=array_accessTokenSecurity_Attachment[1].replace('"','')

#print("respuesta consumo API Security con ambiente Attachment:write:app: "+"\n"+token_security_Attachment)

#Consumo API ATTACHMENT REGISTER REQUEST con ambiente Attachment:write:app

import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"requestAttachableId\":\"123498765000000\",\"requestAmount\":15000000.98,\"requestTypeAction\":\"PAGAR\",\"requestPercentage\":\"15.00\",\"bankId\":\"02\",\"accountNumber\":\"01530251620\",\"accountType\":\"CUENTA DE AHORRO\",\"requestExceptionUnattachable\":\"FALSE\",\"requestAttachmentLimit\":\"ORDINARIO\",\"subsidiary\":[{\"subsidiaryNit\":\"900123456-1\",\"subsidiaryName\":\"BANCOLOMBIA PANAMA\"}],\"demandant\":[{\"customerDocumentType\":\"CC\",\"customerDocumentNumber\":\"15360300\",\"customerName\":\"Juan Roberto Franco\"}],\"defendant\":{\"customerDocumentType\":\"CC\",\"customerDocumentNumber\":\"21811845\",\"customerName\":\"Pedro Zapata Restrepo\"},\"judicialOffice\":{\"dataNumber\":\"100208221\",\"dataFile\":\"T2ZpY2lvIGRlbCBlbWJhcmdv\",\"dataDateOffice\":\"2019-09-13\"},\"judicialAnnexes\":[{\"dataNumber\":null,\"dataFile\":null}],\"seizureJudgment\":{\"dataNumber\":null,\"dataFile\":null}}]}"

headers = {
    'content-type': "application/vnd.bancolombia.v1+json",
    #FALTABA AUTHORIZATION!!
    'authorization':"Bearer "+token_security_Attachment,
    'accept': "application/vnd.bancolombia.v1+json"
    }

conn.request("POST", "/v1/operations/specific-product/consumer-services/attachment-registry/registry", payload, headers)

res = conn.getresponse()
data_attachment_register_request = res.read()

#print("respuesta consumo API ATTACHMENT REGISTER REQUEST: "+"\n"+data_attachment_register_request.decode("utf-8"))

#Consumo API ATTACHMENT REGISTER REQUEST LIFT con ambiente Attachment:write:app
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"requestUnattachableId\":\"234560987600000\",\"requestAttachableId\":\"231234987650000\",\"subsidiary\":[{\"subsidiaryNit\":\"900123456-1\",\"subsidiaryName\":\"BANCOLOMBIA PANAMA\"}],\"demandant\":[{\"customerDocumentType\":\"CC\",\"customerDocumentNumber\":\"15360300\"}],\"defendant\":{\"customerDocumentType\":\"CC\",\"customerDocumentNumber\":\"21811845\"},\"judicialOffice\":{\"dataNumber\":\"100208221\",\"dataFile\":\"T2ZpY2lvIGRlbCBkZXNlbWJhcmdv\",\"dataDateOffice\":\"2019-09-13\"},\"judicialAnnexes\":[{\"dataNumber\":null,\"dataFile\":null}]}]}"

headers = {
    'content-type': "application/vnd.bancolombia.v1+json",
    #FALTABA AUTHORIZATION!!
    'authorization':"Bearer "+token_security_Attachment,
    'accept': "application/vnd.bancolombia.v1+json"
    }

conn.request("POST", "/v1/operations/specific-product/consumer-services/attachment-lift/registry", payload, headers)

res = conn.getresponse()
data_attachment_register_lift = res.read()

#print("respuesta consumo API ATTACHMENT REQUEST LIFT: "+"\n"+data_attachment_register_lift.decode("utf-8"))

#Consumo API SECURITY con su ambiente respectivo Attachment:read:app para la API Validate Request Status 1.0.0 y  Validate Request Details 1.0.0
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "grant_type=client_credentials&scope=Attachment:read:app"

headers = {
    'authorization': "Basic ZjI5ODllNmYtNWQzZC00NjAzLWFjODAtNjNlYTk3NWM2OGQ1Oko4bFc3dkQzaEk3d0kybEcyYU8zd1gwdUU2dVgybUo2aVQzc0M1d0MwYlcwY1g0YkMx",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json"
    }

conn.request("POST", "/v1/security/oauth-otp-pymes/oauth2/token", payload, headers)

res = conn.getresponse()
#Convierto la variable data_Security_bytes en String ya que estaba en Bytes.
data_Security_bytes_Validate = res.read()
data_Security_cadena_Validate=data_Security_bytes_Validate.decode()
#Luego, obtengo el token de acceso del array de datos que contiene la variable array_data_security
array_data_security_Validate=data_Security_cadena_Validate.split(",")
array_accessTokenSecurity_Validate=array_data_security_Validate[1].split(":")
token_security_Validate=array_accessTokenSecurity_Validate[1].replace('"','')
#print("respuesta consumo API Security con ambiente Attachment:read:app: "+"\n"+token_security_Validate)

#Consumo de API Validate Request Status 1.0.0 y ambiente Attachment:read:app

import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

headers = { 'accept': "application/vnd.bancolombia.v1+json",
 #FALTABA AUTHORIZATION!!
    'authorization':"Bearer "+token_security_Validate }

conn.request("GET", "/v1/operations/specific-product/consumer-services/attachment-validate/validate?attachmentId=123456789", headers=headers)

res = conn.getresponse()
data_attachment_validate_requestStatus = res.read()

#print("respuesta consumo API Validate Request Status 1.0.0: "+"\n"+data_attachment_validate_requestStatus.decode("utf-8"))

#Consumo de API  Validate Request Details  1.0.0 y ambiente Attachment:read:app
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

headers = { 'accept': "application/vnd.bancolombia.v1+json",
 #FALTABA AUTHORIZATION!!
    'authorization':"Bearer "+token_security_Validate }

conn.request("GET", "/v1/operations/specific-product/consumer-services/attachment-validate-details/validate?attachmentId=123456789", headers=headers)

res = conn.getresponse()
data_attachment_validate_requestDetails = res.read()

#print("respuesta consumo API Validate Request Details  1.0.0: "+"\n"+data_attachment_validate_requestDetails.decode("utf-8"))
