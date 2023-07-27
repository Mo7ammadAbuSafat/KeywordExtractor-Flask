# Keyword Extractor API - Flask

![image](https://github.com/Mo7ammadAbuSafat/KeywordExtractor-Flask/assets/103439731/2720712c-c23d-44a9-ba6e-ff5f53d7be77)

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [spaCy Library](#spacy-library)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description

Keyword Extractor API is a Flask-based project that provides a single endpoint to extract keywords from the text provided in the query. The API utilizes the spaCy library, which is a natural language processing (NLP) library in Python, to perform the keyword extraction.

This project serves as an example of how to integrate spaCy into a Flask API to perform NLP tasks.

## Usage

1. Make sure you have the necessary dependencies installed.
2. Start the API server: `python app.py`
3. The API will be accessible at `http://localhost:5000`.
4. To extract keywords from the text, send a GET request to the following endpoint:

GET /api/extract_keywords?text=example

Replace `example` with the text from which you want to extract keywords.

5. The API will respond with a list of extracted keywords in JSON format.

## Technologies Used

- Flask (Python)
- spaCy (Natural Language Processing Library)

## spaCy Library

spaCy is an open-source NLP library that offers efficient and accurate NLP capabilities. In this project, spaCy is used to tokenize and analyze the input text to extract keywords. The library provides robust features for linguistic processing, including part-of-speech tagging, named entity recognition, and more.

Key points about spaCy integration in this project:

- Installation of spaCy and language model (e.g., en_core_web_sm) in the virtual environment.
- Tokenization of text using spaCy's language model.
- Keyword extraction based on selected criteria (e.g., nouns, entities, or specific parts of speech).

For more information about spaCy, visit the [spaCy website](https://spacy.io/).

## Contributing

Contributions to this project are welcome! If you find any bugs or have suggestions for improvement, please feel free to open an issue or submit a pull request.

1. Fork the project.
2. Create your feature branch: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


## Contact

If you have any questions or feedback regarding this project, you can reach me at:
- Email: mo7ammad.abusafat@gmail.com
- LinkedIn: https://www.linkedin.com/in/mohammad-abusafat/

