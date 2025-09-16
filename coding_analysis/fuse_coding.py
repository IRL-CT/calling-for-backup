import pandas as pd
import os
import glob
import re

def time_to_seconds(time_str):
    """Convert time string HH:MM:SS.mmm to seconds"""
    if not time_str or time_str.strip() == '' or time_str.strip().upper() == 'NA':
        return None
    
    parts = time_str.split(':')
    hours = float(parts[0])
    minutes = float(parts[1])
    seconds = float(parts[2])
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def extract_participant_and_video(filename):
    """Extract participant_id and video_name from filename"""
    # Remove .txt extension
    base_name = filename.replace('.txt', '')
    
    # Split by underscore and get the last part as participant_id
    parts = base_name.split('_')
    if parts[-1].startswith('P'):
        participant_id = parts[-1]  # Last part (e.g., P10)
        video_name = '_'.join(parts[:-1])  # All parts except last (e.g., 2025-02-13_10-28-33_P10)

    else:
        participant_id = parts[-2] 
        video_name = '_'.join(parts[:-2])  # All parts except last two

    return participant_id, video_name

def process_codes_to_dataframe():
    """Process all txt files in codes folder and create a single dataframe"""
    
    # Hard-coded video duration dictionary based on stimulus_dataset_information.xlsx
    video_durations = {
        'skate': 10.26,
        'warehouse': 22.03,
        'stackblocks': 11.3,
        'falldalmata': 21.33,
        'stairs': 10.62,
        'wave': 8.7
    }
    
    # Initialize list to store all rows
    all_rows = []
    
    # Process all txt files in the codes folder
    codes_folder = 'codes'#'../../dados'#'codes'
    txt_files = glob.glob(os.path.join(codes_folder, '*.txt'))
    
    print(f"Found {len(txt_files)} txt files to process...")
    
    for txt_file in txt_files:
        filename = os.path.basename(txt_file)
        participant_id, video_name = extract_participant_and_video(filename)
        
        print(f"Processing {filename} - Participant: {participant_id}, Video: {video_name}")
        
        # Read the txt file
        with open(txt_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Split by tab - expecting 5 columns: code_group, start, end, duration, subcode
            parts = line.split('\t')
            print(f"Line parts ({len(parts)}): {parts}")

            if len(parts) >= 5:
                code_group = parts[0]
                start = parts[2]  
                end = parts[3]
                duration_str = parts[4]
                subcode = parts[5] if len(parts) > 5 else ''
                
                # Convert duration to seconds
                if code_group == 'video' and subcode in video_durations:
                    # Use video duration from dictionary
                    duration_seconds = video_durations[subcode]
                else:
                    # Use duration from file, converted to seconds
                    duration_seconds = time_to_seconds(duration_str)
                
                # Create row for dataframe
                row = {
                    'participant_id': participant_id,
                    'video_name': video_name,
                    'start': start,
                    'end': end,
                    'duration': duration_seconds,
                    'code_group': code_group,
                    'subcode': subcode
                }
                
                all_rows.append(row)
            else:
                # Skip lines that don't have at least 3 columns
                print(f"Warning: Skipping line with insufficient columns ({len(parts)} columns): {line}")
    
    # Create DataFrame
    df = pd.DataFrame(all_rows)
    
    # Sort by participant_id and then by start time
    df = df.sort_values(['participant_id', 'start']).reset_index(drop=True)

    print(f"\nDataFrame created with {len(df)} rows")
    print(f"Columns: {list(df.columns)}")
    print(f"Unique participants: {df['participant_id'].nunique()}")
    print(f"Unique videos: {df['video_name'].nunique()}")
    print(f"Unique code groups: {df['code_group'].unique()}")
    
    # Display first few rows
    print("\nFirst 5 rows:")
    print(df.head())
    
    # Save to CSV
    output_file = 'processed_codes.csv'
    df.to_csv(output_file, index=False)
    print(f"\nDataFrame saved to {output_file}")
    
    return df

# Run the processing
if __name__ == "__main__":
    df = process_codes_to_dataframe()