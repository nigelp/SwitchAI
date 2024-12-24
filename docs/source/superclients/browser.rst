Browser
=======

The Browser is an SuperClient that extends the functionalities of a SwitchAI client used for chat. It enables the AI model to access a website to perform various tasks such as information extraction, summarization, indexing, or answering questions about the website's content.

Here is an example of how to use it:

.. code:: python

    from switchai import SwitchAI, Browser

    client = SwitchAI(provider="openai", model_name="gpt-4o")
    client = Browser(client)

    response = client.chat(
         messages=[
            {
                "role": "user",
                "content": "Can summarize the content of this website: https://example.com?"
            },
        ]
    )

    print(response)

The Browser client will access the website and summarize the content.

Note that, the Browser client cannot access all links. Websites with a paywall or those that require a login to access the content are not supported.

And be mindful of the cost when using this client. As the model accesses the website and processes the content, the cost of the request will be higher than a normal chat request.