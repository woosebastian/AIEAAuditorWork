# https://python.langchain.com/docs/integrations/chat/openai/
# https://python.langchain.com/docs/integrations/chat/openai/
# https://python.langchain.com/docs/integrations/chat/openai/
# https://python.langchain.com/docs/integrations/chat/openai/
# https://platform.openai.com/settings/organization/limits
# https://platform.openai.com/settings/organization/limits
# https://community.openai.com/t/error-code-429-you-exceeded-your-current-quota-please-check-your-plan-and-billing-details/649547/2
# https://platform.openai.com/docs/guides/text-generation?lang=python
# https://chatgpt.com/share/673522c5-616c-800e-a879-e4b9981723c3
# https://chatgpt.com/share/673522c5-616c-800e-a879-e4b9981723c3

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
    # base_url="...",
    organization="org-XcGdFUKpxIrCzhNPDdpsMvbN",
    # organization="AIEA",
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant.",
    ),
    ("human", "What are the differences between CPUs and GPUs?"),
    ("human", "Translate your response into Prolog.")
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)

# from openai import OpenAI
# client = OpenAI()

# completion = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming."
#         }
#     ]
# )

# print(completion.choices[0].message)

## TODO: use the Python wrapper for Prolog to run the Prolog code

# from pylog import Prolog
from pyswip import Prolog

# Create a Prolog instance
prolog = Prolog()

# % Purpose
prolog.assertz('purpose(cpu, general_purpose)')
prolog.assertz('purpose(gpu, parallel_processing)')

# % Architecture
prolog.assertz('architecture(cpu, few_cores_large_cache)')
prolog.assertz('architecture(gpu, many_cores_small_cache)')

# % Performance
prolog.assertz('performance(cpu, high_single_threaded)')
prolog.assertz('performance(gpu, superior_parallel)')

# % Power Consumption
prolog.assertz('power_consumption(cpu, less_power)')
prolog.assertz('power_consumption(gpu, more_power)')

# % Flexibility
prolog.assertz('flexibility(cpu, more_flexible)')
prolog.assertz('flexibility(gpu, less_flexible)')





# Define some Prolog facts and rules
# prolog.assertz("father(john, mary)")
# prolog.assertz("father(john, sam)")
# prolog.assertz("mother(susan, mary)")
# prolog.assertz("parent(X, Y) :- father(X, Y)")
# prolog.assertz("parent(X, Y) :- mother(X, Y)")

# # Run a query on the Prolog database
# results = list(prolog.query("parent(john, Y)"))

# # Print the results
# for result in results:
#     print(result)