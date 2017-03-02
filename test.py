from raven import Client

client = Client('https://809ac179ae8548aab0b7e055cced84df:aa1a0a8f8894432eb514799f12dc953d@sentry.io/144404')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()
