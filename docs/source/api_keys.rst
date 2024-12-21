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

Alternatively, you can set your API key as an environment variable. This approach keeps your code cleaner and avoids exposing sensitive information in your scripts.

In your terminal or environment configuration, use the following command:

.. code:: bash

    export PROVIDER_API_KEY_NAMING="your_api_key"

Replace PROVIDER_API_KEY_NAMING with the following naming convention for the provider you are using:

.. csv-table::
   :widths: 5, 15

    "**OpenAI**", OPENAI_API_KEY
    "**Mistral**", MISTRAL_API_KEY
    "**xAI**", XAI_API_KEY
    "**Anthropic**", ANTHROPIC_API_KEY
    "**Google**", GEMINI_API_KEY
    "**Deepgram**", DEEPGRAM_API_KEY
    "**VoyageAI**", VOYAGE_API_KEY