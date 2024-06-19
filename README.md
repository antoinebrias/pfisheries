# pfisheries

This project is a conversion of the original R project rfisheries by Karthik Ram, Carl Boettiger and Andrew Dyck. The original project can be found here: https://github.com/ropensci/rfisheries. 

This package provides programmatic access to the Open Fisheries API. Open Fisheries is a platform that aggregates global fishery data and currently offers global fish capture landings from 1950 onwards. Read more about that effort [here](https://www.openfisheries.org).

The three same basic functions are implemented. Landings data can be obtained by calling *of_landings()* with a iso3c country code or a a3 species code as argument.
If you don't know the correct species or country codes, you can get a complete list with the following two functions: *of_country_codes()* and *of_species_codes()*

If you have any questions or feedback, feel free to reach out.
