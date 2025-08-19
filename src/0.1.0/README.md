# formatted-sql

A quick, compoundable, mnemonic-based set of abbreviations to write formatted queries.
Striving to be ANSI SQL:2023 compliant, yet based on PostgreSQL syntax.

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

The abbreviation system is designed around mnemonic patterns that mirror SQL's natural structure.
Each trigger uses uppercase letters with colons (`:trigger:`) for easy recognition and follows logical naming conventions.
The `$|$` marker indicates where your cursor will be positioned after expansion.

### Short-hands

Common shortcuts and utilities for faster SQL development.

| Trigger  | Replacement                  | Description                                                        |
| -------- | ---------------------------- | ------------------------------------------------------------------ |
| `;d;`    | `DISTINCT`                   | Distinct keyword                                                   |
| `;n;`    | `NULL`                       | NULL keyword                                                       |
| `;nn;`   | `NOT NULL`                   | NOT NLL keyword                                                    |
| `;ie;`   | `IF EXISTS`                  | In-line existance conditional                                      |
| `;ife;`  | `IF NOT EXISTS`              | In-line non-existance conditional                                  |
| `;btw;`  | `BETWEEN $\|$ AND`           | Range between boolean                                              |
| `;btws;` | `BETWEEN SYMMETRIC $\|$ AND` | Symmetric range between boolean                                    |
| `;l;`    | `LIKE '$\|$'`                | SQL comparator                                                     |
| `;nl;`   | `NOT LIKE '$\|$'`            | SQL negated comparator                                             |
| `;st;`   | `SIMILAR TO '$\|$'`          | SQL regex comparator                                               |
| `;nst;`  | `NOT SIMILAR TO '$\|$'`      | SQL negated regetx comparator                                      |
| `;in;`   | `IN ($\|$)`                  | In-line is-in boolean operator                                     |
| `;ex;`   | `EXISTS (\n\t$\|$\n)`        | Boolean operator: true when argument query returns any row         |
| `;some;` | `SOME (\n\t$\|$\n)`          | Boolean RHS: allowing an operator to check against argument column |
| `;and;`  | `\n\tAND ($\|$)`             | Boolean AND operator                                               |
| `;or;`   | `\n\tOR ($\|$)`              | Boolean OR operator                                                |

### Functions

Supported functions and operators with mnemonic triggers.

| Trigger      | Replacement                 | Description                                               |
| ------------ | --------------------------- | --------------------------------------------------------- |
| `;coal;`     | `COALESCE($\|$, )`          | Concatenate two or more strings                           |
| `;corr;`     | `CORR($\|$, )`              | Correlation between two values                            |
| `;cast;`     | `CAST($\|$ AS )`            | Cast operator                                             |
| `;round;`    | `ROUND($\|$, 2)`            | Mathematical round operator                               |
| `;sub;`      | `SUBSTRING($\|$ FROM FOR )` | Extract substring                                         |
| `;substr;`   | `SUBSTRING($\|$, , )`       | Extract substring (compact)                               |
| `;low;`      | `LOWER($\|$)`               | Make string lowercase                                     |
| `;upp;`      | `UPPER($\|$)`               | Make string uppercase                                     |
| `;incap;`    | `INITCAP($\|$)`             | Make string titlecase                                     |
| `;len;`      | `LENGTH($\|$)`              | Return length (in bytes)                                  |
| `;clen;`     | `CHAR_LENGTH($\|$)`         | Return number of characters                               |
| `;pos;`      | `POSITION('$\|$' IN )`      | Extract index of substring                                |
| `;spos;`     | `STRPOS($\|$, '')`          | Extract index of substring (compact)                      |
| `;left;`     | `LEFT($\|$, )`              | Extract n characters from left.                           |
| `;right;`    | `RIGHT($\|$, )`             | Extract n characters from right                           |
| `;rep;`      | `REPLACE($\|$, , )`         | Replace substring                                         |
| `;rev;`      | `REVERSE($\|$)`             | Reverse substring                                         |
| `;trim;`     | `TRIM()`                    | Trim substring (default spaces from both sides)           |
| `;rtrim;`    | `RTRIM($\|$, )`             | Trim substring (default spaces from right)                |
| `;ltrim;`    | `LTRIM($\|$, )`             | Trim substring (default spaces from left)                 |
| `;lpad;`     | `LPAD($\|$, )`              | Apply left padding of n characters (default padding `*`)  |
| `;rpad;`     | `RPAD($\|$, )`              | Apply right padding of n characters (default padding `*`) |
| `;sa;`       | `STRING_AGG($\|$, )`        | Aggegate column into a string using separator             |
| `;any;`      | `ANY ($\|$)`                | Operator RHS to checks against all elements of an array   |
| `;contains;` | `@> ARRAY['$\|$']`          | Check if a string is prensent in array                    |

