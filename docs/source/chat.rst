Chat
====

SwitchAI provides a straightforward interface to generate text using a wide variety of language models. These models are trained on vast amounts of data, enabling them to interpret multimedia inputs and follow natural language instructions. Based on the given prompts, the models can generate diverse outputs, including code, mathematical equations, structured JSON data, or human-like prose.

Generating Text
---------------
To generate text, use the ``chat`` method of the SwitchAI client. This method accepts a list of messages as input and returns a list of responses. Each input message requires an assigned role, such as "user" or "assistant," to indicate the speaker. The output will include the model's generated response corresponding to each user message.

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

Chat Messages
-------------

Chat messages are collections of prompts or interactions, with each message assigned a specific role, such as "system," "user," "assistant," or "tool." Each message role serves a distinct purpose in the conversation:

1. **System Messages:** System messages are optional and used to set the behavior or context for the AI assistant in a conversation. These messages can:

    - Modify the assistant's personality.

    - Provide specific instructions or guidelines.

    - Include task parameters, creativity constraints, or relevant contextual information.

2. **User Messages:** User messages represent input from a human interacting with the AI assistant.

3. **Assistant Messages:** Assistant messages are the AI's responses to user inputs.

4. **Tool Messages:** Tool messages occur in the context of function calling. These messages appear during the final response formulation when the model formats the output of a tool call for the user.

By structuring messages with these roles, you can effectively guide the AI's behavior and responses to suit your specific needs.

