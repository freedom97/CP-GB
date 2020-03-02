#SECURITY
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "grant_type=client_credentials&scope=Customer:write:app"

headers = {
    'authorization': "Basic ZjI5ODllNmYtNWQzZC00NjAzLWFjODAtNjNlYTk3NWM2OGQ1Oko4bFc3dkQzaEk3d0kybEcyYU8zd1gwdUU2dVgybUo2aVQzc0M1d0MwYlcwY1g0YkMx",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json"
    }

conn.request("POST", "/v1/security/oauth-otp-pymes/oauth2/token", payload, headers)

res = conn.getresponse()
data = res.read()
data_cadena=data.decode()
array_data=data_cadena.split(",")
array_accessTokenSecurity=array_data[1].split(":")
token_security=array_accessTokenSecurity[1].replace('"','')

# print(token_security)

#ENROLL
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"partner\":{\"partnerId\":\"7943543033167872\"},\"user\":{\"documentType\":\"CC\",\"documentNumber\":12345678,\"documentExpeditionDate\":\"2018-08-23\",\"firstName\":\"Alejadro\",\"secondName\":\"Mario\",\"surname\":\"Aguirre\",\"secondSurname\":\"Torres\",\"cellPhone\":3134136767,\"email\":\"abc@email.com\"}}]}"

headers = {
    'authorization': "Bearer"+" "+token_security,
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/v1/reference-data/party/party-data-management/enrollment-users-management/users/actions/start-enrollment", payload, headers)

res = conn.getresponse()
data2 = res.read()

#print(data2.decode("utf-8"))

#CREDITO VEHICULO
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"customer_documentType\":\"CEDULA_CIUDADANIA\",\"customer_documentNumber\":1056789548,\"customer_firstName\":\"CARLOS\",\"customer_secondName\":\"ANTONIO\",\"customer_surname\":\"PEREZ\",\"customer_secondSurname\":\"CANO\",\"customer_cellPhone\":\"3153584687\",\"customer_email\":\"caperez@gmail.com\",\"customer_habeasData\":true}]}"

headers = {
    'authorization': "Bearer"+" "+token_security,
    'userauthorization': "456526",
    'username': "PI12345",
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications", payload, headers)

res = conn.getresponse()
data3 = res.read()

print(data3.decode())