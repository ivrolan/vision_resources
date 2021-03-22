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