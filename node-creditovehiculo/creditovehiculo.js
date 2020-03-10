// SECURITY

// Install request by running "npm install --save request"
var request = require("request");

var options = {
    method: 'POST',
    url: 'https://sbapi.bancolombia.com/v1/security/oauth-otp-pymes/oauth2/token',
    headers: {
        accept: 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        authorization: 'Basic ZjI5ODllNmYtNWQzZC00NjAzLWFjODAtNjNlYTk3NWM2OGQ1Oko4bFc3dkQzaEk3d0kybEcyYU8zd1gwdUU2dVgybUo2aVQzc0M1d0MwYlcwY1g0YkMx'
    },
    form: {
        grant_type: 'client_credentials',
        scope: 'Customer:write:app',
        refresh_token: '56e8865fcbd30a63598fa0c8d3fd3465a105dbcb96c62faa95488d58de19e01b'
    }
};

request(options,

    function(error, response, body) {
        if (error) return console.error('Failed: %s', error.message);
        //Obteniendo el token del arreglo de datos que retorna la variable body
        var tokenbodySecurity = "";
        tokenbodySecurity = body;
        array_tokenBody_security = tokenbodySecurity.split(",");
        array_access_token = array_tokenBody_security[1].split(":");
        token_security = array_access_token[1].replace('"', '');
        token_security2 = token_security.replace('"', '');

        //console.log(token_security);
        //console.log('Success: ', body);

        //ENROLLMENT
        var request = require("request");

        var options = {
            method: 'POST',
            url: 'https://sbapi.bancolombia.com/v1/reference-data/party/party-data-management/enrollment-users-management/users/actions/start-enrollment',
            headers: {
                accept: 'application/json',
                'content-type': 'application/json',
                authorization: 'Bearer' + ' ' + token_security2
            },
            body: {
                data: [{
                    partner: { partnerId: '979028636860416' },
                    user: {
                        documentType: 'CC',
                        documentNumber: 12345678,
                        documentExpeditionDate: '2018-08-23',
                        firstName: 'Alejadro',
                        secondName: 'Mario',
                        surname: 'Aguirre',
                        secondSurname: 'Torres',
                        cellPhone: 3134136767,
                        email: 'abc@email.com'
                    }
                }]
            },
            json: true
        };

        request(options, function(error, response, body) {
            if (error) return console.error('Failed: %s', error.message);
            var token_enrollment_body = "";
            token_enrollment_body = body;

            //console.log('Token enrollment: ', token_enrollment_body)
            //console.log('Success: ', body);
            //ERROR: 401 HTTP:Unauthorized  MOREINFO: application is not registered, or active

            //CREDITO VEHICULO

            var request = require("request");

            var options = {
                method: 'POST',
                url: 'https://sbapi.bancolombia.com/v1/operations/product-specific/loans/consumer-loan/vehicle-credit-applications',
                headers: {
                    accept: 'application/json',
                    'content-type': 'application/json',
                    username: 'PI12345',
                    userauthorization: '456526',
                    authorization: 'Bearer' + ' ' + token_security2
                },
                body: {
                    data: [{
                        customer_documentType: 'CEDULA_CIUDADANIA',
                        customer_documentNumber: 1056789548,
                        customer_firstName: 'CARLOS',
                        customer_secondName: 'ANTONIO',
                        customer_surname: 'PEREZ',
                        customer_secondSurname: 'CANO',
                        customer_cellPhone: '3153584687',
                        customer_email: 'caperez@gmail.com',
                        customer_habeasData: true
                    }]
                },
                json: true
            };

            request(options, function(error, response, body) {
                if (error) return console.error('Failed: %s', error.message);

                console.log('Success: ', body);
            });


        });




    });