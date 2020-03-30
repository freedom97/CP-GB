#Consumo de API SECURITY co ambiente 

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
#Convierto la variable data_Security_bytes en String ya que estaba en Bytes.
data_Security_bytes = res.read()
data_Security_cadena=data_Security_bytes.decode()
#Luego, obtengo el token de acceso del array de datos que contiene la variable array_data_security
array_data_security=data_Security_cadena.split(",")
array_accessTokenSecurity=array_data_security[1].split(":")
token_security=array_accessTokenSecurity[1].replace('"','')

# print("respuesta consumo API Security: "+"\n"+token_security)

#Consumo de API ENROLLMENT
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"partner\":{\"partnerId\":\"7943543033167872\"},\"user\":{\"documentType\":\"CC\",\"documentNumber\":12345678,\"documentExpeditionDate\":\"2018-08-23\",\"firstName\":\"Alejadro\",\"secondName\":\"Mario\",\"surname\":\"Aguirre\",\"secondSurname\":\"Torres\",\"cellPhone\":3134136767,\"email\":\"abc@email.com\"}}]}"

headers = {
    'authorization': "Bearer "+token_security,
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/v1/reference-data/party/party-data-management/enrollment-users-management/users/actions/start-enrollment", payload, headers)

res = conn.getresponse()
#Recibo un conjunto de datos tipo bytes por parte de la API ENROLLMENT, se debe obtener solo el dato de enrollmen_Id_Token y convertir en tipo String
body_enrollment_bytes = res.read()
body_enrollment_cadena=body_enrollment_bytes.decode()
array_body_enrollment=body_enrollment_cadena.split(",")
array_enrollmentIdToken=array_body_enrollment[7].split(":")
data_enrollment=array_enrollmentIdToken[1].replace("}","").replace("]","")
#data_enrollmet
#print("respuesta consumo API Enrollment: "+"\n"+str(data_enrollment))

#Consumo de API CREDITO VEHICULO PRELIMINAR POST No.1
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"customer_documentType\":\"CEDULA_CIUDADANIA\",\"customer_documentNumber\":1056789548,\"customer_firstName\":\"CARLOS\",\"customer_secondName\":\"ANTONIO\",\"customer_surname\":\"PEREZ\",\"customer_secondSurname\":\"CANO\",\"customer_cellPhone\":\"3153584687\",\"customer_email\":\"caperez@gmail.com\",\"customer_habeasData\":true}]}"

headers = {
    'authorization': "Bearer"+" "+token_security,
    'userauthorization':data_enrollment,
    'username': "PI12345",
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications", payload, headers)

res = conn.getresponse()
creditoVehiculo_preliminar_post1 = res.read()

#print("respuesta credito vehiculo preliminar post1: "+"\n"+creditoVehiculo_preliminar_post1.decode())


#En la respuesta de la operación POST No.1 de la API CREDITO VEHICULO PRELIMINAR
#esta contenida la variable application_id, así que se procede a extraer el valor de
#esa variable, la cual se utilizara en las demás APIs de Credito Vehiculo.

array_creditoVehiculo_preliminar_post1=creditoVehiculo_preliminar_post1.decode().split(",")
array_data_creditoVehiculo_preliminar_post1=array_creditoVehiculo_preliminar_post1[5].split(":")
application_id=array_data_creditoVehiculo_preliminar_post1[2]
#print("application_id: "+application_id)

#Consumo de API CREDITO VEHICULO PRELIMINAR POST No.2
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"product_category\":\"CREDITO_VEHICULO_NUEVO\",\"product_subCategory\":\"AUTOMOVIL\",\"vehicle_model\":2019,\"vehicle_mark\":\"NISSAN\",\"vehicle_line\":\"Nissan Latio\",\"vehicle_cost\":35000000,\"vehicle_initialAmount\":10000000,\"vehicle_installmentAmountOther\":900000}]}"

headers = {
    'authorization': "Bearer "+token_security,
    'userauthorization':data_enrollment,
    'username': "PI12345",
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications/"+application_id+"/actions/add-vehicle-information", payload, headers)

res = conn.getresponse()
creditoVehiculo_preliminar_post2 = res.read()

#print("respuesta credito vehiculo preliminar post2: "+"\n"+creditoVehiculo_preliminar_post2.decode("utf-8"))


#Consumo de API CREDITO VEHICULO PRELIMINAR POST No.3
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"commerce_headquarters\":\"E-COMMERCE_VIRTUAL\",\"commerce_idVendor\":1099204407,\"commerce_isFeria\":false,\"commerce_nameTradeShow\":\"Feria del automovil 2018\"}]}"

headers = {
    'authorization': "Bearer "+token_security,
    'userauthorization': data_enrollment,
    'username': "PI12345",
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications/"+application_id+"/actions/add-commerce-information", payload, headers)

res = conn.getresponse()
creditoVehiculo_preliminar_post3 = res.read()

#print("respuesta credito vehiculo preliminar post3: "+"\n"+creditoVehiculo_preliminar_post3.decode("utf-8"))


#Consumo de API CREDITO VEHICULO PRELIMINAR POST No.4
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"economicActivity_occupation\":\"EMPLEADO_PUBLICO\",\"economicActivity_rut\":false,\"economicActivity_establishment\":false,\"economicActivity_profession\":\"CONTADOR\",\"economicActivity_ciiuCode\":\"1001\",\"customer_countryCode\":\"CO\"}]}"

headers = {
    'authorization': "Bearer "+token_security,
    'userauthorization': data_enrollment,
    'username': "PI12345",
    'content-type': "application/json",
    'accept': "application/json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications/"+application_id+"/add-customer-economic-activity", payload, headers)

res = conn.getresponse()
creditoVehiculo_preliminar_post4 = res.read()

#print("respuesta credito vehiculo preliminar post4: "+"\n"+creditoVehiculo_preliminar_post4.decode("utf-8"))

#Consumo de API CREDITO VEHICULO ESTUDIO FINAL POST No.1

import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"customer_departmentCode\":\"05\",\"customer_cityCode\":\"01\",\"customer_birthdate\":\"1983-05-12\",\"customer_civilStatus\":\"DIVORCIADO\",\"customer_gender\":\"M\",\"customer_levelStudy\":\"TECNOLOGICO\",\"customer_housingType\":\"ARRENDADA\",\"customer_housingTime\":\"MAS_DE_2_ANIOS\",\"customer_housignLeaseValue\":650000}]}"

headers = {
    'authorization': "Bearer "+token_security,
    'userauthorization': data_enrollment,
    'username': "PI12345",
    'content-type': "application/vnd.bancolombia.v1+json",
    'accept': "application/vnd.bancolombia.v1+json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications/"+application_id+"/actions/add-aditional-customer-data", payload, headers)

res = conn.getresponse()
creditoVehiculo_estudioFinal_post1 = res.read()

#print("respuesta credito vehiculo estudio final post1: "+"\n"+creditoVehiculo_estudioFinal_post1.decode("utf-8"))

#Consumo de API CREDITO VEHICULO ESTUDIO FINAL POST No.2
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"economicActivity_contractType\":\"INDEFINIDO\",\"economicActivity_time\":\"48_MESES_84_MESES\",\"economicActivity_numberVehicles\":1,\"vehicle_data\":[{\"vehicle_licensePlate\":\"Mazda\",\"vehicle_model\":2019}]}]}"

headers = {
    'authorization': "Bearer "+token_security,
    'userauthorization': data_enrollment,
    'username': "PI12345",
    'content-type': "application/vnd.bancolombia.v1+json",
    'accept': "application/vnd.bancolombia.v1+json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications/"+application_id+"/actions/add-aditional-economic-data", payload, headers)

res = conn.getresponse()
creditoVehiculo_estudioFinal_post2 = res.read()

#print("respuesta credito vehiculo estudio final post2: "+"\n"+creditoVehiculo_estudioFinal_post2.decode("utf-8"))

#Consumo de API CREDITO VEHICULO ESTUDIO FINAL POST No.3
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"financialData_monthlyFixedIncome\":5000000,\"financialData_otherMonthlyIncome\":800000,\"financialData_monthlyExpenses\":5500000,\"linkageFeasibility\":true}]}"

headers = {
    'authorization': "Bearer "+token_security,
    'userauthorization': data_enrollment,
    'username': "PI12345",
    'content-type': "application/vnd.bancolombia.v1+json",
    'accept': "application/vnd.bancolombia.v1+json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications/"+application_id+"/actions/add-aditional-financial-data", payload, headers)

res = conn.getresponse()
creditoVehiculo_estudioFinal_post3 = res.read()

#print("respuesta credito vehiculo estudio final post3: "+"\n"+creditoVehiculo_estudioFinal_post3.decode("utf-8"))

#Consumo de API CREDITO VEHICULO ESTUDIO MANUAL POST No.1

import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"customer_address\":\"CALLE 50 #51-76\",\"customer_phone\":5107770,\"customer_documentExpeditionDate\":\"1991-05-17\",\"customer_retirementManager\":\"COLPENSIONES\"}]}"

headers = {
    'authorization': "Bearer "+token_security,
    'userauthorization': data_enrollment,
    'username': "PI12345",
    'content-type': "application/vnd.bancolombia.v1+json",
    'accept': "application/vnd.bancolombia.v1+json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications/"+application_id+"/actions/supplementary-customer-data", payload, headers)

res = conn.getresponse()
creditoVehiculo_estudioManual_post1 = res.read()

#print("respuesta credito vehiculo estudio manual post1: "+"\n"+creditoVehiculo_estudioManual_post1.decode("utf-8"))

#Consumo de API CREDITO VEHICULO ESTUDIO MANUAL POST No.2
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"company_name\":\"PROMOVER SA\",\"company_position\":\"ANALISTA\",\"company_address\":\"Carrera 50 #35-77\",\"company_phone\":\"7705531\",\"company_departament\":\"05\"}]}"

headers = {
    'authorization': "Bearer "+token_security,
    'userauthorization': data_enrollment,
    'username': "PI12345",
    'content-type': "application/vnd.bancolombia.v1+json",
    'accept': "application/vnd.bancolombia.v1+json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications/"+application_id+"/actions/add-basic-company-data", payload, headers)

res = conn.getresponse()
creditoVehiculo_estudioManual_post2 = res.read()

#print("respuesta credito vehiculo estudio manual post2: "+"\n"+creditoVehiculo_estudioManual_post2.decode("utf-8"))

#Consumo de API CREDITO VEHICULO ESTUDIO MANUAL POST No.3
import http.client

conn = http.client.HTTPSConnection("sbapi.bancolombia.com")

payload = "{\"data\":[{\"commercialReference_data\":[{\"commercialReference_nit\":830543324,\"commercialReference_name\":\"Alkomprar\",\"commercialReference_phone\":5715526,\"commercialReference_city\":\"Medellín\"}]}]}"

headers = {
    'authorization': "Bearer "+token_security,
    'userauthorization': data_enrollment,
    'username': "PI12345",
    'content-type': "application/vnd.bancolombia.v1+json",
    'accept': "application/vnd.bancolombia.v1+json"
    }

conn.request("POST", "/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications/"+application_id+"/actions/add-commercial-reference-data", payload, headers)

res = conn.getresponse()
creditoVehiculo_estudioManual_post3 = res.read()


print("respuesta credito vehículo estudio manual post3: "+creditoVehiculo_estudioManual_post3.decode())