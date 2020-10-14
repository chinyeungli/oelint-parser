<a name="oelint_parser.cls_item"></a>
# oelint\_parser.cls\_item

<a name="oelint_parser.cls_item.Item"></a>
## Item Objects

```python
class Item()
```

Base class for all Stash items

<a name="oelint_parser.cls_item.Item.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(origin, line, infileline, rawtext)
```

constructor

**Arguments**:

- `origin` _str_ - Full path of origin file
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line number in file
- `rawtext` _str_ - Raw input string

<a name="oelint_parser.cls_item.Item.safe_linesplit"></a>
#### safe\_linesplit

```python
 | @staticmethod
 | safe_linesplit(string)
```

Safely split an input line to chunks

**Arguments**:

- `string` _str_ - raw input string
  

**Returns**:

- `list` - list of chunks of original string

<a name="oelint_parser.cls_item.Item.get_items"></a>
#### get\_items

```python
 | get_items()
```

Return single items

**Returns**:

- `list` - lines of raw input

<a name="oelint_parser.cls_item.Item.extract_sub"></a>
#### extract\_sub

```python
 | extract_sub(name)
```

Extract modifiers

**Arguments**:

- `name` _str_ - input string
  

**Returns**:

- `tuple` - clean variable name, modifiers, package specific modifiers

<a name="oelint_parser.cls_item.Item.extract_sub_func"></a>
#### extract\_sub\_func

```python
 | extract_sub_func(name)
```

Extract modifiers for functions

**Arguments**:

- `name` _str_ - input value
  

**Returns**:

- `tuple` - clean function name, modifiers

<a name="oelint_parser.cls_item.Item.IsFromAppend"></a>
#### IsFromAppend

```python
 | IsFromAppend()
```

Item originates from a bbappend

**Returns**:

- `bool` - True if coming from a bbappend

<a name="oelint_parser.cls_item.Item.AddLink"></a>
#### AddLink

```python
 | AddLink(_file)
```

Links files to each other in stash

**Arguments**:

- `_file` _str_ - Full path of file to link against

<a name="oelint_parser.cls_item.Item.GetAttributes"></a>
#### GetAttributes

```python
 | GetAttributes()
```

Get all public attributes of this class

**Returns**:

- `dict` - all public attributes and their values

<a name="oelint_parser.cls_item.Variable"></a>
## Variable Objects

```python
class Variable(Item)
```

Stash item for variables

<a name="oelint_parser.cls_item.Variable.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(origin, line, infileline, rawtext, name, value, operator, flag)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw string
- `name` _str_ - Variable name
- `value` _str_ - Variable value
- `operator` _str_ - Operation performed to the variable
- `flag` _str_ - Optional variable flag

<a name="oelint_parser.cls_item.Variable.IsAppend"></a>
#### IsAppend

```python
 | IsAppend()
```

Check if operation is an append

**Returns**:

- `bool` - True is variable is appended

<a name="oelint_parser.cls_item.Variable.AppendOperation"></a>
#### AppendOperation

```python
 | AppendOperation()
```

Get variable modifiers

**Returns**:

- `list` - list could contain any combination of 'append', ' += ', 'prepend' and 'remove'

<a name="oelint_parser.cls_item.Variable.get_items"></a>
#### get\_items

```python
 | get_items(override="")
```

Get items of variable value

**Returns**:

- `list` - clean list of items in variable value

<a name="oelint_parser.cls_item.Variable.IsMultiLine"></a>
#### IsMultiLine

```python
 | IsMultiLine()
```

Check if variable has a multiline assignment

**Returns**:

- `bool` - True if multiline

<a name="oelint_parser.cls_item.Variable.GetMachineEntry"></a>
#### GetMachineEntry

```python
 | GetMachineEntry()
```

Get machine specific entries in variable

**Returns**:

- `str` - machine specific modifier of variable or ""

<a name="oelint_parser.cls_item.Comment"></a>
## Comment Objects

```python
class Comment(Item)
```

<a name="oelint_parser.cls_item.Comment.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(origin, line, infileline, rawtext)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw string

<a name="oelint_parser.cls_item.Comment.get_items"></a>
#### get\_items

```python
 | get_items()
```

Get single lines of block

**Returns**:

- `list` - single lines of comment block

<a name="oelint_parser.cls_item.Include"></a>
## Include Objects

```python
class Include(Item)
```

<a name="oelint_parser.cls_item.Include.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(origin, line, infileline, rawtext, incname, statement)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw string
- `incname` _str_ - raw name of the include file
- `statement` _str_ - either include or require

<a name="oelint_parser.cls_item.Include.get_items"></a>
#### get\_items

```python
 | get_items()
