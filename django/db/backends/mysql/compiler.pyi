# Stubs for django.db.backends.mysql.compiler (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import compiler

class SQLCompiler(compiler.SQLCompiler):
    def as_subquery_condition(self, alias, columns, compiler): ...

class SQLInsertCompiler(compiler.SQLInsertCompiler, SQLCompiler): ...
class SQLDeleteCompiler(compiler.SQLDeleteCompiler, SQLCompiler): ...
class SQLUpdateCompiler(compiler.SQLUpdateCompiler, SQLCompiler): ...
class SQLAggregateCompiler(compiler.SQLAggregateCompiler, SQLCompiler): ...
