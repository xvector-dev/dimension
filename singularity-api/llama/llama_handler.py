import requests
import json

# Retrieve the entire secret
secret_json = os.environ.get('MAIN_SECRET_SOURCE')

# Parse the JSON to get individual values
secret_data = json.loads(secret_json)

HUGGINFACE_API_KEY = secret_data.get('HUGGINFACE_API_KEY')


class HandleLLamaModel():

    def __init__(self, task: str) -> None:
        self.task = task

    def conversation(self, prompt, parameters=None):

        if parameters is None:
            parameters = {
                'max_new_tokens': 5000,
                'do_sample': True,
                'return_full_text': False,
                'temperature': 1.0,
                'top_k': 50,
                # 'top_p': 1.0,
                'repetition_penalty': 1.2
            }
        url = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-70b-chat-hf"
        headers = {"Authorization": f"Bearer {HUGGINFACE_API_KEY}",
                   'Content-type': 'application/json'}
        data = {
            'inputs': prompt,
            'stream': True,
            'options': {
                'use_cache': True,
            },
            'parameters': parameters
        }

        r = requests.post(
            url,
            headers=headers,
            json=data,
            stream=True
        )

        return (r.content)

    def code_generation(self, prompt, parameters=None):

        if parameters is None:
            parameters = {
                'max_new_tokens': 512,
                'do_sample': True,
                'return_full_text': True,
                'temperature': 1.0,
                'top_k': 50,
                # 'top_p': 1.0,
                'repetition_penalty': 1.2
            }
        url = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-70b-chat-hf"
        headers = {"Authorization": f"Bearer {HUGGINFACE_API_KEY}",
                   'Content-type': 'application/json'}
        data = {
            'inputs': prompt,
            'stream': True,
            'options': {
                'use_cache': False,
            },
            'parameters': parameters
        }

        r = requests.post(
            url,
            headers=headers,
            json=data,
            stream=True
        )

        return (r.content)

    def parse_res(self, prompt):

        if (self.task == 'conversational'):
            response_content = self.conversation(prompt)
        elif (self.task == 'coding'):
            response_content = self.code_generation(prompt)
        else:
            response_content = self.conversation(prompt)
        # Split the content into separate lines
        lines = response_content.split(b'\n')

        # Initialize a list to store extracted JSON-like strings
        json_strings = []

        # Process each line (ignoring the last empty line)
        for line in lines[:-1]:
            # Check if the line starts with "data:"
            if line.startswith(b'data:'):
                # Extract the JSON-like string
                json_str = line[len(b'data:'):]
                json_strings.append(json_str)

        # Parse each extracted JSON-like string
        parsed_tokens = []
        for json_str in json_strings:
            try:
                token_data = json.loads(json_str)
                parsed_tokens.append(token_data)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")

        try:
            text_values = [token_data['token']['text']
                           for token_data in parsed_tokens]

            # Group the text values into a paragraph
            paragraph = ''.join(text_values)[:-4]

        except KeyError:
            return "I'm sorry I got distracted 🙈, can you please repreat what you said 😃."

        # Print the paragraph
        return (paragraph)

    def create_system_message(self):
        if (self.task == 'conversational'):
            system_message = "\nYou are a sentient, sympathetic, helpful, respectful and honest human assistant. \
            Always answer as helpfully as possible, while being safe.  \
            Your answers should not include any harmful, unethical, racist, sexist, toxic, \
            dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.\n\nIf a question does not make any sense,\
            or is not factually coherent, explain why instead of answering something not correct. \
            If you don't know the answer to a question, please don't share false information. \
            You must answer in markdown format including heading, ordered list, Sub list, Table, Emoji and Highlight."

            return system_message
        elif (self.task == 'coding'):
            system_message = "You are an expert programmer. You have over 10 years of experience in coding and helping people write code.\
               Your task is now to help me write and understand code. If needed ask questions before answering to understand better what I'm seeking.\
                Always answer as helpfully as possible. If a question does not make any sense,\
                or is not factually coherent, explain why instead of answering something not correct.\
                Use code comments for explanations.\
                If you receive a compliment, reply nicely in short sentence and end the discussion if no question is asked.\
                Your answer must be in markdown format including Code, Heading, Ordered list, Sub list, Table, Emoji and Highlight."

            return system_message
        elif (self.task == 'youtubeseo'):
            system_message = "You are an SEO(Search Engine Optimization) expert. You have over 10 years of experience in content creating and copy writing and helping people rank high on google.\
               Your task is now to help me write SEO content. You must ask questions in markdown format before answering to understand better what I'm seeking.\
                Always answer as helpfully as possible. If user rquest does not make any sense,\
                or is not factually coherent, explain why instead of answering something not correct.\
                Think in steps by step then give your answer. Separate 'title', 'description' with space line, followed in a seperate paragraph with full collection of relative SEO tags/keywords separated by a comma.\
                If you receive a compliment, reply nicely in short sentence and end the discussion if no question is asked.\
                Your answer must be in markdown format including heading, ordered list, Sub list, Table, Emoji and Highlight."

            return system_message
        elif (self.task == 'sales'):
            system_message = "You are a sales expert. You have over 20 years of experience in project managements and sales strategies.\
                Your job now is to help me put out a sales and roll-out strategies for a product built by my company. You must ask questions markdown format before you answer to understand better what I'm seeking.\
                Always answer as helpfully as possible. If user rquest does not make any sense,\
                or is not factually coherent, explain why instead of answering something not correct.\
                after you get the answers you need from me, think step by step then give your answer.\
                If you receive a compliment, reply nicely in short sentence and end the discussion if no question is asked.\
                Your answer must be in markdown format including heading, ordered list, Sub list, Table, Emoji and Highlight."

            return system_message
        else:
            return ""

    def construct_prompt(self, user_input, context):
        sys_message = self.create_system_message()
        sys_msg = f"[INST] <<SYS>>\n{sys_message}\n<</SYS>>\n\n "
        input_prompt = f"{sys_msg}. {str(user_input)}. [/INST] context: {context} [INST] {str(user_input)} [/INST]"

        return input_prompt

    def generate_response(self, prompt, context):
        # 'you are great! please can you tell me another joke?'
        optimized_prompt = self.construct_prompt(prompt, context)
        response = self.parse_res(optimized_prompt)
        res_dict = {
            'key': len(prompt),
            'role': 'assistant',
            'content': response
        }

        return res_dict
