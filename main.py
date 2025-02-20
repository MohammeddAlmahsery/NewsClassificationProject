import subprocess

# script execution order
scripts = [

    "src/scraping/scraper.py",          # Step 0: Scrape the data
    "src/preprocessing/clean_data.py",        # Step 1: Clean the raw data
    "src/preprocessing/feature_engineering.py",  # Step 2: Transform and balance the data
    "src/models/train.py",            # Step 3: Train the model
    "src/models/evaluate.py"          # Step 4: Evaluate model performance
]

print("Starting the ML pipeline...\n")

# Execute each script sequentially
for script in scripts:
    
    print(f"Running {script}...\n")
    result = subprocess.run(["python", script], capture_output=True, text=True)
    print(result.stdout)  # Print script output
    
    if result.returncode != 0:
        print(f"Error in {script}: {result.stderr}")
        break

print("\nPipeline execution complete!")
