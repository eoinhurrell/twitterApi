#twitterApi - a personal twitter API accessing module

twitterApi is a module I use to scrape twitter for tweets. I was unsatisfied with the python twitter modules i could find, so I wrote my own. 

It's very basic, functionality will be added as needed.


#Usage
IMPORTANT: modify the file 'localSettings.py' to include your own Oauth information.

``
> statuses = twitterApi.getSearchResults('weather')
> print statuses[0]['text']
Nice weather today isn't it?
``
