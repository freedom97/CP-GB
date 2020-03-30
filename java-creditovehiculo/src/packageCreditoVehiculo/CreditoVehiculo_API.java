package packageCreditoVehiculo;

import java.awt.PageAttributes.MediaType;

import javax.xml.ws.Response;

public class CreditoVehiculo_API {
	OkHttpClient client = new OkHttpClient();

	MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
	RequestBody body = RequestBody.create(mediaType, "grant_type=client_credentials&scope=vebveb&refresh_token=8be14f25ddef55cc3e4470fb943e0ed162e8e38dd7b7c53246f7ba10c54a97b5");
	Request request = new Request.Builder()
	  .url("https://sbapi.bancolombia.com/v1/security/oauth-otp-pymes/oauth2/token")
	  .post(body)
	  .addHeader("authorization", "REPLACE_THIS_VALUE")
	  .addHeader("content-type", "application/x-www-form-urlencoded")
	  .addHeader("accept", "application/json")
	  .build();

	Response response = client.newCall(request).execute();

}
