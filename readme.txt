
Implemented in Python

------------------------------------------------------------------------------------------------
Objective: 

	Our project objective is to classify the twitter messages(tweets) into 4 emotional categories (the emotional categories are C1, C2, C3, C4)

------------------------------------------------------------------------------------------------

The entire code is divided into 2 modules:

1st module:

-->The first module (pos61.py) consists of pre-processing and feature extraction techniques
-->Input for this module is raw tweets and part-of-speech tagged data
-->Output of the module is features
-->import nltk toolkit for tagging

2nd module:

-->The second module (labelled51.py) classifies the tweets into 4 emotional categories.
The emotional categories are:
	C1 = Happy-Active (specifies more happy emotions)
	C2 = Happy-Inactive (specifies less happy emotions)
	C3 = Unahappy-Active (specifies less sad emotions)
	C4 = Unhappy-Inactive (specifies more sad emotions)

-->Input for this module is part-of-speech tagged data, seed, special (seed and special contains features)
-->Output of the module is classified tweets(i.e tweets with label C1, C2, C3, C4)

------------------------------------------------------------------------------------------------


