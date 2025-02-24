---
title: CodeSnippetBot
emoji: 💬
colorFrom: yellow
colorTo: purple
sdk: gradio
sdk_version: 5.16.2
app_file: app.py
pinned: false
license: apache-2.0
---

# CodeSnippetBot: Your Personal Code Snippet Manager

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/canstralian/CodeSnippetBot)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![CI](https://github.com/canstralian/CodeSnippetBot/actions/workflows/ci.yml/badge.svg)](https://github.com/canstralian/CodeSnippetBot/actions)

Tired of losing track of those valuable code snippets? CodeSnippetBot is here to rescue you! This Telegram bot acts as your personal code snippet manager, allowing you to easily save, organize, search, and share your code snippets.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributing](#contributing)
- [Future Enhancements](#future-enhancements)
- [Author](#author)
- [License](#license)
- [Contact](#contact)

---

## Features

* **Save Snippets:** Save code snippets with a description/title and the programming language. CodeSnippetBot intelligently tags your snippets for easy searching.
* **Organize Snippets:** Organize your snippets using categories, folders, or custom tags. Keep your code library clean and accessible.
* **Search Snippets:** Quickly find the snippets you need by searching by language, keywords in the description, or even within the code itself.
* **Share Snippets:** Share your code snippets with other Telegram users or groups. Collaborate seamlessly with your team.
* **Syntax Highlighting:** Beautifully formatted code display with syntax highlighting for various programming languages.
* **Easy Copying:** One-click copy to clipboard functionality for quick access to your code.
* **Public/Private Snippets:** Control the visibility of your snippets. Keep some private for personal use and share others with the community.
* **Intuitive Commands:** Simple and easy-to-remember bot commands.
* **Inline Queries:** Search for snippets directly from the chat input.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/canstralian/CodeSnippetBot.git
cd CodeSnippetBot
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root with your configuration settings:

```dotenv
TELEGRAM_API_TOKEN=your_telegram_api_token_here
```

---

## Usage

Interact with the bot in Telegram using the following commands:

- **`/start`**: Start the bot and receive a welcome message.
- **`/help`**: Display a list of available commands and their usage.
- **`/save <language> <description> <code>`**: Save a new snippet.  
  _Example_: `/save python "Quick sort algorithm" def quicksort(arr): ...`
- **`/find <language> <keywords>`**: Search for snippets.  
  _Example_: `/find python "sorting algorithm"`
- **`/list`**: List all your saved snippets.
- **`/view <snippet_id>`**: View a specific snippet (retrieve the snippet ID from `/list`).
- **`/delete <snippet_id>`**: Delete a snippet.
- **`/edit <snippet_id>`**: Edit a snippet.
- **`/share <snippet_id> <user/group>`**: Share a snippet with a Telegram user or group.

### How to Use the Bot

1. Search for **CodeSnippetBot** on Telegram or use its username.
2. Start a chat with the bot.
3. Use the `/start` command to begin.
4. Follow the instructions and use the commands to manage your code snippets.

---

## Configuration

- **Environment Variables:** Securely store sensitive data like API tokens using environment variables (e.g., via a `.env` file).
- **Configuration Files:** For non-sensitive settings, consider using a configuration file (e.g., `config.ini` or `config.yaml`).

---

## Testing

Run unit tests to ensure everything works as expected:

```bash
pytest --maxfail=1 --disable-warnings -q
```

A CI pipeline is set up via GitHub Actions to automatically run tests on each push or pull request. See [`.github/workflows/ci.yml`](.github/workflows/ci.yml) for details.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes and push your branch.
4. Open a pull request describing your changes.

Be sure to follow our coding standards using tools like `flake8` and `black` for code quality. For more details, refer to our [CONTRIBUTING.md](CONTRIBUTING.md) if available.

---

## Future Enhancements

- **Snippet Versioning:** Track changes to your snippets over time.
- **GitHub Gist Integration:** Import/export snippets seamlessly.
- **Public Snippet Library:** Share your code with the broader community.
- **Code Execution:** Enable sandboxed execution of code snippets.

---

## Author

Canstralian

---

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## Contact

For questions or suggestions, please open an [issue](https://github.com/canstralian/CodeSnippetBot/issues) or contact the maintainer directly.
