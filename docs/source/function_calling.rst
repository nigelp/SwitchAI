Function Calling
================
Function calling connects language models to external data and systems. Developers define functions as tools the model can use based on conversation history, and these functions are executed on the application side with results provided back to the model.

Here’s how to define a function for a model:

.. code:: python

    from switchai import SwitchAI

    client = SwitchAI("gemini-1.5-flash-8b")

    tools = [{
        "type": "function",
        "function": {
            "name": "get_price",
            "description": "Get the price of a product",
            "parameters": {
                "type": "object",
                "properties": {
                    "product": {
                        "type": "string",
                        "description": "The product's name.",
                    },
                }
            }
        }
    }]

    messages = [
        {"role": "user", "content": "What is the price of an iPhone 16?"}
    ]

    response = client.chat(
        messages=messages,
        tools=tools
    )

    print(response.choices[0].tool_calls)


This returns a function call like:

.. code:: json

    {
        "id": null,
        "function": {
            "name": "get_price",
            "arguments": {"product": "iPhone 16"}
        },
        "type": "function"
    }


You can then call the function on the application side and return the result to the model:

.. code:: python

    def get_price(product):
        # Call an external API to get the price of the product
        return 999

    tool_call = response.choices[0].tool_calls[0]
    price = get_price(tool_call["function"]["arguments"]["product"])

    function_call_result_message = {
        "role": "tool",
        "content": f"The iPhone 16 costs {price}",
        "tool_call_id": tool_call.id,
        "tool_name": tool_call.function.name
    }

    messages.append(response.choices[0])
    messages.append(function_call_result_message)

    response = client.chat(
        messages=messages,
        tools=tools
    )

    print(response.choices[0].message.content)

The model uses the returned result to generate a response.

