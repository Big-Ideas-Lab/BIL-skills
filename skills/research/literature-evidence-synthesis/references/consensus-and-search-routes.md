# Consensus MCP and search routes

Consensus MCP is the **mandatory discovery route in both lanes** of this skill. It is a discovery layer: it produces candidates to screen, never verification.

## Endpoint and scoping

- Official endpoint: `https://mcp.consensus.app/mcp`
- Authentication is OAuth and can be initiated without an account; the provider may then prompt for sign-in.
- Enable **only the search capability** for the active task. Do not enable unrelated tools.
- Configure the server once through the agent's MCP configuration, not per task, and never paste tokens into a skill file, repository, or chat.

If the endpoint is unreachable, unconfigured, or unauthenticated:

1. Stop the retrieval step.
2. Disclose the blocker in the deliverable and in the evidence brief's limitations.
3. Do not substitute another route and report the Consensus requirement as satisfied.

An honest disclosure is an acceptable outcome. A silent substitution is not.

## What Consensus can and cannot do

| Allowed | Not allowed |
|---|---|
| Generate candidate papers for a question | Verify that a paper supports a claim |
| Surface papers you would not have found by keyword | Supply a locator (page, table, section) |
| Provide discovery breadth quickly | Substitute for full-text retrieval |
| Suggest follow-up questions | Establish that a body of evidence is complete |

Consensus output frequently carries title, authors, year, journal, and an abstract — and sometimes no DOI. Metadata and abstracts are index records, not evidence.

## Independent routes (decision-grade)

Decision-grade work requires at least one route that is not Consensus, recorded alongside it:

- a bibliographic database query with an explicit query string and date;
- a trial or study registry lookup;
- a preprint server query;
- backward and forward citation chaining from a known eligible paper;
- an authoritative guideline or agency document search.

Record for each route: the exact query, the interface, the date, the filters applied, and the number of records returned before deduplication.

## Search ledger minimum fields

| Field | Meaning |
|---|---|
| `route` | Consensus MCP, or the named independent route |
| `query` | verbatim query string |
| `date` | timestamp of the query |
| `filters` | year range, study type, language, population filters as applied |
| `returned` | records returned before deduplication |
| `dedup_key` | DOI / PMID / title-normalized key |
| `unique` | records new after deduplication |
| `notes` | known coverage gaps for this route |

A search ledger with only one route cannot support a decision-grade review, even if it returns hundreds of records.
