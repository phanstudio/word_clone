# README for Note Rendering System

## Overview
This project is a **Note Rendering System** built using **Python** and **Flet** framework. It allows dynamic formatting and rendering of styled text within a custom text editor. The core features include:
- Handling of styled text using properties like **bold** and **italic**.
- Efficient management of text positions and properties.
- An adaptive rendering system that reflects changes in text formatting and content in real-time.

## Key Components

### `Renderer` Class
The `Renderer` class extends the `ft.Column` class and serves as the main text rendering engine. It is responsible for managing the text input, applying styles, and updating the display based on user interaction.

- **Attributes**:
  - `ST`: The string being rendered and edited.
  - `NT`: A list of positions in the text, marking the start of different text segments.
  - `PT`: A list of `PropT` instances, defining the style (bold, italic, etc.) for each segment.
  - `temp_prop`: A temporary style property that is applied to newly added text segments.
  
- **Key Methods**:
  - `render()`: Renders the text using the stored positions and properties.
  - `correct_overlap()`: Ensures no text segments overlap when styled text is inserted or deleted.
  - `loader()`: A sample loader method to pre-fill the editor with some initial text for testing purposes.
  - `save_property(_pos)`: Saves the current text properties at a given position.

### `simple_button` Class
A utility class for creating customizable buttons with icons or images. These buttons are used in the format panel to apply styling like bold and italic.

- **Attributes**:
  - `custom_data`: The data associated with the button (e.g., bold, italic).
  - `icon` / `img`: The icon or image displayed on the button.
  
- **Method**:
  - `build()`: Builds the button to be displayed in the user interface.

### `format_panel` Class
The format panel contains buttons for applying text styles such as bold and italic. It interacts with the `Renderer` to apply formatting to the selected text.

- **Methods**:
  - `onclick(typ)`: Toggles the bold or italic style based on the button clicked.
  - `_render_properties()`: Updates the format panel to reflect the current styles applied to the text.

### `Notes` Class
A container for the rendered text. This class stores the formatted text and displays it using Flet’s `Text` control.

- **Methods**:
  - `set(_value)`: Sets the text spans to be displayed.
  - `get()`: Retrieves the current text spans.

### `Editor` Class
The `Editor` class manages the input field where users type the text. It detects changes and interacts with the `Renderer` to apply updates in real-time.

- **Methods**:
  - `_onchange()`: Handles the change event when the user modifies the text. It detects the differences from the previous state and updates the `Renderer`.

## Main Functionalities

### Text Styling
The system supports basic text formatting such as:
- **Bold**: Applied via the bold button in the `format_panel`.
- **Italic**: Applied via the italic button in the `format_panel`.

### Real-time Rendering
The text is dynamically rendered as the user types, with styling applied based on the `PropT` properties.

### Overlap Correction
The `Renderer` automatically corrects overlapping or redundant text segments, ensuring that the formatting is applied smoothly.

### Text History and Changes
The system tracks changes to the text, such as insertions, deletions, and replacements. These changes are processed using methods like `nhistory()` and `find_differences()`.

## Installation

1. Install the dependencies using pip:
    ```bash
    pip install flet
    pip install Levenshtein
    ```

2. Import the required modules:
    ```python
    from .note_render import *
    ```

3. Initialize the `Renderer` and integrate it into your UI:
    ```python
    engine = Renderer(parent)
    ```

## Usage Example
```python
renderer = Renderer(_parent=your_parent_object)
renderer.loader()  # Preload some sample data
renderer.render()  # Render the initial text
```

## License
This project is open-source and free to use under the MIT License.

