# formatted-sql

A quick, composable, mnemonic-based set of abbreviations to write formatted ANSI:2023 SQL queries.

## Motivations

Other existing SQL expansion packages suffer from significant limitations that hinder developer productivity:

- **Closed-source solutions** often come with licensing restrictions and cannot be customized to fit specific team workflows or coding standards
- **Non-modular triggers** require the user to delete quite a lot of the expansion, defying the purpose
- **Poor formatting** produces SQL that lacks consistent indentation, and readability standards

This package addresses these issues by providing:
- **Modular design** allowing you to compose complex queries from simple, reusable components
- **Mnemonic triggers** that follow intuitive patterns based on SQL keywords and common abbreviations
- **Consistent formatting** that produces clean, readable SQL following modern best practices

## Abbreviations

The abbreviation system is designed around mnemonic patterns that mirror SQL's natural structure. Each trigger uses uppercase letters with colons (`:TRIGGER:`) for easy recognition and follows logical naming conventions. The `$|$` marker indicates where your cursor will be positioned after expansion.

### Shorthands

Common shortcuts and utilities for faster SQL development.

| Trigger | Replacement | Description | Implemented |
|---------|-------------|-------------|-------------|
| `:nn:` | `NOT NULL` | Not null constraint | ✅ |
| `:pk:` | `PRIMARY KEY` | Primary key constraint | ✅ |
| `:fk:` | `FOREING KEY ($\|$) REFERENCES tbl(col)` | Foreign key constraint | ✅ |
| `:ie:` | `IF EXISTS ` | If exists clause | ✅ |
| `:ine:` | `IF NOT EXISTS ` | If not exists clause | ✅ |
| `:btw:` | `BETWEEN $\|$ AND` | Between range operator | ✅ |
| `:l:` | `LIKE '$\|$'` | Like pattern matching | ✅ |
| `:nl:` | `NOT LIKE '$\|$'` | Not like pattern matching | ✅ |
| `:in:` | `IN ($\|$)` | In list operator | ✅ |

### DQL (Data Query Language)

Expansions for querying and retrieving data from the database.

| Trigger | Replacement | Description | Implemented |
|---------|-------------|-------------|-------------|
| `:g:` | `GROUP BY $\|$` | Group by clause | ✅ |
| `:h:` | `HAVING ($\|$)` | Having clause | ✅ |
| `:or:` | `ORDER BY $\|$` | Order by ascending | ✅ |
| `:ord:` | `ORDER BY $\|$ DESC` | Order by descending | ✅ |
| `:sf:` | `SELECT\n\t$\|$\nFROM tbl AS` | Select statement with formatted layout | ✅ |
| `:wh:` | `WHERE ($\|$)` | Where clause | ✅ |
| `:or:` | `\n\tOR ($\|$)` | Or logical operator  | ✅ |
| `:and:` | `\n\tAND ($\|$)` | And logical operator  | ✅ |
| `:we:` | `WHERE EXISTS (\n\t$\|$\n)` | Where exists subquery | ✅ |
| `:wi:` | `WITH $\|$ AS (\n\t\n)` | Common Table Expression (CTE) | ✅ |
| `:as:` | `,\n$\|$ AS (\n\t\n)` | CTE continuation | ✅ |

### Joins

Supported join and union types .

| Trigger | Replacement | Description | Implemented |
| `:ij:` | `INNER JOIN $\|$ AS\n\tON ` | Inner join with alias | ✅ |
| `:lj:` | `LEFT JOIN $\|$ AS\n\tON ` | Left join with alias | ✅ |
| `:rj:` | `RIGHT JOIN $\|$ AS\n\tON ` | Right join with alias | ✅ |
| `:fj:` | `FULL JOIN $\|$ AS\n\tON ` | Full outer join with alias | ✅ |
| `:u:` | `\n\tUNION\n` | Union operator | ✅ |
| `:ua:` | `\n\tUNION ALL\n` | Union all operator | ✅ |

### DDL (Data Definition Language)

Expansions for defining and modifying database structure.

| Trigger | Replacement | Description | Implemented |
|---------|-------------|-------------|-------------|
| `:cd:` | `CREATE DATABASE $\|$;` | Create database statement | ✅ |
| `:ci:` | `CREATE INDEX $\|$\n\tON tbl (cols);` | Create index statement | ✅ |
| `:ct:` | `CREATE TABLE $\|$ (\n\n);` | Create table | ✅ |
| `:cta:` | `CREATE TABLE $\|$ AS\n` | Create table as select | ✅ |
| `:cva:` | `CREATE VIEW $\|$ AS\n` | Create view statement | ✅ |
| `:ad:` | `ALTER DATABASE $\|$` | Alter database statement | ✅ |
| `:at:` | `ALTER TABLE $\|$` | Alter table statement | ✅ |
| `:av:` | `ALTER VIEW $\|$` | Alter view statement | ✅ |
| `:dd:` | `DROP DATABASE $\|$;` | Drop database statement | ✅ |
| `:di:` | `DROP INDEX $\|$;` | Drop index statement | ✅ |
| `:dt:` | `DROP TABLE $\|$;` | Drop table statement | ✅ |
| `:co:` | `COMMENT '$\|$' ON` | Attach comment clause | ✅ |
| `:re:` | `RENAME $\|$ TO` | Rename object clause | ✅ |
| `:tr:` | `TRUNCATE TABLE '$\|$';` | Rename object clause | ✅ |

### DCL (Data Control Language)

Expansions for managing permissions and access control.

| Trigger | Replacement | Description | Implemented |
|---------|-------------|-------------|-------------|
| `:go:` | `GRANT  OPTION` | atomic GRANT OPTION clause | ✅ |
| `:got:` | `GRANT  ON  TO ` | Grant permissions statement | ✅ |
| `:rof:` | `REVOKE  ON  FROM ` | Revoke permissions statement | ✅ |
| `:cs:` | `CASCADE;` | Revoke cascade final clause | ✅ |

### DML (Data Manipulation Language)

Expansions for inserting, updating, and deleting data.

| Trigger | Replacement | Description | Implemented |
|---------|-------------|-------------|-------------|
| `:ins:` | `INSERT INTO $\|$ (cols)\n\tVALUES ()` | Insert statement with values | ✅ |
| `:up:` | `UPDATE $\|$\nSET` | Update statement template | ✅ |
| `:del:` | `DELETE FROM` | Delete statement | ✅ |
| `:ex:` | `EXPLAIN PLAN FOR\n` | Explain plan | ✅ |
| `:lc:` | `LOCK $|$ IN` | Lock object clause | ✅ |
| `:ex:` | `EXPLAIN PLAN FOR\n` | Explain plan | ✅ |

### TCL (Transaction Control Language)
## Usage Examples

Here are some examples of how these abbreviations compose together:

**Basic Query:**
```sql
-- Type: :SF:id<arrow-down><return>:W:status = 'active'<return>:OR: created_at;
SELECT
    id
FROM user
WHERE status = 'active'
ORDER BY created_at;
```

**Complex Join:**
```sql
-- Type: :SF: u.name, p.title :IJ: posts p :W: u.id = p.user_id
SELECT
u.name, p.title
FROM INNER JOIN posts p AS
	ON  WHERE u.id = p.user_id
```

**CTE Example:**
```sql
-- Type: :WI: active_users :SF: * FROM active_users
WITH active_users AS (

) SELECT
*
FROM active_users
```
