Chat
====

.. toctree::
    :maxdepth: 2
    :hidden:

    vision
    function_calling
    structured_outputs

SwitchAI provides a straightforward interface for generating text using a wide variety of large language models. These models are trained on vast amounts of data, enabling them to perform a wide range of language-related tasks such as text generation, translation, summarization, question answering, and more.

Quickstart
----------
To generate text, use the ``chat`` method of the SwitchAI client. This method accepts a list of messages as input and returns a :ref:`ChatResponse<chatresponse>`. Each input message requires an assigned role, such as "user" or "assistant," to indicate the speaker.

Here's an example of how to use it:

.. code:: python

    from switchai import SwitchAI

    client = SwitchAI(provider="openai", model_name="gpt-4")
    response = client.chat(
        messages=[
            {"role": "system", "content": "You are a friendly assistant."},
            {"role": "user", "content": "Hello, how are you?"}
        ]
    )

    print(response)

The generated response could look like this:

.. code:: json

    {
      "id": "Atf113GwsNo0ksTvFBIfWsOV1KdCx",
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
      },
      "tool_calls": null,
      "usage": {
        "input_tokens": 8,
        "output_tokens": 10,
        "total_tokens": 18
      },
      "finish_reason": "completed"
    }

The responses contains the model response along with other useful information such as the number of input and output tokens, and the reason the conversation ended.


Messages and Roles
------------------
Chat messages are collections of prompts or interactions, with each message assigned a specific role: "system," "user," "assistant," or "tool." Each message role serves a distinct purpose in the conversation:

1. **System messages** are optional messages used to set the behavior or context for the AI model in a conversation. These messages can:
    - Modify the model's behavior.
    - Provide specific instructions or guidelines.
    - Include task parameters, creativity constraints, or relevant contextual information.

2. **User messages** represent input from a human interacting with the AI model.

3. **Assistant messages** are the AI's responses to user inputs.

4. **Tool messages** occur in the context of function calling.

By structuring messages with these roles, you can effectively guide the AI's behavior and responses to suit your specific needs.

Finish Reasons
--------------
The ``finish_reason`` field in the response indicates the reason the conversation ended. Possible values include:

- **completed**: The conversation ended successfully.
- **max_tokens**: The model reached the maximum token limit.
- **tool_calls**: The conversation ended due to a tool call.
- **content_filtering**: Generated content was filtered out.
- **unknown**: The conversation ended for an unknown reason.

Running a Conversation
----------------------

Here's an example of how to run a full conversation with the AI model:

.. code:: python

    from switchai import SwitchAI

    client = SwitchAI(provider="openai", model_name="gpt-4")
    messages = [
        {"role": "system", "content": "You are a friendly assistant."},
    ]

    while True:
        user_input = input("You (CTRL+C to exit): ")
        messages.append({"role": "user", "content": user_input})

        response = client.chat(messages=messages)

        print(f"AI: {response.message.content}")
        messages.append(response.message)

Streaming
---------
Streaming allows you to get responses from the model as they are generated, instead of waiting for the entire response to be generated.

Here's an example of how to use it:

.. code:: python

    from switchai import SwitchAI

    client = SwitchAI(provider="openai", model_name="gpt-4")
    response = client.chat(
        messages=[
            {"role": "system", "content": "You are a friendly assistant."},
            {"role": "user", "content": "Hello, how are you?"}
        ],
        stream=True
    )

    for chunk in response:
        print(chunk)

In this example, the response is returned as a stream of chunks, which you can print or process in real time.