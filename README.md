# Knowledge Base and Agents with Amazon Bedrock

## Amazon Bedrock: Introduction

- Amazon Bedrock is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon which are available for your use through a unified API.
- Amazon Bedrock also offers a broad set of capabilities to build GenAI applications with security, privacy, and responsible AI.
- With Amazon Bedrock:
  - You can easily experiment with and evaluate top foundation models (FMs) for your use case
  - Privately customize them with your data using techniques such as fine-tuning and Retrieve Augmented Generation (RAG)
  - Build agents that execute tasks using your enterprise systems and data sources
- Following are the key features of Amazon Bedrock:
  1. API and Playground to experiment with different prompts and configuration for text, image, and chat
  2. Create knowledge bases (KBs)
  3. Agents that can use foundation models (FMs), make API calls, and query knowledge bases (KBs)
  4. Adapt models to specific tasks and domains with training data
  5. Purchase provisioned throughput for a foundation model (FM) in order to run inference 
  6. Evaluate outputs of different models
  7. Prevent inappropriate or unwanted content by using Guardrails for Amazon Bedrock
- Pricing is based on the volume of input tokens and output tokens, as well as whether you have purchased provisioned throughput for the model
- Model lifecycle: Following are the three states (or versions) of the models in Amazon Bedrock:
  1. Active: The model provider is actively working on this version, and it will continue to get updates such as bug fixes and minor improvements
  2. Legacy: A version is marked legacy when there is a more recent version which provides superior performance. Amazon Bedrock set an EOL (End of License) date for legacy versions. While you can continue to use a legacy version, you should plan to transition to an Active version before the EOL.
  3. EOL: This version is no longer available for use. Any requests made for this version will fail.

## Amazon Bedrock: Implementation

Here, we will see the implementation:

