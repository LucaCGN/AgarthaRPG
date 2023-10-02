[Official documentation on chat from LangChain](https://python.langchain.com/en/latest/modules/models/chat/getting_started.html)

```python

from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


# Supporting libraries
import os
from dotenv import load_dotenv

load_dotenv()

```

```python

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YourAPIKeyIfNotSet')

```

### 0. Simple Input/Output Still works

You just need to pass it as a message instead. More on this in a second.

```python

chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

```

```python

message = [HumanMessage(content="What is the name of the most populous state in the USA?")]

chat(message)

```

### 1. Chat Messages

* HumanMessage: A message sent from the perspective of the human
* AIMessage: A message sent from the perspective of the AI the human is interacting with
* SystemMessage: A message setting the objectives the AI should follow
* ChatMessage: A message allowing for arbitrary setting of role. You won’t be using this too much

```python

messages = [
    SystemMessage(content="Say the opposite of what the user says"),
    HumanMessage(content="I love programming.")
]
chat(messages)

```

```python

messages = [
    SystemMessage(content="Say the opposite of what the user says"),
    HumanMessage(content="I love programming."),
    AIMessage(content='I hate programming.'),
    HumanMessage(content="The moon is out")
]
chat(messages)

```

```python

messages = [
    SystemMessage(content="Say the opposite of what the user says"),
    HumanMessage(content="I love programming."),
    AIMessage(content='I hate programming.'),
    HumanMessage(content="What is the first thing that I said?")
]
chat(messages)

```

#### Batch Messages

```python

batch_messages = [
    [
        SystemMessage(content="You are a helpful word machine that creates an alliteration using a base word"),
        HumanMessage(content="Base word: Apple")
    ],
    [
        SystemMessage(content="You are a helpful word machine that creates an alliteration using a base word"),
        HumanMessage(content="Base word: Dog")
    ],
]
chat.generate(batch_messages)

```

### Prompt Templates
With one or more `MessagePromptTemplates` you can build a `ChatPromptTemplate`

```python

# Make SystemMessagePromptTemplate
prompt=PromptTemplate(
    template="Propose creative ways to incorporate {food_1} and {food_2} in the cuisine of the users choice.",
    input_variables=["food_1", "food_2"]
)

system_message_prompt = SystemMessagePromptTemplate(prompt=prompt)

```

```python

# Output of system_message_prompt
system_message_prompt.format(food_1="Bacon", food_2="Shrimp")

```

```python

# Make HumanMessagePromptTemplate
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

```

```python

# Create ChatPromptTemplate: Combine System + Human
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
chat_prompt

```

```python

chat_prompt_with_values = chat_prompt.format_prompt(food_1="Bacon", \
                                                   food_2="Shrimp", \
                                                   text="I really like food from Germany.")

chat_prompt_with_values.to_messages()

```

```python

response = chat(chat_prompt_with_values.to_messages()).content
print (response)

```

```

Great choice! Here are some creative ways to incorporate bacon and shrimp into German cuisine:

1. Bacon-wrapped shrimp skewers: Marinate shrimp in a mixture of olive oil, garlic, paprika, and cayenne pepper. Wrap each shrimp with a thin slice of bacon and thread onto skewers. Grill over medium heat until the bacon is crispy and the shrimp is pink and cooked through. Serve with a side of mustard for dipping.

2. German shrimp and bacon soup: Start by cooking diced bacon until crispy in a large pot. Remove the bacon and set it aside. Add diced onion, celery, and carrots to the bacon fat and cook until softened. Add chicken or vegetable broth, diced potatoes, and diced cooked shrimp to the pot. Simmer until the potatoes are tender. Serve hot with a sprinkle of crispy bacon on top.

3. Bacon and shrimp sauerkraut: Sauté diced bacon and sliced onions in a skillet until the onions are caramelized. Add sauerkraut, apple cider vinegar, and a little bit of sugar to the pan. Cook until the sauerkraut is tender and the liquid has reduced. Stir in cooked shrimp and reheat briefly. Serve as a side dish with a German-style sausage.

```

#### With Streaming

```python

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY, streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature=0)

resp = chat(chat_prompt_with_values.to_messages())

```

```

Great choice! Here are some creative ways to incorporate bacon and shrimp into German cuisine:

1. Bacon and Shrimp Spätzle: Spätzle is a traditional German egg noodle dish. Add cooked shrimp and crispy bacon to the spätzle and toss with butter and fresh herbs for a delicious and hearty meal.

2. Shrimp and Bacon Sauerkraut: Add cooked shrimp and crispy bacon to sauerkraut for a flavorful and protein-packed side dish. Serve alongside traditional German sausages or pork dishes.

3. Bacon and Shrimp Potato Salad: German potato salad is typically made with bacon and vinegar dressing. Add cooked shrimp to the salad for a unique twist on this classic dish.

4. Shrimp and Bacon Schnitzel: Top a traditional German schnitzel with cooked shrimp and crispy bacon for a decadent and flavorful meal.

5. Bacon and Shrimp Bratwurst: Mix cooked shrimp and crispy bacon into the bratwurst mixture before grilling for a unique and delicious twist on this classic German sausage.

Enjoy experimenting with these creative ways to incorporate bacon and shrimp into your favorite German dishes!

```

```python



```