# vrc-osc-immersion

Tooling to make VRC more immersive by adding input triggers on the client side to trigger sounds or physical objects to signal contact, such as hair or ears ruffled or tail touched/pulled.

This is very much a WIP! Hit up the releases tab for a known working version. You need to install the requirements from requirements.txt (best done by creating a virtualenv/conda, activating it, then `pip install -r requirements.txt` because I haven't done a pyproject.toml yet but it will get converted eventually!)

Currently, to use this:

1. Add VRC Contact Receivers to your ears, with the variable labeled Touch_Ear_L and Touch_Ear_R for appropriate ears.
2. Navigate to `%USERPROFILE%\AppData\LocalLow\VRChat\VRChat\OSC\` and open the user folder for your user ID (can find visiting your own profile at [vrchat.com/home](https://vrchat.com/home/) if need be), and in Avatars, either delete the appropriate `avtr_abcdef.json` file with your avatar's blueprint ID (can find this as well in Unity) and either delete the file, or if custom already, edit it to add an Output entry like so:
```
    {
      "name": "Touch_Ear_L",
      "output": {
        "address": "/avatar/parameters/Touch_Ear_L",
        "type": "Bool"
      }
    },
    {
      "name": "Touch_Ear_R",
      "output": {
        "address": "/avatar/parameters/Touch_Ear_R",
        "type": "Bool"
      }
    },
```
3. After re-building and re-uploading your avatar, launch `main.py` first and then run VR Chat.