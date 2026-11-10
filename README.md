# Backup Scheduler

A small Python script that automatically backs up a file or a folder every 15 seconds. Each backup gets a timestamp in its name, so older backups are never overwritten.

This is a learning project.

## Requirements

- Python 3.8 or newer
- The `schedule` package

```
pip install -r requirements.txt
```

## Usage

```
python backup_scheduler.py
```

The script asks you what to do:

```
Back up a file (1) or a folder (2)? 2
Enter the path of the folder to back up: my_project
Enter the folder to save backups in: backups
Backup running. Press Ctrl+C to stop.
Backed up to backups/10-11-2026_18-44-00_my_project
```

Press `Ctrl+C` to stop.

## What it does

- **File mode:** copies one file into a backup folder, with a timestamp in front of the file name.
- **Folder mode:** copies a whole folder into a new timestamped folder.
- Checks your input at the start (empty answers, missing paths).
- Refuses to put the backup folder inside the folder being backed up.
- If a backup fails, it prints the error and tries again on the next run instead of crashing.

## Known limitations

- Old backups are never deleted, so they pile up and use disk space.
- Folder mode copies everything on every run (no incremental backups).
- Copies are not verified after writing.
- The timestamp format is `day-month-year`, so file lists do not sort in time order.
- The "backup folder inside source folder" check is simple and can wrongly reject folders with similar names (for example `proj` and `proj_backup`).
- Symbolic links are not handled specially.

## Possible improvements

- Delete old backups automatically (keep the newest N).
- Verify copies with file hashes.
- Command-line arguments instead of typed prompts.
- Incremental backups.
