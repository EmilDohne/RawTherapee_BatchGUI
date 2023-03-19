# RawTherapee Batch processor

This documentation aims to extend the tooltips that can be found when hovering above the fields, below you can find a preview which shows all the relevant fields which get described here

![GUI Preview](/docs/GUI_Main.png?raw=True)

## Input Directory

This defines the input directory to crawl for subfolders that contain RAW image data, this can be a root directory such that the data is stored in subfolders as seen below
```
/HDRIs_IN
    |_ /HDRI_01
        |_ IMG_0001.<RawFormat>
        |_ IMG_****.<RawFormat>
    |_ /HDRI_02
        |_ IMG_1001.<RawFormat>
        |_ IMG_****.<RawFormat>
    |_ /HDRI_**
```

## Output Directory

This defines the folder to output the processed image data to, it will mirror the names of the input folders and recreate that structure, continuing with the example from before the output folder would then look something like this

```
/HDRIs_OUT
    |_ /HDRI_01
        |_ IMG_0001.tiff
        |_ IMG_****.tiff
    |_ /HDRI_02
        |_ IMG_1001.tiff
        |_ IMG_****.tiff
    |_ /HDRI_**
```
### Create Subfolder

This option will output an image to a nested folder such that:
```
/HDRIs_OUT
    |_ /HDRI_01
        |_ /HDRI_01
            |_ IMG_0001.tiff
            |_ IMG_****.tiff
```

This can be useful if one wants to stitch the images later and create relevant session and output files detached from the image data

```
/HDRIs_OUT
    |_ /HDRI_01
        |_ /HDRI_01
            |_ IMG_0001.tiff
            |_ IMG_****.tiff
        |_ HDRI_01_Stitched.*
        |_ HDRI_01.EXR
        |_ HDRI_01.jpg
        
```

## Processing Profile

This specifies the processing file (*.pp3) to be used for the processing of the images. If this is empty or an invalid path it will revert to the defaults of RawTherapee

## Raw File Format

This will filter which folders get considered based on their extension. E.g., if you have it set to filter based on **CR2** files it will only create an output for /HDRI_01

```
/HDRIs_IN
    |_ /HDRI_01
        |_ IMG_0001.CR2
        |_ IMG_****.CR2
    |_ /HDRI_02
        |_ IMG_1001.IIQ
        |_ IMG_****.IIQ
```

**This does however not filter which files get processed in the end.** This means that if there is an **IIQ** File in the same directory that file will get processed too!

```
/HDRIs_IN
    |_ /HDRI_01
        |_ IMG_0001.CR2
        |_ IMG_0001.IIQ
        |_ IMG_****.CR2
    |_ /HDRI_02
        |_ IMG_1001.IIQ
        |_ IMG_****.IIQ
```