#### Datetime

Supported date and time functions.

| Trigger   | Replacement           | Description                                                  |
| --------- | --------------------- | ------------------------------------------------------------ |
| `;extr;`  | `EXTRACT($\|$ FROM )` | Extract entity from DATE/INTERVAL/TIMESTAMP(TZ)              |
| `;inter;` | `INTERVAL '$\|$'`     | Define interval from string                                  |
| `;date;`  | `DATE '$\|$'`         | Define date from string                                      |
| `;ts;`    | `TIMESTAMP '$\|$'`    | Define timestamp from string                                 |
| `;tsz;`   | `TIMESTAMPTZ '$\|$'`  | Define timestamp (with timezone) from string                 |
| `;time;`  | `TIME '$\|$'`         | Define time from string                                      |
| `;ol;`    | `OVERLAPS ('$\|$', )` | Check whether previous interval overlaps with the argument   |
| `;age;`   | `AGE($\|$)`           | Substract two timestamps (denfault to now with one argument) |

#### Conditionals

Supported conditional statements.

| Trigger    | Replacement         | Description                            |
| ---------- | ------------------- | -------------------------------------- |
| `;case;`   | `CASE $\|$\nEND`    | Begin conditional block                |
| `;caseas;` | `CASE $\|$\nEND AS` | Begin conditional block (ensure alias) |
| `;when;`   | `WHEN $\|$ THEN`    | Begin branch expression                |

### DQL (Data Query Language)

Expansions for querying and retrieving data from the database.

| Trigger  | Replacement              | Description                                 |
| -------- | ------------------------ | ------------------------------------------- |
| `;with;` | `WITH $\|$ AS (\n\t\n)`  | Begin a CTE clause                          |
| `;as;`   | `,\n$\|$ AS (\n\t\n)`    | Continue with another CTE                   |
| `;s;`    | `SELECT $\|$`            | Single select keyword                       |
| `;f;`    | `FROM $\|$`              | Single from keyword                         |
| `;sf;`   | `SELECT\n\nFROM $\|$ AS` | Combined Select-From clause                 |
| `;w;`    | `WHERE $\|$`             | Declare column level filtering              |
| `;h;`    | `HAVING $\|$`            | Declare filtering at aggregation level      |
| `;ob;`   | `ORDER BY $\|$`          | Begin ordering clause                       |
| `;obd;`  | `ORDER BY $\|$ DESC`     | Begin descending ordering clause            |
| `;oba;`  | `ORDER BY $\|$ ASC`      | Begin ordering clause (explictly ascending) |

#### Sampling

Supported sampling methods to attach to the FROM clause.

| Trigger     | Replacement                                 | Description                                              |
| ----------- | ------------------------------------------- | -------------------------------------------------------- |
| `;sample;`  | `TABLESAMPLE SYSTEM ($\|$)`                 | Randomly samples a given fraction of rows from the table |
| `;rsample;` | `TABLESAMPLE SYSTEM ($\|$) REPEATABLE()`    | Random sampling with deterministic seed                  |
| `;berm;`    | `TABLESAMPLE BERMOULLI ($\|$)`              | Bermolli sampling methods for uniform sampling           |
| `;rberm;`   | `TABLESAMPLE BERMOULLI ($\|$) REPEATABLE()` | Bemoulli sampling with deterministic seed                |

#### Aggregates

Supported aggregate functions with explanatory alias.

