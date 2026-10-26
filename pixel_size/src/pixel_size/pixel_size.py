from pathlib import Path
import json

# ============================
# Calculate pixel size
# ============================

def pixel_size(scope, zoom_factor, calibration_file=None):
    '''
    Function to calculate image pixel size for images accquired at calibrated stereoscopes.
    Available scopes in default calibration file:
    - 'olympus_mignot'
    - 'nikon_common'
    - 'leica_prudhomme'
    '''

    # Resolve default path relative to this script's directory
    if calibration_file is None:
        calibration_file = Path(__file__).parent / 'stereoscope_calibration.json'

    # Read the calibration JSON
    with open(calibration_file, 'r', encoding='utf-8') as f:
        calibrations = json.load(f)

    y0 = calibrations[scope]['mean_y0']
    gamma = calibrations[scope]['mean_gamma']

    y = y0 - zoom_factor ** -gamma

    return y

# ============================
# Update calibration file
# ============================

def save_or_update_calibration(scope, mean_y0, std_y0, mean_gamma, std_gamma, json_path=None):

    json_path = Path(json_path)

    # Resolve default path relative to this script's directory
    if json_path is None:
        json_path = Path(__file__).parent / 'stereoscope_calibration.json'

    # Load existing data if file exists, else start with empty dict
    if json_path.exists():
        with open(json_path, 'r', encoding='utf-8') as f:
            calibrations = json.load(f)
    else:
        calibrations = {}
    
    # Add or update the scope entry (casting to standard python float)
    calibrations[scope] = {
        'mean_y0': float(mean_y0),
        'std_y0': float(std_y0),
        'mean_gamma': float(mean_gamma),
        'std_gamma': float(std_gamma)
    }
    
    # Save back to the JSON file with clean formatting
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(calibrations, f, indent=4)
        
    print(f"Successfully saved calibration for '{scope}' to {json_path}")