```

Get items

**Returns**:

- `list` - include name, include statement

<a name="oelint_parser.cls_item.Function"></a>
## Function Objects

```python
class Function(Item)
```

<a name="oelint_parser.cls_item.Function.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(origin, line, infileline, rawtext, name, body, python=False, fakeroot=False)
```

[summary]

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw string
- `name` _str_ - Raw function name
- `body` _str_ - Function body
  

**Arguments**:

- `python` _bool_ - python function according to parser (default: {False})
- `fakeroot` _bool_ - uses fakeroot (default: {False})

<a name="oelint_parser.cls_item.Function.GetMachineEntry"></a>
#### GetMachineEntry

```python
 | GetMachineEntry()
```

Get machine specific modifiers

**Returns**:

- `str` - machine specific modifier or ""

<a name="oelint_parser.cls_item.Function.IsAppend"></a>
#### IsAppend

```python
 | IsAppend()
```

Return if function appends another function

**Returns**:

- `bool` - True is append or prepend operation

<a name="oelint_parser.cls_item.Function.get_items"></a>
#### get\_items

```python
 | get_items()
```

Get items of function body

**Returns**:

- `list` - single lines of function body

<a name="oelint_parser.cls_item.PythonBlock"></a>
## PythonBlock Objects

```python
class PythonBlock(Item)
```

<a name="oelint_parser.cls_item.PythonBlock.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(origin, line, infileline, rawtext, name)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw string
- `name` _str_ - Function name

<a name="oelint_parser.cls_item.PythonBlock.get_items"></a>
#### get\_items

```python
 | get_items()
```

Get lines of function body

**Returns**:

- `list` - lines of function body

<a name="oelint_parser.cls_item.TaskAssignment"></a>
## TaskAssignment Objects

```python
class TaskAssignment(Item)
```

<a name="oelint_parser.cls_item.TaskAssignment.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(origin, line, infileline, rawtext, name, ident, value)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw string
- `name` _str_ - name of task to be modified
- `ident` _str_ - task flag
- `value` _str_ - value of modification

<a name="oelint_parser.cls_item.TaskAssignment.get_items"></a>
#### get\_items

```python
 | get_items()
```

Get items

**Returns**:

- `list` - function name, flag, modification value

<a name="oelint_parser.cls_item.TaskAdd"></a>
## TaskAdd Objects

```python
class TaskAdd(Item)
```

<a name="oelint_parser.cls_item.TaskAdd.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(origin, line, infileline, rawtext, name, before="", after="")
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `rawtext` _str_ - Raw string
- `name` _str_ - name of task to be executed
  

**Arguments**:

- `before` _str_ - before statement (default: {""})
- `after` _str_ - after statement (default: {""})

<a name="oelint_parser.cls_item.TaskAdd.get_items"></a>
#### get\_items

```python
 | get_items()
```

get items

**Returns**:

- `list` - function name, all before statements, all after statements

<a name="oelint_parser.cls_item.MissingFile"></a>
## MissingFile Objects

```python
class MissingFile(Item)
```

<a name="oelint_parser.cls_item.MissingFile.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(origin, line, infileline, filename, statement)
```

constructor

**Arguments**:

- `origin` _str_ - Full path to file of origin
- `line` _int_ - Overall line counter
- `infileline` _int_ - Line counter in the particular file
- `filename` _str_ - filename of the file that can't be found
- `statement` _str_ - either include or require

<a name="oelint_parser.const_vars"></a>
# oelint\_parser.const\_vars

variable constants

<a name="oelint_parser.const_vars.set_constantfile"></a>
#### set\_constantfile

```python
set_constantfile(obj)
```

set constants

**Arguments**:

- `obj` _dict_ - dictionary with constants

<a name="oelint_parser.const_vars.get_constantfile"></a>
#### get\_constantfile

```python
get_constantfile()
```

return currently set constants

**Returns**:

- `dict` - dictionary with constants

<a name="oelint_parser.const_vars.set_rulefile"></a>
#### set\_rulefile

```python
set_rulefile(obj)
```

set rules

**Arguments**:

- `obj` _dict_ - dictionary with rule definitions

<a name="oelint_parser.const_vars.get_rulefile"></a>
#### get\_rulefile

```python
get_rulefile()
```

get current rules

**Returns**:

- `dict` - dictionary with rule definitions

<a name="oelint_parser.const_vars.get_mandatory_vars"></a>
#### get\_mandatory\_vars

```python
get_mandatory_vars()
```

get mandatory variables

**Returns**:

- `list` - list of mandatory variable names

<a name="oelint_parser.const_vars.get_suggested_vars"></a>
#### get\_suggested\_vars

```python
get_suggested_vars()
```

get suggested variables

**Returns**:

- `list` - list of suggested variable names

<a name="oelint_parser.const_vars.get_known_mirrors"></a>
#### get\_known\_mirrors

```python
get_known_mirrors()
```

get known mirror replacements

**Returns**:

- `dict` - dictionary of known mirror replacements

<a name="oelint_parser.const_vars.get_protected_vars"></a>
#### get\_protected\_vars

```python
get_protected_vars()
```

get protected variables

**Returns**:

- `list` - list of protected variables

<a name="oelint_parser.const_vars.get_protected_append_vars"></a>
#### get\_protected\_append\_vars

```python
get_protected_append_vars()
```

get protected variables in bbappends

**Returns**:

- `list` - list of protected variables

<a name="oelint_parser.const_vars.get_known_vars"></a>
#### get\_known\_vars

```python
get_known_vars()
```

get list of known variables

**Returns**:

- `list` - list of known variable names

<a name="oelint_parser.const_vars.get_known_machines"></a>
#### get\_known\_machines

```python
get_known_machines()
```

get known machines

**Returns**:

- `list` - list of known machine names

<a name="oelint_parser.const_vars.get_base_varset"></a>
#### get\_base\_varset

```python
get_base_varset()
```

get variable baseset
Set includes basic package definitions

**Returns**:

- `dict` - base variable set

<a name="oelint_parser.inlinerep"></a>
# oelint\_parser.inlinerep

<a name="oelint_parser.cls_stash"></a>
# oelint\_parser.cls\_stash

<a name="oelint_parser.cls_stash.Stash"></a>
## Stash Objects

```python
class Stash()
```

<a name="oelint_parser.cls_stash.Stash.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(quiet=False)
```

