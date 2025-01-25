Installation
============

SwitchAI makes it simple to integrate and work with almost any AI provider for virtually any task you can imagine.

It is recommended to install SwitchAI in a **Python virtual environment**. Using a virtual environment helps you manage dependencies across multiple projects and prevents compatibility issues. If you're new to virtual environments, refer to `this guide <https://docs.python.org/3/tutorial/venv.html>`_ for more information.

Start with creating a virtual environment. In your project directory, run the following command to create a virtual environment:

.. code-block:: bash

    python -m venv .env

Depending on your operating system, use one of the following commands:

- **Linux/MacOS:**

  .. code-block:: bash

      source .env/bin/activate

- **Windows:**

  .. code-block:: bash

      .env\Scripts\activate

Once the virtual environment is activated, install SwitchAI using pip:

.. code-block:: bash

    pip install switchai

Installing from Source
----------------------

If you'd like to work with the latest development version of SwitchAI, you can install it directly from the source repository:

.. code-block:: bash

    pip install git+https://github.com/yelboudouri/switchai

This command installs the cutting-edge **main version** of SwitchAI, which includes the most recent updates and fixes. While we strive to keep this version stable and functional, please note that it may occasionally introduce breaking changes.

**When to Use the Source Version:**

- If a bug has been fixed since the last official release, but a new version hasn't been published yet.
- If you want to stay up-to-date with the latest features.

Since the main version is a work in progress, it may not always be stable. If you encounter any issues, please help us improve by opening an Issue in our GitHub repository. We typically resolve most problems within hours or a day.

