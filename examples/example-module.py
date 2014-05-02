#!/usr/bin/env python

import chalk

chalk.blue("Hello world!!")
chalk.yellow("Listen to me!!!")
chalk.red("ERROR", pipe=chalk.stderr)
chalk.magenta('This is pretty cool', opts='bold')
chalk.cyan('...more stuff', opts=('bold', 'underscore'))
