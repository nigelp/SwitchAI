Structured Outputs
==================

Language models generate unstructured text by default, but some applications require structured outputs. For these use cases, you can constrain a model to respond with JSON—a structured data format suitable for automated processing.

To define the expected JSON structure, **Pydantic** can be used to define a schema, ensuring type validation and consistency in the model's output.

Below is an example demonstrating how to use it:

.. code:: python

    from typing import List
    from pydantic import BaseModel, Field

    from switchai import SwitchAI

    # Define a schema for each step in the reasoning process
    class Step(BaseModel):
        explanation: str = Field(..., description="Description of the reasoning or method used in this step.")
        output: str = Field(..., description="Result or outcome of this specific step.")

    # Define a schema for the overall reasoning process
    class MathReasoning(BaseModel):
        steps: List[Step] = Field(..., description="A sequence of steps involved in solving the math problem.")
        final_answer: str = Field(..., description="The final solution or answer to the math problem.")

    # Initialize the client
    client = SwitchAI(
        provider="mistral",
        model_name="mistral-small-latest"
    )

    # Input messages for the language model
    messages = [
        {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
        {"role": "user", "content": "How can I solve 8x + 7 = -23?"}
    ]

    # Get the structured response adhering to the defined schema
    response = client.chat(
        messages=messages,
        response_format=MathReasoning
    )

    print(response)

The response will typically be a JSON object that adheres to the schema defined in the `response_format` parameter. For example:

.. code-block:: json

    {
        "steps": [
            {
                "explanation": "Subtract 7 from both sides of the equation.",
                "output": "8x = -30"
            },
            {
                "explanation": "Divide both sides by 8.",
                "output": "x = -3.75"
            }
        ],
        "final_answer": "-3.75"
    }


While most providers return valid JSON objects that match the defined schema, there may be instances where the response does not conform to the schema (e.g., missing fields or incorrect types). It is recommended to always validate the response to ensure compliance with the schema.

