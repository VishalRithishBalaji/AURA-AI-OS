import importlib
import os


PLUGIN_CACHE = {}


def load_plugin(
    plugin_name: str
):

    try:

        module = importlib.import_module(

            f"plugins.{plugin_name}"
        )

        PLUGIN_CACHE[
            plugin_name
        ] = module

        return module

    except Exception as e:

        print(

            f"Plugin Load Error: {e}"
        )

        return None


def unload_plugin(
    plugin_name: str
):

    if plugin_name in PLUGIN_CACHE:

        del PLUGIN_CACHE[
            plugin_name
        ]


def get_plugin(
    plugin_name: str
):

    return PLUGIN_CACHE.get(
        plugin_name
    )


def discover_plugins():

    plugins = []

    if not os.path.exists(
        "plugins"
    ):

        return plugins

    for file in os.listdir(
        "plugins"
    ):

        if (
            file.endswith(".py")
            and file != "__init__.py"
        ):

            plugins.append(

                file.replace(
                    ".py",
                    ""
                )
            )

    return plugins


def load_all_plugins():

    loaded = []

    for plugin in discover_plugins():

        module = load_plugin(
            plugin
        )

        if module:

            loaded.append(
                plugin
            )

    return loaded