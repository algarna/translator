<h1>Python translator</h1>
<h2>A web app made in Python using the Flask framework and Azure Cognitive Services, following Microsoft's module "Build an AI web app by using Python and Flask".</h2>
<br>
<p>The usage is simple, just enter the text you want to translate, select the target language from the dropdown select and click translate!</p>
<img width="1136" alt="Captura de Pantalla 2022-09-08 a las 11 37 43" src="https://user-images.githubusercontent.com/111655060/189090030-985516bb-5961-4d99-988f-86239bd8e5c6.png">
<p>You will see the original and the translated text in a new page</p>
<img width="1108" alt="Captura de Pantalla 2022-09-08 a las 11 38 04" src="https://user-images.githubusercontent.com/111655060/189090355-6d8d5adc-c24e-45d9-8792-62cd703a30a9.png">
<br>
<h3>Warning</h3>
<p>This app loads the required information to call the Azure API from a .env file located in the src folder. Due to security reasons, this file is not included in the repository. In case you want to try the project, you must activate a translator service in your Azure account and create the .env file with the following information: </p>
<ul>
<li>KEY= the API key from the translator service</li>
<li>ENDPOINT=https://api.cognitive.microsofttranslator.com/</li>
<li>LOCATION= the location of the resource group that contains the translator service (example: westeurope)</li>
</ul>
