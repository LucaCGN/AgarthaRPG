

**RiftCooking: RiftCooking, a culinary application, transforms visual inputs (course photos, ingredient images) into recipes
**: Image-to-text; VL-BERT; scalable real-time translation.
**Replicate - LLAVA: Cloud GPU solution for deploying LLAVA an Image to Text Model.
**OpenAI - ChatGPT: GPT-3.5 (context); GPT-4 (crucial ops, advanced reasoning).
**Autogen: Framework for LLM-powered apps; modular abstractions; data-aware, agentic interaction.
**Firebase BaaS: Auth (Cloud Functions); Firestore (real-time NoSQL, custom logic); Storage (user-triggered, seamless file mgmt); dynamic interaction (event-driven Cloud Functions).
**Pinecone: Scalable vector embedding storage/query; long-term AI memory; RAG; accurate, timely info retrieval.
**Flutter/FlutterFlow: Cross-platform (single codebase); low-code/no-code, visual interface app development.

--------------------------------------------------//---------------------------------------------------

Cost Breakdown: LLava13B - Replicate
#1 dollar = 68 predictions.

-$0.000725/sec is the price of the instance to run the llava model.
-10 too 20s for predictions to run 
-0.0145 per prediction is a conservative estimative based on 20s
-so another conservative estimative is that 1 dollar = 68 interactions with images (both generating and captioning)

Cost Breakdown: Gpt 3.5turbo API
#1 dollar = 25 predictions.

- 16K contex: [Input: $0.003/1K tokens & Output:$0.004/1K tokens]
- Assuming a conservative prediction that we will be having constant close to 16k tokens interactions to manage and fetch context in the app, lets assume 0.04 cents per prediction
- 1/0.04 = 25 predictions.

Cost Breakdown: Gpt 4 API
#1 dollar = 8 predictions.

-8K context: [Input: $0.03/1K tokens & Output:$0.06/1K tokens]
- GPT-4 receive the consolidated and clear output from the APP flow, with the goal always to perform some reasoning that the other models are not quite able to perform. We can expect a conserative general price of 0.04 per 1000k tokens and 3000k tokens as the abv interaction context windows spawn.
- That gives 0.12 per prediction. 1/0.12 = 8

##In the LLM interaction side, we can define one user interaction on avarage as
Free: 3 llava interactions, 12 gpt 3.5 interactions( simplified test mode for 3 immages)
	COST: 1 dollar total
Standart: 3 llava, 4 gpt 3.5
	COST: 0.2 cents per interaction
StandartPlus: 5 llava, 8 gpt 3.5
	COST: 0.4 cents per interaction
Premium: 8 llava, 8 gpt 3.5, 2 gpt 4
	COST: 0.65 cents per interaction

###Estimate Average Monthly User Number of Interactions So We can proceed wih structuring the Pricing of This product

--------------------------------------------------//---------------------------------------------------

Backend Breakdown: Google Firebase

--------------------------------------------------//---------------------------------------------------

App Flow/Features:

-Flow:

Login page
Input Image Page, the initial app page.
Output [MainCourse] or [Ingredients and Cooking Utensils]  Image's Detailed Description.
Output [Receipt]'s or [Receipt Suggestion] as a detailed step by step cooking guide in line with Image Detailed Description.
If user is free
	Show Popup with remaining uses
if user is paid tier 1
	Open specifc receipt chat
If user is pais tier 3
	Open specifc receipt chat with brownsing plugins + voice chat

-extra pages/screens/feature:

user account info/managent
onboardind first login screens
setting screens
lateral menu where the user can have settings


--------------------------------------------------//---------------------------------------------------