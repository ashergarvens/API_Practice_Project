## Setup Requirements
1. You must have a Google API Key for Youtube and make sure it is v03 as stated in the yt documentation
	* https://developers.google.com/youtube/v3/guides/implementation
2. Install all required packages such as:
	* google api client ( on yt site specified)
	* json, pandas, sqlalchemy
3. Once all this is configued with the API, simply run the file.

### Functional Overview
* First contact the api
* Import into a df
* Import that into a sql file which is prenamed, be sure to change it before you run it if you want a different name.

### Refactor Plan
* I want to break all functionality into funcitons as the code base grows
* I'll make unit tests if I have more than one file otherwise manual testing will do for now, I think
