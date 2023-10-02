# 5 Levels Of Summarization: Novice to Expert

Summarization is a fundamental building block of many LLM tasks. You'll frequently run into use cases where you would like to distill a large body of text into a succinct set of points.

Depending on the length of the text you'd like to summarize, you have different summarization methods to choose from.

We're going to run through 5 methods for summarization that start with Novice and end up expert. These aren't the only options, feel free to make up your own. If you find another one you like please share it with the community.

**5 Levels Of Summarization:**
1. **Summarize a couple sentences** - Basic Prompt
2. **Summarize a couple paragraphs** - Prompt Templates
3. **Summarize a couple pages** - Map Reduce
4. **Summarize an entire book** - Best Representation Vectors
5. **Summarize an unknown amount of text** - Agents

First let's import our OpenAI API Key (best practice is to have this as an environment variable but showing it here for clarity)

```python

openai_api_key = 'YourAPIKey'

```

## Level 1: Basic Prompt - Summarize a couple sentences

If you just have a few sentences you want to one-off summarize you can use a simple prompt and copy and paste your text.

This method isn't scalable and only practical for a few use cases...the perfect level #1!

```python

from langchain import OpenAI

```

```python

llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

```

The important part is to provide instructions for the LLM to know what to do. In thise case I'm telling the model I want a summary of the text below

```python

prompt = """
Please provide a summary of the following text

TEXT:
Philosophy (from Greek: φιλοσοφία, philosophia, 'love of wisdom') \
is the systematized study of general and fundamental questions, \
such as those about existence, reason, knowledge, values, mind, and language. \
Some sources claim the term was coined by Pythagoras (c. 570 – c. 495 BCE), \
although this theory is disputed by some. Philosophical methods include questioning, \
critical discussion, rational argument, and systematic presentation.
"""

```

```python

num_tokens = llm.get_num_tokens(prompt)
print (f"Our prompt has {num_tokens} tokens")

```

```

Our prompt has 121 tokens

```

```python

output = llm(prompt)
print (output)

```

```

Philosophy is a systematized study of general and fundamental questions about existence, reason, knowledge, values, mind, and language. It is believed to have been coined by Pythagoras, and its methods include questioning, critical discussion, rational argument, and systematic presentation.

```

Woof 🐶, that summary is still hard to understand. Let me add to my instructions so that the output is easier to understand. I'll tell it to explain it to me like a 5 year old.

```python

prompt = """
Please provide a summary of the following text.
Please provide your output in a manner that a 5 year old would understand

TEXT:
Philosophy (from Greek: φιλοσοφία, philosophia, 'love of wisdom') \
is the systematized study of general and fundamental questions, \
such as those about existence, reason, knowledge, values, mind, and language. \
Some sources claim the term was coined by Pythagoras (c. 570 – c. 495 BCE), \
although this theory is disputed by some. Philosophical methods include questioning, \
critical discussion, rational argument, and systematic presentation.
"""

```

```python

num_tokens = llm.get_num_tokens(prompt)
print (f"Our prompt has {num_tokens} tokens")

```

```

Our prompt has 137 tokens

```

```python

output = llm(prompt)
print (output)

```

```

Philosophy is about asking questions and trying to figure out the answers. It is about thinking about things like existence, knowledge, and values. People have been doing this for a very long time, and it is still done today.

```

Nice! That's much better, but let's look at something we can automate a bit more

## Level 2: Prompt Templates - Summarize a couple paragraphs

