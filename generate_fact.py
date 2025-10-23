import os
import requests
from datetime import date

# Get the API Key from the GitHub Secret
API_KEY = os.environ.get('AI_API_KEY')
# Define the path for the daily fact file
FACT_FILE = 'current_fact.txt'

# The detailed prompt to instruct the AI
PROMPT = (
    "Generate a single, fascinating, and little-known historical culinary fact "
    "about a specific food, dish, or cooking technique. Do not include a title. "
    "The fact must be brief, engaging, and ready for immediate display on a website. "
    "Example: 'The Romans used a fermented fish sauce called garum as a primary seasoning, much like modern cooks use salt and pepper.'"
)

# Function to call the AI API (using a generic structure)
def get_ai_response():
    # --- This needs to be slightly adapted for your chosen API (Groq/Mistral) ---
    # Example using a standard requests structure:
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'mixtral-8x7b-32768', # Use the recommended free model from your provider
        'messages': [{'role': 'user', 'content': PROMPT}],
        'temperature': 0.9
    }
    # In generate_fact.py, inside the get_ai_response function
print(f"DEBUG: Calling API with model: {data['model']}")
# ... rest of the code ...
response = requests.post('https://api.groq.com/openai/v1/chat/completions', headers=headers, json=data) 
# ... rest of the code ...
    # Replace the URL with your chosen provider's chat completions endpoint
    response = requests.post('https://api.groq.com/openai/v1/chat/completions', headers=headers, json=data)
    
    response.raise_for_status() # Raise an exception for bad responses
    
    # Extract the generated text
    fact_text = response.json()['choices'][0]['message']['content'].strip()
    
    return fact_text

# Main execution logic
if __name__ == "__main__":
    try:
        new_fact = get_ai_response()
        
        # Add a timestamp to the fact
        timestamped_fact = f"Fact for {date.today().strftime('%B %d, %Y')}:\n\n{new_fact}"
        
        # Write the new fact to the file
        with open(FACT_FILE, 'w', encoding='utf-8') as f:
            f.write(timestamped_fact)
            
        print(f"Successfully generated and saved fact to {FACT_FILE}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# IMPORTANT: COMMIT THIS FILE TO THE REPOSITORY.
