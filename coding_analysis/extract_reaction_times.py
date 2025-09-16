import pandas as pd

# Read the data
df = pd.read_csv("processed_codes.csv")

# Get unique participants
participants = df['participant_id'].unique()
results = []

for participant in participants:
    # Filter and sort data for this participant
    p_data = df[df['participant_id'] == participant].sort_values('start')
    
    # Find relevant subcodes
    nounderstanding = p_data[p_data['subcode'] == '8nounderstanding3x']
    callisabel = p_data[p_data['subcode'] == '9callisabel']
    
    # Initialize result with NA values
    result = {
        'participant_id': participant,
        'start_1': 'NA', 'end_1': 'NA', 'start_2': 'NA', 
        'end_2': 'NA', 'start_3': 'NA', 'end_3': 'NA'
    }
    
    # Fill in timestamps if available
    if len(nounderstanding) >= 1:
        result['start_1'] = nounderstanding.iloc[0]['end']
    if len(nounderstanding) >= 2:
        result['end_1'] = nounderstanding.iloc[1]['start']
        result['start_2'] = nounderstanding.iloc[1]['end']
    if len(nounderstanding) >= 3:
        result['end_2'] = nounderstanding.iloc[2]['start']
        result['start_3'] = nounderstanding.iloc[2]['end']
    if len(callisabel) >= 1:
        result['end_3'] = callisabel.iloc[0]['start']
        
    results.append(result)

# Save results
reaction_times_df = pd.DataFrame(results)
reaction_times_df.to_csv("reaction_times.csv", index=False)

print("Reaction times extracted and saved to reaction_times.csv")
print("\nResults:")
print(reaction_times_df)