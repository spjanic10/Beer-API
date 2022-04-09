# Beer-API

API application made with the Django REST Framework. 

The API returns a list of beer attributes based on the inputted type of beer.

The application is live at: https://spjanic10.pythonanywhere.com/beer/<beer_type>

The API can also be called from an application such as Postman for testing purposes.

The list of valid beer types are:

- ipa
- brown_ale
- pilsner
- lager
- lambic
- hefeweizen

Within the API, the Beer model contains 5 attributes:

- id
- type
- caloriesPerLiter
- color
- alcoholPercentage

The [test cases](https://github.com/spjanic10/Beer-API/tree/main/beer/tests) that are currently implement include testing for a 200 status code when the type of beer exists, testing for 404 status code when the type of beer is not found and then testing for an appropriate body response when the type of beer is found.
