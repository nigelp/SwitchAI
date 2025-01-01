ImageRetriever
==============

ImageRetriever is a superclient built on top of a multimodal embedding client to provide image retrieval based on text or image queries.

Here is a simple example of how to use the ImageRetriever:

.. code:: python

    from switchai import SwitchAI, ImageRetriever

    client = SwitchAI(provider="VoyageAI", model_name="voyage-multimodal-3")
    image_retriever = ImageRetriever(client, images_folder_path="files/images")

    results = image_retriever.retrieve_images("An orange cat in a green field.")
    print(results)

Here is an example of what the results might look like:

.. code:: python

    {
        "cat.png": 0.92,
        "dog.png": 0.63,
        "bird.png": 0.51,
    }


The ``retrieve_images`` method will return a dictionary with the image file name as the key and the similarity score as the value.
Two similarity metrics are supported: cosine and euclidean. The default is cosine, and the cutting threshold is 0.5. You should experiment with the threshold to get the best results.

After the folder of images is embedded, the client will store all the embeddings in a cache file, so it's not necessary to recompute them every time.

Bear in mind that different providers compute costs per image differently, and even the image resolution could change the cost.