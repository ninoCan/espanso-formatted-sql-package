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
| `:NN:` | `NOT NULL` | Not null constraint | ✅ |
| `:PK:` | `PRIMARY KEY` | Primary key constraint | ✅ |
| `:FK:` | `FOREING KEY ($\|$) REFERENCES tbl(col)` | Foreign key constraint | ✅ |
| `:IE:` | `IF EXISTS ` | If exists clause | ✅ |
| `:INE:` | `IF NOT EXISTS ` | If not exists clause | ✅ |
| `:BTW:` | `BETWEEN $\|$ AND` | Between range operator | ✅ |
| `:L:` | `LIKE '$\|$'` | Like pattern matching | ✅ |
| `:NL:` | `NOT LIKE '$\|$'` | Not like pattern matching | ✅ |
| `:IN:` | `IN ($\|$)` | In list operator | ✅ |

### DQL (Data Query Language)

Expansions for querying and retrieving data from the database.

| Trigger | Replacement | Description | Implemented |
|---------|-------------|-------------|-------------|
| `:G:` | `GROUP BY $\|$` | Group by clause | ✅ |
| `:H:` | `HAVING ($\|$)` | Having clause | ✅ |
| `:OR:` | `ORDER BY $\|$` | Order by ascending | ✅ |
| `:ORD:` | `ORDER BY $\|$ DESC` | Order by descending | ✅ |
| `:SF:` | `SELECT\n\t$\|$\nFROM tbl AS` | Select statement with formatted layout | ✅ |
| `:W:` | `WHERE ($\|$)` | Where clause | ✅ |
| `:O:` | `\n\tOR ($\|$)` | Or logical operator  | ✅ |
| `:A:` | `\n\tAND ($\|$)` | And logical operator  | ✅ |
| `:WE:` | `WHERE EXISTS (\n\t$\|$\n)` | Where exists subquery | ✅ |
| `:WI:` | `WITH $\|$ AS (\n\t\n)` | Common Table Expression (CTE) | ✅ |
| `:AS:` | `,\n$\|$ AS (\n\t\n)` | CTE continuation | ✅ |

### Joins

Supported join and union types .

| Trigger | Replacement | Description | Implemented |
| `:IJ:` | `INNER JOIN $\|$ AS\n\tON ` | Inner join with alias | ✅ |
| `:LJ:` | `LEFT JOIN $\|$ AS\n\tON ` | Left join with alias | ✅ |
| `:RJ:` | `RIGHT JOIN $\|$ AS\n\tON ` | Right join with alias | ✅ |
| `:FJ:` | `FULL JOIN $\|$ AS\n\tON ` | Full outer join with alias | ✅ |
| `:U:` | `\n\tUNION\n` | Union operator | ✅ |
| `:UA:` | `\n\tUNION ALL\n` | Union all operator | ✅ |

### DDL (Data Definition Language)

Expansions for defining and modifying database structure.

| Trigger | Replacement | Description | Implemented |
|---------|-------------|-------------|-------------|
| `:CD:` | `CREATE DATABASE $\|$;` | Create database statement | ✅ |
| `:CI:` | `CREATE INDEX $\|$\n\tON tbl (cols);` | Create index statement | ✅ |
| `:CT:` | `CREATE TABLE $\|$ (\n\n);` | Create table | ✅ |
| `:CTA:` | `CREATE TABLE $\|$ AS\n` | Create table as select | ✅ |
| `:CVA:` | `CREATE VIEW $\|$ AS\n` | Create view statement | ✅ |
| `:AD:` | `ALTER DATABASE $\|$` | Alter database statement | ✅ |
| `:AT:` | `ALTER TABLE $\|$` | Alter table statement | ✅ |
| `:AV:` | `ALTER VIEW $\|$` | Alter view statement | ✅ |
| `:DD:` | `DROP DATABASE $\|$;` | Drop database statement | ✅ |
| `:DI:` | `DROP INDEX $\|$;` | Drop index statement | ✅ |
| `:DT:` | `DROP TABLE $\|$;` | Drop table statement | ✅ |
| `:CO:` | `COMMENT '$\|$' ON` | Attach comment clause | ✅ |
| `:RE:` | `RENAME $\|$ TO` | Rename object clause | ✅ |
| `:TR:` | `TRUNCATE TABLE '$\|$';` | Rename object clause | ✅ |

### DCL (Data Control Language)

Expansions for managing permissions and access control.

| Trigger | Replacement | Description | Implemented |
|---------|-------------|-------------|-------------|
| `:GO:` | `GRANT  OPTION` | atomic GRANT OPTION clause | ✅ |
| `:GOT:` | `GRANT  ON  TO ` | Grant permissions statement | ✅ |
| `:ROF:` | `REVOKE  ON  FROM ` | Revoke permissions statement | ✅ |
| `:CS:` | `CASCADE;` | Revoke cascade final clause | ✅ |
| `:GDOT:` | `GRANT DELETE ON  TO ` | Grant delete permission | ✅ |

### DML (Data Manipulation Language)

Expansions for inserting, updating, and deleting data.

| Trigger | Replacement | Description | Implemented |
|---------|-------------|-------------|-------------|
| `:INS:` | `INSERT INTO $\|$ (cols)\n\tVALUES ()` | Insert statement with values | ✅ |
| `:UP:` | `UPDATE $\|$\nSET` | Update statement template | ✅ |
| `:DEL:` | `DELETE FROM` | Delete statement | ✅ |
| `:EX:` | `EXPLAIN PLAN FOR\n` | Explain plan | ✅ |
| `:LC:` | `LOCK $|$ IN` | Lock object clause | ✅ |
| `:EX:` | `EXPLAIN PLAN FOR\n` | Explain plan | ✅ |

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
