import glob
from rdflib import Graph
import pytest

# Collect all Turtle files under rdf/ and data/, skipping templates and test data
ttl_files = [
    f for f in (glob.glob('rdf/**/*.ttl', recursive=True) + glob.glob('data/**/*.ttl', recursive=True))
    if 'template' not in f and not f.startswith('rdf/__')
]

@pytest.mark.parametrize('ttl_file', ttl_files)
def test_parse_ttl_files(ttl_file):
    g = Graph()
    g.parse(ttl_file, format='turtle')
