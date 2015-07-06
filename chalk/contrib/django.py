from chalk.utils import LOGGING

LOGGING['filters'] = {
    'require_debug_false': {
        '()': 'django.utils.log.RequireDebugFalse'
    },
    'require_debug_true': {
        '()': 'django.utils.log.RequireDebugTrue'
    },
}

LOGGING['handlers']['console']['filters'] = ['require_debug_true', ]
