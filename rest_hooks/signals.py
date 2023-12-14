from django.dispatch import Signal


# args=['action', 'instance']
hook_event = Signal()

# args=['event_name', 'payload', 'user']
raw_hook_event = Signal()

# args=['payload', 'instance', 'hook']
hook_sent_event = Signal()
