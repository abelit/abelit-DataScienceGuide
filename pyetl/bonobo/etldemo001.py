import requests
import bonobo
FABLABS_API_URL = 'https://public-us.opendatasoft.com/api/records/1.0/search/?dataset=fablabs&rows=1000'


def extract_fablabs():
    yield from requests.get(FABLABS_API_URL).json().get('records')

def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(
        extract_fablabs,
        bonobo.Limit(10),
        bonobo.PrettyPrinter(),
    )
    return graph

if __name__ == "__main__":
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser):
        bonobo.run(get_graph())