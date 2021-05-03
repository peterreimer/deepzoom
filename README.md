# deepzoom: Python Deep Zoom Tools

## Installation

    git clone https://github.com/peterreimer/deepzoom.git
    cd deepzoom
    python setup.py install


## Dependencies

- works only with EOL Python 2
- [Pillow, the fork of PIL (the Python Image Library)][pillow]


## Acknowledgements

Initially developed by [Kapil Thangavelu](mailto:kapil.foss@gmail.com).
Powered by [OpenZoom][].

## License

Licensed under the [New BSD Licence][bsd].

## Changelog

### Verson 1.1.0 - December 5, 2012

  - no new functionality, just  cleaning up, switching from distutils to
    setup tools adding myself to copyrights

### Version 1.0.0 – October 6, 2011

  - Added workaround for [IIP][] bug that causes it to serve low-level tiles
    with wrong dimensions.
  - Added `DeepZoomCollection.remove` and `DeepZoomImageDescriptor.remove`
    class methods for removing descriptors and their corresponding tiles
    folders.

### Version 0.9.4 – September 9, 2011

  - Added sample image and made example script executable.
  - Added instructions for installing PIL.

### Version 0.9 – November 14, 2010

  - Fixed issue #1: Bug in the tile saving in ImageCreator.create.
  - Set `CollectionCreator` `max_level` default to `7`.
  - Set `CollectionCreator` `tile_size` default to `256`.

### Version 0.1.2 – May 24, 2009

  - Renamed `DZIDescriptor` to `DeepZoomImageDescriptor` for
    consistency with the OpenZoom SDK descriptor framework.

###  Version 0.1.1 – April 8, 2009

  - Removed unnecessary `urllib2` import.
  - Added description of dependencies.


### Version 0.1.0 – March 23, 2009

  - First release. Nothing is new, or everything is new,
    depending on how you think about it. -- *Google*


[bsd]: http://www.opensource.org/licenses/bsd-license.php
[pillow]: https://python-pillow.org/
[openzoom]: http://openzoom.org
[iip]: http://iipimage.sourceforge.net/
