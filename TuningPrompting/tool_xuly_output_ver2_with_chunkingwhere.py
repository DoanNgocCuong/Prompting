import json
import pandas as pd

# Load the output Excel file
df_output = pd.read_excel('output_data.xlsx')

# Print the columns to check if 'chunk_where' exists
print("Columns in the DataFrame:", df_output.columns.tolist())  # New line for debugging

# Initialize empty lists for questions, answers, and chunk_where
questions = []
answers = []
chunk_wheres = []

# Iterate through each row in the DataFrame
for index, row in df_output.iterrows():
    # Assuming 'assistant_response' column contains JSON data
    json_string = row['assistant_response']
    # Attempt to parse the JSON string
    try:
        parsed_data = json.loads(json_string)  # Check if json_string is valid
    except json.JSONDecodeError:
        print(f"Error decoding JSON in row {index}: {json_string}")
        continue
    
    # Access 'Question', 'Answer', and 'chunk_where' directly from parsed_data
    for item in parsed_data:
        questions.append(item['Question'])  # Corrected line
        answers.append(item['Answer'])      # Corrected line
        # Append 'chunk_where' from the DataFrame row
        chunk_wheres.append(row['chunk_where'])  # Append value from the DataFrame

# Create a list of question-answer pairs with 'chunk_where'
qa_pairs = [{"Question": question, "Answer": answer, "chunk_where": chunk_where} for question, answer, chunk_where in zip(questions, answers, chunk_wheres)]

# Display the question-answer pairs with 'chunk_where'
for pair in qa_pairs:
    print(f"Question: {pair['Question']}\nAnswer: {pair['Answer']}\nChunk Where: {pair['chunk_where']}\n")
    
# Save the results to a new Excel file with 'chunk_where' column
df_qa_pairs = pd.DataFrame(qa_pairs)
df_qa_pairs.to_excel('processed_data_with_chunk_where.xlsx', index=False)