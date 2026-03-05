import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango

class TronTextDisplay(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.HORIZONTAL)
        self.set_spacing(0)
        
        # Main text label
        self.text_label = Gtk.Label()
        self.text_label.set_text("Linux Header")
        self.text_label.set_justify(Gtk.Justification.CENTER)
        self.text_label.set_ellipsize(Pango.EllipsizeMode.END)
        self.text_label.set_max_width_chars(30)
        self.text_label.set_width_chars(30)
        
        # Apply Tron styling
        self.apply_tron_styling()
        
        self.pack_start(self.text_label, True, True, 0)
        
    def apply_tron_styling(self):
        """Apply Tron-themed styling to the text display"""
        # Set CSS name for styling
        self.text_label.set_name("tron-text-label")
        
        # Create CSS provider for Tron styling
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"""
            #tron-text-label {
                color: #00ffff;  /* Neon blue */
                font-family: 'Courier New', monospace;
                font-weight: bold;
                font-size: 14px;
                text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
                background-color: rgba(0, 0, 0, 0.8);
                border: 1px solid #00ffff;
                border-radius: 4px;
                padding: 4px 8px;
            }
            
            #tron-text-label:hover {
                color: #ffffff;
                text-shadow: 0 0 10px #ffffff, 0 0 20px #ffffff;
                border-color: #ffffff;
            }
        """)
        
        # Apply CSS to the screen
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
    def set_text(self, text):
        """Set the text to display"""
        if len(text) > 30:
            text = text[:27] + "..."
        self.text_label.set_text(text)
        
    def get_text(self):
        """Get the current text"""
        return self.text_label.get_text()
        
    def set_alignment(self, alignment):
        """Set text alignment (left, center, right)"""
        if alignment == "left":
            self.text_label.set_justify(Gtk.Justification.LEFT)
        elif alignment == "right":
            self.text_label.set_justify(Gtk.Justification.RIGHT)
        else:  # center
            self.text_label.set_justify(Gtk.Justification.CENTER)
            
    def set_font_color(self, color):
        """Set font color (blue, red, green)"""
        css_provider = Gtk.CssProvider()
        
        if color == "red":
            css_data = b"""
                #tron-text-label {
                    color: #ff0000;
                    text-shadow: 0 0 5px #ff0000, 0 0 10px #ff0000;
                    border-color: #ff0000;
                }
                #tron-text-label:hover {
                    color: #ffffff;
                    text-shadow: 0 0 10px #ffffff, 0 0 20px #ffffff;
                    border-color: #ffffff;
                }
            """
        elif color == "green":
            css_data = b"""
                #tron-text-label {
                    color: #00ff00;
                    text-shadow: 0 0 5px #00ff00, 0 0 10px #00ff00;
                    border-color: #00ff00;
                }
                #tron-text-label:hover {
                    color: #ffffff;
                    text-shadow: 0 0 10px #ffffff, 0 0 20px #ffffff;
                    border-color: #ffffff;
                }
            """
        else:  # blue (default)
            css_data = b"""
                #tron-text-label {
                    color: #00ffff;
                    text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
                    border-color: #00ffff;
                }
                #tron-text-label:hover {
                    color: #ffffff;
                    text-shadow: 0 0 10px #ffffff, 0 0 20px #ffffff;
                    border-color: #ffffff;
                }
            """
            
        css_provider.load_from_data(css_data)
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION + 1)

