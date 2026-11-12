# lighting-sql

Write SQL faster with a compact set of mnemonic Espanso text expansions. Type a short trigger, and Espanso expands it into a ready-to-edit SQL clause or template with your cursor placed where you need it.

```text
;sf;  →  SELECT
        
        FROM 
```

The triggers are designed to be composable: build a query clause by clause, then fill in the marked positions. The package follows PostgreSQL-style syntax and aims for broad ANSI SQL compatibility; some features are database-specific.

## Get started

1. Install [Espanso](https://espanso.org/install/) if you have not already.
2. Copy [`package/package.yml`](package/package.yml) into your Espanso match configuration (for example, `~/.config/espanso/match/lighting-sql.yml`).
3. Reload Espanso, then type a trigger such as `;sf;` in any text field and accept the expansion.

Triggers use semicolons, such as `;sf;` for a formatted `SELECT`/`FROM` skeleton, `;w;` for `WHERE`, and `;ij;` for an `INNER JOIN` template. The `$|$` marker in the configuration indicates the cursor position after expansion.

## What’s included

- Query clauses for `SELECT`, `FROM`, `WHERE`, ordering, grouping, joins, and set operations
- Templates for common functions, aggregates, window functions, and date/time expressions
- DDL, DML, transaction, and graph query language snippets
- Consistent multiline formatting for larger query structures

See the [full trigger reference and examples](package/README.md) for the complete list.

## Contributing

Found a typo or have an idea for a trigger? Open an issue or pull request. Please include the trigger, its expansion, and a short example of how it helps.

To run the repository’s package validation locally, install Python 3.12 and PyYAML, then run from the repository root:

```bash
python -m pip install pyyaml
python .github/scripts/validate/main.py
```

## License

This project is licensed under the [Mozilla Public License 2.0](LICENSE).
