# tag-flow

This script is intended to continuosly create tags according with the [semantic versioning specs](http://semver.org/) in the current head of a git repo. This script only increments the PATCH of the previously tagged version, to increment the MAJOR or MINOR number it is necessary to manually create a tag

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisities

Python 2.7+

### Installing

- Tag the first representative commit of your repo to start the "flow" (e.g. v1.0.0)
- Copy the tag.py or add as submodule:
```
git submodule add git@github.com:bq/tag-flow.git
```
- Inside the repo, use as:
```
tag tag-flow/tag.py
```

Sample output:
```
# python tag-flow/tag.py
Creating new tag: v1.0.45 (previous tag for branch: v1.0.44)
```

## Versioning

We use [SemVer](http://semver.org/) for versioning of course. For the versions available, see the [tags on this repository](https://github.com/bq/tag-flow/tags). 

## Authors

* **Sebastián Varela** - *Initial work* 
* **Iván Martinez** - *Initial work*

See also the list of [contributors](https://github.com/bq/tag-flow/contributors) who participated in this project.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
