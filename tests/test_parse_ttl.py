import glob
from rdflib import Graph
import pytest

# Collect all Turtle files under rdf/ and data/
ttl_files = glob.glob('rdf/**/*.ttl', recursive=True) + glob.glob('data/**/*.ttl', recursive=True)

@pytest.mark.parametrize('ttl_file', ttl_files)
def test_parse_ttl_files(ttl_file):
    g = Graph()
    g.parse(ttl_file, format='turtle')
