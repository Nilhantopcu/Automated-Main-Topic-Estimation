# AAAI Conference Papers Topic Estimation

This Python program automatically estimates the main topics of papers accepted as part of the AAAI Conference on Artificial Intelligence using Naïve-Bayes and Fisher classifiers.

## Project Overview

The main goal of this project is to determine the main topic of AAAI conference papers based on their titles and abstracts. The dataset used for this project is not provided here, and users are expected to prepare their own dataset in the required format.

## Usage
1. Ensure that you have the dataset file (converted_dataset.csv) in the project directory.
2. Run the main script:

```bash
python Automated Main Topic Estimation.py
```

3. Follow the on-screen prompts to choose a classifier (Naïve-Bayes or Fisher).

4. Optionally, set or unset thresholds for any category during classification.

5. The program will determine the main topic for each paper and calculate the accuracy of the classifier using 5-fold cross-validation.

6. View the average accuracy of the classifier on the output.

## Dataset Preparation
Prepare your dataset in the format: title,authors,groups,keywords,topics,abstract,label and save it as converted_dataset.csv.
