"""
GIF Generator
"""

import io
from PIL import Image
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter

# 1. Customize your Python program inside this string
CODE_TO_TYPE = """from typing import Dict, List


class Engineer:
    def __init__(self) -> None:
        self.identity: Dict[str, str] = {
            "title": "Assistant Vice President",
            "role": "Senior Software Engineer",
            "specialty": "Large-Scale Cloud & Big Data Platforms",
            "current_form": "Ultra Instinct Engineer"
        }
        self.training_ground: Dict[str, List[str]] = {
            "hyperbolic_time_chamber": ["Databricks", "Snowflake", "Apache Airflow"],  # Currently Mastering
            "passions": ["Cloud Architecture", "GenAI", "Wilderness Exploration"]
        }

    def power_up(self) -> str:
        return f"⚡ {self.identity['title']} | {self.identity['role']} ⚡"

if __name__ == "__main__":
    dev = Engineer()
    print(dev.power_up())"""

frames = []
current_text = ""

print("Generating clean Dracula animation frames...")

# Official Dracula Theme Colors
DRACULA_BACKGROUND_HEX = "#282a36"
DRACULA_BACKGROUND_RGB = (40, 42, 54)
DRACULA_MUTED_GRAY_HEX = "#6272a4"

# 2. Extract code character-by-character to simulate typing
for char in CODE_TO_TYPE:
    current_text += char
    
    # Configure ImageFormatter to remove the default line background values
    img_data = highlight(
        current_text, 
        PythonLexer(), 
        ImageFormatter(
            font_size=16, 
            style="dracula",
            line_numbers=True,
            line_number_bg=DRACULA_BACKGROUND_HEX,  # Removes yellow background strip
            line_number_fg=DRACULA_MUTED_GRAY_HEX,  # Clean muted gray text numbers
            line_number_pad=8
        )
    )
    
    # Load into memory as an image frame
    packet = io.BytesIO(img_data)
    frame = Image.open(packet).convert("RGB")
    frames.append(frame)

print(f"Generated {len(frames)} frames for the typing animation.")

# 3. Create a standardized background container matching Dracula's dark theme
max_w = max(f.width for f in frames) + 40
max_h = max(f.height for f in frames) + 40

final_frames = []
for f in frames:
    canvas = Image.new("RGB", (max_w, max_h), color=DRACULA_BACKGROUND_RGB) 
    canvas.paste(f, (20, 20))
    final_frames.append(canvas)

# Add a pause at the very end so viewers can read the final script execution
for _ in range(20):
    final_frames.append(final_frames[-1])

# 4. FIX: Call .save() on the first Image OBJECT, not the list wrapper itself
if final_frames:
    first_frame = final_frames[0]
    first_frame.save(
        "typing_code_dracula_clean.gif",
        save_all=True,
        append_images=final_frames[1:],  # Appends the remaining frames here
        duration=50,  
        loop=0        
    )
    print("Success! 'typing_code_dracula_clean.gif' has been created.")
else:
    print("Error: No frames were generated. Check your code string.")