constructor

<a name="oelint_parser.cls_stash.Stash.AddFile"></a>
#### AddFile

```python
 | AddFile(_file, lineOffset=0, forcedLink=None)
```

Adds a file to the stash

**Arguments**:

- `_file` _str_ - Full path to file
  

**Arguments**:

- `lineOffset` _int_ - Line offset from the file that include this file (default: {0})
- `forcedLink` _type_ - Force link against a file (default: {None})
  

**Returns**:

- `list` - List of {oelint_parser.cls_item.Item}

<a name="oelint_parser.cls_stash.Stash.GetRecipes"></a>
#### GetRecipes

```python
 | GetRecipes()
```

Get bb files in stash

**Returns**:

- `list` - List of bb files in stash

<a name="oelint_parser.cls_stash.Stash.GetLoneAppends"></a>
#### GetLoneAppends

```python
 | GetLoneAppends()
```

Get bbappend without a matching bb

**Returns**:

- `list` - list of bbappend without a matching bb

<a name="oelint_parser.cls_stash.Stash.GetLinksForFile"></a>
#### GetLinksForFile

```python
 | GetLinksForFile(filename)
```

Get file which this file is linked against

**Arguments**:

- `filename` _str_ - full path to file
  

**Returns**:

- `list` - list of full paths the file is linked against

<a name="oelint_parser.cls_stash.Stash.GetItemsFor"></a>
#### GetItemsFor

```python
 | GetItemsFor(filename=None, classifier=None, attribute=None, attributeValue=None, nolink=False)
```

Get items for filename

**Arguments**:

- `filename` _str_ - Full path to file (default: {None})
- `classifier` _str_ - class specifier (e.g. Variable) (default: {None})
- `attribute` _str_ - class attribute name (default: {None})
- `attributeValue` _str_ - value of the class attribute name (default: {None})
- `nolink` _bool_ - Consider linked files (default: {False})
  

**Returns**:

- `[type]` - [description]

<a name="oelint_parser.cls_stash.Stash.ExpandVar"></a>
#### ExpandVar

```python
 | ExpandVar(filename=None, attribute=None, attributeValue=None, nolink=False)
```

Expand variable to dictionary

**Arguments**:

- `filename` _str_ - Full path to file (default: {None})
- `attribute` _str_ - class attribute name (default: {None})
- `attributeValue` _str_ - value of the class attribute name (default: {None})
- `nolink` _bool_ - Consider linked files (default: {False})
  

**Returns**:

- `{dict}` - expanded variables from call + base set of variables

<a name="oelint_parser.helper_files"></a>
# oelint\_parser.helper\_files

<a name="oelint_parser.helper_files.get_files"></a>
#### get\_files

```python
get_files(stash, _file, pattern)
```

Get files matching SRC_URI entries

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - current stash
- `_file` _str_ - Full path to filename
- `pattern` _str_ - glob pattern to apply
  

**Returns**:

- `list` - list of files matching pattern

<a name="oelint_parser.helper_files.get_layer_root"></a>
#### get\_layer\_root

```python
get_layer_root(name)
```

Find the path to the layer root of a file

**Arguments**:

- `name` _str_ - filename
  