1. Open [AWS Console](https://aws.amazon.com/marketplace/management/signin).

2. Sign in as a Root user.

3. After successful sign in, change your region to one of the following regions:

   1. US East (N. Virginia)
   2. US West (Oregon)

   This is simply because all features of AWS Bedrock are not available in all regions. Only the above two regions have all the features. Please check the table below for features that are limited by region:

   | Region                   | Model evaluation | Knowledge base | Agents | Fine-tuning (custom models) | Continued pre-training (custom models) | Provisioned Throughput                                    |
   | ------------------------ | ---------------- | -------------- | ------ | --------------------------- | -------------------------------------- | --------------------------------------------------------- |
   | US East (N. Virginia)    | Yes              | Yes            | Yes    | Yes                         | Yes                                    | Yes                                                       |
   | US West (Oregon)         | Yes              | Yes            | Yes    | Yes                         | Yes                                    | Yes                                                       |
   | Asia Pacific (Singapore) | No               | No             | No     | No                          | No                                     | No                                                        |
   | Asia Pacific (Tokyo)     | No               | No             | No     | No                          | No                                     | No                                                        |
   | Europe (Frankfurt)       | No               | No             | No     | No                          | No                                     | No                                                        |
   | AWS GovCloud (US-West)   | No               | No             | No     | Yes                         | No                                     | Yes (only for fine-tuned models, with no commitment term) |

4. Now on the console page, search for "Bedrock" in the above search bar and click on "Amazon Bedrock".

5. Following is a list of examples available in Amazon Bedrock:

   | Examples (1-8)                            | Examples (9-16)                              | Examples (17-24)                    | Examples (25-32)                                           |
   | ----------------------------------------- | -------------------------------------------- | ----------------------------------- | ---------------------------------------------------------- |
   | 1. Action items from a meeting transcript | 9. Create an image (SDXL 1.0)                | 17. Generate variations of an image | 25. Product description to benefits                        |
   | 2. Advanced Q&A with citations            | 10. Creating a table of product descriptions | 18. Google ad copy generation       | 26. Question answering with grounded content               |
   | 3. Chain of thought with Llama 2 (13B)    | 11. Customer Service FAQ Chatbot             | 19. Information extraction          | 27. Removing PII                                           |
   | 4. Chain of thought with Llama 2 (70B)    | 12. Debug code                               | 20. JSON creation                   | 28. Replace an object in an input image using "inpainting" |
   | 5. Character roleplay                     | 13. Earnings call summarization              | 21. JSON output                     | 29. Role play                                              |
   | 6. Code generation                        | 14. Editing text                             | 22. Multiple choice classification  | 30. Software code generation                               |
   | 7. Contract entity extraction             | 15. Few Shot Learning                        | 23. Narrative writing               | 31. Structured summarization with specified context        |
   | 8. Create an image (SDXL 0.8)             | 16. Generating images from a text prompt     | 24. Product description generation  | 32. Transcript summarization                               |
   
   We will start with the first example: Action Items from a Meeting Transcript
   
6. As we have decided to start with example "Action Items from a Meeting Transcript", we need access to "Titan Text G1 - Express v1" LLM.

7. To get the access, click on "Get Started" button at the right side and then click on "Request model access" button on the right side.

8. On "Model access" page, click on "Manage model access" button towards top right corner. After clicking on that button, you will see a checkbox against each model name in the below table.

9. In the below table of models, search for "Titan Text G1 - Express" under "Amazon" section. Click the checkbox against this model name, scroll down to the bottom of the page, and click on "Request model access" button. In my case, I got access within a second.

10. Now, click on "Examples" in the left pane. On "Examples" page, click on tile with heading "Action items from a meeting transcript", its details will open on the right side, there will be a button "Open in Playground", click on it. Now, run the example and make changes to play around it.

11. Now to access "Titan Text G1 - Express" model via its API, we need to create an IAM user. On AWS Management Console, type "IAM" in the search bar, open IAM, click "User" in the left pane, then click on "Create User" button towards the right side. Perform the following steps:

    1. Type the name of user
    
    2. Then tick the checkbox against "Provide user access to the AWS Management Console - optional"
    
    3. Uncheck "Specify a user in Identity Center - Recommended" and click "I want to create an IAM user"
    
    4. Click "Next" button
    
    5. On the next screen, click on "Attach policies directly" tile and then tick the checkbox against "AdministrativeAccess"; scroll down and click "Next" button
    
    6. Finally, click "Create user" button
    
    7. On the next page, click on "Show" link and copy the password. Keep password safely for later use.
    
    8. Now, click on "Create access key" towards the top-right of the page
    
    9. Select "Local code" on the next page, and then click on "Next" button at the bottom of the page
    
    10. On the next page, give a description (optional) and click on "Create access key" button
    
    11. Copy and keep safely - "Access Key" and "Secret access key"
    
    12. In the home directory of your system (i.e., the path shown when you open terminal on your system), create a directory '.aws' and inside it create the following two files:
    
        1. 'credentials'
    
           > [default]
           > aws_access_key_id = paste_your_access_key
           > aws_secret_access_key = paste_your_secret_access_key
    
           
    
        2. 'config'
    
           > [default]
           > region=us-east-1
    
           
    
    13. Finally, run the following Python script to get a list of available foundational models (FMs) on Amazon Bedrock:
    
        ```python
        # packages
        import boto3
        import json
        
        # make API call
        bedrock = boto3.client(
        	service_name='bedrock'
        )
        
        # get list of models
        models = bedrock.list_foundation_models().get('modelSummaries')
        
        # print details of all models
        for model in models:
        	print(model)
        ```
    
        Run the following program to make inference from Amazon Bedrock:
    
        ```python
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
        ```
    
        > **Boto3 'bedrock' vs 'bedrock-runtime' service**
        >
        > Both, 'bedrock' and 'bedrock-runtime' are low-level client. The difference is following:
        >
        > - 'bedrock' is a low-level client for Bedrock that provides API for creating and managing Bedrock models
        > - 'bedrock-runtime' is a low-level client BedrockRuntime that provides API running inference using Bedrock models
        > - 'invoke_model' function is with 'bedrock-runtime'
    
    14. +

## Knowledge Base: Introduction

- A knowledge base is a centralized repository of information that is organized and searchable. It is designed to provide quick access to specific knowledge or information.

- A knowledge base can include answers to frequently asked questions, how-to guides, and troubleshooting instructions.

- Following is an overview of Amazon Knowledge Base:

  1. To create a knowledge base, specify the location of your data, select an embedding model, and configure a vector store for Bedrock to store and update your embeddings.

     > **Vector Store**
     >
     > 1. It is a database to store and retrieve information from vector embeddings generated by AI models (or Large Language Models)
     > 2. The major benefit of using them is that they provide efficient storage and fast retrieval of information

  2. Query your knowledge base in the test window. You can either retrieve source text chunks or generate responses using the chunks connected with a foundation model (FM)

  3. Integrate your knowledge base into your application as is or add it to agents

- +

## S3 Bucket: Introduction

- We need to create a S3 bucket before creating knowledge base on AWS.
- S3 allows to store and retrieve unlimited amount of data.
- In S3, data is stored as objects but instead of storing them in a file directory, S3 stores them in what we call, a bucket. Here, file directory is replaced by a bucket.
- You can upload an object of size up to 5 TB.
- We can also version objects from accidental deletions.
- We can create multiple buckets and store them across different classes or tiers of data, we can then create permissions to let them access by permitted users only; and we can even stage them between different tiers.
- Following are the different classes of S3 storage:
  1. Amazon S3 Standard
  2. Amazon S3 Standard - Infrequent Access (S3 Standard-IA)
  3. Amazon S3 OneZone - Infrequent Access (S3 OneZone-IA)
  4. Amazon S3 Intelligent Tiering
  5. Amazon S3 Glacier Instant Retrieval
  6. Amazon S3 Glacier Flexible Retrieval

## S3 Bucket: Implementation

Follow the below steps to create a S3 bucket:

1. Sign in in AWS
2. On your AWS Management Console page, search S3 in the top search bar and open it
3. Click on "Create bucket" button towards the right side
4. On the next page, select AWS Region as "us-east-1"
5. Leave Bucket Type as "General purpose"
6. Give name to the bucket
7. Leave Object Ownership as "ACLs disabled (recommended)"
8. Leave "Block Public Access settings for this bucket" as "Block all public access"
9. Leave Bucket Versioning as "Disable"
10. Skip Tags
11. Leave "Default Encryption" as "Server-side encryption with Amazon S3 managed keys (SSE-S3)"
12. Leave "Bucket Key" as "Enable"
13. Click on "Create bucket" button
14. Upload whatever data files you want to put in this bucket

## Knowledge Base: Implementation

Following are the steps to create a knowledge base:

1. Sign in in AWS
2. On AWS Management Console, search Bedrock in the top search bar and open it
3. On the next page, click on "Get started" button towards right side
4. Click on "Knowledge base" link in the left pane
5. Then, click on "Create knowledge base" button towards the bottom-right side
6. Given a name to the knowledge base on the next page
7. Give any description you want for this knowledge base
8. Leave IAM Permissions as "Create and use a new service role"
9. Skip Tags
10. Click on "Next" button
11. On the next page, give Data Source a name
12. Select the previously created S3 bucket (or click on "Browse S3" button and select a S3 bucket, if exists)
13. Click on "Next" button
14. On the next page, select an embedding model (since I have already taken access of "Titan Text - Express" model, thus "Titan Embeddings G1 - Text v1.2" is shown as selected)
15. Leave "Quick create a new vector store - Recommended" selected
16. Click on "Next" button
17. On the next page, review everything and then "Create knowledge base" button towards the bottom-right of the page. If you get error "Knowledge base creation with a root user is not supported. Please sign-in with an IAM user or IAM role and try again.", then obey it.

## Agent: Introduction

- Agents securely connects your data sources, automatically converts data into numerical representations, and augments the user request with the right information to generate an accurate and relevant response.
- For instance, if the user asks about documents required for claims, the agent will look up information from an appropriate knowledge base.

## Agent: Implementation

Following are the steps to create an agent:

1. After sign-in in AWS, open Bedrock from the top search bar of AWS Management Console.
2. On the Bedrock page, click on "Get started" button towards right side.
3. In the left pane, click on Agents.
4. On the new page, enter a name for agent
5. Enter a description of agent
6. Leave User Input, IAM Permissions, and KMS key selection as it is
7. Reduce Idle session timeout to save money
8. Skip Tags
9. Click on "Next" button towards buttom-right side
10. On the next page, select a model
11. Skip Action Groups
12. Select KB
13. Review and finally click on the "Create Agent" button towards the bottom-right side.
14. You can test the connection on the next page

## Evaluation Metrics

- +

