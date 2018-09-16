Why is reStructuredText the right solution?
===========================================
Markdown is simpler, easier and the basic standard in GitHub but Markdown does not allow to generate PDF.

Instead, reStructuredText allows to generate a HTML bundle or a downloadable PDF directly from the built in the Read The Doc repository.

Also, reStructuredText is more flexible and extensible what can be a good point for larger techincal documentations.

Limitations
===========
Related links to a different files have to be done like this

.. codee::
See `readthedocs`_ documentation to get all the information.

.. _readthedocs: readthedocs.rst


Links using:
```
:doc:`Link <link>`

```
