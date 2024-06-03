## Overview
This project generates and groups ATS (Applicant Tracking System) keywords for the role of a Product Manager using OpenAI's GPT-4 model. The primary goal is to ensure the generated keywords are accurate and contextually relevant, and that they can be easily extended to other occupational roles.

## Features
- **Keyword Generation:** Generates a list of 500 unique ATS keywords associated with Product Management.
- **Keyword Grouping:** Groups the generated keywords by similar meaning using AI.
- **Scalability:** The logic is designed to be scalable and extendable to other roles.

## Prerequisites
- Python 3.x
- OpenAI API key

## Usage
1. **Set up your OpenAI API key:**
   Replace `"your-openai-api-key"` in the code with your actual OpenAI API key.
   ```python
   openai.api_key = "your-openai-api-key"
   ```

2. **Run the script:**
   Execute the `resume.py` script to generate and group the keywords.

3. **Output:**
   The script will print the generated keywords and their groups to the console. It will also save the grouped keywords to a file named `grouped_keywords.json`.

## Example Output
The JSON output will look something like this:
```json
{
  "groups": [
    {
      "label": "Project Management & Agile Methodologies",
      "values": [
        "agile development",
        "scrum",
        "kanban",
        "scaled agile framework",
        "safe agile",
        "lean startup"
      ]
    },
    {
      "label": "Product Management Skills",
      "values": [
        "product management software",
        "product launches",
        "product launch planning",
        "product lifecycle"
      ]
    }
  ]
}
```

## Conclusion
This project leverages OpenAI's API for both keyword generation and grouping, ensuring high accuracy and scalability. The approach balances the use of advanced technology with practical implementation, making it suitable for extending to various other occupational roles.
