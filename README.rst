Internet Sabotage
=================

Python package to simulate internet failures for testing purposes.

This fork fix error in original repository. The library is working at 100%.

Installation
------------

.. code:: shell

    $ pip install internet-sabotage2

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
