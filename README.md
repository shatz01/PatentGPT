# Exploring LLM training & finetuning via patents!

Motivation (s):
- Im just a bit bored and want to get my hands dirty by doing this kind of stuff.
- Patents are a MASSIVE source of free, high quality, and easily accessible text data.

## Files of importance
- `download_patents.py`: This file sends requests to the USPTO to download patents.
  - example usage: `python download_patents.py --from-date="2010-01-01" --to-date="2010-01-03"` (this will download all patents from 2010-01-01 to 2010-01-03)

## Installation Instructions
- conda create -n patentgpt_env python=3.10 -y && conda activate patentgpt_env
- if on mac: pip uninstall grpcio; conda install -c conda-forge grpcio=1.43.0 (from skypilot docs https://skypilot.readthedocs.io/en/latest/getting-started/installation.html)
- pip install -r requirements.txt
- pip install "skypilot[all]"  # (this takes a while)

## Stack
- pytorch
- huggingface
- skypilot

## Roadmap
1. download a sample of USPTO
2. parse the pdf's so that we can train models on the data
3. get skypilot working
4. finetune a decoder only model sample dataset
5. download the entire USPTO
6. see how fast we can train a model on the whole thing
7. Can we include image info? patents contain diagrams
8. ... the decision tree of stuff to do has become too large. \<EOSTOKEN\> for now.

