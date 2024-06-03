# Frame extractor from YouTube URLs

- Initiate a [virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/):

```
python -m venv extract-frames-env
source extract-frames-env/Scripts/activate
```

- Install the dependencies: `pip install -r requirements.txt`

- Create a file `yt-videos.csv` with the set of URLs you want to extract. See `yt-videos.example.csv`.

- Execute the script: `python extract_frames.py`

- The frames will be generated in `/frames`
