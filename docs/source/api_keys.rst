API Keys
========

To use any of the supported models, you need an API key provided by the provider of the models you plan to use. SwitchAI makes it easy to authenticate by allowing you to pass your API key directly to the client or set it as an environment variable.

Passing the API Key Directly
----------------------------
You can pass your API key directly when initializing the SwitchAI client, as shown below:

.. code:: python

    from switchai import SwitchAI

    client = SwitchAI(provider="openai", model_name="gpt-4", api_key="your_api_key")
    response = client.chat(
        messages=[
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )

Setting the API Key as an Environment Variable
----------------------------------------------

For improved security and cleaner code, consider setting your API key as an environment variable. The environment variable name should follow this format:

.. code::

    <PROVIDER>_API_KEY

For example, if you’re using a Gemini model provided by Google, the variable name should be ``GOOGLE_API_KEY``.

To set the environment variable, use the following command in your terminal or environment configuration file:

.. code:: bash

    export PROVIDER_API_KEY="your_api_key"

By using environment variables, you reduce the risk of accidentally exposing sensitive information in your codebase. This method is recommended for production environments.
