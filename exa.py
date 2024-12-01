from exa_py import Exa

exa = Exa("7e5ecbba-7546-4043-81aa-00c3e4975db6")
query=input('search here:')
response=exa.search(query,
                   num_results=1,
                   type='keyword',
                   include_domains=['http://www.instagram.com'],
                    use_autoprompt=True,)
for result in response.results:
    print(f'Title:{result.title}')
    print(f'URL:{result.url}')
    print(response)