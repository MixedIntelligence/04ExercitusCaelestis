import json

def analyze_geospatial_threats(data_file):
    """Analyze geospatial data for potential threats."""
    with open(data_file, 'r') as file:
        data = json.load(file)
    
    # Example analysis: Check for flood-prone areas
    flood_threats = [region for region in data if region["risk"] == "flood"]
    return flood_threats

# Example usage
if __name__ == "__main__":
    threats = analyze_geospatial_threats("data/sample_geospatial_data.json")
    print("Identified flood threats:", threats)
