yelp-nlp
========

#### Looking at relationships between:

1. Yelp: Number of reviews
2. Yelp: Text sentiment of reviews
3. Yelp: Stars of reviews
4. City Data: Various other interesting city data (transport, crime rate, employment etc.)

#### Setup

1. Download dataset https://www.yelp.com/dataset_challenge/dataset
2. Extract the file, and rename it to `yelp` and put it into this folder.
3. We clean the yelp data using the `clean-yelp.py` file.
4. We clean the city data using the `clean-city.py` file.

#### Notes on the dataset

- Each file is composed of a single object type, one json-object per-line.
- Take a look at some examples to get you started: https://github.com/Yelp/dataset-examples.
- Amount of businesses per state:

```
{u'ON': 305, u'XGL': 1, u'MN': 1, u'ELN': 8, u'MA': 1, u'NY': 2, u'CA': 1, u'NC': 1, u'MLN': 102, u'WI': 2118, u'SCB': 2, u'NTH': 1, u'FIF': 3, u'GA': 1, u'KHL': 1, u'AZ': 22181, u'EDH': 2841, u'NV': 14583}
```

- Amount of users:
    - 252,898

--

#### Majority of the reviews:

- AZ (Arizona) State data:
    - Companies in AZ State: 22181
    - Reviews in AZ State: 493009

- NV (Nevada) State Data:
    - Companies in Nevada State: 14583
    - Reviews in Nevadate State: 571914

- EDH (Edinburgh, UK) State Data:
    - Companies in EDH State: 2841
    - Reviews in EDH State: 20873

- MLN (Edinburgh, UK) State Data:
    - Companies in MLN State: 102
    - Reviews in MLN State: 600

- ON (Toronto) State Data:
    - Companies in ON State: 305
    - Reviews in ON State: 2158

- ELN (Musselburgh, UK) State Data:
    - Companies in ELN State: 8
    - Reviews in ELN State: 21

--

#### Negligible amount

- NY State data:
    - Companies in New York State: 2
    - Reviews in New York State: 13

- MN State Data:
    - Companies in MN State: 1
    - Reviews in MN State: 3

- CA State Data:
    - Companies in MN State: 1
    - Reviews in MN State: 3

- MA State Data:
    - Companies in MN State: 1
    - Reviews in MN State: 5

- XGL State Data:
    - Companies in XGL State: 1
    - Reviews in XGL State: 3

#### CSV Output

Business: Lat   Long    Stars 
Review: Total   Stars (Review)  Text    Sentiment   Vote*
User: Review Count  Avg Stars   Yelping Since   Fans

--

##### JSON Example

```
{u'average_stars': 3.86,
 u'business_stars': 4,
 u'fans': 53,
 u'latitude': 36.0839363,
 u'longitude': -115.1194225,
 u'review_count': 1025,
 u'review_id': u'S412bghmc2IgqOZUiKmwHQ',
 u'review_stars': 4.5,
 u'sentiment': 0,
 u'stars': 4,
 u'text': u"It's not often that you step into a store and feel like you've been transported to another realm.  That's what you get at this Psychic Eye Book Shop location though.  The smells and the sounds penetrate your senses as your eyes dart from one unique lil object to the next.  It's a great place to go for a different sort of gift, psychic readings or just to browse.  \n\nYou can get books, candles, jewelry, incense, gifts from other countries, house decor, meditation tools, and more.\n\nMy friends and I like it but only make it in every couple of years, it seems.  Btw.. this is a new location!  Check the address if you're gonna stop in. :)\n\nMight see ya there!",
 u'user_votes': u'fPHLPrymsyb6WSFFKoMrTQ',
 u'votes': {u'cool': 1, u'funny': 0, u'useful': 1},
 u'yelping_since': u'2007-03'}
 ```

#### Questions

Stuff we can do:            
- Crime rate vs sentiment       Plot    Regression
- Yelping period vs Avg Rate        Plot    Regression
- Distribution of Reviews to Users      Pie Chart   
- Depression vs Avg Rating      Plot
- Depression vs Yelp Review     Plot    
- Bubble of freq            
    - Picking out users with most extreme sentiment         
    - Word frequency of user

#### Presentation 
- https://docs.google.com/a/nyu.edu/presentation/d/1_BxqvhDsR2Sgj8i5hNiwoocppzBOaLT_8G8CXmUUOr8/edit?usp=sharing

####Extra Information

business
```
{
    'type': 'business',
    'business_id': (encrypted business id),
    'name': (business name),
    'neighborhoods': [(hood names)],
    'full_address': (localized address),
    'city': (city),
    'state': (state),
    'latitude': latitude,
    'longitude': longitude,
    'stars': (star rating, rounded to half-stars),
    'review_count': review count,
    'categories': [(localized category names)]
    'open': True / False (corresponds to closed, not business hours),
    'hours': {
        (day_of_week): {
            'open': (HH:MM),
            'close': (HH:MM)
        },
        ...
    },
    'attributes': {
        (attribute_name): (attribute_value),
        ...
    },
}
```

review
```
{
    'type': 'review',
    'business_id': (encrypted business id),
    'user_id': (encrypted user id),
    'stars': (star rating, rounded to half-stars),
    'text': (review text),
    'date': (date, formatted like '2012-03-14'),
    'votes': {(vote type): (count)},
}
```

user
```
{
    'type': 'user',
    'user_id': (encrypted user id),
    'name': (first name),
    'review_count': (review count),
    'average_stars': (floating point average, like 4.31),
    'votes': {(vote type): (count)},
    'friends': [(friend user_ids)],
    'elite': [(years_elite)],
    'yelping_since': (date, formatted like '2012-03'),
    'compliments': {
        (compliment_type): (num_compliments_of_this_type),
        ...
    },
    'fans': (num_fans),
}
```

check-in
```
{
    'type': 'checkin',
    'business_id': (encrypted business id),
    'checkin_info': {
        '0-0': (number of checkins from 00:00 to 01:00 on all Sundays),
        '1-0': (number of checkins from 01:00 to 02:00 on all Sundays),
        ...
        '14-4': (number of checkins from 14:00 to 15:00 on all Thursdays),
        ...
        '23-6': (number of checkins from 23:00 to 00:00 on all Saturdays)
    }, # if there was no checkin for a hour-day block it will not be in the dict
}
```

tip
```
{
    'type': 'tip',
    'text': (tip text),
    'business_id': (encrypted business id),
    'user_id': (encrypted user id),
    'date': (date, formatted like '2012-03-14'),
    'likes': (count),
}
```
