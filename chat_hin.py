from tts import speech

def chat_hin(query: str):
    if 'तुम कैसे हो' in query:
        speech('मैं बधिया हूँ')

    elif 'तुम क्या कर रहे हो' in query:
        speech("मैं आपका सहायक हूं और आपके आदेशों का पालन कर रहा हूं")

    elif 'मैं क्या कर रहा हूं' in query:
        speech("मेरा अनुमान है कि आप मुझे आदेश दे रहे हो")

    elif 'तुम कहां रहते हो' in query or 'तुम कहां रहते हो' in query or 'तुम्हारा घर कहाँ है' in query \
            or 'तुम्हारा पता क्या है' in query:
        speech('मैं आपके कार्यस्थल या आपके काम की चीजों में रहता हूं जैसे आपका लैपटॉप या कंप्यूटर।')

    elif 'मैं किस से बात कर रहा हूं' in query:
        speech('आप अपने असिस्टेंट(सहायक) जार्विस से बात कर रहे हैं')

    elif 'तुम्हें किसने बनाया' in query:
        speech('मुझे संध्या ने उनके विज्ञान प्रोजेक्ट के लिए बनाया हैं')

    elif 'तुम्हारा नाम क्या है' in query or 'मैं तुम्हें किस नाम से पुकारूं' in query:
        speech("तुम मुझे जार्विस कह सकते हो.")

    elif 'हम तुम्हारा उपयोग कैसे कर सकते हैं' in query:
        speech("आप मुझे अपने काम में मदद करने के लिए आदेश दे सकते हैं जैसे ऐप्स खोलना और बंद करना, समाचार देना, ईमेल भेजना, और बहुत कुछ.")
# You can continue from here.