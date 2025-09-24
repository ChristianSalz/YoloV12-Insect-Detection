# Installation Instructions (Mac)

## 1. Install Homebrew (if not already installed)

Open Terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Verify installation:

```bash
brew --version
```

2. Install Python 3.13 via Homebrew

```bash
brew install python@3.13
```
Make sure your shell uses the correct version:

```bash
brew link python@3.13 --force --overwrite
python3 --version
```

3. Navigate to the Project Folder

```bash
cd /path/to/YoloV12-Insect-Detection
```

4. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate the virtual environment:
```bash
source .venv/bin/activate
```
5. Install Project Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```


