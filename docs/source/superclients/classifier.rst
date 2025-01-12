Classifier
==========

Classifier is a powerful superclient leveraging the capabilities of LLMs and Vision LLMs to classify text and images. The classification task involves predictive modeling to assign the correct label(s) to input data.

Usage Examples
--------------

Text Classification
^^^^^^^^^^^^^^^^^^^

This superclient can classify text into predefined classes. Here's an example:

.. code:: python

    from switchai import SwitchAI, Classifier

    # Initialize the client and classifier
    client = SwitchAI(provider="openai", model_name="gpt-4o")
    classifier = Classifier(client, classes=["negative", "positive"])

    # Classify a text
    response = classifier.classify("I love this movie")
    print(response)  # Output: "positive"

The response will be the predicted label for the input text.

Image Classification
^^^^^^^^^^^^^^^^^^^^
Classifier can also classify images. Note that for this task, the classifier accepts only PIL images. Here's an example:

.. code:: python

    import PIL.Image

    from switchai import SwitchAI, Classifier

    # Initialize the client and classifier
    client = SwitchAI(provider="openai", model_name="gpt-4o")
    classifier = Classifier(client, classes=["cat", "dog"])

    # Open an image using PIL
    pil_image = PIL.Image.open("path/to/image.jpg")

    # Classify the image
    response = classifier.classify(pil_image)
    print(response)  # Output: "cat" or "dog"

Single-Label vs. Multi-Label Classification
-------------------------------------------
By default, Classifier performs single-label classification, where each input is assigned a single label. For multi-label classification, set the  ``multi_label`` parameter to ``True``.

Here’s an example of multi-label classification, where we classify an article title into multiple categories:

.. code:: python

    from switchai import SwitchAI, Classifier

    # Initialize the client and classifier
    client = SwitchAI(provider="openai", model_name="gpt-4o")
    classifier = Classifier(client, classes=["technology", "business", "sports"], multi_label=True)

    # Classify the input text
    response = classifier.classify("Apple Launches New iPhone")
    print(response)  # Output: ["technology", "business"]

Task Details
------------
In many cases, it’s useful to provide the model with additional context about the classification task. This can improve results significantly. Use the ``task_description`` parameter to specify details about the task.

For example, in a hate speech detection task, you can describe what constitutes hate speech:

.. code:: python

    from switchai import SwitchAI, Classifier

    # Initialize the client and classifier
    client = SwitchAI(provider="openai", model_name="gpt-4o")
    classifier = Classifier(
        client,
        classes=["hate speech", "not hate speech"],
        task_description="Classify whether the input text contains "
                         "hate speech. Hate speech includes offensive language, threats, or discrimination."
    )

    # Classify text inputs
    response = classifier.classify("Immigrants are ruining our country!")
    print(response)  # Output: "hate speech"

    response = classifier.classify("We need fairer policies for everyone.")
    print(response)  # Output: "not hate speech"

Batch Classification
---------------------
Classifier can process a list of texts or images in a single call. This feature is useful for classifying large datasets efficiently.

.. code:: python

    from switchai import SwitchAI, Classifier

    # Initialize the client and classifier
    client = SwitchAI(provider="openai", model_name="gpt-4o")
    classifier = Classifier(client, classes=["angry", "happy", "sad", "neutral"])

    # Classify multiple texts
    responses = classifier.classify([
        "I love this movie",
        "I hate this movie",
        "I am feeling sad",
        "I am feeling happy"
    ])

    print(responses)  # Output: ["happy", "angry", "sad", "happy"]

Important Notes
---------------
Classifier uses :doc:`../structured_outputs`, and its accuracy depends on the model and input data. Always verify the returned labels for critical use cases.