| Trigger     | Replacement               | Description                                               |
| ----------- | ------------------------- | --------------------------------------------------------- |
| `;gb;`      | `GROUP BY $\|$`           | Begin grouping clause                                     |
| `;cube;`    | `CUBE($\|$, )`            | Declare the columns that make up the cube                 |
| `;roll;`    | `ROLLUP($\|$)`            | Pick one or more column to rollup against                 |
| `;gs;`      | `GROUPING SETS(\n$\|$\n)` | Grouping sets for advenced aggregation fine-tuning        |
| `;count;`   | `COUNT($\|$)`             | Scalar number of specified rows (\* to include null rows) |
| `;countas;` | `COUNT($\|$) AS`          | Count with alias clause                                   |
| `;sum;`     | `SUM($\|$)`               | Returns scalar sum of values in column                    |
| `;sumas;`   | `SUM($\|$) AS`            | Sum with alias clause                                     |
| `;avg;`     | `AVG($\|$)`               | Return scalar average of values in column                 |
| `;avgas;`   | `AVG($\|$) AS`            | Average with alias clause                                 |
| `;max;`     | `MAX($\|$)`               | Return scalar maximum of values in column                 |
| `;maxas;`   | `MAX($\|$) AS`            | Max with alias clause                                     |
| `;min;`     | `MIN($\|$)`               | Return scalar minimum of values in column                 |
| `;minas;`   | `MIN($\|$) AS`            | Min with alias clause                                     |
| `;std;`     | `STDDEV($\|$)`            | Return scalar starndard deviation of values in column     |
| `;stdas;`   | `STDDEV($\|$) AS`         | Stddev with alias clause                                  |

#### Window Functions

Supported window functions with explanatory alias.

| Trigger   | Replacement                   | Description                                                                   |
| --------- | ----------------------------- | ----------------------------------------------------------------------------- |
| `;win;`   | `WINDOW $\|$ AS ()`           | Create a common window clause to share across multiple functions              |
| `;over;`  | `OVER($\|$)`                  | Specify the window range (default to whole column)                            |
| `;pb;`    | `PARTITION BY `               | Specify the columns over which create multiple windows                        |
| `;rnum;`  | `ROW_NUMBER() OVER($\|$) AS`  | Rank rows (if same values, assign random order)                               |
| `;rank;`  | `RANK() OVER($\|$) AS`        | Rank rows (same rank for equal values, increment by degeneracy)               |
| `;drank;` | `DENSE_RANK() OVER($\|$) AS`  | Rank rows in window (same rank for equal values, but always increment by one) |
| `;first;` | `FIRST_VALUE($\|$) OVER() AS` | Return first value over the window                                            |
| `;last;`  | `LAST_VALUE($\|$) OVER() AS`  | Return last value over the window                                             |
| `;lag;`   | `LAG($\|$) OVER() AS`         | Slide argument column forward (default by one)                                |
| `;lead;`  | `LEAD($\|$) OVER() AS`        | Slide argument column backward (default by one)                               |
| `;ntile;` | `NTILE($\|$) OVER() AS`       | Divide column in n buckets, return bucket number on row                       |

##### window frames

| Trigger | Replacement | Description |
| ------- | ----------- | ----------- |

- trigger: ";rowb;"
  replace: "ROWS BETWEEN $|$ AND"
- trigger: ";ranb;"
  replace: "range BETWEEN $|$ AND"
- trigger: ";prec;"
  replace: "PRECEDING"
- trigger: ";unprec;"
  replace: "UNBOUNDED PRECEDING"
- trigger: ";foll;"
  replace: "FOLLOWING"
- trigger: ";unfoll;"
  replace: "UNBOUNDED FOLLOWING"
- trigger: ";cr;"
  replace: "CURRENT ROW"

#### Joins

Supported join and union types .

| Trigger | Replacement                | Description                |
| ------- | -------------------------- | -------------------------- |
| `:ij:`  | `INNER JOIN $\|$ AS\n\tON` | Inner join with alias      |
| `:lj:`  | `LEFT JOIN $\|$ AS\n\tON`  | Left join with alias       |
| `:rj:`  | `RIGHT JOIN $\|$ AS\n\tON` | Right join with alias      |
| `:fj:`  | `FULL JOIN $\|$ AS\n\tON`  | Full outer join with alias |
| `:u:`   | `\n\tUNION\n`              | Union operator             |
| `:ua:`  | `\n\tUNION ALL\n`          | Union all operator         |

### DDL (Data Definition Language)

Expansions for defining and modifying database structure.

