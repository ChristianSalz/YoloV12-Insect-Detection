# Installation Instructions (Mac)

1. Install Homebrew (if not already installed)

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

6. Download the data from The SPoHF-Roboflow-Project and add the Train/Valid/Test folder to your project
   https://app.roboflow.com/spohf-insect-counting/spohf-kur4x-dokg9/models - go to 'versions' (left menu), select the version, then press 'download dataset'. Copy over the content in the project directory.

> **Important note:**  
> YOLOv12 requires that your `train`, `valid`, and `test` folders are inside a `datasets` folder. Optionally, you can modify the `settings.json`.

7. Use the trainTheModel.py file to train a yolo v12 model - Curreltly MPS (Appel Metal) is broken so train on a CPU

8. Run the predictv12.py to test your model PS: update the path to your trained model

# Installation Instructions (Windows)

1. Go and buy a mac
2. Follow steps above

# Installation Instructions (Linux)

You guys are pros, go and figure out yourself
