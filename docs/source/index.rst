Welcome to SwitchAI
===================

SwitchAI is a lightweight, flexible library that provides a unified interface for interacting with various AI APIs, including OpenAI, Anthropic, Mistral, and more.

Get started
-----------

Here’s a simple example of how to use SwitchAI:

.. code:: python

    from switchai import SwitchAI

    client = SwitchAI(provider="openai", model_name="gpt-4")
    response = client.chat(
        messages=[
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )

.. toctree::
    :maxdepth: 2
    :hidden:

    models
    api_keys
    chat
    function_calling
    embeddings
    speech_to_text
    classes
