===============
Caesar User
===============



Django app to add Keycloak support to Caesar project.


An showcase/demo project is added in the `example folder <example/README.md>`_.

Development
===========

Install development environment:

.. code:: bash

  $ make install-python

------------
Writing docs
------------

Documentation is written using Sphinx and maintained in the docs folder.

To make it easy to write docs Docker support is available.

First build the Docker container:

.. code:: bash

    $ docker build . -f DockerfileDocs -t caesar-user-docs

Run the container

.. code:: bash

    $ docker run -v `pwd`:/src --rm -t -i -p 8050:8050 caesar-user-docs

Go in the browser to http://localhost:8050 and view the documentation which get
refreshed and updated on every update in the documentation source.

--------------
Create release
--------------

.. code:: bash

    $ git checkout master
    $ git pull
    $ bumpversion release
    $ make deploy-pypi
    $ bumpversion --no-tag patch
    $ git push origin master --tags

Release Notes
=============

**unreleased**

**v0.1.2-dev**

**v0.1.1**

* Added support for remote user. Handling identities without registering a User
  model. (thanks to `bossan <https://github.com/bossan>`_)
* Addes support for permissions using resources and scopes.
  (thanks to `bossan <https://github.com/bossan>`_)
* Added example project.
* Updated documentation.

**v0.1.0**

* Correctly extract email field name on UserModel (thanks to `swist <https://github.com/swist>`_)
* Add support for Oauth2 Token Exchange to exchange tokens with remote clients.
  Handy when using multiple applications with different clients which have to
  communicate with each other.
* Support for session iframe