class EditWindow(Gtk.Window):
    def __init__(self, parent_applet):
        super().__init__(title="Edit Linux Header")
        self.parent_applet = parent_applet
        self.set_border_width(10)
        self.set_default_size(400, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        # Main vertical box
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)
        
        # Text entry
        self.text_entry = Gtk.Entry()
        self.text_entry.set_max_length(30)
        self.text_entry.set_placeholder_text("Enter your text (max 30 characters)")
        vbox.pack_start(self.text_entry, False, False, 0)
        
        # Character counter
        self.char_counter = Gtk.Label()
        self.char_counter.set_text("0/30 characters")
        vbox.pack_start(self.char_counter, False, False, 0)
        
        # Customization options
        options_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.pack_start(options_box, False, False, 0)
        
        # Font color selector
        color_label = Gtk.Label("Color:")
        options_box.pack_start(color_label, False, False, 0)
        
        self.color_combo = Gtk.ComboBoxText()
        self.color_combo.append("blue", "Neon Blue")
        self.color_combo.append("red", "Neon Red")
        self.color_combo.append("green", "Neon Green")
        self.color_combo.set_active(0)
        options_box.pack_start(self.color_combo, False, False, 0)
        
        # Alignment selector
        align_label = Gtk.Label("Alignment:")
        options_box.pack_start(align_label, False, False, 0)
        
        self.align_combo = Gtk.ComboBoxText()
        self.align_combo.append("left", "Left")
        self.align_combo.append("center", "Center")
        self.align_combo.append("right", "Right")
        self.align_combo.set_active(1)  # Default to center
        options_box.pack_start(self.align_combo, False, False, 0)
        
        # Buttons
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        vbox.pack_start(button_box, False, False, 0)
        
        # Save button
        save_button = Gtk.Button(label="Save")
        save_button.connect("clicked", self.on_save_clicked)
        button_box.pack_start(save_button, True, True, 0)
        
        # Cancel button
        cancel_button = Gtk.Button(label="Cancel")
        cancel_button.connect("clicked", self.on_cancel_clicked)
        button_box.pack_start(cancel_button, True, True, 0)
        
        # Connect text changed signal for character counter
        self.text_entry.connect("changed", self.on_text_changed)
        
        # Apply Tron styling
        self.apply_tron_styling()
        
    def apply_tron_styling(self):
        """Apply Tron-themed styling to the edit window"""
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"""
            GtkWindow {
                background-color: #000000;
                color: #00ffff;
            }
            
            GtkEntry {
                background-color: #1a1a1a;
                color: #00ffff;
                border: 1px solid #00ffff;
                border-radius: 4px;
                padding: 4px 8px;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
            
            GtkEntry:focus {
                border-color: #ffffff;
                box-shadow: 0 0 5px #ffffff;
            }
            
            GtkLabel {
                color: #00ffff;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
            
            GtkButton {
                background-color: #000000;
                color: #00ffff;
                border: 1px solid #00ffff;
                border-radius: 4px;
                padding: 6px 12px;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
            
            GtkButton:hover {
                background-color: #00ffff;
                color: #000000;
            }
            
            GtkComboBox {
                background-color: #1a1a1a;
                color: #00ffff;
                border: 1px solid #00ffff;
                border-radius: 4px;
            }
        """)
        
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
    def on_text_changed(self, entry):
        """Update character counter"""
        text = entry.get_text()
        length = len(text)
        self.char_counter.set_text(f"{length}/30 characters")
        
    def on_save_clicked(self, button):
        """Save the edited text and settings"""
        text = self.text_entry.get_text()
        color = self.color_combo.get_active_text().lower()
        alignment = self.align_combo.get_active_text().lower()
        
        # Update parent applet
        self.parent_applet.update_text(text, color, alignment)
        self.destroy()
        
    def on_cancel_clicked(self, button):
        """Cancel editing and close window"""
        self.destroy()
        
    def set_current_values(self, text, color, alignment):
        """Set current values in the edit window"""
        self.text_entry.set_text(text)
        self.on_text_changed(self.text_entry)
        
        # Set color combo
        if color == "red":
            self.color_combo.set_active(1)
        elif color == "green":
            self.color_combo.set_active(2)
        else:
            self.color_combo.set_active(0)
            
        # Set alignment combo
        if alignment == "left":
            self.align_combo.set_active(0)
        elif alignment == "right":
            self.align_combo.set_active(2)
        else:
            self.align_combo.set_active(1)