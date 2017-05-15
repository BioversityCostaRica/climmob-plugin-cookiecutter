# Climmob-plugin-cookiecutter

A Cookiecutter (project template) for creating a Climmob plugin.

Requirements
------------

* Python 2.7
* [Climmob](https://github.com/BioversityCostaRica/pyclimmob)
* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

Usage
-----

1. Generate a Pyramid project, following the prompts from the command
    ```sh
    $ cookiecutter https://github.com/BioversityCostaRica/climmob-plugin-cookiecutter.git
    ```
2. Finish configuring the plugin by creating a virtual environment and installing your new project. These steps are output as part of the cookiecutter command above and are slightly different for Windows.
    ```sh
    $ . ./climmob_virtual_env/bin/activate
    $ cd myClimmobPlugin
    $ python setup.py develop
```
    Add the plugin to the climmob list of plugins by editing the following line in development.ini or production.ini
    ```
        #climmob.plugins = examplePlugin to read
        climmob.plugins = myClimmobPlugin
    ```
3. Run your Climmob