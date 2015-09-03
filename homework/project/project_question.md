#Project Question:  Pet Grooming

* What is the question you hope to answer?

Can I predict if a person who has one pet will get a second pet based on the person’s address, home type (apartment, house), grooming frequency and pet breed?

* What data are you planning to use to answer that question?

I plan to use the client database used at my parents’ shop.  The database contains over 3,000 unique clients.  It includes address and contact data, as well as pet data (breed, grooming style, vet).  The appointments are maintained in a separate application.  I should be able to export the data from both applications join them based on phone numbers.

I also plan to use a mapping library, probably OSM, to be able to map the addresses and get a better sense of the home type.

* What do you know about the data so far?

The client and pet data is stored in a SQL database. It can be exported into csv files.  OpenStreetMap (OSM) has an api that I can use to geolocate the client data and pull in other location information.

* Why did you choose this topic?

I chose this topic because I thought it would be neat to apply data science to helping a small business, especially one that is traditionally not techy.  I’m in a unique position where my parents’ own a small business and I have access to their data.

If I’m able to answer my question, my parents could use that information to, maybe, put more focus on retaining these clients or providing them with resources on where to get another pet.