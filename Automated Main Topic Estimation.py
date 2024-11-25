import csv
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def convert_and_save(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        reader = csv.DictReader(input_file)

        fields = ['title', 'authors', 'groups', 'keywords', 'topics', 'abstract', 'label']

        with open(output_file, 'w', newline='', encoding='utf-8') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=fields)
            writer.writeheader()

            for row in reader:
                if 'topics' in row and row['topics']:
                    main_topic = row['topics'].split()[0]  # Select the first topic as the main topic
                    abbreviated_topic = main_topic[:3]  # Create an abbreviated topic title
                    row['label'] = abbreviated_topic  # Add the label column

                    # Write to the new dataset
                    writer.writerow({field: row[field] for field in fields})

# Example usage
convert_and_save('AAAI-14_Accepted_Papers_corrected.txt', 'converted_dataset.csv')

def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    print("Dataset Loaded")
    return data

def preprocess_data(data):
    # Add any additional data preprocessing steps here if needed
    pass

def train_and_evaluate_classifier(X_train, y_train, X_test, y_test, classifier_type):
    if classifier_type == 'Naïve-Bayes':
        classifier = MultinomialNB()
    elif classifier_type == 'Fisher':
        classifier = LogisticRegression()  # You can replace this with your Fisher classifier

    classifier.fit(X_train, y_train)
    predictions = classifier.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    return accuracy

def main():
    # Load the dataset
    file_path = 'converted_dataset.csv'
    data = load_dataset(file_path)

    # Preprocess the data if needed
    preprocess_data(data)

    # Split the dataset into features (X) and labels (y)
    X = [row['abstract'] for row in data]
    y = [row['label'] for row in data]

    # Vectorize the text data using TF-IDF
    vectorizer = TfidfVectorizer()

    # Initialize StratifiedKFold with 5 folds
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    fold_accuracies = []

    for train_index, test_index in skf.split(X, y):
        X_train, X_test = [X[i] for i in train_index], [X[i] for i in test_index]
        y_train, y_test = [y[i] for i in train_index], [y[i] for i in test_index]

        X_train = vectorizer.fit_transform(X_train)
        X_test = vectorizer.transform(X_test)

        # Ask the user to choose a classifier
        classifier_choice = input("Choose a classifier (Naïve-Bayes or Fisher): ").strip().capitalize()

        # Train and evaluate the chosen classifier
        accuracy = train_and_evaluate_classifier(X_train, y_train, X_test, y_test, classifier_choice)
        fold_accuracies.append(accuracy)

    # Calculate and print the average accuracy
    average_accuracy = sum(fold_accuracies) / len(fold_accuracies)
    print(f"\nAverage Accuracy (5-fold cross-validation): {average_accuracy:.2f}")

if __name__ == "__main__":
    main()
