//Consumo API SECURITY con su ambiente respectivo Deposit-account:read:user
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
        //El valor en grant_type es client_credentials no refresh_token para obtener el token de la API SECURITY
        grant_type: 'client_credentials',
        scope: 'Deposit-account:read:user',
        refresh_token: 'df0500b26bdc6a0b0e1a563533bdece21e09e6444041a5de8dd1904f8dc7dedb'
    }
};

request(options, function(error, response, body) {
    if (error) return console.error('Failed: %s', error.message);
    //Obteniendo el token del arreglo de datos que retorna la variable body
    var tokenbodySecurity_Deposit = "";
    tokenbodySecurity_Deposit = body;
    array_tokenBody_security_Deposit = tokenbodySecurity_Deposit.split(",");
    array_access_token_Deposit = array_tokenBody_security_Deposit[1].split(":");
    token_security_Deposit = array_access_token_Deposit[1].replace('"', '');
    token_securityFinally_Deposit = token_security_Deposit.replace('"', '');

    //console.log(token_security);
    //console.log("respuesta consumo API Security: " + "\n", token_securityFinally_Deposit);

    // Consumo API ATTACHMENT IDENTITY ACCOUNT ambiente Deposit-account:read:user
    var request = require("request");

    var options = {
        method: 'POST',
        url: 'https://sbapi.bancolombia.com/v1/operations/product-specific/accounts-partners/attachment-accounts',
        headers: {
            accept: 'application/vnd.bancolombia.v1+json',
            'content-type': 'application/vnd.bancolombia.v1+json',
            //FALTABA AUTHORIZATION!
            'authorization': "Bearer " + token_securityFinally_Deposit

        },
        body: '{"data":[{"customerDocumentType":"CC","customerDocumentNumber":"15290489"}]}'
    };

    request(options, function(error, response, body) {
        if (error) return console.error('Failed: %s', error.message);
        var data_attachment_identity_account = "";
        data_attachment_identity_account = body;

        //console.log("respuesta consumo API ATTACHMENT IDENTITY ACCOUNT: " + "\n", data_attachment_identity_account);


        //Consumo API SECURITY con su ambiente respectivo Attachment:write:app
        var request = require("request");

        var options = {
            method: 'POST',
            url: 'https://sbapi.bancolombia.com/v1/security/oauth-otp-pymes/oauth2/token',
            headers: {
                accept: 'application/json',
                'content-type': 'application/x-www-form-urlencoded',
                authorization: 'Basic ZjI5ODllNmYtNWQzZC00NjAzLWFjODAtNjNlYTk3NWM2OGQ1Oko4bFc3dkQzaEk3d0kybEcyYU8zd1gwdUU2dVgybUo2aVQzc0M1d0MwYlcwY1g0YkMx'
            },
            form:
            //El valor en grant_type es client_credentials no refresh_token para obtener el token de la API SECURITY
            {
                grant_type: 'client_credentials',
                scope: 'Attachment:write:app',
                refresh_token: 'df0500b26bdc6a0b0e1a563533bdece21e09e6444041a5de8dd1904f8dc7dedb'
            }
        };

        request(options, function(error, response, body) {
            if (error) return console.error('Failed: %s', error.message);
            //Obteniendo el token del arreglo de datos que retorna la variable body
            var tokenbodySecurity_Attachment = "";
            tokenbodySecurity_Attachment = body;
            array_tokenBody_security_Attachment = tokenbodySecurity_Attachment.split(",");
            array_access_token_Attachment = array_tokenBody_security_Attachment[1].split(":");
            token_security_Attachment = array_access_token_Attachment[1].replace('"', '');
            token_securityFinally_Attachment = token_security_Attachment.replace('"', '');

            //console.log("respuesta consumo API Security con ambiente Attachment:write:app : " + "\n", token_securityFinally_Attachment);

            //Consumo API ATTACHMENT REGISTER REQUEST con ambiente Attachment:write:app

            var request = require("request");

            var options = {
                method: 'POST',
                url: 'https://sbapi.bancolombia.com/v1/operations/specific-product/consumer-services/attachment-registry/registry',
                headers: {
                    accept: 'application/vnd.bancolombia.v1+json',
                    'content-type': 'application/vnd.bancolombia.v1+json',
                    //FALTABA AUTHORIZATION!
                    'authorization': "Bearer " + token_securityFinally_Attachment
                },
                body: '{"data":[{"requestAttachableId":"123498765000000","requestAmount":15000000.98,"requestTypeAction":"PAGAR","requestPercentage":"15.00","bankId":"02","accountNumber":"01530251620","accountType":"CUENTA DE AHORRO","requestExceptionUnattachable":"FALSE","requestAttachmentLimit":"ORDINARIO","subsidiary":[{"subsidiaryNit":"900123456-1","subsidiaryName":"BANCOLOMBIA PANAMA"}],"demandant":[{"customerDocumentType":"CC","customerDocumentNumber":"15360300","customerName":"Juan Roberto Franco"}],"defendant":{"customerDocumentType":"CC","customerDocumentNumber":"21811845","customerName":"Pedro Zapata Restrepo"},"judicialOffice":{"dataNumber":"100208221","dataFile":"T2ZpY2lvIGRlbCBlbWJhcmdv","dataDateOffice":"2019-09-13"},"judicialAnnexes":[{"dataNumber":null,"dataFile":null}],"seizureJudgment":{"dataNumber":null,"dataFile":null}}]}'
            };

            request(options, function(error, response, body) {
                if (error) return console.error('Failed: %s', error.message);

                var data_attachment_register_request = "";
                data_attachment_register_request = body;

                //console.log("respuesta consumo API ATTACHMENT REGISTER REQUEST: " + "\n", data_attachment_register_request);

                //Consumo API ATTACHMENT REGISTER REQUEST LIFT con ambiente Attachment:write:app

                var request = require("request");

                var options = {
                    method: 'POST',
                    url: 'https://sbapi.bancolombia.com/v1/operations/specific-product/consumer-services/attachment-lift/registry',
                    headers: {
                        accept: 'application/vnd.bancolombia.v1+json',
                        'content-type': 'application/vnd.bancolombia.v1+json',
                        //FALTABA AUTHORIZATION!
                        'authorization': "Bearer " + token_securityFinally_Attachment
                    },
                    body: '{"data":[{"requestUnattachableId":"234560987600000","requestAttachableId":"231234987650000","subsidiary":[{"subsidiaryNit":"900123456-1","subsidiaryName":"BANCOLOMBIA PANAMA"}],"demandant":[{"customerDocumentType":"CC","customerDocumentNumber":"15360300"}],"defendant":{"customerDocumentType":"CC","customerDocumentNumber":"21811845"},"judicialOffice":{"dataNumber":"100208221","dataFile":"T2ZpY2lvIGRlbCBkZXNlbWJhcmdv","dataDateOffice":"2019-09-13"},"judicialAnnexes":[{"dataNumber":null,"dataFile":null}]}]}'
                };

                request(options, function(error, response, body) {
                    if (error) return console.error('Failed: %s', error.message);
                    var data_attachment_register_lift = "";
                    data_attachment_register_lift = body;

                    //console.log("respuesta consumo API ATTACHMENT REQUEST LIFT: " + "\n", data_attachment_register_lift);

                    //Consumo API SECURITY con su ambiente respectivo Attachment:read:app para la API Validate Request Status 1.0.0 y  Validate Request Details 1.0.0
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
                            //El valor en grant_type es client_credentials no refresh_token para obtener el token de la API SECURITY,
                            grant_type: 'client_credentials',
                            scope: 'Attachment:read:app',
                            refresh_token: 'df0500b26bdc6a0b0e1a563533bdece21e09e6444041a5de8dd1904f8dc7dedb'
                        }
                    };

                    request(options, function(error, response, body) {
                        if (error) return console.error('Failed: %s', error.message);
                        //Obteniendo el token del arreglo de datos que retorna la variable body
                        var tokenbodySecurity_Validate = "";
                        tokenbodySecurity_Validate = body;
                        array_tokenBody_security_Validate = tokenbodySecurity_Validate.split(",");
                        array_access_token_Validate = array_tokenBody_security_Validate[1].split(":");
                        token_security_Validate = array_access_token_Validate[1].replace('"', '');
                        token_securityFinally_Validate = token_security_Validate.replace('"', '');

                        //console.log("respuesta consumo API Security con ambiente Attachment:read:app : " + "\n", token_securityFinally_Validate);

                        //Consumo de API Validate Request Status 1.0.0 y ambiente Attachment:read:app
                        var request = require("request");

                        var options = {
                            method: 'GET',
                            url: 'https://sbapi.bancolombia.com/v1/operations/specific-product/consumer-services/attachment-validate/validate',
                            qs: { attachmentId: '123456789' },
                            headers: {
                                accept: 'application/vnd.bancolombia.v1+json',
                                //FALTABA AUTHORIZATION!
                                'authorization': "Bearer " + token_securityFinally_Validate
                            }
                        };

                        request(options, function(error, response, body) {
                            if (error) return console.error('Failed: %s', error.message);
                            var data_attachment_validate_requestStatus = "";
                            data_attachment_validate_requestStatus = body;

                            //console.log("respuesta consumo API Validate Request Status 1.0.0: " + "\n", data_attachment_validate_requestStatus);

                            //Consumo de API  Validate Request Details  1.0.0 y ambiente Attachment:read:app
                            var request = require("request");

                            var options = {
                                method: 'GET',
                                url: 'https://sbapi.bancolombia.com/v1/operations/specific-product/consumer-services/attachment-validate-details/validate',
                                qs: { attachmentId: '123456789' },
                                headers: {
                                    accept: 'application/vnd.bancolombia.v1+json',
                                    //FALTABA AUTHORIZATION!
                                    'authorization': "Bearer " + token_securityFinally_Validate
                                }
                            };

                            request(options, function(error, response, body) {
                                if (error) return console.error('Failed: %s', error.message);
                                var data_attachment_validate_requestDetails = "";
                                data_attachment_validate_requestDetails = body;

                                console.log("respuesta consumo API Validate Request Details  1.0.0: " + "\n", data_attachment_validate_requestDetails);

                            });



                        });





                    });




                });





            });






        });






    });






});