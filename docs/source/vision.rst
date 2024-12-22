Vision
======

The vision capabilities of the model allow it to process images and answer questions about them.

Images can be provided to the model in two primary ways:

- By URL: Passing a link to the image.
- By File Path: Providing the path to a local image file.

Images are included in user messages to interact with the model. Below are examples of how to use each method.

Providing an Image by URL
-------------------------

You can pass an image URL directly to the model. Here’s an example:

.. code:: python

    from switchai import SwitchAI

    client = SwitchAI(provider="openai", model_name="gpt-4o")
    response = client.chat(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image",
                        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    },
                ],
            }
        ]
    )

    print(response)


Uploading a Local Image
-----------------------

If you have an image stored locally, you can provide the file path directly to the model. The library will handle the rest. Here’s an example:

.. code:: python

    from switchai import SwitchAI

    client = SwitchAI(provider="openai", model_name="gpt-4o")
    response = client.chat(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {"type": "image", "image": "path/to/image/file.jpg"},
                ],
            }
        ]
    )

    print(response)


Important Notes
---------------

- While the model's vision capabilities can be applied in various scenarios, it is essential to understand its **limitations**. Be sure to consult the official model documentation for a detailed overview of its constraints and capabilities.
- Additionally, verify how costs are calculated for processing image inputs to avoid unexpected expenses.
