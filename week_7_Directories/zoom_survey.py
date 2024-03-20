survey_title = 'Survey Question - Minnesota Weather'

question = 'Do you like snow?'

yes_response_text = 'Yes!'
no_response_text = 'No'
dont_care_text = 'Don\'t care'

yes_votes = 7
no_votes = 7
dont_care_votes = 2


list_of_choices = ['Yes!', 'No', 'Don\'t care']

for choice in list_of_choices:
    print(choice)
# can solve with dictionary

results_dictionary = {
    'Yes!': 7,
    'No': 7,
    'Dont care': 2
}
# can also list - which uses [] - easy to tell difference that way - dictionaries use {}
# but can also do a dictionary of lists - which will allow us to store more info about each choice
results_list = [
    {
        'response_text': 'Yes!',
        'votes': 7,
        'percentage': 44
    },
    {
        'response_text': 'No',
        'votes': 7,
        'percentage': 44
    },
    {
        'response_text': 'Dont care',
        'votes': 2,
        'percentage': 13
    }
]

for one_result_dictionary in results_list:
    # print(result_dictionary) this is ONE dictionary
    response_text = one_result_dictionary['response_text']
    votes = one_result_dictionary['votes']
    print(f'{response_text} received {votes} votes.')
