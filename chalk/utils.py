
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # Configure the logging formatters
    'formatters': {
        'verbose': {
            '()': 'chalk.log.ChalkFormatter',
            'format': (
                '-------------------\n'
                'pid %(process)d - %(name)s %(levelname)s %(asctime)s '
                '%(module)s.%(funcName)s line: %(lineno)d : %(message)s\n'
                '-------------------'
            ),
            'datefmt': '%H:%M:%S'
        }
    },

    # Configure the handlers, specifying the formatter is optional.
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },

    # Configure your loggers.
    'loggers': {
        '': {
            'handlers': ['console', ],
            'level': 'DEBUG',
            'propagate': False
        },
        'django': {
            'propagate': False,
            'level': 'ERROR'
        },
        'requests': {
            'propagate': True,
            'level': 'ERROR'
        },
    }
}
