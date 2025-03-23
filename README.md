# Dog Matcher

This application helps users find the best dog breed based on their preferences. It uses various filters to narrow down the options and provides detailed information about the selected breed. The application leverages the Gemini API to transform natural language responses from users into values that are used for filtering the database based on criteria.

## Features

- **Size Filter**: Select the preferred size of the dog.
- **Grooming Frequency Filter**: Choose how often you can groom your dog.
- **Shedding Filter**: Specify the acceptable level of shedding.
- **Energy Level Filter**: Indicate the desired energy level of the dog.
- **Trainability Filter**: Define how easy the dog should be to train.
- **Demeanor Filter**: Select the preferred behavior of the dog towards strangers.
- **Temperament Filter**: Choose the most important temperament traits.
- **Translation**: Translate the breed description to Polish.
- **Image Retrieval**: Fetch images of the selected breed from an external API.

## Libraries and Tools Used

- **Python**: The main programming language used for the application.
- **Pandas**: For data manipulation and analysis.
- **Requests**: For making HTTP requests to external APIs.
- **dotenv**: For loading environment variables from a `.env` file.
- **Google Generative AI**: For generating content based on user input.
- **The Dog API**: For retrieving images of dog breeds. *(https://www.thedogapi.com)*

## Data Source
The dog breed database comes from the *https://tmfilho.github.io/akcdata/*.
