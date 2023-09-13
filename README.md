[![pypi](https://img.shields.io/pypi/v/finvader.svg)](https://pypi.python.org/pypi/finvader)
[![python](https://img.shields.io/pypi/pyversions/finvader.svg)](https://pypi.python.org/pypi/finvader)
[![License: MIT](https://badgen.net/badge/license/apache-2-0/blue)]([https://opensource.org/licenses/MIT](https://opensource.org/license/apache-2-0/))


# FinVADER
**VADER sentiment classifier updated with financial lexicons**


**VADER** *(Valence Aware Dictionary and sEntiment Reasoner)* classifier is a mainstream model for sentiment analysis using a 
general-language human-curated lexicon, including linguistic features expressed on social media. As such, the model works
worse on texts that use domain-specific language, such as finance or economics.

**FinVADER** improves VADER's classification accuracy, including two finance lexicons: [SentiBignomics](https://github.com/consose/SentiBigNomics),
and [Henry's word list](https://journals.sagepub.com/doi/10.1177/0021943608319388). *SentiBigNomics* is a detailed financial lexicon for aspect-based sentiment analysis with 
approximately 7300 terms containing a polarity score ranging in [-1,1] for each item. *Henry's lexicon* covers 189 words 
appearing in the company earnings press releases. 

FinVADER outperforms VADER on Financial PhraseBank data: 

![finvader_accuracy](https://github.com/PetrKorab/FinVADER/assets/62357254/6f464bb2-1d9c-4cb7-ba63-f535c6a1fda6)

![vader_accuracy](https://github.com/PetrKorab/FinVADER/assets/62357254/6bc4080b-ce1a-499f-9dbd-de8cf8f1ecdc)

The code for this benchmark test is [here](https://github.com/PetrKorab/FinVADER/blob/main/finvader_benchmark.ipynb)

**** 


## Installation

FinVADER requires [Python 3.8 - 3.11](https://www.python.org/downloads/), and [NLTK](http://www.nltk.org). 

To install using pip, use:

`pip install finvader`


## Usage

* **Import the library**:


``` python
from finvader import finvader
```

* **Select lexicons:**


``` python
def finvader(text = 'str',                    # Text
             indicator = 'str',               # VADER's indicator: 'pos'/'neg'/'neu'/'compound' 
             use_sentibignomics: bool= False, # Use SentiBignomics lexicon
             use_henry: bool= False):         # Use Henry's lexicon
) 
```

* **Use the classifier:**

``` python
text = "The period's sales dropped to EUR 30.6 m from EUR 38.3 m, according to the interim report, released today."

scores = finvader(text, 
                  use_sentibignomics = True, 
                  use_henry = True, 
                  indicator = 'compound' )
```

## Documentation, examples and tutorials

For examples of coding, read these  tutorials:

**FinVADER: Sentiment Analysis for Financial Applications** [here](https://medium.com/python-in-plain-english/finvader-sentiment-analysis-for-financial-applications-6ab3c08840b4)
**Fine-tuning VADER Classifier with Domain-specific Lexicons** [here](https://medium.com/mlearning-ai/fine-tuning-vader-classifier-with-domain-specific-lexicons-1b23f6882f2)


**** 

Please visit [here](https://github.com/PetrKorab/finvader/issues) for any questions, issues, bugs, and suggestions.
