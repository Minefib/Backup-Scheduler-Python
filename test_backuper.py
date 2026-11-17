import os
from backuper import backup_file, backup_dir


def test_backup_file(tmp_path):
    src = tmp_path / "note.txt"
    src.write_text("hello world")

    dest = tmp_path / "backups"
    dest.mkdir()

    result = backup_file(str(src), str(dest))
    assert os.path.isfile(result)
    with open(result) as f:
        assert f.read() == "hello world" 
def test_backup_folder(tmp_path):
    src = tmp_path / "folder"
    src.mkdir()
    (src / "a.txt").write_text("hello")

    dest = tmp_path / "backups"
    dest.mkdir()

    result = backup_dir(str(src), str(dest))
    assert os.path.isdir(result)
    copied = os.path.join(result, "a.txt")
    assert os.path.isfile(copied)
    with open(copied) as f:
        assert f.read() == "hello"
def test_backup_file_missing(tmp_path):
    dest = tmp_path / "backups"
    dest.mkdir()
    assert os.path.isdir(dest)
    with pytest.raises(OSError):
        backup_file(str(tmp_path / "nope.txt"), str(dest))