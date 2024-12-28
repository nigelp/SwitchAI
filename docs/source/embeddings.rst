Embeddings
==========

Embeddings are numerical representations of data that capture semantic meaning and context. Data with similar meanings or relationships are represented by embeddings that are “closer” to each other in a shared vector space. Embeddings can be generated for various modalities, including text, images, audio, and more, allowing for a wide range of applications in machine learning and artificial intelligence. For example, embeddings enable comparisons, clustering, and semantic understanding of complex data types.

Text Embeddings
---------------

Text embeddings specifically represent textual data in a vector space. These embeddings help capture the semantic meaning and context of the text, enabling comparisons between different texts. For instance, the sentences *“I took my dog to the vet”* and *“I took my cat to the vet”* would have similar embeddings because they describe a comparable context.

To generate text embeddings, use the ``embed`` method. This method accepts a string or a list of strings as input and returns an ``EmbeddingResponse`` object. Here's an example:

.. code:: python

   from switchai import SwitchAI

   client = SwitchAI(provider="google", model_name="text-embedding-ada-002")
   response = client.embed(
       input=[
           "I took my dog to the vet",
           "I took my cat to the vet"
       ]
   )

   print(response)

The response includes the embedding vectors along with additional metadata:

.. code:: json

   {
       "id": null,
       "object": "list",
       "model": "text-embedding-ada-002",
       "usage": {
           "input_tokens": 10,
           "total_tokens": 10
       },
       "embeddings": [
           {
               "index": 0,
               "data": [0.1, 0.2, 0.3, 0.4, 0.5]
           },
           {
               "index": 1,
               "data": [0.6, 0.7, 0.8, 0.9, 1.0]
           }
       ]
   }

The dimensionality of the embedding vectors depends on the model used. For example:

- **OpenAI’s text-embedding-ada-002 model** generates 1,536-dimensional embeddings.
- **Google’s models/text-embedding-004 model** generates 768-dimensional embeddings.

Higher dimensionality enables more nuanced text representations, allowing for deeper semantic comparisons.

Multimodal Embeddings
---------------------

Multimodal embedding models transform unstructured data from multiple modalities into a shared vector space. These models support text and content-rich images, such as figures, photos, slide decks, and document screenshots. This eliminates the need for complex text extraction or ETL pipelines.

.. code:: python

   from switchai import SwitchAI
   from PIL import Image

   client = SwitchAI(provider="VoyageAI", model_name="voyage-multimodal-3")
   response = client.embed(
       input=[
           "I took my dog to the vet",
           Image.open("dog.jpg")
       ]
   )

   print(response)

This returns the embeddings for the text and the image in a shared vector space via the ``EmbeddingResponse`` object. The embeddings can be used to compare the text and the image, or to analyze their relationships.