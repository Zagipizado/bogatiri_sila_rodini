import autogen

config_list = [
    {
         'model': 'gpt-4',
    "base_url": "http://localhost:8090",
    'api_key': 'Your API key',
    "seed": 42,  # change the seed for different trials
    "temperature": 1.0,
    # "request_timeout": 120,
    }
]

gpt4_config = {"config_list": [{
        "base_url": "http://localhost:8090",
        "model": "gpt-4", "temperature": 1.0, "api_key": "123"}]}
  

user_proxy = autogen.ConversableAgent(
   name="Mother_Russia",
   system_message="You are a thought that came to the mind of the bogatyr Dobrynya Nikitich",
   code_execution_config=False,
)

Dobrynya = autogen.ConversableAgent(
    name="Dobrynya_Nikitich",
    system_message='''You are the bogatyr Dobrynya Nikitich. A strong and wise bogatyr from Russian epics. You are quite old and hardened in numerous battles with the Polovtsians.
    Your thoughts are pragmatic, you do not give in to emotions and always think soberly. Your main goal is to put an end to the Polovtsians and other enemies of Rus. You live in 9 century a.c.
''',
    llm_config=gpt4_config,
    human_input_mode="NEVER"
)

Alyosha = autogen.ConversableAgent(
    name="Alyosha_Popovich",
    llm_config=gpt4_config,
    system_message='''You are the bogatyr Alyosha Popovich from Russian epics. You were born in the glorious city of Rostov. You are still quite young and emotional, you are used to solving all problems on the fly, yielding to emotions.
    Throughout your life, you have been strong enough for this, but now you understand deep down that the danger of the Polovtsian army is too high, and your efforts may not be enough. You have the wise bogatyr Dobrynya Nikitich in your team,
    whose word you respect. Your main goal is to defeat the Polovtsian army. You live in 9 century a.c.
''',
    human_input_mode="NEVER"
)

Dobrynya.initiate_chat(recipient=Alyosha,message="You are a thought that came to the mind of the bogatyr Dobrynya Nikitich", max_turns=5)
# groupchat = autogen.GroupChat(agents=[user_proxy, Dobrynya, Alyosha], messages=[], max_round=5)
# manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

# user_proxy.initiate_chat(
#     manager,
#     message="""
# Develop a plan to defeat the Polovtsian army. Speak russian.
# """,
# )
