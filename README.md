* HAS UNFIXED BUGS *

======================================
Phishing Detection Using Random Forest
======================================



Detect phishing websites using machine learning

cross checking function -> compare_with_google can be used to cross check the results of the model.

usage : 

    detect:
        from phishing_detection import phishing_detection
        print(phishing_detection.detect('google.com'))
        
    compare_with_google:
        url=<some url>
        api=<your google cloud console api key>
        
        print(compare_with_google(url,api))
        

* Free software: MIT license
* Documentation: https://phishing-detection.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
