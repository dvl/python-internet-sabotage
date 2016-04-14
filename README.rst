Internet Sabotage
=================

Python package to simulate internet failures for testing purposes.

Instalation
-----------

.. code:: shell

    $ pip install internet-sabotage

Usage
-----

.. code:: python

    from internet_sabotage import no_connection

    with no_connection():
        response = requests.get('http://httpbin.org/ip')

or

.. code:: python

    from internet_sabotage import no_connection

    @no_connection
    def test_something():
        pass

License
-------

MIT
