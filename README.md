# Demo MsWord Clone
An ms word clone in this read me i explain each aspect of the program

# Table of content
[readme for edit view](#readme for Edit Note View)

To run the app:
```
flet run
```
# README for Edit Note View
## Overview
The **EditNoteView** class is part of a note-taking application built using the **Flet** framework. It provides a user interface for editing and formatting text, with a toolbar for applying text styles and an editor to capture user input. The view is designed for users to create and modify notes with ease, while supporting functionalities like text formatting, saving, and more.

## Key Components

### `EditNoteView` Class
`EditNoteView` extends the `ft.Column` class and serves as the main view for creating and editing notes. It contains a toolbar for formatting options, an editor for text input, and a header for saving or naming notes.

- **Attributes**:
  - `head`: Default title for the note, initialized as `'Untitled Note'`.
  - `tool_bar`: A toolbar with formatting buttons like bold and italic.
  - `editor`: The text editor where users input and format their notes.
  - `render_engine`: An instance of the `Renderer` class that handles text rendering and formatting.

- **Key Methods**:
  - `header()`: Creates a header row with a save button, a note title input, and a help button.
  - `onback()`: A placeholder for handling the "back" event when implemented.

### UI Components

#### Header
The header consists of:
- **Save Button**: A button represented by a save icon, which will allow users to save their notes.
- **Note Title Input**: A text field where users can input or modify the note's title. By default, it shows "Untitled Note".
- **Help Button**: A button that displays a help icon and can trigger additional functionality (currently set to print a message when clicked).

#### Toolbar
The toolbar (`tool_bar`) provides options for text formatting such as bold, italic, and other styles, allowing users to format their text.

#### Editor
The editor (`editor`) is where users can type and see their notes. It interacts with the `Renderer` class to apply formatting and render the text.

### Integrations
- **Renderer**: The `Renderer` class handles the logic for rendering formatted text. It interacts with the editor and the format panel, applying the necessary styles as users modify the text.
- **Format Panel**: The format panel provides options like bold, italic, etc., to format the selected text.

## Installation

1. **Install Flet Framework**:
    ```bash
    pip install flet
    ```

2. **Import the Required Modules**:
    Ensure the `Renderer`, `Editor`, and `format_panel` components are available from the main project folder:
    ```python
    from .note_render import Renderer, Editor, format_panel
    from .constants import *
    from .utility import *
    ```

## Example Usage

```python
# Create an instance of the note editing view
note_view = EditNoteView()

# Set it up in your Flet page or UI
page.controls.append(note_view)
```

## Customization

- **Note Title**: Users can modify the title of the note using the input field in the header.
- **Text Formatting**: The toolbar provides buttons for formatting the text in the editor. This includes options like bold and italic, which are handled by the `Renderer` and `format_panel`.
- **Save Functionality**: The save button is designed to trigger saving functionality. You can implement the save logic inside the `on_click` event handler of the save button.

## Features to Add
- **Save and Load**: Implement saving and loading notes functionality, possibly using file storage or a database.
- **Help Button Action**: Customize the help button to display instructions or guide the user.
- **Back Button**: Add navigation functionality using the `onback()` method.

## License
This project is open-source and free to use under the MIT License.
