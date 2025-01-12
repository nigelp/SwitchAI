Vision
======

The vision capabilities of the model allow it to process images and answer questions about them.

Images can be provided to the model in several ways:

- By URL: Passing a link to the image.
- By File Path: Providing the path to a local image file.
- In Raw Format: Passing the image as raw bytes.
- As a PIL Image: Passing an image object created using the Python Imaging Library (PIL).

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

Passing an Image in Raw Format
------------------------------

You can also provide an image in raw format (bytes). Here’s an example:

.. code:: python

    from switchai import SwitchAI

    with open("path/to/image/file.jpg", "rb") as image_file:
        raw_image = image_file.read()

    client = SwitchAI(provider="openai", model_name="gpt-4o")
    response = client.chat(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {"type": "image", "image": raw_image},
                ],
            }
        ]
    )

    print(response)

Using a PIL Image
------------------

Alternatively, you can pass an image as a PIL Image object. Here’s how:

.. code:: python

    from switchai import SwitchAI
    from PIL import Image

    pil_image = Image.open("path/to/image/file.jpg")

    client = SwitchAI(provider="openai", model_name="gpt-4o")
    response = client.chat(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {"type": "image", "image": pil_image},
                ],
            }
        ]
    )

    print(response)

Important Notes
---------------

- While the model's vision capabilities can be applied in various scenarios, it is essential to understand its **limitations**. Be sure to consult the official model documentation for a detailed overview of its constraints and capabilities.
- Additionally, verify how costs are calculated for processing image inputs to avoid unexpected expenses.
