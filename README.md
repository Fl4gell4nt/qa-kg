# Semantic Knowledge Base for QA Domain – `schweidler/semantics/qa-kg`

This repository is the foundation for a **personal semantic knowledge base (PKMS)**, designed and maintained by **Rene Schweidler** to support his professional work as a **Software Quality Assurance Engineer** in an R&D environment.

It follows semantic web best practices using **RDF/Turtle**, **Dublin Core**, **SKOS**, and custom OWL ontologies.

## 🎯 Purpose

To capture, interlink, and query domain-specific knowledge using a modular, extensible RDF/OWL structure for:

- Self-learning and documentation
- Reusable reference and semantic linking
- Long-term personal knowledge continuity

## 🧠 Ontological Modules

| File                              | Description |
|-----------------------------------|-------------|
| `rdf/core/upper-ontology.ttl`                 | Upper ontology for high-level concepts |
| `rdf/glossaries/core/core-glossary.ttl`       | SKOS glossary of QA-related terms |
| `rdf/glossaries/domain/test-glossary.ttl`     | Test domain terminology |
| `rdf/glossaries/domain/scrum-glossary.ttl`    | Scrum domain terminology |
| `rdf/vocabularies/meronymy-vocabulary.ttl`    | Meronymy Ontology |
| `rdf/taxonomies/qa-taxonomy.ttl`              | Subsumption hierarchy for QA types, activities |
| `rdf/vocabularies/scrum-vocabulary.ttl`       | Scrum-based software development modeling |
| `rdf/vocabularies/org-people-vocabulary.ttl`  | People, roles, teams, and org units |
| `rdf/vocabularies/artifacts-vocabulary.ttl`   | Knowledge artifact ontology (notes, test plans, checklists, ...) |

## 🏷️ Base IRI

This ontology is served at the following **persistent IRI namespace**:

```
https://w3id.org/schweidler/semantics/qa-kg#
```

It will resolve to this repository hosted via GitHub Pages.

## 🧰 Technologies

- RDF 1.1 Turtle syntax
- OWL 2 (lightweight profiles)
- SHACL validation (optional)
- GitHub Pages for hosting ontologies
- w3id.org for permanent IRI resolution

## 📦 Deployment

This repo is served via **GitHub Pages**, and the w3id redirect is configured under:

```
w3id.org/schweidler/semantics/qa-kg/
```

## 🛠️ Future Additions

- SHACL shape definitions
- RDF ingest pipeline for capturing daily knowledge logs
- SPARQL templates for querying
- SvelteKit-based lightweight UI for browsing

---

Maintained with ❤️ by Rene Schweidler
