# TV Episode Renamer

A lightweight Python CLI tool that renames TV show episode video files by fetching their actual episode titles from [TVmaze](https://www.tvmaze.com/).

---

## 🔧 Features

- Automatically detects and renames files like:
  ```
  Malcolm in the Middle S01E10.mkv
  → Malcolm in the Middle S01E10 - Stock Car Races.mkv
  ```
- Fetches episode titles using the free TVmaze API.
- Cleans illegal filename characters automatically.
- CLI flags for:
  - Custom directory
  - File extension filter
  - Dry-run mode
  - Verbose logging

---

## 🚀 Usage

### 🔨 Requirements

- Python 3.6+
- `requests` module

Install requirements:
```bash
pip install requests
```

### 🏃 Run the script

```bash
python tv_renamer.py
```

### 📁 Example Usage

```bash
# Rename all valid video files in the current directory
python tv_renamer.py

# Specify a custom directory
python tv_renamer.py --dir "/path/to/your/episodes"

# Preview changes without renaming files
python tv_renamer.py --dry-run

# Limit to specific extensions
python tv_renamer.py --ext mkv mp4 avi

# Verbose mode (shows skipped files, debug info)
python tv_renamer.py --verbose
```

---

## 💡 Supported Formats

The script supports the following file name pattern:

```
Show Name S01E01.ext
```

It handles these video formats by default:

- `.mkv`
- `.mp4`
- `.avi`
- `.mov`
- `.flv`

You can customize this with the `--ext` flag.

---

## 🧼 Filename Sanitization

Episode titles fetched from TVmaze may contain characters invalid in filenames (`\ / : * ? " < > |`). These are automatically replaced with underscores (`_`) to ensure cross-platform safety.

---

## 🌐 API Used

- [TVmaze API](https://www.tvmaze.com/api)
  - No authentication required.
  - Fast and reliable for episode metadata.

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋 FAQ

### Will this overwrite existing files?
No. The script does not overwrite files. It renames only when the target filename does not exist. You can use `--dry-run` to preview the result first.

### Can I use it on macOS or Linux?
Yes. It's fully cross-platform. Works wherever Python runs.

### Does it fetch subtitles or cover images?
No. This tool only renames the video files with accurate episode titles.

---

## 🤝 Contributions

Pull requests, suggestions, and issues are welcome! Let's make it smarter and broader (e.g., subtitle renaming, fuzzy matching, show aliases, etc.).
