from textwrap import dedent

def main():
    display_actions_message()


def display_actions_message():

    vars = dict(
        separator='=' * 79,
    )
    msg = dedent(
        """
        %(separator)s
        This is a scaffolding of a Climmob plugin. You can use it as a started
        to create complex plugins
        %(separator)s

        To make Climmob run this plugin do:
            
        Activate the Climmob environment .
            . /path/to/ClimmobEnv/bin/activate
            
        Change directory into your newly created plugin.
            cd {{ cookiecutter.plugin_name }}

        Build the plugin
            python setup.py develop

        Add the plugin to the climmob list of plugins by editing the line
            #climmob.plugins = examplePlugin to read
            climmob.plugins = {{ cookiecutter.plugin_name }}
        

        Run Climmob again
        """ % vars)
    print(msg)


if __name__ == '__main__':
    main()