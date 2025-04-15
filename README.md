# Aksara Lampung Classification

## About

This program designed to classify Aksara Lampung digitally handwritten. The model used is by finetuning VIT base patch16 224 from Google.

## Installation

1. Clone this repository using:

    ``` git clone https://github.com/brilbrilbril/aksara_lampung_classification.git ```

2. You can use virtual environment (optional, but recommended).
3. Install all dependencies by executing:

    ``` pip install -r requirements.txt ```

4. You MUST finetune the model first because github free does not allow large file such weight and bias from the model
5. Run all cells in __finetuning_vit.ipynb__
6. You do not need to execute __aug.py__, since it's a program to augment the images file externally
7. After the model saved as "aksara_model" directory, run the __app.py__ 

    ``` streamlit run app.py ```