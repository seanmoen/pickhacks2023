# PickHacks2023

Our project helps consumers reach gas stations that are environmentally friendly. We judge gas stations based on their parent company's ESG score. The higher the ESG score the more enviornmentally friendly the company is. We connect consumers to these gas stations by texting a message using Twilio with the highest rated nearby gas station.

Our project uses three different APIs:

1. Google Maps API - Get list of gas stations near given location
2. yesg - API to receive ESG scores of companies
3. Twilio - Send a text message with highest rated ESG score.


# Setup
For the Google Maps API file to work, you need a "config.env" that just contains your Google Maps API key on a single line.

For the Twilio API to work, you need a 

# Process
First the location of the user is sent to Google Map API, which returns a list of nearby gas stations. Our implementation currently does not read the device location and instead uses a default implementation. For the code example, we used the location of the Gale Bullman Multipurpose Building.

Next, the ESG scores are obtained.

Then, the most enviornmentally safe gas station is sent to the user's phone.
