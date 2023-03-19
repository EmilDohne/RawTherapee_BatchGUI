# RawTherapee Batch processor

I have recently found myself batch processing a large amount of data for the processing of HDRIs using [RawTherapee](https://www.rawtherapee.com/). While it is possible to batch submit files into the internal queue this becomes rather tedious when dealing with large datasets spread over multiple folders. ***RawTherapee Batch*** aims to simplify this and abstracts away the interaction with *rawtherapee_cli.exe*.

If you are looking to contribute to the codebase please read through [Contributing](#contributing). If you are looking to install the application and use it as is please read [Installation](#installation)

---
![GUI Preview](/docs/GUI_Main.png?raw=True)

---


## Features

- Batch Processing of raw image data using RawTherapee
- Ability to specify a Processing profile (*.pp3)
- Interactive preview of the processing steps
- Ability to filter folders based on whether or not they contain raw data

## Limitations

- The **Raw File Format** Combobox currently only determines what folders get processed by RawTherapee, if there is multiple raw file formats or jpgs they will also get converted. As such please make sure there are no duplicate files in the source directory as this would cause the alphabetically last extension to be used for conversion, e.g. if you have <ins>*IMG_0001.CR2*</ins> and <ins>*IMG_0001.jpg*</ins> in the same directory it will convert <ins>*IMG_0001.jpg*</ins> last and overwriting the previous conversion.For more information please visit the [RawTherapee Documentation](https://rawpedia.rawtherapee.com/Main_Page)
- Currently only supports 16bit uncompressed TIFF export, although adding more options would be rather trivial
- Currently only supports Windows systems

## Contributing

Contributions to this project are highly encouraged and always welcome! If you're looking for a starting point on what to contribute check out the [limitations](#limitations) section.


### Windows
To contribute, please follow these rough guidelines:

1. Create a fork of the repository
2. Clone it locally
3. Set up your virtualenv using 
    ```cmd
    cd <working directory>
    py -m pip install -r requirements.txt
    ```
4. Modify the code to fix a bug or implement a feautre
5. Update this [README.md](README.md)
6. Update the version number in both */main.py* and */main.spec* following [SemVer](https://semver.org/)
7. Build the executable using pyinstaller using
    ```cmd
    py -m PyInstaller main.spec
    ```
8. Create a new release 
9. Publish and create a pull request!


## Installation

The Installation of ***RawTherapee Batch*** is quite straightforward and only requires the latest executable found in the [Releases](/releases/latest) section to be stored somewhere locally and executed.
