# PickHacks2023

Our project helps consumers reach gas stations that are environmentally friendly. We judge gas stations based on their parent company's ESG score. The higher the ESG score the more enviornmentally friendly the company is. We connect consumers to these gas stations by texting a message using Twilio with the highest rated nearby gas station.

Our project uses three different APIs:

1. Google Maps API - Get list of gas stations near given location
2. yesg - API to receive ESG scores of companies
3. Twilio - Send a text message with highest rated ESG score.


# Setup
For the Google Maps API file to work, you need a "config.env" that just contains your Google Maps API key on a single line.

For the Twilio API to work, you need a "api_key.env" that contains the "Secret". An account ID and sid is also needed.

# Process
First the location of the user is sent to Google Map API, which returns a list of nearby gas stations. Our implementation currently does not read the device location and instead uses a default implementation. For the code example, we used the location of the Gale Bullman Multipurpose Building.

Most publicly traded companies have an ESG score. ESG stands for Environmental Social Govenernance. We will be focused on the E in ESG. Using the yesg library which pulls scores from the sutanalytics database, our code matches each gas station whithin a certain radius to its appropriate Environmental score. By doing this our users can make the most environmentaly concious choice, and choose the gas staion that is the best for the planet.

Then, the most enviornmentally safe gas station is sent to the user's phone.

# Front end
By using html, css, we developed an interactive website, where users can do various course of actions - from learning more about us, finding out the impact of vehicle gas emission, we believe this will educate, instruct, and galvanize cleaner energy usage. 

The theme of the websites surrounds nature. With that, we try various ways to capture the users' engagement by changing phrase upon cursor movement. We also employ a search bar, where we you will be given direct access to our platform by simply entering your name and phone number. 
