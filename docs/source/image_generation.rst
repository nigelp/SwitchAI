Image Generation
================

Image generation is a task where the model generates an image based on the input text.

The example below demonstrates how to generate an image using the **SwitchAI** client.

.. code:: python

    from switchai import SwitchAI

    client = SwitchAI(provider="replicate", model_name="black-forest-labs/flux-schnell")
    response = client.generate_image(
        "Photo of a ultra realistic sailing ship, dramatic light, "
        "pale sunrise, cinematic lighting, battered, low angle, "
        "trending on artstation, 4k, hyper realistic, focused, extreme details, "
        "unreal engine 5, cinematic, masterpiece, art by studio ghibli, intricate "
        "artwork by john william turner"
    )

    image = response.images[0]
    image.show()

The ``generate_image`` method returns an ``ImageGenerationResponse``, which contains the generated images. The generated image should look like:

.. image:: _static/ship.png
    :alt: ship.png