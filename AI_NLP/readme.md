What is Stemming?

Stemming is the process of removing suffixes/prefixes to get the root word.

Example:

"running" → "run"

"flies" → "fli"

"happiness" → "happi"

The stem may not always be a valid English word (unlike lemmatization, which produces valid dictionary forms).


Stemming algorithms:

        1.  Porters:

                  
                   PorterStemmer is a stemming algorithm in NLTK (Natural Language Toolkit).
                   It reduces words to their root/stem form by chopping off common endings like -ing, -ed, -s, -ly, etc.

        2.  Lancaster:


                   It’s a rule-based stemming algorithm that applies an iterative set of rules to reduce words to their root.

                   Unlike PorterStemmer, it is more aggressive → it cuts words down more heavily, sometimes too much.

                   Because of this, it often produces very short stems
        3.  Snowball:

     

                   Developed by Martin Porter (the same person who created PorterStemmer).

                   It’s part of the Snowball framework (a language for writing stemming algorithms).

                   Supports multiple languages (English, French, German, Spanish, etc.), unlike Porter or Lancaster, which mostly focus on English.

                   Less aggressive than Lancaster, but often produces cleaner stems than Porter.

                   The Snowball Stemmer (also called the Porter2 stemmer) is an improved version of the original Porter stemmer. It’s available in NLTK and is widely used in NLP because it balances accuracy and aggressiveness better than Lancaster or Porter

