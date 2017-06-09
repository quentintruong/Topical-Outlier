## Solution to The Phantom Intern Challenge: #3: Topical Outlier

## Challenge Statement
3. Given a set of ten words identify a topical outlier. For example in the following set, sausage is an outlier: “red green blue orange white black sausage purple pink”

## Program Clarification
I assume the use of the English language.

## Approach
Use gensim for semantic modelling and basically all processing. 

Use pretrained vector representation of words provided by Google.

Use predefined library methods to search for outlier.

## Requires

python3.5 

gensim

a pretrained word2vec model

## To Run
1. Clone directory
2. Download Google's pretrained word2vec model from https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit and place inside directory
3. Run the following command in directory
```$ python3.5 topical_outlier.py```

## Note
Program is slow (~4 minutes on 2016 Macbook Air) due to inherently large dataset and large amount of computation.
