Speech to text
==============
Transcribing spoken language into written text is a common task in many applications, such as voice assistants, transcription services, and video captioning. SwitchAI provides a simple interface to convert audio files or live speech into text using state-of-the-art speech-to-text models.

.. code-block:: python

    from switchai import SwitchAI

    client = SwitchAI(provider="deepgram", model_name="nova")
    response = client.transcribe(
        audio_path="path/to/audio/file.wav",
    )

    print(response.text)


The ``transcribe`` method returns a ``TranscriptionResponse``, which contains the transcribed text.

Specifying the Audio Language
-----------------------------
To improve accuracy, you can specify the language of the audio file using the ``language`` parameter. This helps the model better interpret the speech content:


.. code-block:: python

    from switchai import SwitchAI

    client = SwitchAI(provider="deepgram", model_name="nova")
    response = client.transcribe(
        audio_path="path/to/audio/file.wav",
        language="fr"
    )

    print(response.text)


By providing the language, the transcription model can deliver more accurate results.