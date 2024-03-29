# packages
import boto3
import json

# make API call
bedrock = boto3.client(
	service_name='bedrock-runtime'
)

# defining parameters
model_id = "amazon.titan-text-express-v1"
accept = "application/json"
content_type = "application/json"
prompt = "Meeting transcript: Miguel: Hi Brant, I want to discuss the workstream  for our new product launch Brant: Sure Miguel, is there anything in particular you want to discuss? Miguel: Yes, I want to talk about how users enter into the product. Brant: Ok, in that case let me add in Namita. Namita: Hey everyone Brant: Hi Namita, Miguel wants to discuss how users enter into the product. Miguel: its too complicated and we should remove friction.  for example, why do I need to fill out additional forms?  I also find it difficult to find where to access the product when I first land on the landing page. Brant: I would also add that I think there are too many steps. Namita: Ok, I can work on the landing page to make the product more discoverable but brant can you work on the additonal forms? Brant: Yes but I would need to work with James from another team as he needs to unblock the sign up workflow.  Miguel can you document any other concerns so that I can discuss with James only once? Miguel: Sure. From the meeting transcript above, Create a list of action items for each person."
body = json.dumps({
	"inputText": prompt,
	"textGenerationConfig": {
		"maxTokenCount": 4096,
		"stopSequences": [],
		"temperature": 0,
		"topP": 1
	}
})

# inference step
response = bedrock.invoke_model(
	body=body,
	modelId=model_id,
	accept=accept,
	contentType=content_type
)

# get response body
response_body = json.loads(response.get("body").read())

# print response
print(f"Input token count: {response_body['inputTextTokenCount']}")
for result in response_body['results']:
	print(f"Token count: {result['tokenCount']}")
	print(f"Output text: {result['outputText']}")
	print(f"Completion reason: {result['completionReason']}")
