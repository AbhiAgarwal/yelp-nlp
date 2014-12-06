from textblob import TextBlob

def sentimentAnalysis(text):
	blob = TextBlob(text)
	print blob.sentiment.polarity

sentimentAnalysis(
'''
It's not often that you step into a store and feel like you've been transported to another realm.  That's what you get at this Psychic Eye Book Shop location though.  The smells and the sounds penetrate your senses as your eyes dart from one unique lil object to the next.  It's a great place to go for a different sort of gift, psychic readings or just to browse.  
You can get books, candles, jewelry, incense, gifts from other countries, house decor, meditation tools, and more.
My friends and I like it but only make it in every couple of years, it seems.  Btw.. this is a new location!  Check the address if you're gonna stop in. :)
Might see ya there!
'''
)