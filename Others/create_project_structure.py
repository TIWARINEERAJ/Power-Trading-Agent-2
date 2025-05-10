import os

# Define the folder structure and files
project_name = "power-trading-agent"
structure = {
    project_name: {
        "config": ["config.yaml"],
        "data": ["iex_prices.csv", "weather_data.csv"],
        "src": {
            "agents": ["rule_based_agent.py", "rl_agent.py"],
            "data_fetcher": ["iex_api.py", "weather_api.py"],
            "models": ["price_forecaster.py", "demand_predictor.py"],
            "executor": ["simulated_executor.py", "broker_executor.py"],
            "risk_manager.py": None,
            "backtester.py": None,
            "logger.py": None,
            "main.py": None,
        },
        "notebooks": ["price_forecasting.ipynb"],
        "requirements.txt": None,
        "Dockerfile": None,
        "README.md": None,
        ".gitignore": None,
    }
}

def create_structure(base_path, struct):
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                pass  # Create an empty file
            print(f"Created file: {path}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    create_structure(current_dir, structure)
    print("\n✅ Project structure created successfully!")