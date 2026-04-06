import os
import json
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found. Please check your .env file.")
    exit(1)

# Initialize the new modern GenAI client
client = genai.Client(api_key=api_key)

def summarize_meeting(transcript: str, prompt_template: str) -> str:
    """Sends the transcript and prompt to the Gemini API."""
    full_prompt = f"{prompt_template}\n\nTranscript:\n{transcript}"
    
    try:
        # Use the highly capable gemini-2.5-flash model
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=full_prompt
        )
        return response.text
    except Exception as e:
        return f"API Error: {e}"

def run_evaluation():
    print("Starting LLM evaluation with Advanced Prompt...\n")
    
    # Load the evaluation set
    with open("eval_set.json", "r", encoding="utf-8") as f:
        eval_cases = json.load(f)

    # Advanced Prompt (Revision 2 from our prompts.md)
    advanced_prompt = """
    You are an expert Hardware Project Manager. Analyze the following manufacturing supply chain meeting transcript.
    Extract ONLY the actionable items. 
    Format as a Markdown list. 
    For each item, specify:
    - Task: (What needs to be done. Translate vague hardware acronyms if necessary)
    - DRI (Directly Responsible Individual): (Who is doing it)
    - Deadline: (When it is due, if mentioned)
    Ignore all off-topic chatter. CRITICAL: Pay extreme attention to decision reversals, sarcasm, and conditional plans ("If X, then Y"). Only output the *final* agreed-upon tasks.
    """

    output_filename = "run_results.md"
    
    with open(output_filename, "w", encoding="utf-8") as out_file:
        out_file.write("# Final Evaluation Results (Advanced Prompt)\n\n")
        
        for case in eval_cases:
            print(f"Processing case: {case['id']}...")
            out_file.write(f"## Case: {case['id']} ({case['type']})\n")
            out_file.write(f"**Expected Output**: {case['expected_output']}\n\n")
            
            result = summarize_meeting(case["transcript"], advanced_prompt)
            
            out_file.write(f"### Model Output:\n{result}\n")
            out_file.write("---\n")
            
    print(f"\nEvaluation complete. Check '{output_filename}' for results.")

if __name__ == "__main__":
    run_evaluation()