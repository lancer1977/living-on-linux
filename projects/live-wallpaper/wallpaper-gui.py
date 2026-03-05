#!/usr/bin/python3
"""
Live Wallpaper GUI Controller
Simple Tkinter application for managing xwinwrap + mpv live wallpaper
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import os
import sys
import threading
import time
from pathlib import Path

class WallpaperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Wallpaper Controller")
        self.root.geometry("500x600")
        self.root.resizable(True, True)
        
        # Configuration paths
        self.wallpaper_dir = Path.home() / ".local" / "wallpaper"
        self.scripts_dir = self.wallpaper_dir / "scripts"
        self.videos_dir = self.wallpaper_dir / "videos"
        self.shaders_dir = self.wallpaper_dir / "shaders"
        
        # State variables
        self.wallpaper_running = False
        self.current_video = ""
        self.current_shader = ""
        self.use_shader = tk.BooleanVar(value=False)
        self.autostart_enabled = tk.BooleanVar(value=False)
        
        # Setup UI
        self.setup_ui()
        self.check_initial_state()
        
    def setup_ui(self):
        """Setup the main GUI interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Live Wallpaper Controller", 
                               font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Video Selection
        ttk.Label(main_frame, text="Video File:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        video_frame = ttk.Frame(main_frame)
        video_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.video_entry = ttk.Entry(video_frame, width=50)
        self.video_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        browse_video_btn = ttk.Button(video_frame, text="Browse", command=self.browse_video)
        browse_video_btn.grid(row=0, column=1)
        
        # Shader Selection
        ttk.Label(main_frame, text="Shader File (Optional):").grid(row=3, column=0, sticky=tk.W, pady=5)
        
        shader_frame = ttk.Frame(main_frame)
        shader_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.shader_entry = ttk.Entry(shader_frame, width=50, state='disabled')
        self.shader_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        
        self.shader_checkbox = ttk.Checkbutton(shader_frame, text="Use Shader", 
                                              variable=self.use_shader, 
                                              command=self.toggle_shader_ui)
        self.shader_checkbox.grid(row=0, column=1)
        
        browse_shader_btn = ttk.Button(shader_frame, text="Browse", command=self.browse_shader, state='disabled')
        browse_shader_btn.grid(row=0, column=2)
        self.browse_shader_btn = browse_shader_btn
        
        # Controls Frame
        controls_frame = ttk.LabelFrame(main_frame, text="Controls", padding="10")
        controls_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=20)
        
        # Status Label
        self.status_label = ttk.Label(controls_frame, text="Status: Not Running", 
                                     font=("Helvetica", 10, "italic"))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        
        # Control Buttons
        self.start_btn = ttk.Button(controls_frame, text="Start Wallpaper", 
                                   command=self.start_wallpaper, style='Accent.TButton')
        self.start_btn.grid(row=1, column=0, padx=5, pady=5)
        
        self.stop_btn = ttk.Button(controls_frame, text="Stop Wallpaper", 
                                  command=self.stop_wallpaper, state='disabled')
        self.stop_btn.grid(row=1, column=1, padx=5, pady=5)
        
        self.restart_btn = ttk.Button(controls_frame, text="Restart", 
                                     command=self.restart_wallpaper, state='disabled')
        self.restart_btn.grid(row=1, column=2, padx=5, pady=5)
        
        # Settings Frame
        settings_frame = ttk.LabelFrame(main_frame, text="Settings", padding="10")
        settings_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        autostart_check = ttk.Checkbutton(settings_frame, text="Autostart on Login", 
                                         variable=self.autostart_enabled, 
                                         command=self.toggle_autostart)
        autostart_check.grid(row=0, column=0, sticky=tk.W)
        
        # Info Frame
        info_frame = ttk.LabelFrame(main_frame, text="Information", padding="10")
        info_frame.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        info_text = tk.Text(info_frame, height=6, width=60, wrap=tk.WORD, state='disabled')
        info_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Make frames expand properly
        main_frame.columnconfigure(0, weight=1)
        video_frame.columnconfigure(0, weight=1)
        shader_frame.columnconfigure(0, weight=1)
        controls_frame.columnconfigure(0, weight=1)
        settings_frame.columnconfigure(0, weight=1)
        info_frame.columnconfigure(0, weight=1)
        
        # Set initial info text
        self.set_info_text("Live Wallpaper Controller\n\n"
                          "• Select a video file to use as wallpaper\n"
                          "• Optionally select a GLSL shader for effects\n"
                          "• Use Start/Stop/Restart to control the wallpaper\n"
                          "• Enable autostart for automatic startup")
    
    def set_info_text(self, text):
        """Set the information text in the info box"""
        # Find the text widget by searching through children
        info_text = None
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.LabelFrame):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Text):
                        info_text = child
                        break
                if info_text:
                    break
        
        if info_text:
            info_text.config(state='normal')
            info_text.delete(1.0, tk.END)
            info_text.insert(tk.END, text)
            info_text.config(state='disabled')
        else:
            print("Warning: Could not find info text widget")
    
    def check_initial_state(self):
        """Check initial state and populate fields"""
        # Check if wallpaper is already running
        self.wallpaper_running = self.is_wallpaper_running()
        self.update_status()
        
        # Set default video if exists
        default_video = self.videos_dir / "loop.mp4"
        if default_video.exists():
            self.current_video = str(default_video)
            self.video_entry.insert(0, str(default_video))
        
        # Check autostart status
        self.check_autostart_status()
    
    def is_wallpaper_running(self):
        """Check if wallpaper is currently running"""
        try:
            result = subprocess.run(['pgrep', '-f', 'xwinwrap'], 
                                  capture_output=True, text=True)
            return result.returncode == 0
        except:
            return False
    
    def update_status(self):
        """Update the status display"""
        if self.wallpaper_running:
            self.status_label.config(text="Status: Running", foreground="green")
            self.start_btn.config(state='disabled')
            self.stop_btn.config(state='normal')
            self.restart_btn.config(state='normal')
        else:
            self.status_label.config(text="Status: Not Running", foreground="red")
            self.start_btn.config(state='normal')
            self.stop_btn.config(state='disabled')
            self.restart_btn.config(state='disabled')
    
    def browse_video(self):
        """Open file dialog to select video file"""
        file_path = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[("Video files", "*.mp4 *.avi *.mkv *.webm *.mov"),
                      ("All files", "*.*")]
        )
        if file_path:
            self.current_video = file_path
            self.video_entry.delete(0, tk.END)
            self.video_entry.insert(0, file_path)
    
    def browse_shader(self):
        """Open file dialog to select shader file"""
        file_path = filedialog.askopenfilename(
            title="Select Shader File",
            filetypes=[("GLSL files", "*.glsl"), ("All files", "*.*")]
        )
        if file_path:
            self.current_shader = file_path
            self.shader_entry.delete(0, tk.END)
            self.shader_entry.insert(0, file_path)
    
    def toggle_shader_ui(self):
        """Enable/disable shader UI elements"""
        if self.use_shader.get():
            self.shader_entry.config(state='normal')
            self.browse_shader_btn.config(state='normal')
        else:
            self.shader_entry.config(state='disabled')
            self.browse_shader_btn.config(state='disabled')
    
    def start_wallpaper(self):
        """Start the live wallpaper"""
        if not self.current_video:
            messagebox.showwarning("Warning", "Please select a video file first!")
            return
        
        if not Path(self.current_video).exists():
            messagebox.showerror("Error", "Selected video file does not exist!")
            return
        
        # Build the command
        script_path = self.scripts_dir / "start-wallpaper-shader.sh"
        if not script_path.exists():
            script_path = self.scripts_dir / "start-wallpaper.sh"
        
        if not script_path.exists():
            messagebox.showerror("Error", "Wallpaper scripts not found. Please run setup-live-wallpaper.sh first!")
            return
        
        # Update the script with current selections
        self.update_script_with_selections()
        
        # Start wallpaper in background thread
        threading.Thread(target=self.run_wallpaper, daemon=True).start()
        
        # Update status
        self.wallpaper_running = True
        self.update_status()
        
        messagebox.showinfo("Success", "Wallpaper started successfully!")
    
    def stop_wallpaper(self):
        """Stop the live wallpaper"""
        try:
            subprocess.run(['pkill', '-f', 'xwinwrap'], check=True)
            self.wallpaper_running = False
            self.update_status()
            messagebox.showinfo("Success", "Wallpaper stopped!")
        except subprocess.CalledProcessError:
            messagebox.showwarning("Warning", "Could not stop wallpaper. It may have already stopped.")
    
    def restart_wallpaper(self):
        """Restart the live wallpaper"""
        self.stop_wallpaper()
        time.sleep(1)  # Wait a moment
        self.start_wallpaper()
    
    def update_script_with_selections(self):
        """Update the wallpaper script with current video and shader selections"""
        # This would modify the script to use the selected files
        # For now, we'll use environment variables or command line arguments
        pass
    
    def toggle_autostart(self):
        """Toggle autostart functionality"""
        script_path = self.scripts_dir / ("enable-autostart.sh" if self.autostart_enabled.get() 
                                         else "disable-autostart.sh")
        
        if script_path.exists():
            try:
                subprocess.run([str(script_path)], check=True)
                status = "enabled" if self.autostart_enabled.get() else "disabled"
                messagebox.showinfo("Success", f"Autostart {status}!")
            except subprocess.CalledProcessError:
                messagebox.showerror("Error", f"Failed to {'enable' if self.autostart_enabled.get() else 'disable'} autostart!")
        else:
            messagebox.showerror("Error", "Autostart scripts not found. Please run setup-live-wallpaper.sh first!")
    
    def check_autostart_status(self):
        """Check if autostart is currently enabled"""
        autostart_file = Path.home() / ".config" / "autostart" / "live-wallpaper.desktop"
        if autostart_file.exists():
            # Check if the file is executable (enabled)
            self.autostart_enabled.set(os.access(autostart_file, os.X_OK))
    
    def run_wallpaper(self):
        """Run the wallpaper script in background"""
        try:
            # Use the enhanced script with shader support
            script_path = self.scripts_dir / "start-wallpaper-shader.sh"
            
            # Set environment variables for the script
            env = os.environ.copy()
            env['WALLPAPER_VIDEO'] = self.current_video
            if self.use_shader.get() and self.current_shader:
                env['WALLPAPER_SHADER'] = self.current_shader
            
            subprocess.run([str(script_path)], env=env, check=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start wallpaper: {str(e)}")
            self.wallpaper_running = False
            self.update_status()

def main():
    """Main entry point"""
    # Check if required directories exist
    wallpaper_dir = Path.home() / ".local" / "wallpaper"
    scripts_dir = wallpaper_dir / "scripts"
    
    if not scripts_dir.exists():
        response = messagebox.askyesno("Setup Required", 
                                      "Wallpaper scripts not found. Would you like to run the setup script first?")
        if response:
            try:
                subprocess.run([str(Path(__file__).parent / "setup-live-wallpaper.sh")], check=True)
            except Exception as e:
                messagebox.showerror("Error", f"Setup failed: {str(e)}")
                return
    
    # Create and run GUI
    root = tk.Tk()
    app = WallpaperGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()