import json
import os
import logging

class SettingsManager:
    def __init__(self, applet_dir):
        self.applet_dir = applet_dir
        self.data_file = os.path.join(applet_dir, "data", "text_data.json")
        self.default_settings = {
            "text": "Linux Header",
            "color": "blue",
            "alignment": "center"
        }
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def load_settings(self):
        """Load settings from JSON file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    settings = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    return {**self.default_settings, **settings}
            else:
                # Create default file
                self.save_settings(self.default_settings)
                return self.default_settings.copy()
        except Exception as e:
            self.logger.error(f"Error loading settings: {e}")
            return self.default_settings.copy()
            
    def save_settings(self, settings):
        """Save settings to JSON file"""
        try:
            # Ensure data directory exists
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            
            with open(self.data_file, 'w') as f:
                json.dump(settings, f, indent=2)
            self.logger.info("Settings saved successfully")
        except Exception as e:
            self.logger.error(f"Error saving settings: {e}")
            
    def update_text(self, text, color, alignment):
        """Update text and settings"""
        # Ensure text doesn't exceed 30 characters
        if len(text) > 30:
            text = text[:30]
            
        settings = {
            "text": text,
            "color": color,
            "alignment": alignment
        }
        
        self.save_settings(settings)
        return settings
        
    def get_current_settings(self):
        """Get current settings"""
        return self.load_settings()