Version 1.7.2
=============

The library has been tested using Agda 2.6.3.

* In accordance with changes to the flags in Agda 2.6.3, all modules that previously used
  the `--without-K` flag now use the `--cubical-compatible` flag instead.
  
* Updated the code using `primFloatToWord64` - the library API has remained unchanged.
