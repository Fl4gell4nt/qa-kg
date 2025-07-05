# 📛 RDF Naming Policy for `qa-kg`

This document defines naming conventions for all RDF resources, files, and components in your Personal Knowledge Management System (PKMS) focused on Software Quality Assurance and Semantic Knowledge Representation.

---

## 1. General Principles

| Principle           | Description                                                              |
|---------------------|--------------------------------------------------------------------------|
| ✅ Clarity          | Use meaningful, unambiguous names.                                       |
| ✅ Consistency      | Follow the same naming pattern across all modules.                       |
| ✅ Scope Separation | Distinguish clearly between concepts, files, modules, etc.               |
| ✅ Language-Agnostic| Avoid whitespace, special characters, and localized words in IRIs.       |

---

## 2. Ontology Module & File Naming

### Format:
ontologies/{module-name}/{version}/module-name.ttl

markdown
Copy
Edit

### Examples:
- `ontologies/upper/0.1.0/upper.ttl`
- `ontologies/scrum/0.1.0/scrum.ttl`
- `ontologies/people-org/0.1.0/people-org.ttl`

---

## 3. Namespace and Prefix Naming

| Context             | Prefix   | Example                         |
|---------------------|----------|---------------------------------|
| Upper Ontology      | `upper:` | `upper:Agent`                   |
| Scrum Ontology      | `scrum:` | `scrum:Sprint`                  |
| Glossary SKOS       | `gl:`    | `gl:AcceptanceTest`             |
| People & Org        | `org:`   | `org:Department`                |
| QA Domain Ontology  | `qa:`    | `qa:TestCase`                   |
| Shapes (SHACL)      | `sh:`    | `sh:SprintShape`                |

---

## 4. Class Naming

- **Style:** PascalCase  
- **Type:** Nouns only  
- **Form:** Singular  
- **Avoid:** Underscores, numbers, or abbreviations unless well-known

**Examples:**
- `qa:TestCase`
- `scrum:ScrumRole`
- `org:Employee`

---

## 5. Property Naming

- **Style:** camelCase  
- **Object Properties:** Verb-like (e.g., `hasRole`, `reportsBug`)  
- **Datatype Properties:** Descriptive (e.g., `testCaseId`, `createdAt`)

**Examples:**
- `qa:hasTestResult`
- `qa:createdAt`

---

## 6. Instance Naming

- **Style:** kebab-case or lowerCamelCase  
- **Globally Unique:** Include identifying context (e.g., dates, IDs)

**Examples:**
- `data:sprint42`
- `data:daily-scrum-2025-07-01`
- `data:product-owner-schweidler`

---

## 7. SKOS Concept Naming (Glossary)

- **Prefix:** `gl:`  
- **Style:** PascalCase  
- **Type:** Always use `skos:Concept`

**Examples:**
- `gl:RegressionTest`
- `gl:BugSeverity`
- `gl:AcceptanceCriteria`

---

## 8. SHACL Shape Naming

- **Prefix:** `sh:`  
- **Style:** PascalCase  
- **Type:** `sh:NodeShape` or `sh:PropertyShape`

**Examples:**
- `sh:TestCaseShape`
- `sh:ScrumEventShape`

---

## 9. IRI & Base Naming

Use a clear, persistent, and human-readable IRI base:

https://w3id.org/schweidler/semantics/qa-kg/{module}/[resource]

markdown
Copy
Edit

### Examples:
- `https://w3id.org/schweidler/semantics/qa-kg/scrum/Sprint`
- `https://w3id.org/schweidler/semantics/qa-kg/qa-domain/TestCase`

---

## 10. Annotation Guidelines

Each `owl:Class` and `owl:ObjectProperty` must include:

- `rdfs:label` (with language tag, e.g. `@en`)
- `rdfs:comment` for a short definition
- Optionally: `skos:scopeNote`, `dct:description`

### Example:
```turtle
qa:TestCase a owl:Class ;
    rdfs:label "Test Case"@en ;
    rdfs:comment "A unit of testing that specifies input, execution conditions, and expected results."@en ;
    skos:scopeNote "Used to validate that a specific functionality behaves as expected under defined conditions."@en .
This document is the canonical style guide for the QA Knowledge Graph and should be followed when curating or extending RDF resources.
```

## 11. File Naming Conventions

All RDF file names should use **kebab-case** (lowercase with hyphens) and follow this format:

**{domain|module}-{type}.ttl**

#### Components:
- `{domain|module}` — short, lowercase name for the domain or module (e.g. `qa`, `scrum`, `org`)
- `{type}` — purpose of the file, selected from:
  - `ontology` — OWL ontology
  - `glossary` — SKOS-based concept collection
  - `vocabulary` — controlled list of properties or terms
  - `taxonomy` — hierarchical structure (e.g. `skos:broader`)
  - `shapes` — SHACL shapes for validation
  - `data` — instance data
  - `mappings` — links or alignments to other ontologies
  - `imports` — owl:imports declarations for grouping files

#### ✅ Examples:

| File Name                  | Description                                             |
|---------------------------|---------------------------------------------------------|
| `qa-glossary.ttl`         | Glossary of QA-related concepts                         |
| `qa-taxonomy.ttl`         | Subsumption hierarchy of QA concepts                    |
| `qa-ontology.ttl`         | Main QA domain ontology                                 |
| `scrum-ontology.ttl`      | Ontology for Scrum processes and roles                  |
| `artifacts-vocabulary.ttl`| Controlled list of work artifact types                  |
| `org-ontology.ttl`        | Organization, roles, and person modeling                |
| `qa-shapes.ttl`           | SHACL shapes for QA model validation                    |
| `qa-data.ttl`             | Sample data instances for the QA domain                 |
| `qa-mappings.ttl`         | Alignments to FOAF, DUL, Dublin Core, etc.              |
| `qa-imports.ttl`          | File aggregating owl:imports of all QA modules          |

#### 📌 Rules:
- Use `.ttl` extension for all Turtle files.
- Avoid version numbers in file names. Versioning is handled by folder structure (e.g. `ontologies/qa/0.1.0/qa-ontology.ttl`).
- Keep names short, precise, and meaningful.
- Avoid generic names like `core.ttl` or `model.ttl`.
- Use singular nouns for module names, unless the file is a taxonomy or glossary.