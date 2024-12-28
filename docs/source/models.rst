Supported Models
================

SwitchAI provides seamless integration with a variety of AI models from multiple providers, offering you flexibility to choose the best model for your use case. Below is the complete list of supported models organized by provider.

Chat
----
These models are optimized for generating human-like responses in chat applications.

.. csv-table::
   :widths: 5, 30

    **OpenAI**, "``gpt-4o-mini``, ``gpt-4o``, ``o1-preview``, ``o1-mini``, ``gpt-4``"

    **Mistral**, "``mistral-large-latest``, ``mistral-small-latest``, ``pixtral-large-latest``, ``pixtral-12b``, ``open-mistral-7b``, ``open-mixtral-8x7b``, ``open-mixtral-8x22b``"

    **xAI**, "``grok-beta``, ``grok-vision-beta``"

    **Anthropic**, "``claude-3-5-sonnet-latest``, ``claude-3-5-haiku-latest``, ``claude-3-opus-latest``"

    **Google**, "``gemini-1.5-flash``, ``gemini-1.5-pro``, ``gemini-1.5-flash-8b``"

Embeddings
----------
Embedding models generate numerical representations of data for tasks like similarity search, clustering, and classification.


Text
^^^^

.. csv-table::
   :widths: 5, 30

    **OpenAI**, "``text-embedding-ada-002``, ``text-embedding-3-small``, ``text-embedding-3-large``"

    **Mistral**, "``mistral-embed``"

    **Google**, "``models/text-embedding-004``, ``models/embedding-001``"

    **VoyageAI**, "``voyage-3-large``, ``voyage-3``, ``voyage-3-lite``, ``voyage-code-3``, ``voyage-finance-2``, ``voyage-law-2``, ``voyage-code-2``"

Text and Images
^^^^^^^^^^^^^^^

.. csv-table::
   :widths: 5, 30

    **VoyageAI**, "``voyage-multimodal-3``"

Speech to Text
--------------
Speech to text models convert spoken language into written text.

.. csv-table::
   :widths: 5, 30

    **OpenAI**, "``whisper-1``"

    **Deepgram**, "``nova-2``, ``nova``, ``enhanced``, ``base``, ``whisper-tiny``, ``whisper-small``, ``whisper-base``, ``whisper-medium``, ``whisper-large``"

    **Replicate**, "``openai/whisper``"

Image Generation
----------------
Image generation models create images from textual descriptions.

.. csv-table::
   :widths: 5, 30

    **OpenAI**, "``dall-e-3``, ``dall-e-2``"

    **Replicate**, "``black-forest-labs/flux-schnell``, ``stability-ai/sdxl``"