Prompt templates are a great way to dynamically place text within your prompts. They are like [python f-strings](https://realpython.com/python-f-strings/) but specialized for working with language models.

We're going to look at 2 short Paul Graham essays

```python

from langchain import OpenAI
from langchain import PromptTemplate
import os

```

```python

paul_graham_essays = ['../data/PaulGrahamEssaySmall/getideas.txt', '../data/PaulGrahamEssaySmall/noob.txt']

essays = []

for file_name in paul_graham_essays:
    with open(file_name, 'r') as file:
        essays.append(file.read())

```

Let's print out a preview of the essays to see what they look like

```python

for i, essay in enumerate(essays):
    print (f"Essay #{i+1}: {essay[:300]}\n")

```

```

Essay #1: January 2023(Someone fed my essays into GPT to make something that could answer
questions based on them, then asked it where good ideas come from.  The
answer was ok, but not what I would have said. This is what I would have said.)The way to get new ideas is to notice anomalies: what seems strange,


Essay #2: January 2020When I was young, I thought old people had everything figured out.
Now that I'm old, I know this isn't true.I constantly feel like a noob. It seems like I'm always talking to
some startup working in a new field I know nothing about, or reading
a book about a topic I don't understand well

```

Next let's create a prompt template which will hold our instructions and a placeholder for the essay. In this example I only want a 1 sentence summary to come back

```python

template = """
Please write a one sentence summary of the following text:

{essay}
"""

prompt = PromptTemplate(
    input_variables=["essay"],
    template=template
)

```

Then let's loop through the 2 essays and pass them to our LLM. I'm applying .strip() on the summaries to remove the white space on the front and back of the output

```python

for essay in essays:
    summary_prompt = prompt.format(essay=essay)
    
    num_tokens = llm.get_num_tokens(summary_prompt)
    print (f"This prompt + essay has {num_tokens} tokens")
    
    summary = llm(summary_prompt)
    
    print (f"Summary: {summary.strip()}")
    print ("\n")

```

```

This prompt + essay has 205 tokens
Summary: Exploring anomalies at the frontiers of knowledge is the best way to generate new ideas.


This prompt + essay has 500 tokens
Summary: This text explores the idea that feeling like a "noob" is actually beneficial, as it is inversely correlated with actual ignorance and encourages us to discover new things.

```

## Level 3: Map Reduce - Summarize a couple pages multiple pages

If you have multiple pages you'd like to summarize, you'll likely run into a token limit. Token limits won't always be a problem, but it is good to know how to handle them if you run into the issue.

The chain type "Map Reduce" is a method that helps with this. You first generate a summary of smaller chunks (that fit within the token limit) and then you get a summary of the summaries.\

Check out [this video](https://www.youtube.com/watch?v=f9_BWhCI4Zo) for more information on how chain types work

```python

from langchain import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

```

```python

paul_graham_essay = '../data/PaulGrahamEssays/startupideas.txt'

with open(paul_graham_essay, 'r') as file:
    essay = file.read()

```

Let's see how many tokens are in this essay

```python

llm.get_num_tokens(essay)

```

That's too many, let's split our text up into chunks so they fit into the prompt limit. I'm going a chunk size of 10,000 characters. 

> You can think of tokens as pieces of words used for natural language processing. For English text, **1 token is approximately 4 characters** or 0.75 words. As a point of reference, the collected works of Shakespeare are about 900,000 words or 1.2M tokens.

This means the number of tokens we should expect is 10,000 / 4 = ~2,500 token chunks. But this will vary, each body of text/code will be different

```python

text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap=500)

docs = text_splitter.create_documents([essay])

```

```python

num_docs = len(docs)

num_tokens_first_doc = llm.get_num_tokens(docs[0].page_content)

print (f"Now we have {num_docs} documents and the first one has {num_tokens_first_doc} tokens")

```

```

Now we have 5 documents and the first one has 2086 tokens

```

Great, assuming that number of tokens is consistent in the other docs we should be good to go. Let's use LangChain's [load_summarize_chain](https://python.langchain.com/en/latest/use_cases/summarization.html) to do the `map_reducing` for us. We first need to initialize our chain

```python

summary_chain = load_summarize_chain(llm=llm, chain_type='map_reduce',
#                                      verbose=True # Set verbose=True if you want to see the prompts being used
                                    )

```

Now actually run it

```python

output = summary_chain.run(docs)

```

```python

output

```

This summary is a great start, but I'm more of a bullet point person. I want to get my final output in bullet point form.

In order to do this I'm going to use custom promopts (like we did above) to instruct the model on what I want.

The map_prompt is going to stay the same (just showing it for clarity), but I'll edit the combine_prompt.

```python

map_prompt = """
Write a concise summary of the following:
"{text}"
CONCISE SUMMARY:
"""
map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text"])

```

```python

combine_prompt = """
Write a concise summary of the following text delimited by triple backquotes.
Return your response in bullet points which covers the key points of the text.
```{text}```
BULLET POINT SUMMARY:
"""
combine_prompt_template = PromptTemplate(template=combine_prompt, input_variables=["text"])

```

```python

summary_chain = load_summarize_chain(llm=llm,
                                     chain_type='map_reduce',
                                     map_prompt=map_prompt_template,
                                     combine_prompt=combine_prompt_template,
#                                      verbose=True
                                    )

```

```python

output = summary_chain.run(docs)

```

```python

print (output)

```

```

- Y Combinator suggests that the best startup ideas come from looking for problems, preferably ones that the founders have themselves.
- Good ideas should appeal to a small number of people who need it urgently.
- To find startup ideas, one should look for things that seem to be missing and be prepared to question the status quo.
- College students should use their college experience to prepare themselves for the future and build things with other students.
- Tricks for coming up with startup ideas on demand include looking in areas of expertise, talking to people about their needs, and looking for waves and gaps in the market.
- Sam Altman points out that taking the time to come up with an idea is a better strategy than most founders are willing to put in the time for.
- Paul Buchheit suggests that trying to sell something bad can lead to better ideas.

```

## Level 4: Best Representation Vectors - Summarize an entire book

In the above method we pass the entire document (all 9.5K tokens of it) to the LLM. But what if you have more tokens than that?

What if you had a book you wanted to summarize? Let's load one up, we're going to load [Into Thin Air](https://www.amazon.com/Into-Thin-Air-Personal-Disaster/dp/0385494785) about the 1996 Everest Disaster

```python

from langchain.document_loaders import PyPDFLoader

# Load the book
loader = PyPDFLoader("../data/IntoThinAirBook.pdf")
pages = loader.load()

# Cut out the open and closing parts
pages = pages[26:277]

# Combine the pages, and replace the tabs with spaces
text = ""

for page in pages:
    text += page.page_content
    
text = text.replace('\t', ' ')

```

```python

num_tokens = llm.get_num_tokens(text)

print (f"This book has {num_tokens} tokens in it")

```

```

This book has 139472 tokens in it

```

Wow, that's over 100K tokens, even [GPT 32K](https://help.openai.com/en/articles/7127966-what-is-the-difference-between-the-gpt-4-models) wouldn't be able to handle that in one go. At [0.03 per 1K prompt tokens](https://help.openai.com/en/articles/7127956-how-much-does-gpt-4-cost), this would cost us $4.17 just for the prompt alone.

So how do we do this without going through all the tokens? Pick random chunks? Pick equally spaced chunks?

I kicked off a [twitter thread](https://twitter.com/GregKamradt/status/1653060004226924544) with a proposed solution to see if I was off base. I'm calling it the Best Representation Vectors method (not sure if a name already exists for it).

**Goal:** Chunk your book then get embeddings of the chunks. Pick a subset of chunks which represent a wholistic but diverse view of the book. Or another way, is there a way to pick the top 10 passages that describe the book the best?

Once we have our chunks that represent the book then we can summarize those chunks and hopefully get a pretty good summary.

Keep in mind there are tools that would likely do this for you, and with token limits increasing this won't be a problem for long. But if you want to do it from scratch this might help.

This is most definitely not the optimal answer, but it's my take on it for now! If the [clustering](https://scikit-learn.org/stable/modules/clustering.html) experts wanna help improve it that would be awesome.

**The BRV Steps:**
1. Load your book into a single text file
2. Split your text into large-ish chunks
3. Embed your chunks to get vectors
4. Cluster the vectors to see which are similar to each other and likely talk about the same parts of the book
5. Pick embeddings that represent the cluster the most (method: closest to each cluster centroid)
6. Summarize the documents that these embeddings represent

Another way to phrase this process, "Which ~10 documents from this book represent most of the meaning? I want to build a summary off those."

Note: There will be a bit of information loss, but show me a summary of a whole book that doesn't have information loss ;)

```python

# Loaders
from langchain.schema import Document

# Splitters
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Model
from langchain.chat_models import ChatOpenAI

# Embedding Support
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Summarizer we'll use for Map Reduce
from langchain.chains.summarize import load_summarize_chain

# Data Science
import numpy as np
from sklearn.cluster import KMeans

```

I'm going to initialize two models, gpt-3.5 and gpt4. I'll use gpt 3.5 for the first set of summaries to reduce cost and then gpt4 for the final pass which should hopefully increase the quality.

```python

text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", "\t"], chunk_size=10000, chunk_overlap=3000)

docs = text_splitter.create_documents([text])

```

```python

num_documents = len(docs)

print (f"Now our book is split up into {num_documents} documents")

```

```

Now our book is split up into 78 documents

```

Let's get our embeddings of those 78 documents

```python

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

vectors = embeddings.embed_documents([x.page_content for x in docs])

```

Now let's cluster our embeddings. There are a ton of clustering algorithms you can chose from. Please try a few out to see what works best for you!

```python

# Assuming 'embeddings' is a list or array of 1536-dimensional embeddings

# Choose the number of clusters, this can be adjusted based on the book's content.
# I played around and found ~10 was the best.
# Usually if you have 10 passages from a book you can tell what it's about
num_clusters = 11

# Perform K-means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42).fit(vectors)

```

Here are the clusters that were found. It's interesting to see the progression of clusters throughout the book. This is expected because as the plot changes you'd expect different clusters to emerge due to different semantic meaning

```python

kmeans.labels_

```

This is sweet, but whenever you have a clustering exercise, it's hard *not* to graph them. Make sure you add colors.

We also need to do dimensionality reduction to reduce the vectors from 1536 dimensions to 2 (this is sloppy data science but we are working towards the 80% solution)

```python

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Taking out the warnings
import warnings
from warnings import simplefilter

# Filter out FutureWarnings
simplefilter(action='ignore', category=FutureWarning)

# Perform t-SNE and reduce to 2 dimensions
tsne = TSNE(n_components=2, random_state=42)
reduced_data_tsne = tsne.fit_transform(vectors)

# Plot the reduced data
plt.scatter(reduced_data_tsne[:, 0], reduced_data_tsne[:, 1], c=kmeans.labels_)
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.title('Book Embeddings Clustered')
plt.show()

```

```

<Figure size 640x480 with 1 Axes>

```

Awesome, not perfect, but pretty good directionally. Now we need to get the vectors which are closest to the cluster centroids (the center).

The function below is a quick way to do that (w/ help from ChatGPT)

```python

# Find the closest embeddings to the centroids

# Create an empty list that will hold your closest points
closest_indices = []

# Loop through the number of clusters you have
for i in range(num_clusters):
    
    # Get the list of distances from that particular cluster center
    distances = np.linalg.norm(vectors - kmeans.cluster_centers_[i], axis=1)
    
    # Find the list position of the closest one (using argmin to find the smallest distance)
    closest_index = np.argmin(distances)
    
    # Append that position to your closest indices list
    closest_indices.append(closest_index)

```

Now sort them (so the chunks are processed in order)

```python

selected_indices = sorted(closest_indices)
selected_indices

```

It's intersting to see which chunks pop up at most descriptive. How does your distribution look?

Let's create our custom prompts. I'm going to use gpt4 (which has a bigger token limit) for the combine step so I'm asking for long summaries in the map step to reduce the information loss.

```python

llm3 = ChatOpenAI(temperature=0,
                 openai_api_key=openai_api_key,
                 max_tokens=1000,
                 model='gpt-3.5-turbo'
                )

```

```python

map_prompt = """
You will be given a single passage of a book. This section will be enclosed in triple backticks (```)
Your goal is to give a summary of this section so that a reader will have a full understanding of what happened.
Your response should be at least three paragraphs and fully encompass what was said in the passage.

```{text}```
FULL SUMMARY:
"""
map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text"])

```

I kept getting a timeout errors so I'm actually going to do this map reduce manually

```python

map_chain = load_summarize_chain(llm=llm3,
                             chain_type="stuff",
                             prompt=map_prompt_template)

```

Then go get your docs which the top vectors represented.

```python

selected_docs = [docs[doc] for doc in selected_indices]

```

Let's loop through our selected docs and get a good summary for each chunk. We'll store the summary in a list.

```python

# Make an empty list to hold your summaries
summary_list = []

# Loop through a range of the lenght of your selected docs
for i, doc in enumerate(selected_docs):
    
    # Go get a summary of the chunk
    chunk_summary = map_chain.run([doc])
    
    # Append that summary to your list
    summary_list.append(chunk_summary)
    
    print (f"Summary #{i} (chunk #{selected_indices[i]}) - Preview: {chunk_summary[:250]} \n")

```

```

Summary #0 (chunk #0) - Preview: The passage describes the author's experience of reaching the summit of Mount Everest on May 10, 1996, and the events that followed. The author, who was part of a New Zealand-based team, had been fantasizing about this moment for months but found him 

Summary #1 (chunk #12) - Preview: In this passage, the author and his team are at Lobuje, a village at 16,200 feet, preparing to move to Base Camp. They receive news that Tenzing, a Sherpa who had fallen into a crevasse, had been rescued by a team of Sherpas and was resting at Base C 

Summary #2 (chunk #26) - Preview: In this passage, the author describes two events that occurred on Everest. The first event involves a Sherpa named Ngawang Topche who was suffering from High Altitude Pulmonary Edema (HAPE), a potentially lethal illness caused by climbing too high to 

Summary #3 (chunk #29) - Preview: In this passage, the author describes the equipment and personal items they brought with them on their expedition to climb Mount Everest. They have a lot of electronic equipment, including laptops, cameras, and tape recorders, as well as climbing gea 

Summary #4 (chunk #39) - Preview: In this passage, the author describes his ascent up the Lhotse Face towards the South Col, the launching pad for the summit assault on Mount Everest. He struggles to pass slower climbers on the single rope and worries about the hazards of falling roc 

Summary #5 (chunk #41) - Preview: In this passage, the author describes their experience waiting on a ledge for over 45 minutes in subzero temperatures while waiting for the rest of their group to catch up. They observe a peculiar sight of a Sherpa, Lopsang Jangbu, towing a weak clim 

Summary #6 (chunk #51) - Preview: This passage describes the harrowing experience of a group of climbers on Mount Everest during a severe storm. The climbers, including guides and clients, were stranded at the lip of a 7,000-foot drop down the Kangshung Face, just 1,000 horizontal fe 

Summary #7 (chunk #54) - Preview: In this passage, the author recounts the events of May 10, 1996, when Scott Fischer and his team reached the summit of Mount Everest. Fischer complained of feeling unwell and took off his oxygen mask shortly after leaving the summit. Lopsang Jangbu,  

Summary #8 (chunk #65) - Preview: The passage describes the aftermath of the tragic events that occurred during the 1996 Everest climbing season. The author, who was a journalist and a member of one of the expeditions, reflects on the memorial service held for the climbers who lost t 

Summary #9 (chunk #71) - Preview: The passage discusses the controversy surrounding Jon Krakauer's book, "Into Thin Air," and its portrayal of Anatoli Boukreev, a professional climbing guide who was involved in the 1996 Mount Everest disaster. Boukreev took issue with Krakauer's acco 

Summary #10 (chunk #75) - Preview: In this passage, the author addresses the controversy surrounding his book, "Into Thin Air," which details the tragic events of the 1996 Everest disaster. He refutes claims made by Boukreev/DeWalt that Reinhold Messner endorsed Anatoli Boukreev's act

```

Great, now that we have our list of summaries, let's get a summary of the summaries

```python

summaries = "\n".join(summary_list)

# Convert it back to a document
summaries = Document(page_content=summaries)

print (f"Your total summary has {llm.get_num_tokens(summaries.page_content)} tokens")

```

```

Your total summary has 4002 tokens

```

```python

llm4 = ChatOpenAI(temperature=0,
                 openai_api_key=openai_api_key,
                 max_tokens=3000,
                 model='gpt-4',
                 request_timeout=120
                )

```

```python

combine_prompt = """
You will be given a series of summaries from a book. The summaries will be enclosed in triple backticks (```)
Your goal is to give a verbose summary of what happened in the story.
The reader should be able to grasp what happened in the book.

```{text}```
VERBOSE SUMMARY:
"""
combine_prompt_template = PromptTemplate(template=combine_prompt, input_variables=["text"])

```

```python

reduce_chain = load_summarize_chain(llm=llm4,
                             chain_type="stuff",
                             prompt=combine_prompt_template,
#                              verbose=True # Set this to true if you want to see the inner workings
                                   )

```

Run! Note this will take a while

```python

output = reduce_chain.run([summaries])

```

```python

print (output)

```

```

In this story, the author recounts their experience as part of a New Zealand-based team attempting to summit Mount Everest on May 10, 1996. Despite months of anticipation, the author finds themselves unable to fully appreciate the achievement due to extreme exhaustion, lack of sleep, and the effects of high altitude. After a brief moment at the summit, the author begins their descent, encountering a traffic jam of climbers from multiple expeditions. The author's oxygen tank runs out, forcing them to navigate dangerous terrain without supplemental oxygen. Unbeknownst to the climbers, a disaster is about to unfold, resulting in the deaths of eight climbers, including two of the author's teammates.

The story also highlights the challenges and dangers of high-altitude mountaineering, as well as the importance of teamwork and respect for local cultures and customs. The author and their team face various obstacles, including altitude sickness, treacherous terrain, and the reliance on Sherpas, who work incredibly hard for little pay. The author emphasizes the need to show gratitude and respect to the Sherpas, who are essential to the success of the climbers.

Throughout the story, the author describes various events and challenges faced by the climbers, including medical emergencies, the importance of proper acclimatization, and the difficulties of providing medical care in a remote, high-altitude environment. The author also discusses the cultural differences between Western climbers and Sherpas, who are often reluctant to acknowledge physical infirmities due to an element of machismo in their culture.

As the climbers continue their ascent, they face physical and mental challenges, as well as the individualistic nature of the climb. The author emphasizes the importance of timing and weather conditions in determining the success of a summit assault. The story also touches on the controversy surrounding the author's book, "Into Thin Air," and its portrayal of Anatoli Boukreev, a professional climbing guide involved in the 1996 Everest disaster.

In the aftermath of the tragedy, the author reflects on the emotional impact, including survivor's guilt and the grief of the families and loved ones of the deceased. The author also considers the role of hubris in the disaster and questions their own actions during the storm. The story highlights the complex emotions and difficult questions that arise in the wake of such a devastating event, as well as the contentious nature of reporting on a tragedy and the importance of accuracy and thorough research in journalism.

```

Wow that was a long process, but you get the gist, hopefully we'll see some library abstractions in the coming months that do this automatically for us! Let me know what you think on [Twitter](https://twitter.com/GregKamradt)

## Level 5: Agents - Summarize an unknown amount of text

What if you have an unknown amount of text you need to summarize? This may be a verticalize use case (like law or medical) where more research is required as you uncover the first pieces of information.

We're going to use agents below, this is still a very actively developed area and should be handled with care. Future agents will be able to handle a lot more complicated tasks.

```python

from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.utilities import WikipediaAPIWrapper

llm = ChatOpenAI(temperature=0, model_name='gpt-4', openai_api_key=openai_api_key)

```

We're going to use the Wiki search tool and research multiple topics

```python

wikipedia = WikipediaAPIWrapper()

```

Let's define our toolkit, in this case it's just one tool

```python

tools = [
    Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="Useful for when you need to get information from wikipedia about a single topic"
    ),
]

```

Init our agent

```python

agent_executor = initialize_agent(tools, llm, agent='zero-shot-react-description', verbose=True)

```

Then let's ask a question that will need multiple documents

```python

output = agent_executor.run("Can you please provide a quick summary of Napoleon Bonaparte? \
                          Then do a separate search and tell me what the commonalities are with Serena Williams")

```

```

[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3mI need to find information about Napoleon Bonaparte and then about Serena Williams to identify commonalities between them.
Action: Wikipedia
Action Input: Napoleon Bonaparte[0m
Observation: [36;1m[1;3mPage: Napoleon
Summary: Napoleon Bonaparte (born Napoleone Buonaparte; 15 August 1769 – 5 May 1821), later known by his regnal name Napoleon I, was a Corsican-born French military commander and political leader who rose to prominence during the French Revolution and led successful campaigns during the Revolutionary Wars. He was the de facto leader of the French Republic as First Consul from 1799 to 1804, then Emperor of the French from 1804 until 1814 and again in 1815. Napoleon's political and cultural legacy endures to this day, as a highly celebrated and controversial leader. He initiated many liberal reforms that have persisted in society, and is considered one of the greatest military commanders in history. His campaigns are still studied at military academies worldwide. Between three and six million civilians and soldiers died in what became known as the Napoleonic Wars.Napoleon was born on the island of Corsica, not long after its annexation by France, to a native family descending from minor Italian nobility. He supported the French Revolution in 1789 while serving in the French army, and tried to spread its ideals to his native Corsica. He rose rapidly in the Army after he saved the governing French Directory by firing on royalist insurgents. In 1796, he began a military campaign against the Austrians and their Italian allies, scoring decisive victories and becoming a national hero. Two years later, he led a military expedition to Egypt that served as a springboard to political power. He engineered a coup in November 1799 and became First Consul of the Republic.
Differences with the United Kingdom meant France faced the War of the Third Coalition by 1805. Napoleon shattered this coalition with victories in the Ulm campaign, and at the Battle of Austerlitz, which led to the dissolution of the Holy Roman Empire. In 1806, the Fourth Coalition took up arms against him. Napoleon defeated Prussia at the battles of Jena and Auerstedt, marched the Grande Armée into Eastern Europe, and defeated the Russians in June 1807 at Friedland, forcing the defeated nations of the Fourth Coalition to accept the Treaties of Tilsit. Two years later, the Austrians challenged the French again during the War of the Fifth Coalition, but Napoleon solidified his grip over Europe after triumphing at the Battle of Wagram.
Hoping to extend the Continental System, his embargo against Britain, Napoleon invaded the Iberian Peninsula and declared his brother Joseph the King of Spain in 1808. The Spanish and the Portuguese revolted in the Peninsular War aided by a British army, culminating in defeat for Napoleon's marshals. Napoleon launched an invasion of Russia in the summer of 1812. The resulting campaign witnessed the catastrophic retreat of Napoleon's Grande Armée. In 1813, Prussia and Austria joined Russian forces in a Sixth Coalition against France, resulting in a large coalition army defeating Napoleon at the Battle of Leipzig. The coalition invaded France and captured Paris, forcing Napoleon to abdicate in April 1814. He was exiled to the island of Elba, between Corsica and Italy. In France, the Bourbons were restored to power.
Napoleon escaped in February 1815 and took control of France. The Allies responded by forming a Seventh Coalition, which defeated Napoleon at the Battle of Waterloo in June 1815. The British exiled him to the remote island of Saint Helena in the Atlantic, where he died in 1821 at the age of 51.
Napoleon had an extensive impact on the modern world, bringing liberal reforms to the lands he conquered, especially the regions of the Low Countries, Switzerland and parts of modern Italy and Germany. He implemented many liberal policies in France and Western Europe.

Page: Napoleon III
Summary: Napoleon III (born Charles Louis Napoléon Bonaparte; 20 April 1808 – 9 January 1873) was the first President of France (as Louis-Napoléon Bonaparte) from 1848 to 1852, and the last monarch of France as Emperor of the French from 1852 until he was deposed in absentia on 4 September 1870. A nephew of Napoleon I and cousin of the disputed Napoleon II, he was elected to the presidency of the Second Republic in 1848, and he seized power by force in 1851 when he could not constitutionally be reelected. He later proclaimed himself Emperor of the French and founded the Second Empire, reigning until the defeat of the French Army and his capture by Prussia and its allies at the Battle of Sedan in 1870. Napoleon III was a popular monarch who oversaw the modernization of the French economy and filled Paris with new boulevards and parks. He expanded the French overseas empire, made the French merchant navy the second largest in the world, and personally engaged in two wars. Maintaining leadership for 22 years, he was the longest-reigning leader of France since the fall of the Ancien Régime, though his reign would ultimately end on the battlefield.
Napoleon III commissioned a grand reconstruction of Paris carried out by the man he appointed as prefect of the Seine, Baron Georges-Eugène Haussmann. He expanded and consolidated the railway system throughout the nation and modernized the banking system. Napoleon III promoted the building of the Suez Canal and established modern agriculture, which ended famines in France and made the country an agricultural exporter. He negotiated the 1860 Cobden–Chevalier Free Trade Agreement with Britain and similar agreements with France's other European trading partners. Social reforms included giving French workers the right to strike, the right to organize, and the right for women to be admitted to a French university.
In foreign policy, Napoleon III aimed to reassert French influence in Europe and around the world. In Europe, he allied with Britain and defeated Russia in the Crimean War (1853–1856). His regime assisted Italian unification by defeating the Austrian Empire in the Franco-Austrian War and later annexed Savoy and Nice through the Treaty of Turin as its deferred reward. At the same time, his forces defended the Papal States against annexation by Italy. He was also favourable towards the 1859 union of the Danubian Principalities, which resulted in the establishment of the United Principalities of Moldavia and Wallachia. Napoleon III doubled the area of the French colonial empire with expansions in Asia, the Pacific, and Africa. On the other hand, the intervention in Mexico, which aimed to create a Second Mexican Empire under French protection, ended in total failure. From 1866, Napoleon III had to face the mounting power of Prussia as its Chancellor Otto von Bismarck sought German unification under Prussian leadership. In July 1870, Napoleon III reluctantly declared war on Prussia after pressure from the general public. The French Army was rapidly defeated and Napoleon III was captured at Sedan. He was swiftly dethroned and the Third Republic was proclaimed in Paris. After he was released from German custody, he went into exile in England, where he died in 1873.



Page: House of Bonaparte
Summary: The House of Bonaparte (originally Buonaparte) is a former imperial and royal European dynasty of Italian (Genoese) origin. It was founded in 1804 by Napoleon I, the son of Corsican nobleman Carlo Buonaparte and Letizia Buonaparte (née Ramolino).  Napoleon was a French military leader who rose to power during the French Revolution and who, in 1804, transformed the First French Republic into the First French Empire, five years after his coup d'état of November 1799 (18 Brumaire).  Napoleon and the Grande Armée had to fight against every major European power (except for the ones he was allied with, including Denmark-Norway) and dominated continental Europe through a series of military victories during the Napoleonic Wars.  He installed members of his family on the thrones of client states, expanding the power of the dynasty.
The House of Bonaparte formed the Imperial House of France during the French Empire, together with some non-Bonaparte family members. In addition to holding the title of Emperor of the French, the Bonaparte dynasty held various other titles and territories during the Napoleonic Wars, including the Kingdom of Italy, the Kingdom of Spain, the Kingdom of Westphalia, the Kingdom of Holland, and the Kingdom of Naples. The dynasty held power for around a decade until the Napoleonic Wars began to take their toll. Making very powerful enemies, such as Austria, Britain, Russia, and Prussia, as well as royalist (particularly Bourbon) restorational movements in France, Spain, the Two Sicilies, and Sardinia, the dynasty eventually collapsed due to the final defeat of Napoleon at the Battle of Waterloo and the restoration of former dynasties by the Congress of Vienna.
During the reign of Napoleon I, the Imperial Family consisted of the Emperor's immediate relations – his wife, son, siblings, and some other close relatives, namely his brother-in-law Joachim Murat, his uncle Joseph Fesch, and his stepson Eugène de Beauharnais.
Between 1852 and 1870, there was a Second French Empire, when a member of the Bonaparte dynasty again ruled France: Napoleon III, the youngest son of Louis Bonaparte. However, during the Franco-Prussian War of 1870–1871, the dynasty was again ousted from the Imperial Throne. Since that time, there has been a series of pretenders. Supporters of the Bonaparte family's claim to the throne of France are known as Bonapartists. Current head Jean-Christophe, Prince Napoléon, has a Bourbon mother.[0m

```

```

Thought:[32;1m[1;3mI now know the summary of Napoleon Bonaparte. I need to find information about Serena Williams to identify commonalities between them.
Action: Wikipedia
Action Input: Serena Williams[0m
Observation: [36;1m[1;3mPage: Serena Williams
Summary: Serena Jameka Williams (born September 26, 1981) is an American retired professional tennis player. Considered among the greatest tennis players of all time, she was ranked world No. 1 in singles by the Women's Tennis Association (WTA) for 319 weeks, including a joint-record 186 consecutive weeks, and finished as the year-end No. 1 five times. She won 23 Grand Slam singles titles, the most by any player in the Open Era, and the second-most of all time. She is the only player, male or female, to accomplish a Career Golden Slam in both singles and doubles.Along with her older sister Venus, Serena Williams was coached by her parents Oracene Price and Richard Williams. Turning professional in 1995, she won her first major singles title at the 1999 US Open. From the 2002 French Open to the 2003 Australian Open, she was dominant, winning all four major singles titles (each time over Venus in the final) to achieve a non-calendar year Grand Slam and the career Grand Slam, known as the 'Serena Slam'. The next few years saw her claim two more singles majors, but suffer from injury and decline in form. Beginning in 2007, however, she gradually returned to form despite continued injuries, retaking the world No. 1 singles ranking. Beginning at the 2012 Wimbledon Championships, Williams returned to dominance, claiming Olympic gold (completing the Career Golden Slam in singles) and winning eight out of thirteen singles majors, including all four in a row from 2014–15 to achieve a second "Serena Slam". At the 2017 Australian Open, she won her 23rd major singles title, surpassing Steffi Graf's Open Era record. She then took a break from professional tennis after becoming pregnant and reached four major finals upon returning to play. In August 2022, Williams announced her impending "evolution" away from professional tennis and played what was expected to be her final match at the 2022 US Open.Williams also won 14 major women's doubles titles, all with her sister Venus, and the pair was unbeaten in major doubles finals (the best unbeaten record in major finals in any discipline of the sport). The pair achieved a non-calendar year Grand Slam between the 2009 Wimbledon Championships and the 2010 French Open, which granted the sisters the doubles world No. 1 ranking. Serena won four Olympic gold medals, three in women's doubles—an all-time joint record in tennis, shared with her sister. The duo are the only women in the Open Era to win Olympic gold in both singles and doubles. She also won two major mixed doubles titles, both in 1998. She is the only singles player, male or female, to complete three Career Golden Slams – one in women's singles and two in same-sex doubles.The arrival of the Williams sisters has been credited with ushering in a new era of power and athleticism on the women's professional tennis tour. Serena holds a combined 39 major titles: 23 in singles, 14 in women's doubles, and two in mixed doubles. She is joint-third on the all-time list and second in the Open Era for total major titles. She is the most recent woman to simultaneously hold all four major singles titles (2002–03 and 2014–15), and the most recent woman to win the Surface Slam (major titles on hard, clay and grass courts in the same calendar year), doing so in 2015. She is also, with Venus, the most recent player to have simultaneously held all four major women's doubles titles (2009–10).
Williams was the world's highest paid woman athlete in 2016, earning almost $29 million. She repeated this feat in 2017 when she was the only woman on Forbes' list of the 100 highest-paid athletes, with $27 million in prize money and endorsements. She won the Laureus Sportswoman of the Year award a record four times (2003, 2010, 2016, 2018), and in December 2015 was named Sportsperson of the Year by Sports Illustrated magazine. She is the highest-earning woman athlete of all time.

Page: Williams sisters
Summary: The Williams sisters are two professional American tennis players: Venus Williams (b. 1980), a seven-time Grand Slam title winner (singles), and Serena Williams (b. 1981), twenty-three-time Grand Slam title winner (singles), both of whom were coached from an early age by their parents Richard Williams and Oracene Price.
Both sisters have been ranked by the Women's Tennis Association at the world No. 1 position in both singles and doubles. In 2002, after the French Open, Venus and Serena Williams were ranked world No. 1 and No. 2 on singles, respectively, marking the first time in history that sisters occupied the top two positions. On 21 June 2010, Serena and Venus again held the No. 1 and No. 2 rankings spots in singles, respectively, some eight years after first accomplishing this feat. At the time, Serena was three months shy of her 29th birthday and Venus had just celebrated her 30th birthday.
There is a noted professional rivalry between the sisters in singles — between the 2001 US Open and the 2017 Australian Open, they contested nine major finals. They became the first two players, female or male, to contest four consecutive major singles finals, from the 2002 French Open to the 2003 Australian Open; Serena famously won all four to complete the first of two "Serena Slams" (non-calendar year Grand Slams). Between 2000 and 2016, they collectively won 12 Wimbledon singles titles (Venus five, and Serena seven). Nonetheless, they remain very close, often watching each other's matches in support, even after one of them had been knocked out of a tournament.
By winning the 2001 Australian Open doubles title, they became the fifth pair of women to complete the career Grand Slam in doubles, and the only pair to complete the career Golden Slam in doubles. At the time, Venus and Serena were only 20 and 19 years old, respectively. Since then, they have gone on to add another two Olympic gold medals at the 2008 Beijing Olympics and the 2012 London Olympics. Moreover, the duo would go on to win a non-calendar year Grand Slam in doubles between 2009 Wimbledon and 2010 Roland Garros, which made them the co-No. 1 doubles players on 7 June 2010. Their most recent major doubles title came at the 2016 Wimbledon Championships.
Both players have won four gold medals at the Olympics, one each in singles and three in doubles— all won together— the most of any tennis players. Venus has also won a silver in mixed doubles at the 2016 Rio Olympics. As a duo, they have also completed the double career Golden Slam in doubles.  Between the two of them, they have completed the Boxed Set, winning all four grand slams in singles, women's doubles, and mixed doubles. They split all four mixed doubles titles in 1998.



Page: Venus Williams
Summary: Venus Ebony Starr Williams (born June 17, 1980) is an American professional tennis player. A former world No. 1 in both singles and doubles, Williams has won seven Grand Slam singles titles, five at Wimbledon and two at the US Open. She is widely regarded as one of the all-time greats of the sport.Along with her younger sister, Serena, Venus Williams was coached by her parents Oracene Price and Richard Williams. Turning professional in 1994, she reached her first major final at the 1997 US Open. In 2000 and 2001, Williams claimed the Wimbledon and US Open titles, as well as Olympic singles gold at the 2000 Sydney Olympics. She first reached the singles world No. 1 ranking on 25 February 2002, becoming the first African American woman to do so in the Open era, and the second of all-time after Althea Gibson. She reached four consecutive major finals between 2002 and 2003, but lost each time to Serena. She then suffered from injuries, winning just one major title between 2003 and 2006. Williams returned to form starting in 2007, when she won Wimbledon (a feat she repeated the following year). In 2010, she returned to the world No. 2 position in singles, but then suffered again from injuries. Starting in 2014, she again gradually returned to form, culminating in two major final appearances at the Australian Open and Wimbledon in 2017.
Along with her seven singles major titles, Williams has also won 14 women's doubles major titles, all partnering Serena; the pair are unbeaten in Grand Slam doubles finals. She became the world No. 1 in doubles for the first time on June 7, 2010, alongside Serena, after the pair completed a non-calendar-year Grand Slam at the French Open. The pair also won three Olympic gold medals in women's doubles, in 2000, 2008, and 2012, adding to Venus' singles gold in 2000 and her mixed doubles silver in 2016. Williams has also won two mixed doubles major titles, both in 1998.
The Williams sisters are credited with ushering in a new era of power and athleticism on the women's professional tennis tour. With 49 WTA Tour singles titles, Williams trails only her sister Serena among active players with the most singles titles. With 22 WTA doubles titles and two mixed doubles titles, her combined total of 73 WTA titles is also second among active players behind Serena. She is also one of only two active players to have reached the singles finals of all four majors, along with Serena. Williams was twice the season prize money leader (in 2001 and 2017), and ranks second behind Serena in all-time career prize money winnings, having earned over US$42 million as of March 2022.[0m

```

```

Thought:[32;1m[1;3mI now know the summaries of both Napoleon Bonaparte and Serena Williams. I can identify commonalities between them.

Final Answer: Napoleon Bonaparte and Serena Williams both achieved remarkable success in their respective fields, with Napoleon being one of the greatest military commanders in history and Serena being one of the greatest tennis players of all time. They both dominated their fields during their peak years and have left lasting legacies. Additionally, they both faced challenges and setbacks in their careers but managed to overcome them and continue to excel. However, it is important to note that their fields of expertise are vastly different, with Napoleon being a military and political leader, while Serena is a professional athlete.[0m

[1m> Finished chain.[0m

```

```python

print (output)

```

```

Napoleon Bonaparte and Serena Williams both achieved remarkable success in their respective fields, with Napoleon being one of the greatest military commanders in history and Serena being one of the greatest tennis players of all time. They both dominated their fields during their peak years and have left lasting legacies. Additionally, they both faced challenges and setbacks in their careers but managed to overcome them and continue to excel. However, it is important to note that their fields of expertise are vastly different, with Napoleon being a military and political leader, while Serena is a professional athlete.

```

Awesome, good luck summarizing!

```python



```

```python



```

```python



```

```python



```

```python



```

```python



```