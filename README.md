# Packaging Pulumi Python Components

This example shows how to create a proper Python package to hold the [components](https://www.pulumi.com/blog/pulumi-components/).

The `greeter` folder is a normal Python package, with a `pyproject.toml` file to define the package metadata and dependencies.

The `greeter-plugin` is a Pulumi Component Plugin that exposes the components from the `greeter` package. It follows the required conventions for this folder to be recognized as such a plugin (`requirements.txt`, `PulumiPlugin.yaml` and `__main__.py`.) If the `greeter` package is published independently on PyPI, it could just be referenced in `requirements.txt` by it's name & version.

Note that when running this locally, you need to create `./greeter-plugin/venv`:

```bash
cd greeter-plugin
python -m venv venv
./venv/bin/pip install -r requirements.txt
```

You can then run the example:

```bash
cd example
pulumi up
```
