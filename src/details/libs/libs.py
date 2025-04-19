def hello(name='user'):
    return f'hello {name}'

def parse_os(user_agent: str) -> str:
    if 'Windows' in user_agent:
        return 'Windows'
    elif 'Mac OS X' in user_agent or 'Macintosh' in user_agent:
        return 'macOS'
    elif 'Linux' in user_agent:
        return 'Linux'
    elif 'Android' in user_agent:
        return 'Android'
    elif 'iPhone' in user_agent or 'iPad' in user_agent:
        return 'iOS'
    else:
        return 'Unknown OS'