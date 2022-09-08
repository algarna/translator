<h1>Python translator</h1>
A web app made in Python using the Flask framework and Azure Cognitive Services, following Microsoft's module "Build an AI web app by using Python and Flask".
This app loads the required information to call the Azure API from a .env file located in the src folder. Due to security reasons, this file is not included in the repository. In case you want to try the project, you must activate a translator service in your Azure account and create the .env file with the following information: 
KEY= the API key from the translator service
ENDPOINT=https://api.cognitive.microsofttranslator.com/
LOCATION= the location of the resource group that contains the translator service (example: westeurope)