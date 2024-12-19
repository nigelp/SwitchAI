Embeddings
==========

Embeddings are numerical representations of text that capture semantic
meaning and context. Texts with similar meanings have embeddings that
are “closer” to each other in the vector space. For example, the
sentences *“I took my dog to the vet”* and *“I took my cat to the vet”*
would have similar embeddings because they describe a similar context.

Embeddings can be used to compare different texts and understand their
relationships. For instance, if the embeddings for the words *“cat”* and
*“dog”* are close together, you can infer that these words share similar
meanings, contexts, or both.

Generating Embeddings
---------------------

To generate embeddings, use the ``embed`` method. This method accepts a
string or a list of strings as input and returns an
``EmbeddingResponse`` object. Here’s an example:

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

The response contains the embedding vectors along with additional
metadata:

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

The dimensionality of the embedding vectors depends on the model being
used. For example:

- **OpenAI’s text-embedding-ada-002 model** generates 1,536-dimensional embeddings.

- **Google’s models/text-embedding-004 model** generates 768-dimensional embeddings.

The higher the dimensionality, the more nuanced the representation of
the text, allowing for deeper semantic comparisons.