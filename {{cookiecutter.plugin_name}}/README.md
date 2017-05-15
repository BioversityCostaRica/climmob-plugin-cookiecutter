{{ cookiecutter.project_name }}
==============

Getting Started
---------------

- Create a Python virtual environment.
```
sh virtualenv {{ cookiecutter.plugin_name }}_env
```
- Activate the environment .
```
. ./{{ cookiecutter.plugin_name }}_env/bin/activate
```

- Change directory into your newly created plugin.
```
cd {{ cookiecutter.plugin_name }}
```

- Build the plugin
```
python setup.py develop
```

- Add the plugin to the climmob list of plugins by editing the following line in development.ini or production.ini
```
    #climmob.plugins = examplePlugin
    climmob.plugins = {{ cookiecutter.plugin_name }}
```

- Run Climmob again