**Returns**:

- `str` - path to layer root or empty string

<a name="oelint_parser.helper_files.find_local_or_in_layer"></a>
#### find\_local\_or\_in\_layer

```python
find_local_or_in_layer(name, localdir)
```

Find file in local dir or in layer

**Arguments**:

- `name` _str_ - filename
- `localdir` _str_ - path to local dir
  

**Returns**:

- `str` - path to found file or None

<a name="oelint_parser.helper_files.get_scr_components"></a>
#### get\_scr\_components

```python
get_scr_components(string)
```

Return SRC_URI components

**Arguments**:

- `string` _str_ - raw string
  

**Returns**:

- `dict` - scheme: protocol used, src: source URI, options: parsed options

<a name="oelint_parser.helper_files.safe_linesplit"></a>
#### safe\_linesplit

```python
safe_linesplit(string)
```

Split line in a safe manner

**Arguments**:

- `string` _str_ - raw input
  

**Returns**:

- `list` - safely split input

<a name="oelint_parser.helper_files.guess_recipe_name"></a>
#### guess\_recipe\_name

```python
guess_recipe_name(_file)
```

Get the recipe name from filename

**Arguments**:

- `_file` _str_ - filename
  

**Returns**:

- `str` - recipe name

<a name="oelint_parser.helper_files.guess_base_recipe_name"></a>
#### guess\_base\_recipe\_name

```python
guess_base_recipe_name(_file)
```

Get the base recipe name from filename

**Arguments**:

- `_file` _str_ - filename
  

**Returns**:

- `str` - recipe name

<a name="oelint_parser.helper_files.guess_recipe_version"></a>
#### guess\_recipe\_version

```python
guess_recipe_version(_file)
```

Get recipe version from filename

**Arguments**:

- `_file` _str_ - filename
  

**Returns**:

- `str` - recipe version

<a name="oelint_parser.helper_files.expand_term"></a>
#### expand\_term

```python
expand_term(stash, _file, value, spare=[], seen={})
```

Expand a variable (replacing all variables by known content)

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - current stash
- `_file` _str_ - Full path to file
- `value` _str_ - Variable value to expand
  

**Returns**:

- `str` - expanded value

<a name="oelint_parser.helper_files.get_valid_package_names"></a>
#### get\_valid\_package\_names

```python
get_valid_package_names(stash, _file, strippn=False)
```

Get known valid names for packages

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - current stash
- `_file` _str_ - Full path to file
  

**Returns**:

- `list` - list of valid package names

<a name="oelint_parser.helper_files.get_valid_named_resources"></a>
#### get\_valid\_named\_resources

```python
get_valid_named_resources(stash, _file)
```

Get list of valid SRCREV resource names

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - current stash
- `_file` _str_ - Full path to file
  

**Returns**:

- `list` - list of valid SRCREV resource names

<a name="oelint_parser.const_func"></a>
# oelint\_parser.const\_func

<a name="oelint_parser.parser"></a>
# oelint\_parser.parser

<a name="oelint_parser.parser.get_full_scope"></a>
#### get\_full\_scope

```python
get_full_scope(_string, offset, _sstart, _send)
```

get full block of an inline statement

**Arguments**:

- `_string` _str_ - input string
- `offset` _int_ - offset in string
- `_sstart` _int_ - block start index
- `_send` _int_ - block end index
  

**Returns**:

- `str` - full block on inline statement

<a name="oelint_parser.parser.prepare_lines_subparser"></a>
#### prepare\_lines\_subparser

```python
prepare_lines_subparser(_iter, lineOffset, num, line, raw_line=None)
```

preprocess raw input

**Arguments**:

- `_iter` _interator_ - line interator object
- `lineOffset` _int_ - current line index
- `num` _int_ - internal line counter
- `line` _int_ - input string
- `raw_line` _string, optional_ - internal line representation. Defaults to None.
  

**Returns**:

- `list` - list of preproccessed chunks

<a name="oelint_parser.parser.prepare_lines"></a>
#### prepare\_lines

```python
prepare_lines(_file, lineOffset=0)
```

break raw file input into preprocessed chunks

**Arguments**:

- `_file` _string_ - Full path to file
- `lineOffset` _int, optional_ - line offset counter. Defaults to 0.
  

**Returns**:

- `list` - preprocessed list of chunks

<a name="oelint_parser.parser.get_items"></a>
#### get\_items

```python
get_items(stash, _file, lineOffset=0)
```

parses file

**Arguments**:

- `stash` _oelint_parser.cls_stash.Stash_ - Stash object
- `_file` _string_ - Full path to file
- `lineOffset` _int, optional_ - line offset counter. Defaults to 0.
  

**Returns**:

- `list` - List of oelint_parser.cls_item.* representations

