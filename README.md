# homework_git_

Git is a specific open-source version control system created by Linus Torvalds in 2005.

Specifically, Git is a distributed version control system, which means that the entire codebase and history is available on every developer’s computer, which allows for easy branching and merging.

Parse strings using a specification based on the Python format() syntax.

parse() is the opposite of format()

The module is set up to only export parse(), search(), findall(), and with_pattern() when import * is used:

from parse import * From there it’s a simple thing to parse a string:

parse("It's {}, I love it!", "It's spam, I love it!") <Result ('spam',) {}> _[0] 'spam' Or to search a string for some pattern:

search('Age: {:d}\n', 'Name: Rufus\nAge: 42\nColor: red\n') <Result (42,) {}> Or find all the occurrences of some pattern in a string:

''.join(r[0] for r in findall(">{}<", "

the bold text

")) 'the bold text' If you’re going to use the same pattern to match lots of strings you can compile it once:
from parse import compile p = compile("It's {}, I love it!") print(p) <Parser "It's {}, I love it!"> p.parse("It's spam, I love it!") <Result ('spam',) {}> (“compile” is not exported for import * usage as it would override the built-in compile() function)

The default behaviour is to match strings case insensitively. You may match with case by specifying case_sensitive=True:

parse('SPAM', 'spam', case_sensitive=True) is None True