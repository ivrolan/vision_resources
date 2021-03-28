# Vision Resources

[here](http://ycb-benchmarks.s3-website-us-east-1.amazonaws.com/), you can find the dataset images provided by the organization

## add_prefix.sh

This script can be used for adding a prefix name to some files. For example, you will want to do this if you hace two folder with images of different object classes and these images have the same names.

For example:
```
$ ls mydir
    file1
    file1
$ ./add_prefix.sh mydir my_prefix
$ ls mydir
    my_prefixfile1
    my_prefixfile2
```

### Usage:

```
$ ./add_prefix.sh path_to_folder prefix_name
```

## create_labelme_json.py

The script takes 2 arguments, the path to a folder and the name of the label to use in every json. The folder must contain:

- `masks` folder containing `.pbm` files (it can contain more than the masks that will be used)
- `.jpg` files to classify in a labelme json

It will generate as `.json` files as `.jpg` in the folder. The masks in the masks folder must be named the same as its corresponding images and followed by `_mask.pbm`.
> If we have `pepito.jpg` in the folder, the masks folder must contain a `pepito_mask.pbm` file. 


For example:

```
$ python3 create_labelme_json.py path_to_folder 'label to use'
```