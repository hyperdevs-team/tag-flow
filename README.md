# tag-flow

This script is intended to continuosly create tags according to the [semantic versioning specs](http://semver.org/) in the current head of a git repo. This script only increments the PATCH of the previously tagged version, to increment the MAJOR or MINOR number it is necessary to manually create a tag or use one of the arguments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisities

Python 2.7+

### Installing

- Tag the first representative commit of your repo to start the "flow" (e.g. v1.0.0)
- Copy tag.py in your project or add it as a submodule:
```
git submodule add git@github.com:bq/tag-flow.git
```
- Inside the repo, use one of these:
```
python tag-flow/tag.py
python tag-flow/tag.py bump-minor
python tag-flow/tag.py bump-major
```

## Samples

### Increment patch
```
# python tag-flow/tag.py
Creating new tag: v1.0.45 (previous tag for branch: v1.0.44)
```

### Increment minor
```
# python tag-flow/tag.py bump-minor
Creating new tag: v1.1.0 (previous tag for branch: v1.0.44)
```

### Increment major
```
# python tag-flow/tag.py bump-major
Creating new tag: v2.0.0 (previous tag for branch: v1.0.44)
```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/bq/tag-flow/tags). 

## Authors

* **[Sebastián Varela](https://github.com/sebastianvarela)** - *Initial work* 
* **[Iván Martinez](https://github.com/imartinez)** - *Initial work*
* **[Adrián García](https://github.com/adriangl)** - *Special contributor*

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
