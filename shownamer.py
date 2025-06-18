import os
import re
import requests
import argparse

# Default supported video extensions
DEFAULT_EXTENSIONS = [".mkv", ".mp4", ".avi", ".mov", ".flv"]

# Regex to parse filename
FILENAME_PATTERN = re.compile(
    r"^(?P<show>.+?)\s+[Ss](?P<season>\d{2})[Ee](?P<episode>\d{2})"
)

# Characters not allowed in filenames
INVALID_CHARS = r'\/:*?"<>|'


def sanitize_filename(name):
    """Remove or replace characters that are not allowed in filenames."""
    return ''.join(c if c not in INVALID_CHARS else '_' for c in name)


def get_episode_title(show_name, season, episode):
    """Query TVmaze API for the episode title."""
    response = requests.get(
        "https://api.tvmaze.com/singlesearch/shows", params={"q": show_name}
    )
    if response.status_code != 200:
        return None
    show_data = response.json()
    show_id = show_data["id"]

    episode_response = requests.get(
        f"https://api.tvmaze.com/shows/{show_id}/episodebynumber",
        params={"season": season, "number": episode},
    )
    if episode_response.status_code != 200:
        return None
    return episode_response.json()["name"]


def rename_files(directory, extensions, dry_run=False, verbose=False):
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() not in extensions:
            continue

        match = FILENAME_PATTERN.match(name)
        if not match:
            if verbose:
                print(f"[skip] {filename}: doesn't match expected pattern")
            continue

        show = match.group("show").strip()
        season = int(match.group("season"))
        episode = int(match.group("episode"))

        episode_title = get_episode_title(show, season, episode)
        if not episode_title:
            print(f"[fail] {filename}: could not fetch episode title")
            continue

        safe_title = sanitize_filename(episode_title)
        new_filename = f"{show} S{season:02}E{episode:02} - {safe_title}{ext}"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_filename)

        if dry_run:
            print(f"[dry-run] {filename} → {new_filename}")
        else:
            os.rename(src, dst)
            print(f"[renamed] {filename} → {new_filename}")


def main():
    parser = argparse.ArgumentParser(
        description="Rename TV episode files by fetching episode titles."
    )
    parser.add_argument(
        "--dir",
        default=os.path.dirname(os.path.abspath(__file__)),
        help="Directory containing video files (default: current script dir)",
    )
    parser.add_argument(
        "--ext",
        nargs="*",
        default=DEFAULT_EXTENSIONS,
        help="List of allowed video file extensions (default: common types)",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview renaming without making changes"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Show skipped files and debug info"
    )

    args = parser.parse_args()

    rename_files(
        directory=args.dir,
        extensions=[e.lower() if e.startswith(".") else "." + e.lower() for e in args.ext],
        dry_run=args.dry_run,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    main()