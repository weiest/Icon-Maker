# Icon Maker
This project is a personal project used to generate icons to be used on the Elgato Stream Deck

## Getting Started
This is a Python Application that takes in images in a folder, adding an icon a little offset from the middle which allows text to be below through the Elgato Stream Deck's Application.

### Prerequisites
Intentioally, this is built for use alongside the Elgato Stream Deck, if you want to modify this for other reasons, go ahead.

### Installing
A step by step series of examples that tell you how to get a development env running

1. Install all the requirements
```
pip install -r requirements.txt
```

2. Add icons into the `input` folder and create an `output` folder.

3. Run the application
```
python main.py
```

All images should be in the output, adjust the code to your own taste.

### Images
Usually I would use transparent `.png` images with black icon, this converts it to white.