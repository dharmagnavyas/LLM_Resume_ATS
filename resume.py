import openai
import json

# Set up OpenAI API key
openai.api_key = "sk-proj-V2TpSMtULtlBpEhIPreBT3BlbkFJ3E35kfcjH73uY4sJksha"

# Function to generate ATS keywords using OpenAI API
def generate_keywords(batch_size=100):
    prompt = f"Generate a list of {batch_size} unique ATS keywords associated with the role of a Product Manager. List them as '1. keyword', '2. keyword', and so on."
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    keywords = response['choices'][0]['message']['content'].strip().split('\n')
    keywords = [keyword.strip() for keyword in keywords if keyword.strip()]
    return keywords

# Generate 500 unique ATS keywords by making multiple API calls
all_keywords = []
keywords_set = set()

while len(keywords_set) < 500:
    new_keywords = generate_keywords(batch_size=100)
    for keyword in new_keywords:
        # Check if keyword is in the expected format 'number. keyword'
        if '. ' in keyword:
            normalized_keyword = keyword.split('. ', 1)[1].strip().lower()
            if normalized_keyword not in keywords_set:
                keywords_set.add(normalized_keyword)
                all_keywords.append(keyword.split('. ', 1)[1].strip())
        if len(keywords_set) >= 500:
            break

# Ensure numbering from 1 to 500
all_keywords = list(keywords_set)[:500]
all_keywords = [f"{i+1}. {keyword}" for i, keyword in enumerate(all_keywords)]

# Print the generated list of keywords
print("Generated Keywords:")
for keyword in all_keywords:
    print(keyword)

# Remove the numbers for grouping purposes
cleaned_keywords = [keyword.split('. ', 1)[1] for keyword in all_keywords]

# Group keywords by meaning using OpenAI API
group_prompt = f"Group the following words by the same meaning into JSON format with 'label' as the group name and 'values' as the list of keywords:\n{', '.join(cleaned_keywords)}"
group_response = openai.ChatCompletion.create(
    model="gpt-4-turbo-preview",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": group_prompt}
    ]
)

# Extract and parse grouped keywords
grouped_keywords_raw = group_response['choices'][0]['message']['content'].strip()
print("\nRaw Group Response:\n", grouped_keywords_raw)

# Ensure the raw response is valid JSON
if grouped_keywords_raw.startswith("{") and grouped_keywords_raw.endswith("}"):
    grouped_keywords_raw = f"[{grouped_keywords_raw}]"

# Try to load the response as JSON
try:
    groups = json.loads(grouped_keywords_raw)
    print("\nParsed Groups:\n", groups)
except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)
    print("Raw Group Response:\n", grouped_keywords_raw)
    groups = []  # Handle the error by initializing an empty list

# Print groups and keywords if groups are not empty
if groups:
    print("\nGrouped Keywords:")
    for group in groups:
        print(f"Group: {group['label']}")
        print(f"Keywords: {', '.join(group['values'])}")

# Output to JSON if groups are not empty
if groups:
    with open('grouped_keywords.json', 'w') as f:
        json.dump(groups, f, indent=4)

print("Keywords grouped successfully.")