| Trigger | Replacement                           | Description               |
| ------- | ------------------------------------- | ------------------------- |
| `:cd:`  | `CREATE DATABASE $\|$;`               | Create database statement |
| `:ci:`  | `CREATE INDEX $\|$\n\tON tbl (cols);` | Create index statement    |
| `:ct:`  | `CREATE TABLE $\|$ (\n\n);`           | Create table              |
| `:cta:` | `CREATE TABLE $\|$ AS\n`              | Create table as select    |
| `:cva:` | `CREATE VIEW $\|$ AS\n`               | Create view statement     |
| `:ad:`  | `ALTER DATABASE $\|$`                 | Alter database statement  |
| `:at:`  | `ALTER TABLE $\|$`                    | Alter table statement     |
| `:av:`  | `ALTER VIEW $\|$`                     | Alter view statement      |
| `:dd:`  | `DROP DATABASE $\|$;`                 | Drop database statement   |
| `:di:`  | `DROP INDEX $\|$;`                    | Drop index statement      |
| `:dt:`  | `DROP TABLE $\|$;`                    | Drop table statement      |
| `:co:`  | `COMMENT '$\|$' ON`                   | Attach comment clause     |
| `:re:`  | `RENAME $\|$ TO`                      | Rename object clause      |
| `:tr:`  | `TRUNCATE TABLE '$\|$';`              | Rename object clause      |

#### Constraints

Supported constraints on DDL

| Trigger | Replacement                     | Description                        |
| ------- | ------------------------------- | ---------------------------------- |
| `:pk:`  | `PRIMARY KEY`                   | Primary key constraint             |
| `:fk:`  | `FOREING KEY ($\|$) REFERENCES` |
| `:un:`  | `UNIQUE ($\|$)`                 | Unique constraint                  |
| `:nd:`  | `NULLS DISTINCT`                | Some unique constraint can be null |
| `:nnd:` | `NULLS NOT DISTINCT`            | No unique constraint can be null   |

### DCL (Data Control Language)

Expansions for managing permissions and access control.

| Trigger | Replacement        | Description                  |
| ------- | ------------------ | ---------------------------- |
| `:go:`  | `GRANT  OPTION`    | atomic GRANT OPTION clause   |
| `:got:` | `GRANT  ON  TO`    | Grant permissions statement  |
| `:rof:` | `REVOKE  ON  FROM` | Revoke permissions statement |
| `:cs:`  | `CASCADE;`         | Revoke cascade final clause  |

### DML (Data Manipulation Language)

Expansions for inserting, updating, and deleting data.

| Trigger | Replacement                                 | Description                  |
| ------- | ------------------------------------------- | ---------------------------- |
| `:iis:` | `INSERT INTO $\|$ (cols)\n\tVALUES ()`      | Insert statement with values |
| `:up:`  | `UPDATE $\|$\nSET`                          | Update statement template    |
| `:df:`  | `DELETE FROM`                               | Delete statement             |
| `:ex:`  | `EXPLAIN PLAN FOR\n`                        | Explain plan                 |
| `:lc:`  | `LOCK $\|$ IN`                              | Lock object clause           |
| `:cpa:` | `CREATE PROCEDURE '$\|$' AS\nBEGIN\n\nEND;` | Create procedure statement   |
| `:cp:`  | `CALL $\|$();`                              | Call procedure clause        |

### TCL (Transaction Control Language)

Expansion for managing transactional control

| Trigger | Replacement               | Description                 |
| ------- | ------------------------- | --------------------------- |
| `:bt:`  | `BEGIN TRANSACTION $\|$;` | Begin transaction statement |
| `:c:`   | `COMMIT;`                 | End transaction statement   |
| `:r:`   | `ROLLBACK;`               | Rollback statement          |
| `:s:`   | `SAVEPOINT $\|$ IN`       | Save checkpoint clause      |

### GQL (Graph Query Language)

Manipulate property graphs.

| Trigger | Replacement | Description |
| ------- | ----------- | ----------- |

# TODO: complete table

## Usage Examples

Here are some examples of how these abbreviations compose together:

### Basic Query

Type: `:SF:id<arrow-down><return>:W:status = 'active'<return>:OR: created_at;`
to obtain:

```sql
SELECT
    id
FROM user
WHERE status = 'active'
ORDER BY created_at;
```

**Complex Join:**

# TODO: clean examples below

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
