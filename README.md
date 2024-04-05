# Exploring LLM training & finetuning via patents!

Motivation (s):
- Im just a bit bored and want to get my hands dirty by doing this kind of stuff.
- Patents are a MASSIVE source of free, high quality, and easily accessible text data.

## Files of importance
- `download_patents.py`: This file sends requests to the USPTO to download patents.

## Installation Instructions
- pip install -r requirements.txt

## Roadmap
1. download a sample of USPTO
2. parse the pdf's so that we can train models on the data
3. get skypilot working
4. finetune a decoder only model sample dataset
5. download the entire USPTO
6. see how fast we can train a model on the whole thing
7. Can we include image info? patents contain diagrams
8. ... the decision tree of stuff to do has become too large. <EOSTOKEN> for now.

